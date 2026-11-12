# Windows Tooling Updates: OleView.NET - Project Zero

Source: https://projectzero.google/2024/12/windows-tooling-updates-oleviewnet.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Google Project Zero

This is a short blog post about some recent improvements I've been making to the [OleView.NET](http://oleview.net) tool which has been released as part of version 1.16. The tool is designed to discover the attack surface of Windows COM and find security vulnerabilities such as privilege escalation and remote code execution. The updates were recently presented at the Microsoft Bluehat conference in Redmond under the name "[DCOM Research for Everyone!](https://github.com/tyranid/infosec-presentations/blob/master/Bluehat/2024/DCOM%2520Research%2520for%2520Everyone!.pdf)". This blog expands on the topics discussed to give a bit more background and detail that couldn't be fit within the 45-minute timeslot. This post assumes a knowledge of COM as I'm only going to describe a limited number of terms.

## Using the [OleView.NET](http://oleview.net) Tooling

Before we start the discussion it's important to understand how you can get hold of the [OleView.NET](http://oleview.net) tool and some basic usage. The simplest way to get the tooling is to install it from the PowerShell gallery with the Install-Module OleViewDotNet command. This installs both the PowerShell module and the GUI.


Next you need to parse the COM registration artifacts into an internal database. You can do this by running the Get-ComDatabase command. Once it's finished you're ready to go. You will notice that it can take a long time to complete, so it'd be annoying to have to do this every time you want to start researching. For that reason you can use the command Set-ComDatabase -Default to write out the database to a default storage location. Now the next time you start PowerShell you can just run an inspection command, such as Get-ComClass and the default database will be automatically loaded.


This default database is also shared with the GUI, which you can start by running the Show-ComDatabase command. For general research I find the GUI to be easier to use and you can click around and look at the COM registration information. For analysis, the ability to script through PowerShell is more important.

## Researching COM Services

Performing security research in COM usually involves the following steps::

- Enumerate potential COM classes of interest. These might be classes which are accessible outside of a sandbox, running at high privilege or designed to be remotely exposed.
- Validate whether the COM classes are truly accessible from the attack position. COM has various security controls which determine what users can launch, activate and access an object. Understanding these security controls allows the list of COM classes of interest to be limited to only those that are actually part of the attack surface.
- Enumerate exposed interfaces, determine what they do and call methods on them to test for security vulnerabilities.


The last step is the focus of the updates to the tooling, making it easier to determine what an exposed interface does and call methods to test the behavior. The goal is to minimize the amount of reverse engineering needed (although generally some is still required) as well as avoid needing to write code outside of the tooling to interact with the COM service under test.


