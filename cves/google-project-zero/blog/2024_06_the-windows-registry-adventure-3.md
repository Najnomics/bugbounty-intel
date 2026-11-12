# The Windows Registry Adventure #3: Learning resources - Project Zero

Source: https://projectzero.google/2024/06/the-windows-registry-adventure-3.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk, Google Project Zero


When tackling a new vulnerability research target, especially a closed-source one, I prioritize gathering as much information about it as possible. This gets especially interesting when it's a subsystem as old and fundamental as the Windows registry. In that case, tidbits of valuable data can lurk in forgotten documentation, out-of-print books, and dusty open-source code – each potentially offering a critical piece of the puzzle. Uncovering them takes some effort, but the payoff is often immense. Scraps of information can contain hints as to how certain parts of the software are implemented, as well as why – what were the design decisions that lead to certain outcomes etc. When seeing the big picture, it becomes much easier to reason about the software, understand the intentions of the original developers, and think of the possible corner cases. At other times, it simply speeds up the process of reverse engineering and saves the time spent on deducing certain parts of the logic, if someone else had already put in the time and effort.


One great explanation for how to go beyond the
            binary and utilize all available sources of information was presented by Alex Ionescu in
            the keynote of OffensiveCon 2019 titled ["Reversing
                Without Reversing"](https://www.google.com/url?q=https://www.youtube.com/watch?v%3D2D9ExVc0G10&sa=D&source=editors&ust=1719419260925259&usg=AOvVaw3LnsRqXBHEQsSo_ypMfgN3). My registry security audit did involve a lot of hands-on
            reverse engineering too, but it was heavily supplemented with information not coming directly from
            ntoskrnl.exe. And while Alex's talk discussed researching Windows as a whole, this blog post provides a
            concrete case study of how to apply these ideas in practice. The second goal of the post is to consolidate
            all collected materials into a single, comprehensive summary that can be easily accessed by future
            researchers on this topic. The full list may seem overwhelming as it includes some references to overlapping
            information, so the ones I find key have been marked with the 🔑 symbol. I highly recommend reviewing
            these resources, as they provide context that will be helpful for understanding future posts.

## Microsoft Learn

Official documentation is probably the first and most intuitive thing to study when dealing with a new API. For Microsoft, this means the Microsoft Learn (formerly MSDN Library), a vast body of technical information maintained for the benefit of Windows software developers. It is wholly available online, and includes the following sections and articles devoted to the registry:

- 
            🔑 
            
                
                    [Registry](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry&sa=D&source=editors&ust=1719419260925792&usg=AOvVaw0agpd0xSGxOkcQNj63yNkS)
                – the main page about all registry-related subjects. It contains a wealth of knowledge, and
                is a must read for anyone deeply interested in this system mechanism. It is divided into three sections:
- 
                        [About the Registry](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/sysinfo/about-the-registry&sa=D&source=editors&ust=1719419260926040&usg=AOvVaw2Z-n3Gm2jH6dWyxe8e1FlI)
                    – provides an introduction to the registry and many of its fundamental concepts.
- 
                        [Using the Registry](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/sysinfo/using-the-registry&sa=D&source=editors&ust=1719419260926310&usg=AOvVaw3x3HEA8m9cEwcqAMxVdroL)
                    – provides several examples of how to perform certain common tasks using the Registry
                    API in
                    C++.
- [Registry
                        Reference](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-reference&sa=D&source=editors&ust=1719419260926535&usg=AOvVaw1ucGm_DnsJrbPjiwB-QnQJ) – includes complete documentation of all functions that
                    make
                    up the Registry API (see [Registry
                        Functions](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-functions&sa=D&source=editors&ust=1719419260926667&usg=AOvVaw0M5cMM7jBfGvv6PTHUPgwQ)), and specifies the [Registry
                        element size limits](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-element-size-limits&sa=D&source=editors&ust=1719419260926822&usg=AOvVaw3n9UY5Yu93oMS0YuExsJQG).

- [Windows
                    registry information for advanced users](https://www.google.com/url?q=https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users&sa=D&source=editors&ust=1719419260927075&usg=AOvVaw3wmHnDsrZ0kapdpVJsrWJr) – a separate article that
                discusses the principles of the registry. It appears to be somewhat outdated (the latest version
                mentioned is Windows Vista), and based on an old KB256986 article that can be traced back to [at
                    least 2004](https://www.google.com/url?q=https://web.archive.org/web/20041014015655/http://support.microsoft.com/kb/256986&sa=D&source=editors&ust=1719419260927250&usg=AOvVaw3gsDKCguqwFzwDZYhnh1v6).
- [Inside
                    the Windows NT Registry](https://www.google.com/url?q=https://www.itprotoday.com/windows-78/inside-windows-nt-registry&sa=D&source=editors&ust=1719419260927444&usg=AOvVaw09BQFK_6biwhVlehhEZXEX) and [Inside
                    the Registry](<https://www.google.com/url?q=https://learn.microsoft.com/en-us/previous-versions//cc750583(v%3Dtechnet.10)&sa=D&source=editors&ust=1719419260927582&usg=AOvVaw0ILGQkrYOswH17UJx985Ye>) – two articles
                published by Mark Russinovich in the Windows NT Magazine in 1997 and 1999, respectively.
- [Windows
                    2000 Registry Reference](<https://www.google.com/url?q=https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc974061(v%3Dmsdn.10)&sa=D&source=editors&ust=1719419260927802&usg=AOvVaw3alclpBc43QVp2dWGV-VkV>) – a web
                mirror of regentry.chm, an official help file bundled with the Windows 2000 Resource Kit. It includes a
                brief introduction to the registry followed by detailed descriptions of the standard registry content,
                i.e. keys and values used for advanced configuration of the system and applications.

- [Windows
                    Server 2003 Resource Kit Registry Reference](<https://www.google.com/url?q=https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc778196(v%3Dws.10)&sa=D&source=editors&ust=1719419260928024&usg=AOvVaw1arlS6ioKQqunhQ-EuKL3Z>) – a similar, but more recent reference for Windows
                Server 2003.

- [Using
                    the Registry Functions to Consume Counter Data](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/perfctrs/using-the-registry-functions-to-consume-counter-data&sa=D&source=editors&ust=1719419260928279&usg=AOvVaw0edjiiNj9ftcHQWWnkGex6) – information about collecting performance data through
                the registry pseudo-keys: HKEY\_PERFORMANCE\_DATA, HKEY\_PERFORMANCE\_TEXT and
                HKEY\_PERFORMANCE\_NLSTEXT.
- [Offline
                    Registry Library](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/devnotes/offline-registry-library-portal&sa=D&source=editors&ust=1719419260928498&usg=AOvVaw0RKTlr3-wRaNznkQcKeuof) – complete
                documentation of the built-in Windows offreg.dll library, which can be used to inspect / operate on
                registry hives without loading them in the operating system.
- Registry system call documentation, e.g.
            [ZwCreateKey](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey&sa=D&source=editors&ust=1719419260928745&usg=AOvVaw0b8--9rg8cL3tmxL0qaruP) – a reference guide to the kernel-mode support of the
                registry, which reveals numerous details about how it works internally and how the high-level API
                functions are implemented under the hood.
- [Filtering
                    Registry Calls](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/filtering-registry-calls&sa=D&source=editors&ust=1719419260928982&usg=AOvVaw22v1Rw2J7WBijPJdxhruLN) – a set of eight articles detailing how to correctly
                implement registry callbacks as a kernel driver developer.

- [CmRegisterCallbackEx
                    function (wdm.h)](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex&sa=D&source=editors&ust=1719419260929252&usg=AOvVaw1Mlmkd6d_H9p7deMfmC9c1) – documentation of the CmRegisterCallbackEx routine
                used for registering callbacks. From there, one can browse to other relevant pages, such as the
                documentation of the [callback
                    function prototype](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function&sa=D&source=editors&ust=1719419260929403&usg=AOvVaw10Rr8gExyjf8OxneIb9MZw), and further to the documentation of all of the
                operation-specific structures (such as [REG\_CREATE\_KEY\_INFORMATION](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_create_key_information&sa=D&source=editors&ust=1719419260929551&usg=AOvVaw1oDgmvtzyO_z0YnuKUVCfZ)).

- [\[MS-RRP\]:
                    Windows Remote Registry Protocol](https://www.google.com/url?q=https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rrp/0fa3191d-bb79-490a-81bd-54c2601b7a78&sa=D&source=editors&ust=1719419260929778&usg=AOvVaw2VamwJMFBN_uq1JE1TXYyk) – technical specification of the RPC
                protocol used by the Remote Registry feature.

## Blogs and online resources

Due to the fact that the registry stores a substantial amount of traces of user activity, it is a popular source of information in forensic investigations. As a result, a number of articles and blog posts have been published throughout the years, focusing on the internal hive structure, registry-related kernel objects, and recovering deleted data. Below is the list of non-official registry resources I have managed to find online, from earliest to latest:


- [WinReg.txt](https://www.google.com/url?q=http://pogostick.net/~pnh/ntpasswd/WinReg.txt&sa=D&source=editors&ust=1719419260930285&usg=AOvVaw1lQoK1mdLSLZKgZ54JV54j),
                author unknown (signed as B.D.) – documentation of the hive binary formats in Windows 3.x
                (SHCC3.10), Windows 95 (CREG) and Windows
                NT (regf) based on reverse engineering. It was likely the first public write-up outlining the
                undocumented structure of the hives.
- [Security
                    Accounts Manager](https://www.google.com/url?q=https://web.archive.org/web/20190717124313/http://www.beginningtoseethelight.org/ntsecurity/index.htm&sa=D&source=editors&ust=1719419260930566&usg=AOvVaw0bzp_31FNjPoRkIucdMJJ5), author unknown (signed as
            clark@hushmail.com) – a comprehensive article primarily focused on the user
                management internals in Windows 2000 and XP, dissecting a number of binary structures used by the
            SAM component. Since user and credential
                management is highly tied to the registry (all of the authentication data is stored there), the article
                also includes a "Registry Structure" section that explains the encoding of regf hive
                files.
- 🔑 [Windows
                    registry file format specification](https://www.google.com/url?q=https://github.com/msuhanov/regf/blob/master/Windows%2520registry%2520file%2520format%2520specification.md&sa=D&source=editors&ust=1719419260930969&usg=AOvVaw01AppKMx17kxmQ40zJDio0), Maxim
                Suhanov – a high-quality and relatively up-to-date specification of the regf format versions 1.3
                to 1.6, with extra bits of information regarding the ancient versions 1.1 and 1.2.
- [Windows
                    NT Registry File (REGF) format specification](<https://www.google.com/url?q=https://github.com/libyal/libregf/blob/main/documentation/Windows%2520NT%2520Registry%2520File%2520(REGF)%2520format.asciidoc&sa=D&source=editors&ust=1719419260931245&usg=AOvVaw3TQI8ty6cYDNqKABWKkhBp>), Joachim Metz – another
                independently developed specification of the regf format associated with the
            libregf library.
- [Push
                    the Red Button](https://www.google.com/url?q=https://moyix.blogspot.com/search/label/registry&sa=D&source=editors&ust=1719419260931479&usg=AOvVaw2jWtpJubQ_9AD1holuohYV), Brendan Dolan-Gavitt (moyix) – a personal blog focused on security, reverse engineering
                and forensics. It contains a number of interesting registry-related posts dating back to
                2007-2009.
- [Windows
                    Incident Response](https://www.google.com/url?q=https://windowsir.blogspot.com/search/label/Registry&sa=D&source=editors&ust=1719419260931760&usg=AOvVaw2KjYL-Dj6josNqSkm2x6p9), Harlan Carvey – a
                technical blog dedicated to incident response and digital analysis of Windows, with a variety of posts
                dealing with the registry published between 2006-2022.
- [My
                    DFIR Blog](https://www.google.com/url?q=https://dfir.ru/?s%3Dregistry&sa=D&source=editors&ust=1719419260932015&usg=AOvVaw3XVMCaxW7BAeqkb3-j8Jaw), Maxim Suhanov – another blog concentrating on digital forensics
                with many mentions of the Windows registry. It provides some original information that's hard to
                find elsewhere, see e.g. [Containerized
                    registry hives in Windows](https://www.google.com/url?q=https://dfir.ru/2020/08/15/containerized-registry-hives-in-windows/&sa=D&source=editors&ust=1719419260932256&usg=AOvVaw3P5QUsQogwenB2aMUZPo46).
- [Digging
                    Up the Past: Windows Registry Forensics Revisited](https://www.google.com/url?q=https://www.mandiant.com/resources/blog/digging-up-the-past-windows-registry-forensics-revisited&sa=D&source=editors&ust=1719419260932565&usg=AOvVaw15OqdOqe4rurf0H8R9AqXE), David Via – a blog post by Mandiant discussing the recovery
                of data from registry hives and transactional logs.
- [Creating
                    Registry Links](https://www.google.com/url?q=https://scorpiosoftware.net/2020/07/17/creating-registry-links/&sa=D&source=editors&ust=1719419260932855&usg=AOvVaw0FpH1t8d08TSokmWL0tNok) and [Mysteries
                    of the Registry](https://www.google.com/url?q=https://scorpiosoftware.net/2022/04/15/mysteries-of-the-registry/&sa=D&source=editors&ust=1719419260933035&usg=AOvVaw1Qn3SYF03C4J05-L-DQ5CM), Pavel Yosifovich – two
                blog posts covering the creation of symbolic links in the registry, and its overall internal
                structure.
- [Windows
                    Registry](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Windows_Registry&sa=D&source=editors&ust=1719419260933296&usg=AOvVaw1jNF0kLz5Ia_x2u7yAbSWI), Wikipedia contributors – as
                usual, Wikipedia doesn't disappoint, and even though the article includes few deeply technical
                details, it features extensive sections on the history of the registry, its high level design and role
                in the system.


Furthermore, [The
                Old New Thing](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/&sa=D&source=editors&ust=1719419260933753&usg=AOvVaw0EWx8a08YtEQfY3wWCBWAY) is a fantastic, technical blog exploring the quirks, design
            decisions, and historical context behind Windows features. It is written by a Microsoft employee of over 30
            years, Raymond Chen, with an astounding consistency of one post per day. While the blog posts are not
        technically documentation, they are very highly regarded in the community and
            can be considered a de-facto Microsoft knowledge resource – only more fun than Microsoft Learn. Over
            the course of the last 20+ years, Raymond would sometimes write about the registry, sharing interesting
            behind-the-scenes stories and anecdotes concerning this feature. I have tried to find and compile all of the
            relevant registry-related posts in the single list below:


- [Why
                    is a registry file called a "hive"?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20030808-00/?p%3D42943&sa=D&source=editors&ust=1719419260934223&usg=AOvVaw01WdHr1SXnVQIrQFfBcK4I) (August 8th, 2003)
- [The
                    long and sad story of the Shell Folders key](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20031103-00/?p%3D41973&sa=D&source=editors&ust=1719419260934467&usg=AOvVaw3Vzz5ZMFiKZULHmtSn6BCy) (November 3rd, 2003)
- [Beware
                    of non-null-terminated registry strings](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20040824-00/?p%3D38063&sa=D&source=editors&ust=1719419260934700&usg=AOvVaw0sTngHTVXtTKcNkiOMUpcl) (August 24th, 2004)
- [The
                    performance cost of reading a registry key](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20060222-11/?p%3D32193&sa=D&source=editors&ust=1719419260934933&usg=AOvVaw1LYUDcRap8eQd6EL5ZUDAT) (February 22nd, 2006)
- [The
                    .Default user is not the default user](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20070302-00/?p%3D27783&sa=D&source=editors&ust=1719419260935174&usg=AOvVaw0kOvsbUVcWUbgbq4vf4vnu) (March 2nd, 2007)
- [Why
                    are INI files deprecated in favor of the registry?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20071126-00/?p%3D24383&sa=D&source=editors&ust=1719419260935440&usg=AOvVaw0K1JKDbzNmAgDTTP6fWsEE) (November 26th, 2007)
- [How
                    did registry keys work in 16-bit Windows?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20080117-00/?p%3D23783&sa=D&source=editors&ust=1719419260935817&usg=AOvVaw0-iIZ8yTaSocz7lqDqhDXv) (January 17th, 2008)
- [Why
                    do registry keys have a default value?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20080118-00/?p%3D23773&sa=D&source=editors&ust=1719419260936041&usg=AOvVaw3EEvRSEj9zMGmj_VWkhBfw) (January 18th, 2008)
- [Why
                    can’t you apply ACLs to registry values?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20090123-00/?p%3D19403&sa=D&source=editors&ust=1719419260936290&usg=AOvVaw2oBGmUYmYwJwXwynmpU-1K) (January 23rd, 2009)
- [What
                    is the terminology for describing the various parts of the registry?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20090204-00/?p%3D19263&sa=D&source=editors&ust=1719419260936528&usg=AOvVaw1i-e6CWT3Yot-ND9Yv8ZIt) (February 4th, 2009)
- [What
                    the various registry data types mean is different from how they are handled](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20090205-00/?p%3D19243&sa=D&source=editors&ust=1719419260936767&usg=AOvVaw3UvT0tacu5DHRjXhSdu6aj) (February 5th, 2009)
- [The
                    inability to lock someone out of the registry is a feature, not a bug](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20090326-00/?p%3D18703&sa=D&source=editors&ust=1719419260937008&usg=AOvVaw3AIcdhVCkoCBlp7oGu2wr4) (March 26th, 2009)
- [Why
                    is there the message '!Do not use this registry key' in the registry?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20110322-00/?p%3D11163&sa=D&source=editors&ust=1719419260937258&usg=AOvVaw1aP67uXZwASfZv92IkVrhI) (March 22nd, 2011)
- [Why
                    is the registry a hierarchical database instead of a relational one?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20110907-00/?p%3D9713&sa=D&source=editors&ust=1719419260937492&usg=AOvVaw0o3fkFGFJlrbOimfjSe33q) (September 7th, 2011)
- [Cheap
                    amusement: Searching for spelling errors in the registry](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20120510-00/?p%3D7663&sa=D&source=editors&ust=1719419260937718&usg=AOvVaw1u_iU--z3w7lAn6JnuTLV6) (May 10th, 2012)
- [What
                    was the registry like in 16-bit Windows?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20120521-00/?p%3D7573&sa=D&source=editors&ust=1719419260937956&usg=AOvVaw02egU_Y-mcEBNRCXNNxcFR) (May 21st, 2012)
- [Why
                    does RegOpenKey sometimes (but not always) fail if I use two backslashes instead of
                    one?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20121004-00/?p%3D6413&sa=D&source=editors&ust=1719419260938196&usg=AOvVaw2wwszWngXZT704yHNQWLNH) (October 4th, 2012)
- [Why
                    do I get notified for changes to HKEY\_CLASSES\_ROOT when nobody is writing to
                    HKEY\_CLASSES\_ROOT?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20121205-00/?p%3D5913&sa=D&source=editors&ust=1719419260938467&usg=AOvVaw0myyGtwpHf6YBG7ch_CHtB) (December 5th,
                2012)
- [RegNotifyChangeKeyValue
                    sucks less](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20150226-00/?p%3D44583&sa=D&source=editors&ust=1719419260938702&usg=AOvVaw047hlj6fm32TH5LH_gXjt3) (February 26th, 2015)
- [So
                    how bad is it that I’m calling RegOpenKey instead of RegOpenKeyEx?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20160120-00/?p%3D92892&sa=D&source=editors&ust=1719419260938946&usg=AOvVaw05mheyvAjmnt-NCgNYewqN) (January 20th, 2016)
- [How
                    can I change a registry key from within the debugger?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20160908-00/?p%3D94275&sa=D&source=editors&ust=1719419260939176&usg=AOvVaw3Z59hNqMxGtPVsKm2IKTZs) (September 8th, 2016)
- [If
                    I simply want to create a registry key but don’t intend to do anything else with it, what
                    security access mask should I ask for?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20161128-00/?p%3D94815&sa=D&source=editors&ust=1719419260939385&usg=AOvVaw0WsnH8VNye5CQ75oWpa5Je) (November 28th, 2016)
- [Diagnosing
                    why you cannot create a stable subkey under a volatile parent key](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20170525-00/?p%3D96225&sa=D&source=editors&ust=1719419260939560&usg=AOvVaw3oxC29G9PZ0U1IfW3WWnT5) (May 25th, 2017)
- [How
                    can I programmatically inspect and manipulate a registry hive file without mounting
                    it?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20181015-00/?p%3D99975&sa=D&source=editors&ust=1719419260939728&usg=AOvVaw0USGVjGop5ZnsxOzD3nehK) (October 15th, 2018)
- [It
                    rather involved being on the other side of this airtight hatchway: Messing with somebody’s
                    registry](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20190109-00/?p%3D100665&sa=D&source=editors&ust=1719419260939898&usg=AOvVaw0KG5HjKheobU-oHUCUNXyz) (January 9th, 2019)
- [Why
                    doesn’t RegSetKeySecurity propagate inheritable ACEs, but SetSecurityInfo
                    does?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20200102-00/?p%3D103287&sa=D&source=editors&ust=1719419260940087&usg=AOvVaw1MKONf9oZuQHMSOSWaAX-m) (January 2nd, 2020)
- [The
                    sad but short story of the SM\_AccessoriesName registry value](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20200310-00/?p%3D103549&sa=D&source=editors&ust=1719419260940260&usg=AOvVaw1cUB77W9RQB76Wos51ludK) (March 10th, 2020)
- [Why
                    does RegNotifyChangeKeyValue stop notifying once the key is
                    deleted?](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20200507-00/?p%3D103733&sa=D&source=editors&ust=1719419260940426&usg=AOvVaw37M0ysGm_RvzzwV3T5mQ5T) (May 7th, 2020)
- [How
                    can I emulate the REG\_NOTIFY\_THREAD\_AGNOSTIC flag on systems that don’t support it? part
                    1](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20201221-00/?p%3D104574&sa=D&source=editors&ust=1719419260940600&usg=AOvVaw1xhCga5yl_O8TyCSqh6kSB) (December 21st, 2020)
- [How
                    can I emulate the REG\_NOTIFY\_THREAD\_AGNOSTIC flag on systems that don’t support it? part
                    2](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20201222-00/?p%3D104582&sa=D&source=editors&ust=1719419260940789&usg=AOvVaw0O6mWlS5iCO2moFHDgIp7L) (December 22nd, 2020)
- [How
                    can I emulate the REG\_NOTIFY\_THREAD\_AGNOSTIC flag on systems that don’t support it? part
                    3](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20201223-00/?p%3D104584&sa=D&source=editors&ust=1719419260941340&usg=AOvVaw1Jiej2alDhR6UF4POxVxaS) (December 23rd, 2020)
- [How
                    can I emulate the REG\_NOTIFY\_THREAD\_AGNOSTIC flag on systems that don’t support it? part
                    4](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20201224-00/?p%3D104599&sa=D&source=editors&ust=1719419260941791&usg=AOvVaw32oqMZqomMlvh1DqQA3U-a) (December 24th, 2020)
- [How
                    can I emulate the REG\_NOTIFY\_THREAD\_AGNOSTIC flag on systems that don’t support it? part
                    5](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20201225-00/?p%3D104602&sa=D&source=editors&ust=1719419260942214&usg=AOvVaw1E0jHpOZNo64Scm4udJyFn) (December 25th, 2020)
- [The
                    history of passing a null pointer as the key name to RegOpenKeyEx](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20210723-00/?p%3D105479&sa=D&source=editors&ust=1719419260942786&usg=AOvVaw1qelrSSSAQgyesL5LTGohR) (July 23rd, 2021)
- [On
                    the failed unrealized promise of RegOverridePredefKey](https://www.google.com/url?q=https://devblogs.microsoft.com/oldnewthing/20231020-00/?p%3D108911&sa=D&source=editors&ust=1719419260943455&usg=AOvVaw2O02OvtNX0tQl8svJpbimS) (October 20th, 2023)

## Academic papers and presentations

Recovering meaningful artifacts from the registry during digital forensics is also a
            problem known in academia. To find relevant works, I often begin by typing the titles of a few known papers
            in [Google
                Scholar](https://www.google.com/url?q=https://scholar.google.com/&sa=D&source=editors&ust=1719419260944494&usg=AOvVaw0YtTbdmRySGLWusI2xMggq), and then delve into a breadth-first search
            of their bibliographies. Here's what I managed to find pertaining to the registry:


- [Forensic
                    analysis of the Windows registry in memory](https://www.google.com/url?q=https://www.sciencedirect.com/science/article/pii/S1742287608000297&sa=D&source=editors&ust=1719419260945439&usg=AOvVaw2WSEbMsB3gaE4Wr_ah3RJg) (2008), Brendan Dolan-Gavitt – a paper detailing
                techniques for extracting and analyzing Windows registry data from physical memory dumps.
- [Recovering
                    deleted data from the Windows registry](https://www.google.com/url?q=http://sentinelchicken.com/research/registry_recovery/&sa=D&source=editors&ust=1719419260946172&usg=AOvVaw2vb0OH8A0LAHei4k0JKzlw) (2008), Timothy D. Morgan – a paper and accompanying
                slide deck that examine deleted registry data structures in NT-based Windows systems, propose an
                algorithm for their recovery, and introduce the RegLookup tool to implement this recovery
                process.
- [Forensic
                    analysis of unallocated space in Windows registry hive files](https://www.google.com/url?q=http://sentinelchicken.com/data/JolantaThomassenDISSERTATION.pdf&sa=D&source=editors&ust=1719419260946926&usg=AOvVaw2dMGxYEU66bxVK7qe0U0aJ) (2008), Jolanta Thomassen – a 63-page MSc dissertation
                demonstrating the feasibility of recovering deleted or updated Windows registry keys from unallocated
                space within hive files.
- [The
                    internal structure of the Windows Registry](https://www.google.com/url?q=https://web.archive.org/web/20090529202753/http://amnesia.gtisc.gatech.edu/~moyix/suzibandit.ltd.uk/MSc/Registry%2520Structure%2520-%2520Main%2520V4.pdf&sa=D&source=editors&ust=1719419260947881&usg=AOvVaw0Us3lO7Q4JHc_08-oFGvdW) (2009), Peter Norris – a 144-page MSc thesis focusing on
                the reconstruction of damaged registry files, analysis of historical states, and the extraction of
                standalone forensic evidence from dispersed fragments.
- [The
                    Windows NT Registry File Format](https://www.google.com/url?q=http://www.sentinelchicken.com/data/TheWindowsNTRegistryFileFormat.pdf&sa=D&source=editors&ust=1719419260948654&usg=AOvVaw2r5dgqdcU9xRI8HULMDHit) (2009),
                Timothy D. Morgan – a concise paper providing a comprehensive description of the regf format data
                structures.
- [Windows
                    Kernel Internals: NT Registry Implementation](https://www.google.com/url?q=https://www.i.u-tokyo.ac.jp/edu/training/ss/lecture/new-documents/Lectures/09-Registry/Registry.pdf&sa=D&source=editors&ust=1719419260949481&usg=AOvVaw2rR2BkNKB0fcaoXBqAsH4L) (2009), David B. Probert – a slide deck discussing the
                registry internals through the lens of the Windows kernel, offering a unique perspective of a Windows
                kernel developer.

## Open-source software

To paraphrase a famous saying, source code is worth a thousand words. Sometimes it is far easier to grasp a concept or design by looking straight at code instead of reading an English explanation. And while the canonical implementation of the registry is the Windows kernel, a number of open-source projects have been developed over the years to operate on registry hives. They are typically either based on regf format analysis performed by the developer itself, or on existing documentation and other open-source tools. The three main reasons for their existence are a) computer forensics, b) emulating Windows behavior on other host platforms, c) directly accessing the SAM hive to change/reset local user credentials. Whatever the reason, such projects may prove useful in better understanding the internal hive format, and help in building proof-of-concept hives if necessary. A list of all the relevant open-source libraries and utilities I have found is shown below:


- [libregf](https://www.google.com/url?q=https://github.com/libyal/libregf&sa=D&source=editors&ust=1719419260951444&usg=AOvVaw1wbD9_bHavG5GJmZhtapst) – a library written in C with Python bindings,
- [hivex](https://www.google.com/url?q=https://github.com/libguestfs/hivex&sa=D&source=editors&ust=1719419260952045&usg=AOvVaw0hmo--_R1EL0lFfFcu0zrq) –
                a library written in C as part of the [libguestfs](https://www.google.com/url?q=https://libguestfs.org/&sa=D&source=editors&ust=1719419260952382&usg=AOvVaw3crw_JVJLgs5MYNBi7s7MI) project, with bindings for OCaml, Perl, Python and
                Ruby,
- [cmlib](https://www.google.com/url?q=https://github.com/reactos/reactos/tree/master/sdk/lib/cmlib&sa=D&source=editors&ust=1719419260952995&usg=AOvVaw2sqQNPUUMV3NWrRZ--xApY) –
                a module implemented in C as part of [ReactOS](https://www.google.com/url?q=https://reactos.org/&sa=D&source=editors&ust=1719419260953315&usg=AOvVaw1KlgNHuZha4B6baXWahSIk), which closely resembles the Windows implementation,
- [chntpw](https://www.google.com/url?q=https://pogostick.net/~pnh/ntpasswd/&sa=D&source=editors&ust=1719419260953855&usg=AOvVaw0JHZPpnmH0ZwyCk8v4aaCG) (The Offline Windows Password Editor) – a tool developed
                in C between 1997-2014 to manage Windows user passwords offline directly in the SAM hive. The
                registry-related code is located in ntreg.c (regf parser) and reged.c (a basic registry editor),
- [Samba](https://www.google.com/url?q=https://www.samba.org/&sa=D&source=editors&ust=1719419260954449&usg=AOvVaw0M9HM1tM-l50d645uRf2c2) – the Samba project includes yet another implementation
                of the Windows registry (under source3/registry and source4/lib/registry),
- [regipy](https://www.google.com/url?q=https://github.com/mkorman90/regipy&sa=D&source=editors&ust=1719419260954958&usg=AOvVaw0RhCPn3TAD4ARIeo1doAD5) – a Python registry hive parsing library and
                accompanying tools,
- [yarp](https://www.google.com/url?q=https://github.com/msuhanov/yarp/&sa=D&source=editors&ust=1719419260955438&usg=AOvVaw12DN7_ee88FD4Xyuimn07r) –
                literally yet another registry parser (in Python),
- [Registry](https://www.google.com/url?q=https://github.com/EricZimmerman/Registry&sa=D&source=editors&ust=1719419260956158&usg=AOvVaw2ZaptRk23JnoVLBVoWsTHc) – a hive parser written in C#,
- [nt-hive](https://www.google.com/url?q=https://github.com/ColinFinck/nt-hive&sa=D&source=editors&ust=1719419260956686&usg=AOvVaw0y1NmJXYcAXA4duUe3gaja) – a hive parser written in Rust (with read-only
                capabilities),
- [Notatin](https://www.google.com/url?q=https://github.com/strozfriedberg/notatin&sa=D&source=editors&ust=1719419260957252&usg=AOvVaw1tg1CYodxFTex-VHDv-AfP) – another hive parser written in Rust, including Python
                bindings and helper binaries.


Lastly, at the time of this writing, simply searching for some internal kernel
            function names on [GitHub](https://www.google.com/url?q=https://github.com/&sa=D&source=editors&ust=1719419260957999&usg=AOvVaw1GBW5kCguqYC_YKYM2U5jh) might
            reveal how certain functionality was implemented in Windows itself 20+ years ago.

## SDK Headers

Header files distributed with Software Development Kits are an interesting case, because on one hand they are an official resource with information that Microsoft intends the developers to use, but on the other – they are a bit more concealed, as online documentation isn't always kept up to date with regards to their contents. We can thus explore their local copies on disk and sometimes find artifacts (function declarations, structure definitions, comments) that are not publicly documented online. Some of the headers most relevant to the registry are:


- [winreg.h](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/api/winreg/&sa=D&source=editors&ust=1719419260959782&usg=AOvVaw0ZBrSIqPhtAe3inJ529PzZ) (user-mode) – the primary registry header on the list,
                containing the prototypes of functions and structures from the official Registry API.
- [wdm.h](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/&sa=D&source=editors&ust=1719419260960477&usg=AOvVaw3cDD1enjMeMLlzYsmAf2aJ) (kernel-mode)
                – specifies a number of interesting constants/flags and types used by the system call interface of
                the registry, for example hive load flags (third argument of NtLoadKey2, such
                as REG\_LOAD\_HIVE\_OPEN\_HANDLE etc.) or key/value query structures
                (KEY\_TRUST\_INFORMATION, KEY\_VALUE\_LAYER\_INFORMATION, etc.).
- [ntddk.h](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/&sa=D&source=editors&ust=1719419260960889&usg=AOvVaw0niS_TzAw-hM92Z2KvXHc0) (kernel-mode)
                – contains some types not found elsewhere, e.g. KEY\_LAYER\_INFORMATION.
- [winnt.h](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/api/winnt/&sa=D&source=editors&ust=1719419260961095&usg=AOvVaw1E28iy16B4PgEF8POYpJOx) (user-mode) – mostly equivalent to wdm.h.
- [winternl.h](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows/win32/api/winternl/&sa=D&source=editors&ust=1719419260961259&usg=AOvVaw1d0osga5nxpsMkcR3PCahf) (user-mode)
                – contains the declarations of some registry-related system calls
                (NtRenameKey, NtSetInformationKey).

## Security research

Learning about prior security research can be especially useful when starting a new project yourself. Not only does it often reveal deep technical details about the target, but it also comes from like-minded professionals who look at the code through a security lens, and may inspire ideas of further weaknesses or areas that require more attention. When it comes to the registry, I think that relatively little work has been done in the public space compared to its high complexity and the pivotal role it plays in the Windows operating system. Nevertheless, there were some materials that I found extremely insightful, especially those by my colleague James Forshaw from Project Zero. The full list of security-relevant resources I have managed to gather on this topic is shown below (including some references to my own publications from the past):


- [Case
                    study of recent Windows vulnerabilities](https://www.google.com/url?q=https://j00ru.vexillium.org/slides/2010/confidence.pdf&sa=D&source=editors&ust=1719419260961763&usg=AOvVaw0_-hjsGRJPbe3zOg5sMppI) (2010), Gynvael Coldwind, Mateusz Jurczyk – a
                presentation on several security bugs Gynvael and I found during our brief registry research in
                2009/2010.
- [Microsoft
                    Kernel Integer Overflow Vulnerability](https://www.google.com/url?q=https://www.fortinet.com/blog/threat-research/microsoft-kernel-integer-overflow-vulnerability&sa=D&source=editors&ust=1719419260961959&usg=AOvVaw3G2wknr8OBH7aIgwdYiQF-) (2016), Honggang Ren – a write-up on CVE-2016-0070, a
                Windows kernel vulnerability in the loading of malformed hive files.
- [Project
                    Zero bug tracker](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/list?q%3Did%253A873%252C874%252C876%252C993%26can%3D1&sa=D&source=editors&ust=1719419260962143&usg=AOvVaw3YT7h6ZbgxaMmg-35a2MA8) (2016), James Forshaw,
                Mateusz Jurczyk – four bug reports submitted to Microsoft as a result of naive registry hive
                fuzzing.
- [Project
                    Zero bug tracker](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/list?q%3Did%253A123%252C215%252C865%252C870%252C871%252C872%252C875%252C1492%252C1494%252C1554%252C1599%252C1786%252C1795%252C2047%252C2048%252C2120%252C2129%26can%3D1&sa=D&source=editors&ust=1719419260962359&usg=AOvVaw3wqrPPu_BmLT9VwglTof1R) (2014-2020), James
                Forshaw – 17 vulnerabilities related to the registry discovered by James, many of them are logic
                issues at the intersection of registry and other system mechanisms (security impersonation, file
                system).

## Books

For a 20+ year old codebase such as the registry, it is expected that some resources
            covering it in the early days were published on paper rather than on the Internet. For this reason, part of
            my standard routine is to search [Google
                Books](https://www.google.com/url?q=https://books.google.com/&sa=D&source=editors&ust=1719419260962643&usg=AOvVaw0-UAZXVeUgJjNJEhCqVwuZ) for various technical terms and keywords
            related to the specific technology and see what pop ups. For the registry, these could be e.g.
            "regedit", "regf", "hbin", "LOG1", "RegCreateKey",
            "NtCreateKey", "HvAllocateCell", "\Registry\Machine", "key control
            block" and so on. In some cases this yields books with unique, strictly technical information, while in
            others the most insightful part is the historical perspective and being able to see how the given technology
            was perceived soon after it first came out. And sometimes the value of the book is a complete surprise until
            it arrives in the mailbox, as it is neither offered for sale as an ebook nor has preview available in Google
            Books, and so a hard copy is required.


The books that I found which are either fully or partially dedicated to the Windows registry are (latest to oldest):


- 🔑 [Windows
                    Internals (Part 2, 7th Edition)](https://www.google.com/url?q=https://www.google.com/books/edition/Windows_Internals_Part_2/L8UIvAEACAAJ?hl%3Den&sa=D&source=editors&ust=1719419260963035&usg=AOvVaw3nOf2wp7mYzIK_V4ps1w69) by Andrea
                Allievi, Alex Ionescu, Mark E. Russinovich, David A. Solomon – the Windows Internals series is an
                in-depth technical guide that delves into the architecture, components, and underlying mechanisms of the
                operating system. The latest edition, covering Windows 10, features a dedicated 35-page chapter on the
                registry, and explores many technical details that are difficult to find elsewhere. Notably, the
                registry has been covered in the book since Windows Internals 4 (corresponding to Windows XP/Server
                2003), with explanations progressively expanding in subsequent editions. Comparing these chapters could
                be an interesting exercise to observe how the registry has evolved throughout the years.
- [Windows
                    Registry Forensics](https://www.google.com/url?q=https://www.google.com/books/edition/Windows_Registry_Forensics/BtVtBgAAQBAJ?hl%3Den&sa=D&source=editors&ust=1719419260963350&usg=AOvVaw0vMnD5Xl-eQljUT5lPZtTW) by Harlan Carvey
- [Microsoft
                    Windows Registry Guide](https://www.google.com/url?q=https://www.google.com/books/edition/Microsoft_Windows_Registry_Guide_2nd_Edi/rayHzwEACAAJ?hl%3Den&sa=D&source=editors&ust=1719419260963534&usg=AOvVaw3FJBsGCrSlM7MgMMITi5FS) by Jerry
                Honeycutt
- [Managing
                    the Windows NT Registry](https://www.google.com/url?q=https://www.google.com/books/edition/Managing_the_Windows_NT_Registry/rYIhAQAAIAAJ?hl%3Den&sa=D&source=editors&ust=1719419260963707&usg=AOvVaw3QUPD9LwuKFhT4EHvK6qct) and [Managing
                    the Windows 2000 Registry](https://www.google.com/url?q=https://www.google.com/books/edition/Managing_the_Windows_2000_Registry/36lOt-iJ6kEC?hl%3Den&sa=D&source=editors&ust=1719419260963831&usg=AOvVaw0NGhMulnvWz9qNm1EyHJM-) by Paul E.
                Robichaux
- [Inside
                    the Registry for Microsoft Windows 95](https://www.google.com/url?q=https://www.google.com/books/edition/Inside_the_Registry_for_Microsoft_Window/zDr22AwXWqsC?hl%3Den&sa=D&source=editors&ust=1719419260964034&usg=AOvVaw3OqukDCCGGF56KUGWYM4o_) by
                Günter Born
- [Inside
                    the Windows 95 Registry](https://www.google.com/url?q=https://www.google.com/books/edition/Inside_the_Windows_95_Registry/ZLZQAAAAMAAJ?hl%3Den&sa=D&source=editors&ust=1719419260964265&usg=AOvVaw0BQ_2kprRoXuQ5dygXqFYs) by Ron
                Petrusha

## Patents

Another useful source of information that may be otherwise difficult to find are
            patents, indexed by [Google
                Patents](https://www.google.com/url?q=https://patents.google.com/&sa=D&source=editors&ust=1719419260964570&usg=AOvVaw1mNgUsigveI52zhI9nWF5u). A particularly valuable result that I found this way is 🔑 [Containerized Configuration](https://www.google.com/url?q=https://patents.google.com/patent/US20170279678A1/en&sa=D&source=editors&ust=1719419260964681&usg=AOvVaw1A0MmARNgoEH6VuVcCMXLo) (US20170279678A1), Microsoft's patent from 2016 that thoroughly
            explains the core concepts behind differencing hives and layered keys in registry. These mechanisms are part
            of a new feature introduced in Windows 10 Anniversary Update to better support containerization, but any
            official documentation of how it works is nowhere to be found. The patent is thus a great aid in
            understanding the intricate aspects of this new registry functionality, adding the necessary context and
            helping to make sense of otherwise highly cryptic kernel functions like
        CmpPrepareDiscardAndReplaceKcbAndUnbackedHigherLayers.

## Manual analysis

So far, all of the resources we've discussed were accessible through a web browser, a text editor, or in physical form. But there is another type of information source that is equally, if not more, important, and that requires more specialized tooling to make sense of it. What I mean by that is the knowledge we can extract from the executable images in Windows responsible for handling the registry, both in terms of the "standard" reverse-engineering and also fully taking advantage of any helpful artifacts in or around them. I'll write more about the hands-on reversing process in upcoming posts, and now we will turn our attention to those artifacts that present us with clear-cut information without the need for deduction.


On a side note, by far the most essential file to be looking at is ntoskrnl.exe, the core NT kernel image. It contains the entirety of the kernel-space registry implementation and is of interest both from the security and functional perspective. I have personally spent 99% of my manual analysis time looking at that particular binary, but it's worth noting that there are a few other executables and libraries related to the registry as well:


- winload.exe – the Windows Boot Loader, which executes before the Windows kernel. One of its responsibilities is to load the SYSTEM hive into memory and read some configuration from it, so it includes a partial copy of the registry code from ntoskrnl.exe.
- offreg.dll – the Offline Registry Library, which also shares some registry code with the kernel (but executes in user-mode).
- kernelbase.dll – one of the primary WinAPI libraries, implementing a majority of the user-space Registry API.
- ntdll.dll – another core user-mode library which provides a bridge between the Registry API and the kernel registry implementation.
- regsvc.dll – a DLL implementing the Remote Registry Service.


Let's investigate what types of information about the registry are readily available to us by running a disassembler/decompiler. I personally use IDA Pro + Hex-Rays and so the examples below are based on them.

### 🔑 Public symbols (PDB)

Microsoft makes public symbols available for a majority of executable images found in
            C:\Windows, for the benefit of developers and security researchers. By "public" symbols I mean PDB
            files that mainly contain the names of functions found in the binaries, which help in symbolizing system
            stack traces during debugging or in the event of a crash. In the past, the symbols used to be bundled with
            the system installation media or on a separate Resource Kit disc, and later they were available for download
            in the form of pre-packaged archives from the Microsoft website. Both of these channels have been
            deprecated, and currently the only supported way to obtain the symbols is on a per-file basis from the
        [Microsoft
                Symbol Server](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/microsoft-public-symbols&sa=D&source=editors&ust=1719419260966122&usg=AOvVaw1CUphRjOVmjkz5MtmvwQ27). The PDB files can be downloaded directly with the official [SymChk](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/using-symchk&sa=D&source=editors&ust=1719419260966252&usg=AOvVaw1Y4RO-pSVwSCNJ4Ki_2mhy) tool, or indirectly through software that supports the symbol
            server (e.g. IDA Pro, WinDbg).


As for ntoskrnl.exe specifically, its accompanying symbols are one of the most
            invaluable sources of information. As mentioned in an earlier post, the Windows kernel follows a consistent
            naming convention, so we can immediately see which internal routines are related to the registry, and where
            the entry points (registry-related system call handlers) that we might start our analysis from are. It shows
            us the extent of the code we are dealing with (1000+ registry functions) and makes it possible to perform
            analysis such as the one shown in [blog
                post #2](/2024/04/the-windows-registry-adventure-2.html) (counting lines of code per system version) out-of-the-box, without doing
            any reverse engineering work. And perhaps most importantly, the function names make it substantially easier
            to reason about the code while doing the actual reversing, especially for functions with very descriptive
            names, like CmpCheckAndFixSecurityCellsRefcount or
        CmpPromoteSingleKeyFromParentKcbAndChildKeyNode.


The other type of information we can find in the kernel debug symbols are types: enums, structures and unions. However, there are two caveats. First, only some types are included in the PDBs, and it's not clear what criteria Microsoft uses to decide whether to publish them or not. My rough estimate is that \~50% of the registry types can be found there, mostly the fundamental ones. Secondly, even though the prototypes of some types are in the symbols, neither the function arguments nor local variables are annotated with their types, so it is still necessary to determine the corresponding types and manually annotate the variables for the decompiled output to make any sense. Nevertheless, having access to this information is still a huge help both in understanding code on a local level and also grasping the bigger picture.


The structures that can be found in the public symbols are:

- Hive descriptors (HHIVE, CMHIVE) and related structures
- Hive bin and cell structures (HBIN, CM\_KEY\_NODE, CM\_KEY\_VALUE, CM\_KEY\_SECURITY, ...)
- Key object related structures (CM\_KEY\_BODY, CM\_KEY\_CONTROL\_BLOCK, ...)
- Some transaction related structures (CM\_TRANS, CM\_KCB\_UOW, ...)
- Some layered-key related structures (CM\_KCB\_LAYER\_INFO, ...)


Meanwhile, the ones that are missing and need to be manually reconstructed are:

- The parse context and path information structures (as used by CmpParseKey)
- Some transaction related structures (on-disk transaction log records, lightweight transaction object descriptors, ...)
- Virtualization-related structures
- Most layered-key related structures


Most of the relevant type names start with
            "CM", so it's easy to find them in the Local Types window in IDA:


I would like to take this opportunity to thank Microsoft for making
            the symbols available for download, and encourage other vendors to do the same for their products.
            🙂


### Debug/Checked builds of Windows

Microsoft used to publish debug/checked builds of Windows (in addition to
            "free" builds) from Windows NT to early Windows 10. The [difference](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/checked-and-free-build-differences&sa=D&source=editors&ust=1719419260968815&usg=AOvVaw0R8e3pRntzVwKO67ew2f2S) between
            them was that the debug/checked builds had some compiler optimizations disabled, and they enabled extra
            debugging checks to identify internal system state inconsistencies as early as possible. The developers of
            kernel-mode drivers were encouraged to test them on debug/checked Windows builds before considering them as
            stable and shipping them to customers. Unfortunately, these special builds have been
            discontinued and don't exist anymore for the
            latest Windows 10 and 11.


These old builds can be quite valuable in the context of reverse engineering, because the extra checks may reveal some invariants and assumptions that the code makes, but which are not obvious when looking at retail builds. What is more, the checks are often verbose and include calls to functions like RtlAssert, DbgPrint, DbgPrintEx etc., passing a textual representation of the failed assertion, the source code file name and/or the line number. These may disclose the names of variables, structure members, enums, constants and other types of information. Let's see some examples:


DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "\tImplausible size %lx\n", v13);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "\tKey is bigger than containing cell.\n");

DbgPrintEx(DPFLTR\_CONFIG\_ID, 0, "invalid name starting with NULL on key %08lx\n", a3);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 0, "invalid (ODD) name length on key %08lx\n", a3);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "\tNo key signature\n");

DbgPrintEx(DPFLTR\_CONFIG\_ID, 0, "\tData:%08lx - unallocated Data\n", v20);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "Class:%08lx - Implausible size \n", v20);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "SecurityCell is HCELL\_NIL for (%p,%08lx) !!!\n", a1, v67);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "SecurityCell %08lx bad security for (%p,%08lx) !!!\n", v86, a1, v73);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 0, "Root cell cannot be a symlink or predefined handle\n");

DbgPrintEx(DPFLTR\_CONFIG\_ID, 0, "invalid flags on root key %lx\n", v31);

DbgPrintEx(DPFLTR\_CONFIG\_ID, 24u, "\tWrong parent value.\n");

The CmpCheckKey function is responsible for verifying the structural correctness of every key in a newly loaded hive, and for every problem it encounters, it prints a more or less verbose message. This can help us better understand what each of these checks is intended to accomplish.


DbgPrintEx(DPFLTR\_CONFIG\_ID, 0, "CmKCBToVirtualPath ==> Could not get name even from parent KCB = %p!!!!\n", a1);

This message can be interpreted as some kind of a fallback mechanism failing when
            converting a registry path. It could indicate an interesting/brittle code construct, and indeed, the
            surrounding code did turn out to be affected by a 16-bit integer overflow and a resulting pool memory
            corruption (reported in Project Zero [issue
                #2341](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2341&sa=D&source=editors&ust=1719419260973702&usg=AOvVaw0SMrH7PXSKM-4BGHgURnhi)). In consequence, the entire block of code (including the vulnerability) was
            removed, as it was functionally redundant and didn't serve any practical purpose.


RtlAssert("(\*VirtContext) & CMP\_VIRT\_IDENTITY\_RESTRICTED", "minkernel\\ntos\\config\\cmveng.c", 3554u, 0i64);

This single line of code in CmpIsSystemEntity reveals a few pieces of information: the name of the function argument (VirtContext), an internal name of a flag that is not documented in any other resources (CMP\_VIRT\_IDENTITY\_RESTRICTED), and the source file name and line number of the expression (minkernel\ntos\config\cmveng.c:3554). Such information can be ported into our main disassembler database (such as an .idb) and later help us better understand other areas of code that use the same object/flags.


DbgPrintEx(DPFLTR\_CONFIG\_ID, 22u, "Error\[1\] %lx while processing CmLogRecActionDeleteKey\n", v12);

This and similar calls in CmpDoReDoRecord inform us of the internal names of the transaction record types (CmLogRecActionCreateKey, CmLogRecActionDeleteKey etc.), which again are not publicly mentioned anywhere else.

## Debugging and experimentation

Poking and prodding the registry of a running Windows system is the last way of learning about it that comes to my mind. In some sense it is a required step, because we can only get so far by reading static documentation and code. At some point, we will be forced to investigate the real memory mappings corresponding to the hives, explore the contents of in-memory registry objects, or verify that a specific function behaves the way we think it does. Thankfully, there are some tools that make it possible to peek into the internal registry state beyond what the standard utilities like Regedit allow. They are briefly described in the sections below.

### Extended Regedit alternatives

The built-in Regedit.exe utility offers quite basic functionality, and while it is
            adequate for most tinkering and system administration purposes, some third party developers have created
            custom registry editors with an extended set of options. I haven't personally used them so
            I cannot attest to their quality, but they may offer some benefits to other
            researchers. One example is [Total
                Registry](https://www.google.com/url?q=https://github.com/zodiacon/TotalRegistry&sa=D&source=editors&ust=1719419260975682&usg=AOvVaw0ndduj9AIaPe2f0oFloYdb), whose main advantage is being able to
            browse the internal registry tree structure (rooted in \Registry) in addition to the standard high-level
            view with the five HKEY\_\* root keys.

### Process Monitor

[Process
                Monitor](https://www.google.com/url?q=https://learn.microsoft.com/en-us/sysinternals/downloads/procmon&sa=D&source=editors&ust=1719419260975937&usg=AOvVaw0D49B5A87nI5PgYZ1zyFlE) is a part of the Sysinternals suite of
            utilities, and is a widely known program for monitoring all file system, registry and process/thread
            activity in Windows in real time. Of course in this case, we are specifically interested in registry
            monitoring. For every operation taking place, we can see a corresponding line in the output window, which
            specifies the time, type of operation, originating process, registry key path, result of the operation and
            other details (all of this is highly configurable):



ProcMon is a great tool for exploring what the registry is like as an interface, and
            how applications in the system use it. It is the most helpful when dealing with logical bugs, and attacking
            more privileged processes through the registry rather
            than attacking the registry implementation itself. For example, I used it to find a suitable exploitation
            primitive for Project Zero [issue
                #2492](https://www.google.com/url?q=https://bugs.chromium.org/p/project-zero/issues/detail?id%3D2492&sa=D&source=editors&ust=1719419260976471&usg=AOvVaw0Mcn_ZMdYfb6ANgKjm2UBy), which allowed me to demonstrate that predefined keys were inherently insecure,
            leading to their deprecation. One of its advantages is that it works out-of-the-box without any special
            system configuration (other than the admin rights required to load a driver), and it's certainly a must
            have in a researcher's toolbox.

### 🔑 WinDbg and the !reg extension

WinDbg attached as a kernel debugger to a test (virtual) machine is the ultimate tool
            to explore the inner workings of the Windows kernel. I have used it extensively at every step of my
            research, to analyze how the registry works, reproduce any bugs that I found, and develop reliable
            proof-of-concept exploits. While its standard debugger functionality is powerful enough for most tasks, it
            also comes with a dedicated [!reg](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-reg&sa=D&source=editors&ust=1719419260976834&usg=AOvVaw1K4yYNzg1gLPti7AfjhOcn) [extension](https://www.google.com/url?q=https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/-reg&sa=D&source=editors&ust=1719419260976946&usg=AOvVaw08nW9BbJ5E_x87T5eW8uAE) that automates the process of traversing registry-specific
            structures and presents them in an accessible way. The full list of its options is shown below:


reg \<command> \<params> - Registry extensions

querykey|q \<FullKeyPath> - Dump subkeys and values

keyinfo \<HiveAddr> \<KnodeAddr> - Dump subkeys and values, given knode

kcb \<Address> - Dump registry key-control-blocks

knode \<Address> - Dump registry key-node struct

kbody \<Address> - Dump registry key-body struct

kvalue \<Address> - Dump registry key-value struct

valuelist \<HiveAddr> \<KnodeAddr> - Dumps list of values for a particular knode

subkeylist \<HiveAddr> \<KnodeAddr> - Dumps list of subkeys for a particular knode

baseblock \<HiveAddr> - Dump the baseblock for the specified hive

seccache \<HiveAddr> - Dump the security cache for the specified hive

hashindex \<HiveAddr> \<conv\_key> - Find the hash entry given a Kcb ConvKey

openkeys \<HiveAddr|0> - Dump the keys opened inside the specified hive

openhandles \<HiveAddr|0> - Dump the handles opened inside the specified hive

findkcb \<FullKeyPath> - Find the kcb for the corresponding path

hivelist - Displays the list of the hives in the system

viewlist \<HiveAddr> - Dump the pinned/mapped view list for the specified hive

freebins \<HiveAddr> - Dump the free bins for the specified hive

freecells \<BinAddr> - Dump the free cells in the specified bin

dirtyvector\<HiveAddr> - Dump the dirty vector for the specified hive

cellindex \<HiveAddr> \<cellindex> - Finds the VA for a specified cell index

freehints \<HiveAddr> \<Storage> \<Display> - Dumps freehint info

translist \<RmAddr|0> - Displays the list of active transactions in this RM

uowlist \<TransAddr> - Displays the list of UoW attached to this transaction

locktable \<KcbAddr|ThreadAddr> - Displays relevant LOCK table content

convkey \<KeyPath> - Displays hash keys for a key path input

postblocklist - Displays the list of threads which have 1 or more postblocks posted

notifylist - Displays the list of notify blocks in the system

ixlock \<LockAddr> - Dumps ownership of an intent lock

finalize \<conv\_key> - Finalizes the specified path or component hash

dumppool \[s|r\] - Dump registry allocated paged pool

s - Save list of registry pages to temporary file

r - Restore list of registry pages from temp. file

As we can see, the extension offers a wide selection of commands related to various components of the registry: hives, keys, values, security descriptors, transactions, notifications and so on. I have found many of them to be immensely useful, either on a regular basis (e.g. querykey, kcb, hivelist), or for more specialized tasks when experimenting with a particular feature (e.g. translist, uowlist for transactions).


The best way to discover its potential is to see it in action on a specific example. I used a Windows 11 guest system for this purpose. Let's query an existing HKEY\_LOCAL\_MACHINE\Software\DefaultUserEnvironment key to find out more about it:


kd> !reg querykey \Registry\Machine\Software\DefaultUserEnvironment



Found KCB = ffff888788731ad0 :: \REGISTRY\MACHINE\SOFTWARE\DEFAULTUSERENVIRONMENT


Hive ffff88877af5c000

KeyNode 000001e6ed0334b4


\[ValueType\] \[ValueName\] \[ValueData\]

REG\_EXPAND\_SZ Path %USERPROFILE%\AppData\Local\Microsoft\WindowsApps;

REG\_EXPAND\_SZ TEMP %USERPROFILE%\AppData\Local\Temp

REG\_EXPAND\_SZ TMP %USERPROFILE%\AppData\Local\Temp

Here, we have referenced the key by its internal NT object manager registry path starting with \Registry. The relation between the high-level paths known from Regedit / the Registry API and the internal paths used by the kernel will be detailed in a future post – for now, we just need to know that these paths are equivalent. We can learn a few things from the command output: the key is cached in memory and the KCB (Key Control Block, represented by the CM\_KEY\_CONTROL\_BLOCK structure) is located at address 0xffff888788731ad0. The address of the SOFTWARE hive descriptor is 0xffff88877af5c000, and that's where the HHIVE / CMHIVE structures are stored. HHIVE is the first member of CMHIVE at offset 0, hence why their addresses line up, similar to how the KPROCESS / EPROCESS structures work. Furthermore, the key node (CM\_KEY\_NODE), the definitive representation of a key within the hive file, is mapped at address 0x1e6ed0334b4. You may notice that this is a user-mode address, and that's because in modern versions of Windows, hive files are generally operated on via section-based mappings within the user address space of a thin "Registry" process (you can find it in Task Manager). Lastly, we can see that the key has three values and we are provided with their types, names and data.


Next, we can use !reg kcb to learn more about the key based on its cached KCB data:


kd> !reg kcb ffff888788731ad0


Key : \REGISTRY\MACHINE\SOFTWARE\DEFAULTUSERENVIRONMENT

RefCount : 0x0000000000000001

Flags : CompressedName,

ExtFlags :

Parent : 0xffff88877ab517e0

KeyHive : 0xffff88877af5c000

KeyCell : 0xe824b0 \[cell index\]

TotalLevels : 4

LayerHeight : 0

MaxNameLen : 0x0

MaxValueNameLen : 0x8

MaxValueDataLen : 0x66

LastWriteTime : 0x 1d861d2:0xdb7718d1

KeyBodyListHead : 0xffff888788731b48 0xffff888788731b48

SubKeyCount : 0

Owner : 0x0000000000000000

KCBLock : 0xffff888788731bc8

KeyLock : 0xffff888788731bd8

This is a summary of some of the KCB components that the author of the extension deemed the most important. We can see the value of the reference count, flags shown in textual form, the KCB address of the key's parent, the address of the hive, etc. Let's resolve the virtual address of the key node by using !reg cellindex:


kd> !reg cellindex 0xffff88877af5c000 0xe824b0


Map = ffff88877ec20000 Type = 0 Table = 7 Block = 82 Offset = 4b0

MapTable = ffff88877ec37000

MapEntry = ffff88877ec37c30

BinAddress = 000001e6ed033001, BlockOffset = 0000000000000000

BlockAddress = 000001e6ed033000


pcell: 000001e6ed0334b4

The result is 0x1e6ed0334b4, the same value that !reg querykey returned to us earlier. In order to inspect the contents of the key node, we can use !reg knode:


kd> !reg knode 1e6ed0334b4


Signature: CM\_KEY\_NODE\_SIGNATURE (kn)

Name : DefaultUserEnvironment

ParentCell : 0x20

Security : 0x98f300 \[cell index\]

Class : 0xffffffff \[cell index\]

Flags : 0x20

MaxNameLen : 0x0

MaxClassLen : 0x0

MaxValueNameLen : 0x8

MaxValueDataLen : 0x66

LastWriteTime : 0x 1d861d2:0xdb7718d1

SubKeyCount\[Stable \]: 0x0

SubKeyLists\[Stable \]: 0xffffffff

SubKeyCount\[Volatile\]: 0x0

SubKeyLists\[Volatile\]: 0xffffffff

ValueList.Count : 0x3

ValueList.List : 0xe825a8

A very similar effect can be achieved by finding the Registry process, switching to its context, and inspecting the memory directly by overlaying it onto the CM\_KEY\_NODE structure layout:


kd> !process 0 0

\*\*\*\* NT ACTIVE PROCESS DUMP \*\*\*\*

PROCESS ffffe30198ef5040

SessionId: none Cid: 0004 Peb: 00000000 ParentCid: 0000

DirBase: 001ae002 ObjectTable: ffff88877a285f00 HandleCount: 3302.

Image: System


PROCESS ffffe30198fe1080

SessionId: none Cid: 0040 Peb: 00000000 ParentCid: 0004

DirBase: 1002c002 ObjectTable: ffff88877a277b40 HandleCount: 0.

Image: Registry


\[...\]


kd> .process ffffe30198fe1080

Implicit process is now ffffe301\`98fe1080

WARNING: .cache forcedecodeuser is not
            enabled

kd> dt \_CM\_KEY\_NODE 1e6ed0334b4

nt!\_CM\_KEY\_NODE

+0x000 Signature : 0x6b6e

+0x002 Flags : 0x20

+0x004 LastWriteTime : \_LARGE\_INTEGER 0x01d861d2\`db7718d1

+0x00c AccessBits : 0x3 ''

+0x00d LayerSemantics : 0y00

+0x00d Spare1 : 0y00000 (0)

+0x00d InheritClass : 0y0

+0x00e Spare2 : 0

+0x010 Parent : 0x20

+0x014 SubKeyCounts : \[2\] 0

+0x01c SubKeyLists : \[2\] 0xffffffff

+0x024 ValueList : \_CHILD\_LIST

+0x01c ChildHiveReference : \_CM\_KEY\_REFERENCE

+0x02c Security : 0x98f300

+0x030 Class : 0xffffffff

+0x034 MaxNameLen : 0y0000000000000000 (0)

+0x034 UserFlags : 0y0000

+0x034 VirtControlFlags : 0y0000

+0x034 Debug : 0y00000000 (0)

+0x038 MaxClassLen : 0

+0x03c MaxValueNameLen : 8

+0x040 MaxValueDataLen : 0x66

+0x044 WorkVar : 0

+0x048 NameLength : 0x16

+0x04a ClassLength : 0

+0x04c Name : \[1\] "敄"

In the listing above, we can see the full extent of information stored in the hive for each key. The name in the last line is incorrectly displayed as 敄, because formally the type of CM\_KEY\_NODE.Name is wchar\_t\[1\], but since the name consists of ASCII-only characters, it is compressed down so that each wchar\_t element stores two characters of the name (as indicated by the flag 0x20 translated by WinDbg as CompressedName). So 敄 is in fact the two first letter of the name, "De", represented as a UTF-16 code point.


This is only a glimpse of what is possible with WinDbg and the !reg extension. I highly encourage you to experiment with other options if you're curious about the mechanics of the registry and want to explore further.

## Conclusion

In this post, I have aimed to share my methodology for gathering information and learning about new vulnerability research targets. I hope that you find some of it useful, either as a generalized approach that applies to other software, or as a comprehensive knowledge base for the registry itself. Also, if you think I've missed any resources, I'll be more than happy to learn about them. See you in the next post!
