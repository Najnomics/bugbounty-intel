# 🛡️ RoKRAT: A New Level of Stealth by APT37

- **Source URL:** https://www.genians.co.kr/en/blog/threat_intelligence/rokrat_shellcode_steganographic
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/393 (id 393)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## **◈ Key Findings**

- A new variant of the RoKRAT malware used by the APT37 group has been identified.
- The malware employs a two-stage encrypted shellcode injection method to hinder analysis.
- A steganography technique was discovered in which malicious code is concealed within image files.
- Fileless attacks continue to be used to evade detection by security solutions.
- Efficient EDR monitoring optimized for abnormal endpoint behavior detection is now essential.

## **1.  Overview**

Genians Security Center (GSC) has identified a new variant of the malware used by the APT37 group during an ongoing analysis. This threat actor is known for employing a malware strain commonly referred to as RoKRAT. In this case, the attacker utilizes shortcut files with the .lnk extension, embedding Cmd or PowerShell commands within them to carry out the attack.

This type of attack continues to be observed in South Korea, indicating a high level of threat activity. Its persistence suggests that it remains an effective method of compromise. For this reason, security administrators at organizations or institutions with multiple business endpoints must stay informed about the various attack techniques and tactics associated with this threat.

Shortcut files typically feature a small arrow in their default icon, allowing them to be distinguished visually to some extent. Of course, user-created shortcuts for folders or files are generally harmless and should not be misunderstood. However, if a shortcut file is found inside a compressed archive received via email or instant messaging platforms such as SNS, it is highly likely to be malicious. Security administrators should therefore understand how modern threats are delivered, the characteristics of file extensions, and the distinct visual traits of icons.

Enhancing employees’ security awareness through regular internal training and case sharing can significantly improve the organization’s overall security posture. In addition, adopting EDR or MDR solutions can help establish a more systematic and efficient threat management framework.

This report provides technical insights based on recent threat cases, and can be used to support the development of effective defense strategies.



## **2. Background** 

Genians continuously analyzes the diverse threat activities of the APT37 group and provides threat intelligence reports to support cyber threat response efforts.