To achieve this goal, [OleView.NET](http://oleview.net) will pull together any sources of interface information it has, then provide a mechanism to inspect and invoke methods on the interface through the UI or via PowerShell. The sources of information that it currently pulls together are:

1. Known interfaces, either defined in the base .NET framework class libraries or inside [OleView.NET](http://oleview.net).
2. COM interface definitions present in the Global Assembly Cache.
3. Registered type libraries.
4. Windows Runtime interfaces.
5. Extracted proxy class marshaling information.


One useful benefit of gathering this information, is that the tool formats the interface as "source code" so you can manually inspect it.

## Formatting Interfaces Definitions

The [OleView.NET](http://oleview.net) tool uses a database object to represent all the artifacts it has analyzed on your system. The latest released version defines some of these objects to be convertible to "source code". For example the following can be converted if the tool can determine some meta data that to represent the artifact:

- COM interfaces
- COM proxies
- COM Windows Runtime classes.
- Type libraries, interfaces and classes.


How you get to this conversion depends on whether you're using the PowerShell or the UI. The simplest approach is PowerShell, using the ConvertTo-ComSourceCode command. For example, the following will convert an interface object into source code:


PS> Get-ComInterface -Name IMyInterface | ConvertTo-ComSourceCode -Parse


Note that we also need to pass a -Parse option to the command. Some metadata such as type libraries and proxies can be expensive to parse so it won't do that automatically. However, once they're been parsed in the current session the metadata is cached for further use, so for example if you formatted a single interface in a type library, all other interfaces are now also parsed and can be formatted.


The output of this command is the converted "source code" as text. The format depends on metadata source. For example the following is the output from a Windows Runtime type:


\[Guid("155eb23b-242a-45e0-a2e9-3171fc6a7fdd")\]

interface IUserStatics

{

/\* Methods \*/

UserWatcher CreateWatcher();

IAsyncOperation\<IReadOnlyList\<User>> FindAllAsync();

IAsyncOperation\<IReadOnlyList\<User>> FindAllAsync(UserType type);

IAsyncOperation\<IReadOnlyList\<User>> FindAllAsync(UserType type,

UserAuthenticationStatus status);

User GetFromId(string nonRoamableId);

}


As Windows Runtime types are defined using metadata similar to .NET then the output is a pseudo C# format. In contrast for type library or proxy it's look more like the following:


\[

odl,

uuid(00000512-0000-0010-8000-00AA006D2EA4),

dual,

oleautomation,

nonextensible

\]

interface \_Collection : IDispatch {

\[id(1), propget\]

HRESULT Count(\[out, retval\] int\* c);

\[id(0xFFFFFFFC), restricted\]

HRESULT \_NewEnum(\[out, retval\] IUnknown\*\* ppvObject);

\[id(2)\]

HRESULT Refresh();

};


This is in the Microsoft Interface Definition Language (MIDL) format, the type library version should be pretty accurate and could even be recompiled by the MIDL compiler. For proxies some of the information is lost and so the MIDL generated isn't completely accurate, but as we'll see later there's limited reasons to take the output and recompile.


Another thing to note is that proxies lose name information when compiled from MIDL to their C marshaled representation. Therefore the tool just generates placeholder names, for example, method names are of the form "ProcN". If the proxy is for a type that has a known definition, such as from a Windows Runtime type or a type library then the tool will try and automatically apply the names. If not, you'll need to manually change them if you want them to be anything other than the default.


You can change the names from PowerShell by modifying the proxy object directly. For example the "IBitsTest1" interface looks like the following before doing anything:


\[

object,

uuid(51A183DB-67E0-4472-8602-3DBC730B7EF5),

\]

interface IBitsTest1 : IUnknown {

HRESULT Proc3(\[out, string\] wchar\_t\*\* p0);

}


You can modify "Proc3" with the following script:


PS> $proxy = Get-ComProxy -Iid 51A183DB-67E0-4472-8602-3DBC730B7EF5

PS> $proxy.Procedures\[0\].Name = "GetBitsDllPath"

PS> $proxy.Procedures\[0\].Parameters\[0\].Name = "DllPath"


Now the formatted output looks like the following:


\[

object,

uuid(51A183DB-67E0-4472-8602-3DBC730B7EF5),

\]

interface IBitsTest1 : IUnknown {

HRESULT GetBitsDllPath(\[out, string\] wchar\_t\*\* DllPath);

}


This renaming will also be important when we come back to calling proxied methods. Obviously it'd be annoying to run this script every time, so you can cache the names using the following command:

PS> Export-ComProxyName -Proxy $p -ToCache


This will write out a file describing the names to a local cache file. When the proxy is loaded again in another session this cache file will be automatically applied. The Export-ComProxyName and corresponding Import-ComProxyName commands allow you to read and write XML or JSON files representing the proxy names which you can modify in a text editor if that's easier.


One of the quickest wins is to enumerate the interfaces for a COM object, then pass the output of that through the ConvertTo-ComSource code command. For example:


PS> $obj = New-ComObject -Clsid 4575438f-a6c8-4976-b0fe-2f26b80d959e

PS> Get-ComInterface -Object $obj | ConvertTo-ComSourceCode -Parse


This creates a new COM object based on its CLSID, enumerates the interfaces it supports and then passes them through the conversion process to get out a "source code" representation of the interfaces.


To view the source code in the GUI you first need to open one of the database views from the Registry menu. In the resulting window, there will be a tree view of artifacts. You need to open the source code viewer window by right clicking the tree and selecting the Show Source Code option in the context menu. This will result in a view similar to the following:



You can also automatically enable the source code view from the View→Registry View Options menu. In that menu you can also enable automatically parsing the interface information, which is off by default.


You might notice in the screenshot that there's some text which is underlined. This indicates names which can be changed, and it is only used for proxies. You can right click the name and choose Edit Name from the context menu to bring up a text entry dialog. You can then change the name to suit. If you want to persist the names between sessions then set the Save Proxy Names on Exit option in the registry view options. Then when you exit any modified proxies will be written to the cache.


If you want to edit a proxy from PowerShell in a similar GUI you can use following command:


PS> Edit-ComSourceCode $proxy


This will show a dialog similar to the following where you can do edits to the proxy name information:


## Genering Interfaces from a Proxy Definition


Now on to the more important side of these updates, the ability to invoke methods on the interfaces exposed by an object you want to research. The tool has always given you some ability to invoke methods as long as the object has a .NET interface to call through reflection. This could either be through a known interface type, such as a built-in one or the Windows Runtime interfaces or by converting a type library into a .NET assembly on demand.


What's new is the ability to generate an interface based on a proxy definition and then use that to invoke methods. Initially I tried to implement this by generating an .NET interface dynamically which would then use the existing .NET interop to call the proxy methods. This worked fine for simple proxies but quickly hit problems when doing anything more complex:

- Some types are hard to represent in easy to use .NET types, such as pointers to structures. This is "handled" in the type library converter by just exporting them as IntPtr parameters which means the caller has to manually marshal the data. Get this wrong and the tool crashes.
- Any structures need to be accurately laid out so the native marshaler can read and write to the correct field locations. Get this wrong and the tool crashes.
- Did I mention that if you get this wrong the tool crashes?


Fortunately I already had a solution, my [sandbox library](https://github.com/googleprojectzero/sandbox-attacksurface-analysis-tools.v1) already had the ability to dynamically generate a [.NET class from parsed NDR data](/2019/12/calling-local-windows-rpc-servers-from.html), in fact I was already using the library to parse the NDR data for proxies so I realized could I repurpose the existing client builder for COM proxy clients. I needed to do some simple refactoring of the code to make it build from a COM proxy instance rather than an RPC server, but I quickly had an RPC client. This RPC client doesn't directly interact with any native marshaling code, so it's unlikely to crash. Also any complex structures are built in a way which makes it easy to modify from .NET removing the problems around pointers. One issue with using the RPC client method is the same interface could be used for both in-process and out-of-process objects. Due to the way COM is designed a client usually doesn't need to care about where the object is, but in this case it must be accessible via a proxy. This isn't that big an issue, there's no security boundary between in-process COM objects and so being able to call methods on them isn't that interesting.


The next problem was the RPC transport. COM calls have an additional input and output parameter, the [ORPTHIS](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dcom/d57e9fd9-8e8b-45b8-99ea-9b0266009676) and [ORPCTHAT](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dcom/10ffacb5-c8b2-4b6a-bccc-9e515818661f) structures, that need to be added to the call. These parameters could have been added to the RPC client, but it would seem best to make the clients agnostic of the transport. Instead as my RPC code has pluggable RPC transport I was able to reimplement a custom version over the top of the existing ALPC and TCP transports which added the additional parameters to any call. That wasn't the end of it though, ALPC needs an additional pair of parameters, LocalThis and LocalThat, which are potentially different depending on versions of Windows. Also you need to add support for additional services such as the OXID resolver and communication with the local DCOM activator. While I implemented all this it wasn't as reliable as I'd like, however it's still present in the [source code](https://github.com/tyranid/oleviewdotnet/tree/master/OleViewDotNet/Rpc/Clients) if you want to play with it.


As an aside, I should point out that [Clement Rouault](https://x.com/hakril), one of the original researchers into ALPC RPC protocol of which parts of my own implementation is inspired, recently released a very [similar project](https://blog.exatrack.com/STUBborn/) for their Python tooling which implements the ALPC DCOM protocol.


I decided that I'd need a different approach, in the COM runtime the RPC channel used by a proxy instance is represented by the [IRpcChannelBuffer](https://learn.microsoft.com/en-us/windows/win32/api/objidl/nn-objidl-irpcchannelbuffer) interface. An object implementing this interface is connected to the proxy during initialization, it is then used to send and receive NDR formatted data from the client to the server. The implementation handles all the idiosyncrasies such as the additional parameters, handling OXID resolving and reference counting. If we could get hold of a proxy object's instance of the IRpcChannelBuffer object, we could use that instead of implementing our own protocol, the challenge was how to get it.


After a bit of research I found that we can use the documented [NdrProxyInitialize](https://learn.microsoft.com/en-us/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyinitialize) function to get hold of the interface from its MIDL\_STUB\_MESSAGE structure by passing in the interface pointer to a proxy. While it wouldn't be as flexible as a fully custom implementation this gave me an easy way to handle the transport without worrying about platform or protocol differences. It could also work from an existing COM object, just query the appropriate interface, extract the buffer and make calls to the remote server.


Of course nothing is that simple, I discovered that while the IRpcChannelBuffer object is a COM object it has a broken implementation of IMarshal. As .NET's COM interop tries to query for IMarshal when generating a Runtime Callable Wrapper, it will immediately crash the process. I had to [manually dispatch the calls](https://github.com/tyranid/oleviewdotnet/blob/master/OleViewDotNet/Rpc/Transport/RpcChannelBuffer.cs) to the method through native delegates, but at least it works.

## Calling Interface Methods

Okay, so how do you use the tool to call arbitrary methods? For the GUI it works like it always has, when you create an instance of a COM object, usually by right clicking an entry in a view and selecting Create Instance you'll get a new object information window similar to the following:



At the bottom of the window is a list of supported interfaces. In the right column is an indicator if there's a viewer for that interface. If it's set to Yes, then you can double click it to bring up an invocation window like the following:



From this window you can double click a method to bring up a new dialog where you can specify the arguments and invoke the method as shown below.



Once invoked it'll show the resulting output parameters and if the return value is an integer will assume it's a HRESULT error code. These windows are the same for "reflected" interfaces such as type libraries and Windows Runtime interfaces as well as proxy clients. The names of proxy methods won't be automatically updated if you change them when the interface window is open. You'll need to go back to the object information window and double click the interface again to get it to recreate the client.


For PowerShell you can specify an Iid argument when using the New-ComObject command or use the Get-ComObjectInterface command to query an existing COM object for a new interface. The tooling will pick the best option for calling the interface from the options available to it, including generating the RPC client dynamically.


PS> $obj = New-ComObject -Clsid 4991D34B-80A1-4291-83B6-3328366B9097

PS> $test = Get-ComObjectInterface $o -Iid 51A183DB-67E0-4472-8602-3DBC730B7EF5

PS> $test.GetBitsDllPath()


DllPath retval

------- ------

c:\windows\system32\qmgr.dll 0


To make it easier to call interface methods from PowerShell the exposed methods on the object will be modified to wrap output parameters in a single return value. You can see this in the listing above, the DllPath parameter was originally an output only parameter. Rather than deal with that in the script a return structure was automatically created containing the DllPath as well as the HRESULT return value. If the parameter is an input and output then the method signature accepts the input value and the return value contains the output value.


If the definitions for your interface don't already exist you can import them into the tool to be used by the automatic interface selection. To do this you'll need to define the interfaces as .NET types and compile them into an assembly. Then in the GUI use the File→Import Interop Assembly menu option or for PowerShell use the Add-ComObjectInterface command. Both of these options allow you to specify the assembly will be automatically loaded the next time you start the tool. This will make a copy of the DLL to a central location so that it can be accessed even if you delete the library later.


If all you have is an IDL file for a set of COM interfaces you can import them into the tool indirectly with help from the Windows SDK. First compile the IDL file using the MIDL compiler to generate a type library, then use the [TLBIMP](https://learn.microsoft.com/en-us/dotnet/framework/tools/tlbimp-exe-type-library-importer) command to generate an Assembly file from the type library. Finally you can import it using the previous paragraph's methods.


There's plenty to discover in [OleView.NET](http://oleview.net) which I've not covered here. I'd encourage you to play around, or check out the [source code](https://github.com/tyranid/oleviewdotnet) on github.
