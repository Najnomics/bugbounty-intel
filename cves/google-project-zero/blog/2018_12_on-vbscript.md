# On VBScript - Project Zero

Source: https://projectzero.google/2018/12/on-vbscript.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Ivan Fratric, Google Project Zero


Introduction


Vulnerabilities in the [VBScript](https://en.wikipedia.org/wiki/VBScript) scripting engine are a well known way to attack Microsoft Windows. In order to reduce this attack surface, in Windows 10 Fall Creators Update, Microsoft [disabled](https://blogs.windows.com/msedgedev/2017/07/07/update-disabling-vbscript-internet-explorer-11/#rwFwvJ9JSX18pj2h.97) VBScript execution in Internet Explorer in the Internet Zone and the Restricted Sites Zone by default. Yet this did not deter attackers from using it - in 2018 alone, there have been at least two instances of 0day attacks using vulnerabilities in VBScript: [CVE-2018-8174](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8174) and [CVE-2018-8373](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8373). In both of these cases, the delivery method for the exploit were Microsoft Office files with an embedded object which caused malicious VBScript code to be processed using the Internet Explorer engine. For a more detailed analysis of the techniques used in these exploits please refer to their analysis by the original discoverers [here](https://securelist.com/root-cause-analysis-of-cve-2018-8174/85486/) and [here](https://blog.trendmicro.com/trendlabs-security-intelligence/use-after-free-uaf-vulnerability-cve-2018-8373-in-vbscript-engine-affects-internet-explorer-to-run-shellcode/).


Because of this dubious popularity of VBScript, multiple security researchers took up the challenge of finding (and reporting) other instances of VBScript vulnerabilities, including a number of variants of those vulnerabilities used in the wild. Notably, researchers working with the Zero day initiative discovered [multiple instances of vulnerabilities](https://www.thezdi.com/blog/2018/5/15/its-time-to-terminate-the-terminator) relying on VBScript Class\_Terminate callback and Yuki Chen of Qihoo 360 Vulcan Team discovered [multiple variants](http://blogs.360.cn/post/from-a-patched-itw-0day-to-remote-code-execution-part-i-from-patch-to-new-0day.html) of CVE-2018-8174 (one of the exploits used in the wild).


As a follow up to those events, this blog post tries to answer the following question: Despite all of the existing efforts from Microsoft and the security community, how easy is it to still discover new VBScript vulnerabilities? And how strong are Windows policies intended to stop these vulnerabilities from being exploited?


Even more VBScript vulnerabilities


The approach we used to find VBScript vulnerabilities was quite straightforward: We used the already published [Domato](https://github.com/googleprojectzero/domato) grammar fuzzing engine and wrote a grammar that describes the built-in VBScript functions, various callbacks and other common patterns. This is the same approach we used successfully [previously](/2017/12/apacolypse-now-exploiting-windows-10-in_18.html) to find multiple vulnerabilities in the JScript scripting engine and it was relatively straightforward to do the same for VBScript. The grammar and the generator script can be found [here](https://github.com/googleprojectzero/domato/tree/master/vbscript).


This approach resulted in uncovering three new VBScript vulnerabilities that we reported to Microsoft and are now fixed. The vulnerabilities are interesting, not because they are complex, but precisely for the opposite reason: they are pretty straightforward (yet, somehow, still survived to this day). Additionally, in several cases, there are parallels that can be drawn between the vulnerabilities used in the wild and the ones we found.


To demonstrate this, before taking a look at the first vulnerability the fuzzer found, let’s take a look at a PoC for the latest VBScript 0day found in the wild:


Class MyClass

Dim array

Private Sub Class\_Initialize

ReDim array(2)

End Sub


Public Default Property Get P

ReDim preserve array(1)

End Property

End Class


Set cls = new MyClass

cls.array(2) = cls



cls.array(2) = cls


In it, the left side is evaluated first and the address of variable at cls.array(2) is computed. Then, the right side is evaluated, and because cls is an object of type MyClass which has a default property getter, it triggers a callback. Inside the callback, the array is resized and the address of the variable computed previously is no longer valid - it now points to the freed memory. This results in writing to a freed memory when the line above gets executed.


Now, let’s compare this sample to the PoC for the first issue we found:


Class MyClass

Private Sub Class\_Terminate()

dict.RemoveAll

End Sub

End Class


Set dict = CreateObject("Scripting.Dictionary")

Set dict.Item("foo") = new MyClass

dict.Item("foo") = 1


On the first glance, this might not appear all that similar, but in reality they are. The line that triggers the issue is


dict.Item("foo") = 1


In it, once again, the left side is allocated first and the address of dict.Item("foo") is computed. Then, a value is assigned to it, but because there is already a value there it needs to be cleared first. Since the existing value is of the type MyClass, this results in a Class\_Terminate() callback, in which the dict is cleared. This, once again, causes that the address computed when evaluating the left side of the expression now points to a freed memory.


In both of these cases, the pattern is:

1. Compute the address of a member variable of some container object
2. Assign a value to it
3. Assignment causes a callback in which the container storage is freed
4. Assignment causes writing to a freed memory


The two differences between these two samples are that:

1. In the first case, the container used was an array and in the second it was a dictionary
2. In the first case, the callback used was a default property getter, and in the second case, the callback was Class\_Terminate.


Perhaps it was because this similarity with a publicly known sample that this variant was also independently discovered by a researcher working with Trend Micro's Zero Day Initiative and Yuki Chen of Qihoo 360 Vulcan Team. Given this similarity, it would not be surprising if the author of the 0day that was used in the wild also knew about this variant.


The second bug we found wasn’t directly related to any 0days found in the wild (that we know about), however it is a classic example of a scripting engine vulnerability:


Class class1

Public Default Property Get x

ReDim arr(1)

End Property

End Class


set c = new class1

arr = Array("b", "b", "a", "a", c)

Call Filter(arr, "a")


In it, a Filter function gets called on an array. The Filter function walks the array and returns another array containing just the elements that match the specified substring ("a" in this case). Because one of the members of the input array is an object with a default property getter, this causes a callback, and in the callback the input array is resized. This results in reading variables out-of-bounds once we return from the callback into the implementation of the Filter function.


A possible reason why this bug survived this long could be that the implementation of the Filter function tried to prevent bugs like this by checking if the array size is larger (or equal) than the number of matching objects at every iteration of the algorithm. However, this check fails to account for array members that do not match the given substring (such as elements with the value of "b" in the PoC).


In their advisory, Microsoft (initially) incorrectly classified the impact of this issue as an infoleak. While the bug results in an out-of-bounds read, what is read out-of-bounds (and subsequently returned to the user) is a VBScript variable. If an attacker-controlled data is interpreted as a VBScript variable, this can result in a lot more than just infoleak and can easily be converted into a code execution. This issue is a good example of why, in general, an out-of-bounds read can be more than an infoleak: it always depends on precisely what kind of data is being read and how it is used.


The third bug we found is interesting because it is in the code that was already heavily worked on in order to address CVE-2018-8174 and the [variants](http://blogs.360.cn/post/from-a-patched-itw-0day-to-remote-code-execution-part-i-from-patch-to-new-0day.html) found by the Qihoo 360 Vulcan Team. In fact, it is possible that the bug we found was introduced when fixing one of the previous issues.


We initially became aware of the problem when the fuzzer generated a sample that resulted in a NULL-pointer dereference with the following (minimized) PoC:


Dim a, r


Class class1

End Class


Class class2

Private Sub Class\_Terminate()

set a = New class1

End Sub

End Class


a = Array(0)

set a(0) = new class2

Erase a

set r = New RegExp

x = r.Replace("a", a)


Why does this result in a NULL-pointer dereference? This is what happens:

1. An array a is created. At this point, the type of a is an array.
2. An object of type class2 is set as the only member of the array
3. The array a is deleted using the Erase function. This also clears all array elements.
4. Since class2 defines a custom destructor, it gets called during Erase function call.
5. In the callback, we change the value of a to an object of type class1.The type of a is now an object.
6. Before Erase returns, it sets the value of variable a to NULL. Now, a is a variable with the type object and the value NULL.
7. In some cases, when a gets used, this leads to a NULL-pointer dereference.


But, can this scenario be used for more than a NULL-pointer dereference. To answer this question, let’s look at step 5. In it, the value of a is set to an object of type class1. This assignment necessarily increases the reference count of a class1 object. However, later, the value of a is going to be set to NULL without decrementing the reference count. When the PoC above finishes executing, there will be an object of type class1 somewhere in memory with a reference count of 1, but no variable will actually point to it. This leads us to a reference leak scenario. For example, consider the following PoC:


Dim a, c, i


Class class1

End Class


Class class2

Private Sub Class\_Terminate()

set a = c

End Sub

End Class


Set c = New class1

For i = 1 To 1000

a = Array(0)

set a(0) = new class2

Erase a

Next


Using the principle described above, the PoC above will increase the reference count for variable c to 1000 when in reality only one object (variable c) will hold a reference to it. Since a reference count in VBScript is a 32-bit integer, if we increase it sufficient amount of times, it is going to overflow and the object might get freed when there are still references to it.


The above is not exactly true, because custom classes in VBScript have protection against reference count overflows, however this is not the case for built-in classes, such as RegExp. So, we can just use an object of type RegExp instead of class1 and the reference count will overflow eventually. As every reference count increase requires a callback, “eventually” here could mean several hours, so the only realistic exploitation scenario would be someone opening a tab/window and forgetting to close it - not really an APT-style attack (unlike the previous bugs discussed) but still a good example how the design of VBScript makes it very difficult to fix the object lifetime issues.


Hunting for reference leaks


In an attempt to find more reference leaks issues, a simple modification was made to the fuzzer: A counter was added and, every time a custom object was created, in the class constructor, this counter was increased. Similarly, every time an object was deleted, this counter was decreased in the class destructor. When a sample finishes executing and all variables are clear, if this counter is larger than 0, this means there was a reference leak somewhere.


This approach immediately resulted in a variant to the previously described reference leak, which is almost identical but uses [ReDim](https://bugs.chromium.org/p/project-zero/issues/detail?id=1673) instead of Erase. Microsoft responded that they are considering this a duplicate of the Erase issue.


Unfortunately there is a problem with this approach that prevents it from discovering more interesting reference leak issues: The approach can’t distinguish between “pure” reference leak issues and reference leak issues that are also memory leak issues and thus don’t necessarily have the same security impact. One example of issues this approach gets stuck on are circular references (imagine that object A has a reference to object B and object B also has reference to object A). However, we still believe that finding reference leaks can be automated as described later in this blog post.


Bypassing VBScript execution policy


As mentioned in the introduction, in Windows 10 Fall Creators Update, Microsoft [disabled](https://blogs.windows.com/msedgedev/2017/07/07/update-disabling-vbscript-internet-explorer-11/#rwFwvJ9JSX18pj2h.97) VBScript execution in Internet Explorer in the Internet Zone and the Restricted Sites Zone by default. This is certainly a step in the right direction. However, let’s also examine the weaknesses in this approach and its implementation.


Firstly, note that, by default, this policy only applies to the Internet Zone and the Restricted Sites Zone. If a script runs (or an attacker can make it run) in the Local Intranet Zone or the Trusted Sites Zone, the policy simply does not apply. Presumably this is to strike a balance between the security for the home users and business users that still rely on VBScript on their local intranet. However, it is somewhat debatable whether leaving potential gaps in the end-user security vs. having (behind-the-times) businesses that still rely on VBScript change a default setting strikes the right balance. In the future, we would prefer to see VBScript completely disabled by default in the Internet Explorer engine.


Secondly, when implementing this policy, Microsoft forgot to account for some places where VBScript code can be executed in Internet Explorer. Specifically, Internet Explorer supports [MSXML](https://en.wikipedia.org/wiki/MSXML) object that has the ability to run VBScript code in XSL Transformations, for example like in the code below.


\<?xml version='1.0'?>

\<xsl:stylesheet version="1.0"

xmlns:xsl="http://www.w3.org/1999/XSL/Transform"

xmlns:msxsl="urn:schemas-microsoft-com:xslt"

xmlns:user="http://mycompany.com/mynamespace">


\<msxsl:script language="vbscript" implements-prefix="user">

Function xml(str)

a = Array("Hello", "from", "VBscript")

xml = Join(a)

End Function

\</msxsl:script>


\<xsl:template match="/">

\<xsl:value-of select="user:xml(.)"/>

\</xsl:template>


\</xsl:stylesheet>


Microsoft did not disable VBScript execution for MSXML, even for websites running in the Internet Zone. This issue was [reported](https://bugs.chromium.org/p/project-zero/issues/detail?id=1669) to Microsoft and fixed at the time of publishing this blog post.


You might think that all of these issues are avoidable if Internet Explorer isn’t used for web browsing, but unfortunately the problem with VBScript (and IE in general) runs deeper than that. Most Windows applications that render web content do it using the Internet Explorer engine, as is the case with Microsoft Office that was used in the recent 0days. It should be said that, earlier this year, Microsoft disabled VBScript creation in Microsoft Office (at least the most recent version), so this popular vector has been blocked. However, there are other applications, including those from third parties, that also use IE engine for rendering web content.


Future research ideas


During this research, some ideas came up that we didn’t get around to implement. Rather than sitting on them, we’ll list them here in case a reader looking for a light research project wants to pick one of them up:


- Combine[VBScript](https://github.com/googleprojectzero/domato/tree/master/vbscript) fuzzer with the [JScript](https://github.com/googleprojectzero/domato/tree/master/jscript) fuzzer in a way that allows VBScript to access JScript objects/functions and vice-versa. Perhaps issues can be found in the interaction of these two engines. Possibly callbacks from one engine (e.g. default property getter from VBScript) can be triggered in unexpected places in the other engine.


- Create a better tool for finding reference leaks. This could be accomplished by running IE in the debugger and setting breakpoints on object creation/deletion to track addresses of live objects. Afterwards, memory could be scanned similarly to how it was done[here](https://github.com/googleprojectzero/p0tools/blob/master/JITServer/cfgtool.cpp) to find if there are any objects alive (with reference count >0) that are not actually referenced from anywhere else in the memory (note: Page Heap should be used to ensure there are no stale references from freed memory).


- Other objects. During the previous year, a number of bugs were found that rely on Scripting.Dictionary object. Scripting.Dictionary is not one of the built-in VBScript objects, but rather needs to be instantiated using CreateObject function. Are there any other objects available from VBScript that would be interesting to fuzz?


Conclusion


VBScript is a scripting engine from a time when a lot of today’s security considerations weren’t in the forefront of anyone’s thoughts. Because of this, it shouldn’t be surprising that it is a crowd favorite when it comes to attacking Windows systems. And although it received a lot of attention from the security community recently, new vulnerabilities are still straightforward to find.


Microsoft made some good steps in attack surface reduction recently. However in combination with an execution policy bypass and various applications relying on Internet Explorer engine to render web content, these bugs could still endanger even users using best practices on up-to-date systems. We hope that, in the future, Microsoft is going to take further steps to more comprehensively remove VBScript from all security-relevant contexts.
