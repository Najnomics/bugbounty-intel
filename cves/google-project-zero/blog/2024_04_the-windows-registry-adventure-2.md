# The Windows Registry Adventure #2: A brief history of the feature - Project Zero

Source: https://projectzero.google/2024/04/the-windows-registry-adventure-2.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk, Google Project Zero


Before diving into the low-level security aspects of the registry, it is important to understand its role in the operating system and a bit of history behind it. In essence, the registry is a hierarchical database made of named "keys" and "values", used by Windows and applications to store a variety of settings and configuration data. It is represented by a tree structure, in which keys may have one or more sub-keys, and every subkey is associated with exactly one parent key. Furthermore, every key may also contain one or more values, which have a type (integer, string, binary blob etc.) and are used to store actual data in the registry. Every key can be uniquely identified by its name and the names of all of its ascendants separated by the special backslash character ('\'), and starting with the name of one of the top-level keys (HKEY\_LOCAL\_MACHINE, HKEY\_USERS, etc.). For example, a full registry path may look like this: HKEY\_CURRENT\_USER\Software\Microsoft\Windows. At a high level, this closely resembles the structure of a file system, where the top-level key is equivalent to the root of a mounted disk partition (e.g. C:\), keys are equivalent to directories, and values are equivalent to files. One important distinction, however, is that keys are the only type of securable objects in the registry, and values play a much lesser role in the database than files do in the file system. Furthermore, specific subtrees of the registry are stored on disk in binary files called registry hives, and the hive mount points don't necessarily correspond one-to-one to the top-level keys (e.g. the C:\Windows\system32\config\SOFTWARE hive is mounted under HKEY\_LOCAL\_MACHINE\Software, a one-level nested key).


Fundamentally, there are only a few basic operations that can be performed in the registry. These operations are summarized in the table below:

| Hives |  |  | 
| Load hive | Unload hive | Flush hive to disk | 
| Keys |  |  | 
| Open key | Create key | Delete key | 
| Rename key | Set/query key security | Set/query key flags | 
| Enumerate subkeys | Notify on key change | Query key path | 
| Query number of open subkeys | Close key handle |  | 
| Values |  |  | 
| Set value | Delete value | Enumerate values | 
| Query value data |  |  | 


Before we dive into any of them in particular, let's first trace the registry's evolution and the path that led to its current state.

## Windows 3.1

The registry was first introduced in Windows 3.1 released in 1992. It was designed as a centralized configuration store meant to address the many shortcomings of basic text configuration files from MS-DOS (e.g. config.sys) and the slightly more structured .INI files from very early versions of Windows. But the first registry was nothing like we know it today: there was only one top-level key (an equivalent of HKEY\_CLASSES\_ROOT) and only one hive (C:\windows\reg.dat) limited to 64 KB in size, formatted in a custom binary format represented by the magic bytes "SHCC3.10". There were no values (data was assigned directly to keys), and the registry was used solely for OLE/COM and file type registration. This is what the first Regedit.exe looked like when launched in advanced mode:


The first Registry Editor running on Windows 3.1


Despite its limitations, the Windows 3.1 registry was an important milestone, as it established long-lasting concepts like its hierarchical structure and paved the way for today's advanced registry features.

## Windows NT 3.1, 3.5 and 3.51

One year later in 1993, a new version of Windows was released based on a completely refreshed and more robust kernel design: Windows NT 3.1. To this day, the original NT kernel continues to be the underpinning of all modern versions of Windows up to and including Windows 11 – and the same can be said for its registry implementation. The biggest functional registry changes found in Windows NT 3.x as compared to Windows 3.1 were:

- Introducing many new top-level keys (HKLM, HKCU, HKU) and thus extending the scope of information intended to be stored in the registry.
- Replacing the single reg.dat hive file with a number of separate hives (default, sam, security, software, system located in C:\winnt\system32\config).
- Introducing named values with several possible data types.
- Making registry keys securable.
- Eliminating the 64 KB registry hive limit.


To accommodate these new features, Windows adopted a novel binary format called "regf", which was specifically designed to support the expanded functionality. The core principles behind the format remained unchanged across the NT 3.x version line, but it continued to internally evolve, as signified by the increasing version numbers encoded in the hive file headers. Specifically, pre-release builds of Windows NT 3.1 used regf v1.0, Windows NT 3.1 RTM used regf v1.1, and Windows NT 3.5 and 3.51 used regf v1.2.


Lastly, while Regedit.exe remained the simplistic "Registration Info Editor", a new utility, RegEdt32.exe, was added with far more options and unrestricted access to the system registry. Despite its dated appearance, the structure of the UI began to resemble the shape of the modern registry and the core concepts behind today's registry editor:


RegEdt32.exe running on Windows NT 3.1


Notably, Windows NT 3.1 was the first system whose parts of code are still used today in Windows 11. Based on this observation, we can now confidently claim that the registry code base is over 30 years old.

## Windows 95

Not long after, in the summer of 1995, Windows 95 was officially released to the public. It quickly became a huge hit, mostly thanks to innovations in the user interface – it was the first version to feature a taskbar, the Start menu, and the general look and feel that we now associate with Windows. With regards to the registry internals, though, it wasn't particularly interesting. It continued the trend started by Windows NT 3.x of expanding the registry into an even more central part of the operating system, and borrowed many of the same high-level concepts. However, since it was based on a completely different kernel than NT, the underlying registry implementation differed, too. All of the registry data was typically stored in just two files: C:\WINDOWS\System.dat and C:\WINDOWS\User.dat. They were encoded in yet another binary format indicated by the "CREG" signature, which was more capable than the Win3.1 format, but inferior to WinNT's regf (e.g. it didn't support security descriptors). The same format was later inherited by subsequent systems from the 9x series, namely Windows 98 and Me, but its legacy ended there. According to my knowledge, the CREG format had minimal impact on the registry's development in the NT line, so a deeper discussion of its internals isn't necessary.


Arguably, the one thing that had the most lasting impact in Windows 95 related to registry was the complete redesign of Regedit.exe, both functionally and visually. It gained the ability to browse the entire registry tree, read existing values and create new ones, rename keys, and search for text strings within keys, values and data. At first glance, it looks almost identical to the modern Registry Editor, with the exception of a few missing options, such as loading custom hives or managing key security. Even the program icon has remained largely unchanged and to many power users, it is synonymous with the Windows registry up to this day:


Redesigned Regedit.exe running on Windows 95

## Windows NT 4.0

The debut of Windows NT 4.0 in 1996 marked another important milestone for the registry, but this time mostly on the technical side. In terms of visuals, NT 4.0 adopted the same graphical interface as Windows 95, including the new and improved Regedit.exe. As a result of the Regedit addition, Windows NT 4.0 now included two competing registry editors: Regedit from Windows 95 and RegEdt32 from Windows NT 3.x. They shared some overlapping functionality (e.g. the ability to manually traverse the registry and inspect individual values), but each offered some unique features too: only Regedit was capable of searching for data in values, while only RegEdt32 supported managing the security of registry keys. I suspect that the presence of two different tools must have been confusing for users who wanted to modify the system's internal settings: not only did they have to understand the structure of the registry and how to navigate it, but also know which tool to use for a specific task. Both utilities made their way into Windows 2000, but they were finally merged in Windows XP into a single Regedit.exe program. RegEdt32.exe can still be found on modern versions of Windows in C:\Windows\system32 as a historical artifact, but all it currently does is just launch Regedit.exe and terminate.


As mentioned earlier, the really important changes in NT 4.0 happened under the hood. Between the release of NT 3.51 and NT 4.0, the kernel developers updated some internal aspects of the regf format to simplify it and make it more efficient. Furthermore, a new optimization called "fast leaves" was introduced, which added special four-byte hints to the subkey lists in order to speed up key lookups. These changes were substantial and not backwards-compatible, so the version had to be increased again, leading to regf v1.3. This is noteworthy because 1.3 is the earliest hive type that is considered a modern version and that is still supported by today's Windows 10 and 11, even though newer format versions up to 1.6 exist now too. It means that one can copy a hive file off of a Windows NT 4.0 system, load it in Regedit on Windows 11, examine and modify it, copy it back, and each of these steps will work without issue. What is more, the support is not just there for reading archival hives – in documented API functions such as [RegSaveKeyExA](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regsavekeyexa), version 1.3 is represented by the REG\_STANDARD\_FORMAT enum, indicating that it is considered the "standard" even as of today. And indeed, there are some core system hives in Windows 11, such as UsrClass.dat mounted at HKEY\_USERS\\\<SID>\_Classes, that are still encoded in the regf v1.3 format. So in that sense, Windows NT 4.0 and 11, despite being released decades apart and representing vastly different technological eras, exhibit a fundamental connection.

## Modern times

Based on the fact that both the regf hive format and the graphical interface of Regedit have essentially remained the same between 1996 and 2024, one could assume that the internal registry implementation hasn't changed that much, either. We can try to prove or disprove this hypothesis by performing a little experiment, measuring the volume of registry-related code in each consecutive version of Windows. To ensure a consistent methodology and make the survey security-relevant, we will focus on the kernel-mode part of the Configuration Manager, which largely constitutes a local attack surface. Such an analysis is technically feasible and even relatively easy to achieve, because:

- The entirety of the kernel registry-related code is compiled into a single executable image: ntoskrnl.exe.
- Debug symbols (PDB/DBG files) for the kernels of all NT-family systems were made publicly available by Microsoft, either via the Microsoft Symbol Server, symbol packages downloadable from the Microsoft website, or symbol files bundled with the system installation media.
- The kernel code follows a consistent naming convention, where all function names related to the registry start with either "Hv" (standing for Hive), "Cm" (standing for Configuration Manager) or "Vr" (likely standing for Virtualized Registry), with a few minor exceptions.
- There are some very good reverse-engineering tools available today, which can help us count the number of assembly instructions or even the number of decompiled C-like source code lines corresponding to the registry engine.


In my case, I used IDA Pro with Hex-Rays to decompile the entire kernel of each NT-line system, and then ran a post-processing script to extract the registry related functions. After counting the numbers of lines and plotting them on a diagram, here is what we get:



As we can see, there has been an enormous, steady growth of the code base, starting at around 10,000 lines of code in NT 4.0 and increasing tenfold to around 100,000 lines in Windows 11. It is important to reiterate that this only covers the kernel portions of the registry and ignores code found in user-mode libraries such as advapi32.dll, KernelBase.dll or ntdll.dll. Furthermore, I expect that the decompiled code is more dense than the original source code because it doesn't include any comments or whitespace. Taking all this into account, the total extent of the registry code managed by Microsoft is probably much bigger than the numbers shown above.


Going back to the kernel registry code, its expansion in time has been substantial, both in absolute and relative terms. But if these developments are invisible to the average user, what does all of the new code do? The changes can be divided into three major categories:

- Optimizations: changes making the registry more efficient, e.g. introducing a "hash leaf" subkey index type to make key lookups even faster in regf v1.5, or adding a native system call to rename keys in-place without involving an expensive copy+delete operation on an entire subtree.
- Backwards compatibility: changes meant to make legacy applications run seamlessly on modern systems, e.g. [registry virtualization](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-virtualization).
- New features: changes adding new functionality to the registry or adapting it to new use cases. These are either made available via a new API (thus mainly relevant to software developers), or not documented at all and only used by Windows internally. Examples include support for values larger than 1 MB, [registry callbacks](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex), [support for transactions](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeytransactedw), [application hives](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regloadappkeyw), and differencing hives.


Interestingly, the biggest changes weren't occurring with any regularity, but rather were concentrated in just four versions of Windows: NT 3.1–4.0, XP, Vista and 10 Anniversary Update (1607). This is illustrated in the timeline below:



This is of course not an exhaustive list: it includes the features that I have found to be the most interesting during the security audit, but it is missing modifications related to incremental logging, improvements to how hive files are managed and mapped in memory, and many other optimizations, stability improvements and refactorings implemented by Microsoft throughout the years. But it goes to show that the registry is a highly complex part of the Windows kernel, and one with a lot of potential for deep, interesting bugs just waiting to be discovered.


In the next post, I will share a number of useful sources of information I have discovered while researching the registry. Some of them may be more obvious than others, but all of them have significantly helped me understand certain aspects of the technology or given me the necessary context that I was missing. Until next time!
