# Internet Explorer EPM Sandbox Escape CVE-2014-6350 - Project Zero

Source: https://projectzero.google/2014/12/internet-explorer-epm-sandbox-escape.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

# Posted by James Forshaw


This month Microsoft fixed 3 different Internet Explorer Enhanced Protected Mode (EPM) sandbox escapes which I disclosed in August. Sandboxes are one of the main areas of interest for Project Zero (and me in particular) as they are choke points for an attacker successfully exploiting a remote code execution vulnerability.

All three bugs are fixed in [MS14-065](https://technet.microsoft.com/library/security/MS14-065), you can read the original reports [here](https://code.google.com/p/google-security-research/issues/detail?id=95), [here](https://code.google.com/p/google-security-research/issues/detail?id=97) and [here](https://code.google.com/p/google-security-research/issues/detail?id=99). CVE-2014-6350 is perhaps the most interesting of the bunch, not because the bug is particularly special but the technique to exploit it to get code execution out of the sandbox is unusual. It demonstrates a potential attack against DCOM hosts if there’s an accompanying memory disclosure vulnerability. This blog post is going to go into a bit more detail about how you can exploit the vulnerability.

## What Was the Vulnerability?

The vulnerability was due to weak permissions on the broker process when IE is running in EPM mode. This didn’t actually affect the old Protected Mode (PM) for reasons I’ll soon explain. The EPM sandbox contains the untrusted tab processes which handle internet content, the broker process acts a mediator providing privileged services to the tabs when required. Interaction between the tabs and the broker uses a DCOM based IPC mechanism. 



User
Permissions
S-1-15-3-4096 (IE Capability SID)
Read Memory, Query Information
Current User
Full Control
SYSTEM 
Full Control


We can call [OpenProcess](http://msdn.microsoft.com/en-gb/library/windows/desktop/ms684320%28v=vs.85%29.aspx) passing it the PID of the broker and the desired access of PROCESS\_VM\_READ and the kernel will return the sandboxed process an appropriate handle. With this handle it’s trivial to read arbitrary memory from the broker using the [ReadProcessMemory](http://msdn.microsoft.com/en-gb/library/windows/desktop/ms680553%28v=vs.85%29.aspx) API. This even correctly handles invalid memory addresses so nothing should crash unexpectedly. 

BOOL ReadMem(DWORD ppid, LPVOID addr, LPVOID result, SIZE\_T size) {
    HANDLE hProcess = OpenProcess(PROCESS\_VM\_READ,
                                      FALSE,
                                      ppid);
    BOOL ret = FALSE;

if(hProcess) {
        ret = ReadProcessMemory(hProcess,
                 addr,
                 result,
                 size,
                 NULL);
        CloseHandle(hProcess);
    }

return ret;
}

Things get a bit more complicated if you’re on 64-bit Windows and trying to exploit from a 32-bit tab process, Wow64 gets in the way. You can’t directly use ReadProcessMemory to read memory from the 64-bit broker. You can use something like [wow64ext](https://code.google.com/p/rewolf-wow64ext/) to get around this limitation, but for now we’ll just ignore it.

But wait, what about PM, why isn’t the bug there as well? In PM only the single access check is performed so we should get Full Control but we don’t due to the Mandatory Integrity Label (IL) feature introduced in Windows Vista. When a process tries to open another the access check in the kernel will first compare the IL of the calling process against the value specified in the target process’ System ACL (SACL). If the calling process’ IL is lower than that specified by the target process the maximum access is limited to a small subset of the available access permissions (such as PROCESS\_QUERY\_LIMITED\_INFORMATION). This will block PROCESS\_VM\_READ or anything more dangerous even before the DACL is checked. 

Okay so let’s take a look at the token for the EPM sandboxed process in Process Explorer, we can clearly see the token has the Low Mandatory Level (highlighted in the below screenshot).
## Exploiting the Vulnerability

The original PoC supplied in the [issue tracker](https://code.google.com/p/google-security-research/issues/detail?id=97) exploited a method in one of the broker IPC interfaces to read arbitrary files on the system. By reading a per-process HMAC key the PoC could forge a valid token and call the appropriate method (CShDocVwBroker::GetFileHandle) to open the file. This is useful for EPM because the AppContainer prevents reading arbitrary files. Still this is only a read, not a write. Ideally we would like to be able to completely escape the sandbox, not just disclose the contents of files. 

This might initially seem like a difficult task, but it turns out there are more technologies which use per-process secrets to make themselves secure. One such technology is my all-time favourite Windows technology, COM (I might be joking when I say that). Turns out there’s a way of getting code execution in many application which implement remote COM services, as long as we’re able to disclose the content of the hosting process. 
### COM Threading Models, Apartments and Interface Marshaling

COM is used by many different components in Windows from the Explorer Shell to local privileges services such as BITS. Each use case has different requirements and restrictions, for example UI code needs all code to run on a single thread otherwise the the OS will get unhappy. On the other hand a utility class might be completely thread safe. To support these requirements COM supports a couple of [threading models](http://msdn.microsoft.com/en-us/library/ms809971.aspx) which relieves some of the burden on the programmer. 

An object is contained within an Apartment which defines how methods on the object can be called. There are two types of Apartments, Single Threaded Apartment (STA) and Multi Threaded Apartment (MTA). When considering how these apartments interact with how methods are called we need to define the relationship between the caller and the object. For that we’ll define the caller of methods as the Client and the object as the Server. 

The Client’s Apartment is determined by the flag passed to [CoInitializeEx](http://msdn.microsoft.com/en-us/library/windows/desktop/ms695279%28v=vs.85%29.aspx) (we default to STA if the “legacy” [CoInitialize](<http://msdn.microsoft.com/en-us/library/windows/desktop/ms678543(v=vs.85).aspx>) is called instead). The Server’s apartment depends on the COM object threading model definition in the Windows registry. This can be one of three settings, Free (means multi-threaded), Apartment (means single-threaded) and Both. If the Client and Server have compatible apartments (which really only occurs when the server object is registered as supporting both threading models). then calls made to the object are direct function pointer dereferences via the object’s virtual function table. However in the case of STA calling MTA or MTA calling STA we need to proxy the calls in someway, COM does this through the process of [Marshaling](http://msdn.microsoft.com/en-gb/library/windows/desktop/ms692621%28v=vs.85%29.aspx). We can summarise this in the following table. 

Client
Server
Inter-object communication via:
STA
Free
Marshaling, unless server implements the free-threaded marshaler and is in the same process
MTA
Apartment
Marshaling
STA
Both
Direct Access
MTA
Both
Direct access


Marshaling refers to the process of serializing method calls to the Server object. This is especially important in STA as all methods must be called on a single thread. This is typically coordinated using a Windows message loop, in fact if your application has no windows or message loop it will create them for you if you create a STA. When a Client calls an object in an incompatible apartment it really calls a special proxy object. This proxy knows about each different COM interface and method, including what parameters each method takes. 

The proxy takes the parameters, serializes the information using the built-in COM marshaling code and packages them up to be sent to the server. At the server side a dispatcher unmarshals the parameters and then invokes the appropriate method on the Server object. Any return values are sent back to the client in the same way.
### The Free-Threaded Marshaler

Okay so how’s this going to help in exploiting the memory disclosure vulnerability? To understand I need to describe something called the [Free-Threaded Marshaler](http://msdn.microsoft.com/en-us/library/windows/desktop/ms694500%28v=vs.85%29.aspx) (FTM). This is referred to in the previous table when a STA Client calls a method on a multi-threading capable Server. It seems awfully wasteful that the Client needs to go through this whole proxing/marshaling effort. Can’t it just call the object directly? This is what the FTM solves. 

When a COM object is instantiated in an incompatible apartment a reference to that object must be passed back to the caller. This is achieved using the same marshaling operations as during a call. In fact this same mechanism is used when a call is made to a object method which takes COM object parameters. The mechanism the marshaler uses to pass this reference is to build a special data stream called an [OBJREF](http://msdn.microsoft.com/en-us/library/cc226828.aspx). This stream contains all the information a Client needs to construct a proxy object and contact the Server. This implements a pass-by-reference semantic for COM objects. An example of an OBJREF is shown below:
[IMarshal](http://msdn.microsoft.com/en-us/library/windows/desktop/dd542707%28v=vs.85%29.aspx) interface. 

This feature is used by the FTM to “cheat” the system. Instead of passing across the original object’s data, it instead just passes a pointer to the original object in memory serialized in the OBJREF. When unmarshaled this pointer is deserialized and returned to the caller. It acts as a fake-proxy and effectively just allows direct calls to be made on the original object.

The implementation of the FTM lies in combase.dll specifically the CStaticMarshaler class. For Windows 7 it’s in ole32.dll and is called CFreeMarshaler instead. Looking at CStaticMarshaler::UnmarshalInterface we have code which is roughly as follows:

HRESULT CStaticMarshaler::UnmarshalInterface(IStream\* pStm,
                                             REFIID riid, 
                                             void\*\* ppv) {
  DWORD mshlflags;
  BYTE  secret\[16\];
  ULONGLONG pv;

if (!CStaticMarshaler::\_fSecretInit) {
    return E\_UNEXPECTED;
  }

pStm->Read(&mshlflags, sizeof(mshlflags));
  pStm->Read(&pv, sizeof(p));
  pStm->Read(secret, sizeof(secret));

if (SecureCompareBuffer(secret, CStaticMarshaler::\_SecretBlock)) {
    \*ppv = (void\*)pv;

if ((mshlflags == MSHLFLAGS\_TABLESTRONG) 
    || (mshlflags == MSHLFLAGS\_TABLEWEAK)) {
 ((IUnknown\*)\*ppv)->AddRef();
    }

return S\_OK;
  } else {
    return E\_UNEXPECTED;
  } 
}

Note that the method checks that the secret is initialized first, this prevents accidentally using a zero-secret value if it was uninitialized. Also note the use of a secure comparison function to combat timing attacks against the secret check. Actually this is a case of not-back porting fixes. In Windows 7 the comparison uses a repe cmdsd instruction, which isn’t constant time. Therefore on Windows 7 you might be able to exploit this check by mounting a side-channel timing attack, although I think it would be pretty complex and time consuming to do so.

In the end our structure looks like the following:
[IMarshal::GetUnmarshalClass](<http://msdn.microsoft.com/en-us/library/windows/desktop/ms688645(v=vs.85).aspx>) which returns the CLSID of the COM object to use when reconstructing the code and [IMarshal:MarshalInterface](<http://msdn.microsoft.com/en-us/library/windows/desktop/ms692716(v=vs.85).aspx>) which will package up the appropriate pointer value for the exploit. A simple example is shown below:

GUID CLSID\_FreeThreadedMarshaller = 
{ 0x0000033A, 0x0000, 0x0000, 
{ 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x46, } };

HRESULT STDMETHODCALLTYPE CFakeObject::GetUnmarshalClass(
 REFIID riid,
 void \*pv,
 DWORD dwDestContext,
 void \*pvDestContext,
 DWORD mshlflags,
 CLSID \*pCid)
{
 memcpy(pCid, &CLSID\_FreeThreadedMarshaller, 
  sizeof(CLSID\_FreeThreadedMarshaller));

return S\_OK;
}

HRESULT STDMETHODCALLTYPE CFakeObject::MarshalInterface(
        IStream \*pStm,
        REFIID riid,
        void \*pv,
        DWORD dwDestContext,
        void \*pvDestContext,
        DWORD mshlflags)
{
   pStm->Write(&\_mshlflags, sizeof(\_mshlflags), NULL);
   pStm->Write(&\_pv, sizeof(\_pv), NULL);
   pStm->Write(&\_secret, sizeof(\_secret), NULL);

return S\_OK;
}

Simple enough. We’ll get to how this is used later.
## Escaping the Sandbox


With the background out of the way it’s time to escape the sandbox. There are three things we need to do to get code execution from the sandbox in the broker process:
1. 
Extract the FTM per-process secret from the broker.
2. 
Construct a fake v-table and a fake object pointer.
3. 
Marshal an object into the broker to get code executed.


### Extract Per-Process Secret

This should be a pretty easy task, we know where the secret’s held in memory as the load address of combase.dll is going to be the same in the sandbox process as the broker process. Even though Windows Vista introduced ASLR system DLLs are only randomised once at boot, therefore combase.dll is going to be mapped to the same location in every process. This is a weakness in ASLR on Windows, especially for local privilege escalation .But if you dump the values during normal IE operation you’ll see a problem:
[IEShowSaveFileDialog](<http://msdn.microsoft.com/en-us/library/ie/ms537318(v=vs.85).aspx>) API call (which is actually implemented by various broker calls). Obviously this will display some UI but it doesn’t really matter, by the time the dialog is displayed the FTM is already initialized, there isn’t anything the user could do about it. 

For now we’ll just hard code the offsets into combase.dll. But of course you could find them dynamically by initializing the FTM in the sandboxed process and finding the offset through a memory search for the marshaled secret. 
### Constructing a Fake V-Table

Now the next challenge is to get our fake v-table into the broker process. As we can read out the broker’s memory we could certainly do something like heap flooding using one of the broker APIs, but is there an easier way? The IE broker and sandboxed processes share a few memory sections to pass settings and information between themselves. Some of these sections are writable by the sandboxed process, therefore all we need to do is find the corresponding mapping in the broker, then modify to our heart’s content. In this case the section \Sessions\X\BaseNamedObjects\URLZones\_user was chosen (where X is the session ID and user is the username), but anything would do as long as it’s already mapped into the broker and writable by the sandboxed process.

We don’t have to do much in the way of brute-forcing to find the section. As we can open the process with PROCESS\_QUERY\_INFORMATION access we can call [VirtualQueryEx](<http://msdn.microsoft.com/en-us/library/windows/desktop/aa366907(v=vs.85).aspx>) to enumerate mapped memory sections. As it returns the size we can quickly skip unmapped areas. Then we can look for a canary value we wrote to the section to determine the exact location. 

DWORD\_PTR FindSharedSection(LPBYTE section, HANDLE hProcess)
{
   // No point starting at lowest value
   LPBYTE curr = (LPBYTE)0x10000;
   LPBYTE max = (LPBYTE)0x7FFF0000;

memcpy(§ion\[0\], "ABCD", 4);

while (curr \< max)
   {
     MEMORY\_BASIC\_INFORMATION basicInfo = { 0 };
     if (VirtualQueryEx(hProcess, curr,
                &basicInfo, sizeof(basicInfo)))
     {
        if ((basicInfo.State == MEM\_COMMIT)
           && (basicInfo.Type == MEM\_MAPPED)
           && (basicInfo.RegionSize == 4096))
        {
           CHAR buf\[4\] = { 0 };
           SIZE\_T read\_len = 0;

ReadProcessMemory(hProcess, (LPBYTE)basicInfo.BaseAddress, 
                             buf, 4, &read\_len);

if (memcmp(buf, "ABCD", 4) == 0)
           {
              return (DWORD\_PTR)basicInfo.BaseAddress;
           }
         }

curr = (LPBYTE)basicInfo.BaseAddress + basicInfo.RegionSize;
      }
      else
      {
         break;
      }
   }

return 0;
}

Once we’ve determined the location of the shared memory section we need to build the v-table and the fake object. What should we call through the v-table? You might think at this point it’s time to build a ROP chain, but of course we don’t really need to do that. As all COM calls use the stdcall calling convention where all arguments are placed on the stack we can call any location we like with 1 argument we almost completely control, the this pointer to our fake object. 

One way of exploiting this is to use a function such as [LoadLibraryW](http://msdn.microsoft.com/en-us/library/windows/desktop/ms684175%28v=vs.85%29.aspx) and construct the fake object with a relative path to a DLL to load. As long as the v-table pointer doesn’t contain any NULs (which makes this technique less useful on 64-bit I might add) we can remove it from the path and cause it to load the library. We can set the lower 16 bits to any arbitrary value we like to eliminate this problem and while we don’t control the upper 16 bits there’s effectively no chance it would end up as a 0 due to the NULL page protection in Windows preventing allocations below the 64KiB point. In the end our fake object looks like:

### Marshaling an Object into Broker

Finally the easy bit, as pretty much all the interfaces to the broker from the sandbox use COM all we need to do is find a call which takes a bare IUnknown pointer and pass it our fake marshaling object. For this purpose I found that you could query for the IEBrokerAttach interface from the Shell Document View broker which has a single function with the following prototype:

HRESULT AttachIEFrameToBroker(IUnknown\* pFrame);

To make this even better before we get hold of the pointer to the broker the frame has already been set, this makes this method fail immediately without touching the pFrame object. Therefore we don’t need to worry about QueryInterface being called. Our exploit is going to 
run before this function ever gets called so we don’t really care. 

So we create our fake object and call this method. This will cause the COM infrastructure to marshal our data into an OBJREF. This ends up on the other side of the IPC channel where the COM infrastructure will unmarshal it. This causes the FTM UnmarshalInterface method to be called, and as we’ve successfully discovered the secret value will happily unpack our fake object pointer. Finally the method will call AddRef on the object as we can set the passed mshlflags to MSHLFLAGS\_TABLESTRONG. This will execute LoadLibraryW with our fake object as the path parameter. This’ll load an arbitrary DLL into the broker, all that’s required is to pop calc and it’s job done. 
## Wrapping it Up

So I’ve added a new PoC to the original [issue](https://code.google.com/p/google-security-research/issues/detail?id=97) for this bug to demonstrate the attack on 32-bit Windows 8.1 update (obviously without the MS14-065 patch). It won’t work directly on 64-bit Windows 8.1 as the broker process runs as 64-bit even if the tab processes might be 32-bit. You’ll need to be a bit more creative to get it to work on 64-bit, but you can easily get control over RIP so it isn’t a major concern. If you want to test it on an up to date machine, then the PoC contains a tool, SetProcessDACL, which modifies a process’s DACL to re-add read permissions for the IE Capability SID. 

Hopefully it gives you an idea on how you could exploit similar bugs. Still, let’s not blame COM for this, since it isn’t really its fault. This is only a demonstration of how a relatively innocuous issue, memory disclosure in a privileged process, completely breaks many security assumptions leading to code execution and elevation of privilege.