- [Analysis of APT37 Attack Case Disguised as a Think Tank for National Security Strategy in South Korea](https://www.genians.co.kr/en/blog/threat_intelligence/toybox-story?hsLang=en)
  - Operation. ToyBox Story
- [Analysis of malicious HWP cases of 'APT37' group distributed through K messenger](https://www.genians.co.kr/blog/threat_intelligence/k-messenger?hsLang=en)
- [Analysis of Cyber Recon Activities Behind APT37 Threat Actor](https://www.genians.co.kr/blog/threat_intelligence/apt37_recon?hsLang=en)

Through case-based analysis by attack type, organizations can gain insight into the evolving tactics and patterns of Advanced Persistent Threats (APTs). While APT37 is known to be linked to North Korea, the threat level posed by state-sponsored hacking groups from countries such as China and Russia is also rising. Previously known attack tools continue to evolve, making ongoing analysis and research increasingly important.

\[Figure 2-1\] Attack Scenario



## **3. Technical Analysis**

### 
**3-1. Analysis of Shortcut (LNK) File**

The malware was distributed via a compressed file named "국가정보와 방첩 원고.zip(*National Intelligence and Counterintelligence Manuscript.zip*)". Inside the archive is a shortcut file titled “국가정보와 방첩 원고.lnk(*National Intelligence and Counterintelligence Manuscript.lnk*)”.

This LNK file is unusually large, with a file size of approximately 54MB (54,160,170 bytes). The abnormal size is due to the inclusion of multiple hidden components within the shortcut, including a decoy document and the RoKRAT shellcode.

Standard shortcut files generally store only simple text-based information, such as file paths and icon metadata, and typically do not exceed a few dozen kilobytes (KB) in size.

\[Figure 3-1\] Distributed Malicious File


The shortcut file contains the following four embedded elements:


\[Figure 3-2\] LNK File Structure and Code Correlation Analysis


The shortcut file contains the following four embedded data:

- A legitimate decoy HWP document
- Shellcode file (ttf01.dat)
- PowerShell command (ttf02.dat)
- Batch command script (ttf03.bat)

Excluding the decoy document, the execution flow of the data is as follows:

- ttf03.bat -> ttf02.dat -> ttf01.dat


\[Figure 3-3\] Code Execution Flow


The ttf03.bat batch file triggers a sequence of PowerShell commands. These commands sequentially execute ttf02.dat to load ttf01.dat, which contains the shellcode block, and apply XOR operations for decoding.


| $exeFile = Get-Content -path $exePath -encoding byte $len = $exeFile.count $newExeFile = New-Object Byte\[\] $len $xK = '3' for ($i = 0; $i -lt $len; $i++) { $newExeFile\[$i\] = $exeFile\[$i\] -bxor $xK\[0\] } | 

\[Table 3-1\] XOR Operation Logic


In the PowerShell script, the string $xK='3' is declared, where the first character corresponds to the ASCII value 0x33 (decimal 51). This value functions as the key used in the XOR operation.

Each byte is decoded using the logic $exeFile\[$i\] -bxor $xK\[0\].

To manually perform the decoding process, the following PowerShell command can be used. This generates the decoded file, named ‘ttf01.dat\_decode’.


| $key = '3' $keyByte = \[byte\]\[char\]$key $inputFile = "D:\ttf01.dat" $outputFile = "D:\ttf01.dat\_decode" $encodedBytes = Get-Content -Path $inputFile -Encoding Byte $decodedBytes = New-Object Byte\[\] $encodedBytes.Length for ($i = 0; $i -lt $encodedBytes.Length; $i++) { $decodedBytes\[$i\] = $encodedBytes\[$i\] -bxor $keyByte } \[IO.File\]::WriteAllBytes($outputFile, $decodedBytes) Write-Host "XOR decoding complete. Output saved to: $outputFile" | 

\[Table 3-2\] PowerShell XOR File Conversion Command


This command enables manual decoding for sequential code analysis in a more convenient manner.


\[Figure 3-4\] Example of Manual PowerShell Decoding


Upon reviewing the decoded content, it is found to contain a typical shellcode block. To conduct a detailed shellcode analysis, further code debugging and payload verification are required.


\[Figure 3-5\] Shellcode Comparison View


### **3-2. Shellcode Analysis**

The XOR transformation logic can be verified through the shellcode debugging process.


\[Figure 3-6\] XOR Transformation Process


Based on the original shellcode data, the XOR operation begins at offset 00000590, using a single-byte key value of 0xAE.

The decoded data is identified as a 32-bit executable (EXE) file. Its Time Date Stamp is 2025-04-21 00:39:59 (UTC), suggesting that the threat actor created the malware at 09:39 AM KST (UTC+9).

The file contains Program Database (PDB) information. PDB files are debugging data generated when a program is built using tools such as Visual Studio on Windows. These files include symbol information, source code mappings, variable names, function names, and other information necessary for debugging.

PDB information embedded in malware can be used to extract various developer-related details and often serves as a clue for identifying similar variants.

- Local file path of the program
- Project name
- Developer information
- Malware type
- Malware version, etc


\[Figure 3-7\] DebugData PDB Path Information


The information includes the string “InjectShellcode”, which may offer insight into the developer’s intent.


| D:\Work\Util\InjectShellcode\Release\ **InjectShellcode.pdb** | 

\[Table 3-3\] PDB String Information


Among the various RoKRAT variants, this is the first time the string "InjectShellcode" has been identified. This appears to be intended to hinder antivirus detection and malware analysis.


\[Figure 3-8\] Memory Injection Routine into the mspaint.exe Process


The 'InjectShellcode' module creates a process for 'mspaint.exe', which is the Windows Paint program, located in the hardcoded path 'C:\Windows\SysWOW64', using the CreateProcessW API function.

Note that in 64-bit environments, Windows uses the Windows-on-Windows 64 (WOW64) subsystem to execute 32-bit applications without modification. However, in recent versions of Windows 11, mspaint.exe is no longer located in the SysWOW64 or System32 directories, as it has been transitioned to a Universal Windows Platform (UWP) application. Although the exact transition date is unclear, user reports suggest that the classic Paint application was removed around October 2024 through cumulative updates.

As a result, the hardcoded mspaint.exe injection method may fail in some environments, causing the malware to malfunction.

If the 'mspaint.exe' file exists in the 'SysWOW64' directory, the malware allocates virtual memory and writes data starting from the value '325869FF25798BC277BF22DEB1DEB967h' in the 'xmmword\_403018' array, writing a total of 0xDA000 (892,928) bytes.

It then performs an XOR operation with the data in the 'xmmword\_402170' array, using the value '32323232323232323232323232323232h'. The result of this operation forms the structure of the second shellcode.


\[Figure 3-9\] Shellcode Decoding Routine


The shellcode repeatedly performs XOR operations starting at offset 000590, which is pointed to by the eax register, using the key value 0xD6 stored in the bl register.

Once the XOR operations are complete, the data is transformed into a 32-bit executable (EXE) file. This file is identified as a variant of RoKRAT.


\[Figure 3-10\] Comparison of Pre- and Post-XOR Results


On July 20, 2025, a new variant was discovered with the file name : “북한이탈주민의 성공적인 남한정착을 위한 아카데미 운영.lnk” (*"Academy Operation for Successful Resettlement of North Korean Defectors in South Korea.lnk"*).

This variant uses 'notepad.exe' instead of the 'mspaint.exe' process located in the 'C:\Windows\SysWOW64' directory. In addition, the malware was developed within a folder named 'Weapon'.


| D:\Work\ **Weapon**\InjectShellcode\Release\**InjectShellcode.pdb** | 

\[Table 3-4\] PDB String Information


The ‘Weapon’ folder was also identified in \[Figure 12\] of the report titled “[Analysis of malicious HWP cases of 'APT37' group distributed through K messenger](https://www.genians.co.kr/blog/threat_intelligence/k-messenger?hsLang=en),” published on February 3, 2025.


### **3-3. RoKRAT Analysis**

The final module obtained after XOR decoding has been identified as a variant of RoKRAT, a tool commonly used by the APT37 group.

RoKRAT has been introduced multiple times in previous reports, including “[Operation. ToyBox Story](https://www.genians.co.kr/en/blog/threat_intelligence/toybox-story?hsLang=en)” and can be referenced for more detailed information.

This variant also performs typical RoKRAT functions with no significant differences from previous versions. The unique identifier string (--wwjaughalvncjwiajs--) was again found in this module. This string is known to be a fixed value included in the Content-Type header when RoKRAT communicates with cloud APIs used as C2 channels.

RoKRAT modules are designed to collect basic system information, document files, and screenshots from infected endpoints, and exfiltrate them via legitimate cloud services such as:

- api.pcloud.com
- cloud-api.yandex.net
- api.dropboxapi.com

The threat actor loads this module using shellcode and a fileless approach, which may explain why its internal functions remain largely unchanged.


\[Figure 3-11\] Internal Strings of RoKRAT


The attacker continues to abuse free cloud storage services as C2 channels.

Accordingly, security teams in organizations and enterprises should closely monitor outbound connections to external cloud services.


\[Figure 3-12\] Dropbox API and Access Token Values


In this case, two Dropbox Access Token keys were used. The key values are listed below and have since been revoked.

- hFkFeKn8jJIAAAAAAAAAAZr14zutJmQzoOx-g5k9SV9vy7phb9QiNCIEO7SAp1Ch
- gYQs1sJ0etEAAAAAAAAAAUsEYLCFpEUR38u0SxDzsfL2F8ZCLokJPGpPsq4OTNUX

The access token values for the variant discovered on July 20, 2025, are as follows:

- Q54LEwmIgyAAAAAAAAAIIMytoGW3\_\_MIEynCsFRSwohgvHI\_fjViYK5ZfrG28teC
- 1yLixfRbcDAAAAAAAAAACJoZNYUJ5tQzE6jjb-mhXhqWZBRYWi8NJQ349sxGdkt\_


## **3-4. C2 Dropbox Account Information**

Using the Dropbox API and access tokens, partial account history information can be retrieved. This allows for the identification of certain details about the threat actor, including email addresses.


| "email": **"nusli.vakil@yandex.com"**, "email\_verified": true, "disabled": false, "country": "US", "locale": "en", "email": **"reddy.kappeta@yandex.com"**, "email\_verified": true, "disabled": false, "country": "US", "locale": "en", "email":  **"leon24609@gmail.com"**, "email\_verified": true, "disabled": false, "country": "GB", "locale": "ko", "email":  **"leon91729@zoho.com"**, "email\_verified": true, "disabled": false, "country": "JP", "locale": "ko", | 

\[Table 3-5\] Dropbox Account Information


\[Figure 3-13\] LinkedIn Account Page (Profile image blurred)


Both Dropbox accounts are registered with Yandex email addresses, a service headquartered in Russia. When searching the usernames from these email addresses, LinkedIn profiles appear in the results; however, it cannot be conclusively determined whether they belong to the same individuals.

Nonetheless, the fact that email addresses used by APT37's operators for cloud service registration continue to surface on LinkedIn is a noteworthy observation. Related findings were previously documented in the “Operation. ToyBox Story” report.



## **4. Hiding Techniques in Images**

### 
**4-1. RoKRAT Identified Using Steganography**

In early July 2025, multiple instances of RoKRAT loaders disguised as Multiple Provider Router DLLs were identified. The original file name was “mpr.dll”, and all observed 32-bit DLL variants exhibited similar functionality.

Some samples were found to contain malicious OLE objects embedded in HWP documents for use in attacks.


\[Figure 4-1\] Analysis View of Malicious HWP Internal Structure


The document contains two OLE objects: BIN001.OLE and BIN002.OLE. One of them is ShellRunas.exe, distributed by Sysinternals, and the other is credui.dll.

When the malicious HWP document is opened and the embedded hyperlink is clicked, a prompt appears asking whether to execute ShellRunas.exe, which was created in the temporary folder (%Temp%). If the user allows the execution, the accompanying malicious module credui.dll is loaded. This behavior is a typical example of DLL side-loading.

The following DLL side-loading cases have been identified in similar attacks, and the listed DLL files act as malicious modules:

- ShellRunas.exe
  - credui.dll
- AccessEnum.exe
  - mpr.dll
- Hhc.exe
  - hha.dll

The credui.dll module downloads an image file named ‘Father.jpg’ from a Dropbox drive and loads it into memory. Notably, the RoKRAT module is embedded within the JPEG image format, a technique commonly referred to as steganography.

Two different images were used for concealment, but the underlying malware structure remained the same. Based on this, further analysis was conducted using the malicious sample disguised as mpr.dll.


\[Figure 4-2\] Malware Sample Disguised as an Image File


The mpr.dll file contains a resource named MYIMAGEFILE. The file contained a resource named 'MYIMAGEFILE'. At a glance, this resource name may give the impression that an image file has been embedded.


\[Figure 4-3\] Resource Section of mpr.dll


The file locates the embedded resource, loads its data, and saves it to the %LOCALAPPDATA% directory as ‘version1.0.tmp’ using the SHGetKnownFolderPath function.


\[Figure 4-4\] Resource Data Creation Function


Next, the file loads ‘version1.0.tmp’ by calling the LoadLibraryW function.


\[Figure 4-5\] Library Load Function


Once the file is loaded, the malware retrieves the addresses of several functions from within the DLL:

- OpenURL
- GetMyFirstResult
- Set\_InstallKey
- Check\_Installed
- ProtectMe

The version1.0.tmp file also contains a resource named “MYIMAGEFILE”, and the resource begins with a valid JPEG image file header.


\[Figure 4-6\] Resource Section of version1.0.tmp


Upon extracting and reviewing the resource, it is found to contain a valid JPEG Exif (Exchangeable Image File Format) header. The image file displays the face of an actual individual.

However, analysis revealed that the version1.0.tmp file contains logic that performs an XOR operation on the image resource data using the key value 0xAA. After the operation, shellcode data was observed at offset 0x4201.


\[Figure 4-7\] Image and Shellcode View


The resulting shellcode undergoes a second XOR operation using the key 0x29, executed through an internal routine. Through this process, the hidden RoKRAT module is revealed.

Although the file begins with a valid JPEG image header, it ultimately loads malicious code through a decoding sequence—a textbook example of steganographic technique.


\[Figure 4-8\] XOR Execution Routine


Analysis of the RoKRAT functionalities used in this sample revealed two cloud access token values:

- pCloud
  - U1XD7ZzVoRYfYDIfLZhPK7ykZ43rMhs5ej88WQ78GctvXupdkFGXy
- Yandex
  - y0\_AgAAAAB6OAV\_AAzOMAAAAAEZECSQAAAy5BcMOOVPsYKi\_OfJu8GQ3fWpZA

These tokens were found to have been in use between 2023 and 2024. 



## **5. Conclusion**

[Genian EDR](https://www.genians.co.kr/products/genian-edr/?hsLang=en) provides clear visibility into threat activity. In cases involving steganographic techniques, the creation process of the version1.0.tmp file, found in the resource section, can be clearly identified.

Although the file has a .tmp extension, it was executed by rundll32.exe as the parent process.


\[Figure 5-1\] Execution of DLL Generated from Embedded Resource

 

When shellcode is injected into the mspaint.exe process to perform a fileless attack, detection by signature- or pattern-based security solutions may be difficult.


\[Figure 5-2\] Communication via Injection into mspaint.exe Process

 

When using an EDR (Endpoint Detection and Response) solution, external communications initiated via shellcode and the Dropbox API can be quickly identified.

Manually reversing and analyzing malware collected from an endpoint can require significant time and effort. However, when the behavior flow of the malware is promptly visualized through EDR, it greatly assists threat analysts within the Security Operations Center (SOC).

Providing a visual representation of the malware’s behavior is a valuable tool for threat analysts, offering several key advantages:

- Comprehensive Understanding of the Attack Flow
  - Visualizing data collected via EDR enables analysts to clearly understand how the malware propagates and infects systems, supporting a full view of the attack sequence.

- Infection Path Analysis
  - Through visual data analysis, it becomes easier to trace how the malware spread within the system. This helps analysts identify the specific attack vectors used by the threat actor.

- Enhanced Threat Detection and Response
  - EDR visualization plays a crucial role in rapidly detecting and responding to threats. It helps identify patterns of malicious activity and supports timely actions to minimize damage.

- Malware Classification and Behavioral Analysis
  - Visualizing malware behavior enables analysts to understand how the malware operates and functions. This information provides a foundation for developing defense strategies and preventing similar attacks.

- Reporting and Documentation
  - EDR visualization supports clearer documentation of threat analysis results. It also improves communication across security teams and serves as a valuable record for future incident response.

In summary, visual analysis of malware via EDR provides deep insights into the technical aspects of an attack and significantly enhances the ability of threat analysts to respond effectively.


\[Figure 5-3\] Investigation View of Cloud-Based C2 Communication Events


Genian EDR tags C2 communication events that abuse legitimate cloud services with corresponding MITRE ATT&CK Techniques, helping security administrators assess potential threats more effectively.

RoKRAT leverages C2 (Command & Control) channels disguised as popular cloud services such as Dropbox, Google Drive, and Yandex Disk. This makes detection difficult for traditional security devices and allows the malware to operate covertly over extended periods.

Notably, RoKRAT operates in a fileless manner, running in memory with minimal artifacts left on disk. As a result, it is often undetectable by conventional antivirus solutions or log-based detection systems. For threats as stealthy and persistent as this, an EDR-based response framework is essential. EDR enables real-time monitoring and detection of behaviors such as script execution, process creation, and network communication attempts that occur after system compromise.

RoKRAT continues to evolve, and recent variants have become highly sophisticated APT malware that cannot be effectively detected or mitigated using only antivirus or SIEM platforms.

This underscores the necessity of adopting an EDR-based defense strategy for the following reasons:

- Real-Time Detection and Analysis of Abnormal Behaviors (XBA)
- Visual Understanding of the Entire Attack Lifecycle
- Immediate Network Isolation and Response Options
- Data Accumulation for Preventing Future Attacks



## **6. Indicator of Compromise**

- ### MD5

a2ee8d2aa9f79551eb5dd8f9610ad557

ae7e18a62abb7f93b657276dcae985b9

d5fe744b9623a0cc7f0ef6464c5530da

f6d72abf9ca654a20bbaf23ea1c10a55

fd9099005f133f95a5b699ab30a2f79b

5ed95cde6c29432a4f7dc48602f82734

16a8aaaf2e3125668e6bfb1705a065f9

64d729d0290e2c8ceaa6e38fa68e80e9

443a00feeb3beaea02b2fbcd4302a3c9

e13c3a38ca58fb0fa9da753e857dd3d5

e4813c34fe2327de1a94c51e630213d1
