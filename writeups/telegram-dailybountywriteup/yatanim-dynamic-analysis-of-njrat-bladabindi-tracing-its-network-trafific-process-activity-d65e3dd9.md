# Dynamic Analysis of njRAT malware (Bladabindi)

- **Source URL:** https://medium.com/@yatanim/dynamic-analysis-of-njrat-bladabindi-tracing-its-network-trafific-process-activity-and-8950ddc972c4
- **Fetched from:** https://medium.com/feed/@yatanim
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14986 (id 14986)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Dynamic Analysis of njRAT malware (Bladabindi): Tracing Its Network Trafific, Process Activity, and Keylogging Behavior

*A beginner-friendly analysis of a real njRAT v0.7d sample using FLARE-VM, REMnux, INetSim, Wireshark, Process Monitor, Process Explorer, and dnSpy.*

In my previous static analysis of njRAT (Bladabindi), I examined its decompiled .NET code to understand its internal structure, installation routine, network communication, and keylogging functionality.

That investigation established what the sample was programmed to do. For the next stage, I wanted to observe what this particular build actually did when executed.

My objectives were to investigate the malware’s Windows host activity, capture and analyze its network communication, dynamically verify the keylogger, and determine whether its persistence and firewall-modification functionality executed.

This writeup documents the analysis process, including the tools and commands used, the observations collected, and the limitations of the available evidence.

All executions were conducted in an isolated VMware environment using harmless test data.

### 1. Sample Information and Analysis Scope

The analyzed file was a 32-bit .NET executable associated with **njRAT (Bladabindi), version 0.7d, build im523**.

**Sample identification**

- Malware family: njRAT / Bladabindi
- File type: PE32 .NET assembly
- SHA-256: ff87cd932e25b024cd10042c186f252fdabdac2c4d4cbc67f89e457697ebbc71
- Configured C2 hostname: phishing\[.\]multimilliontoken\[.\]org
- Configured port: 443/TCP
- Configured mutex identifier: 411e31664bdd9d96369d0a44d5111aef

The sample was originally written in VB.NET. The C# snippets discussed in this article are dnSpy’s decompiled representation of the executable.

Rather than attempting to demonstrate every feature in the RAT, I focused on behaviors that could be observed and supported by evidence from the isolated environment.

### 2. Analysis Environment

I configured two VMware virtual machines on an isolated LAN segment named MalwareLab.

**FLARE-VM (Windows 10)**

IP address: 192.168.77.10/24

Used for malware execution, Windows process monitoring, registry investigation, and .NET debugging.

**REMnux**

IP address: 192.168.77.20/24

Used for network simulation, packet capture, and traffic analysis.

The laboratory had no default gateway or direct Internet connectivity, and host-sharing functionality was disabled during execution.

*Figure 1. Isolated VMware analysis environment consisting of FLARE-VM and REMnux connected through the MalwareLab LAN segment.*

### 2.1 Configuring the network

On REMnux, I configured the analysis interface using:

sudo ip addr add 192.168.77.20/24 dev ens33

This was a temporary address assignment, so it needed to be applied again after rebooting REMnux.

On FLARE-VM, I configured the Windows adapter with the following values:

- IPv4 address: 192.168.77.10
- Subnet mask: 255.255.255.0
- DNS server: 192.168.77.20
- Default gateway: None

I verified the Windows configuration using:

ipconfig /all

I also verified connectivity between the two virtual machines before beginning malware execution.

### 2.2 Configuring INetSim

The sample was configured to communicate with a public C2 hostname. Rather than allowing any connection to that infrastructure, I used INetSim on REMnux to provide simulated DNS and network services.

The relevant INetSim configuration values were:

service\_bind\_address 192.168.77.20

dns\_default\_ip 192.168.77.20

I started the service using:

sudo inetsim

To confirm that the simulated DNS service was working, I performed a test lookup from FLARE-VM:

nslookup example.com

The response resolved the test hostname to 192.168.77.20.

*Screenshot 2. Successful DNS-resolution test using the simulated DNS service on REMnux.*

This established that Windows could communicate with the simulated DNS service.

An important limitation is that **INetSim is not a functional njRAT controller**. It can respond to network connections and support traffic observation, but it does not implement the complete command-and-response protocol used by the RAT.

### 3. Initial Malware Execution and Host Activity

After completing the laboratory configuration, I executed the malware sample inside FLARE-VM.

I used Process Explorer to identify the running process and inspect its associated resources. Process Monitor was used to investigate the file, registry, and process-related operations recorded during execution.

### 3.1 Identifying the running process

During the first execution, the malware appeared in Process Explorer with PID 6800.

This process ID belonged to that particular run. Later executions received different PIDs.

I inspected the process’s handles and identified an object with the Windows type Mutant.

### 3.2 Investigating mutex activity

The decompiled startup routine OK.ko() contained the following operation:

OK.MT = new Mutex(true, OK.RG, out flag2);

The OK.RG field contained the configured mutex identifier.

The surrounding code checked whether the named mutex was newly created. This logic was consistent with an attempt to prevent duplicate malware instances.

The runtime observation of a Mutant handle supported the presence of mutex-related activity.

However, I did not perform a separate test by executing two instances simultaneously. Therefore, duplicate-instance prevention was identified from the code rather than independently demonstrated.

### 3.3 Registry activity

During the initial investigation, I observed the registry value:

HKCU\di = "!"

The corresponding startup code contained:

OK.F.Registry.CurrentUser.SetValue("di", "!");

This supported the observed registry operation.

However, HKCU\di is not equivalent to the Windows Run key. The presence of this value does not independently establish persistence.

I therefore recorded it as a registry marker created during the malware’s startup activity.

### 4. Network Behavior Analysis

The next phase focused on identifying the malware’s network behavior and determining what information it transmitted.

### 4.1 Capturing traffic with tcpdump

I started INetSim on REMnux and began recording network traffic before executing the sample.

The tcpdump command was:

sudo tcpdump -i ens33 -nn -s 0 -w \~/njrat\_network.pcap

The command captured traffic from the ens33 interface and wrote the packets to njrat\_network.pcap.

After executing the malware, I allowed network traffic to accumulate and stopped tcpdump.

The first capture contained approximately **1,952 packets**.

To inspect the beginning of the saved capture, I used:

sudo tcpdump -nn -r \~/njrat\_network.pcap -c 25

*Screenshot 3. REMnux terminal showing the initial packet capture and recorded network traffic.*

The capture contained traffic from several Windows components.

Therefore, I could not classify every packet sent to REMnux as malware traffic. I needed to distinguish the sample’s communication from unrelated Windows background requests.

### 4.2 Identifying the configured C2 hostname

During static analysis, I had identified the configured hostname:

phishing.multimilliontoken.org

I used tshark to enumerate the requested DNS names in the PCAP:

tshark -r \~/njrat\_network.pcap -Y 'dns.flags.response == 0' -T fields -e dns.qry.name | sort -u

The output included the configured njRAT hostname alongside Windows-related requests.

*Screenshot 4. DNS hostnames extracted from the packet capture using tshark.*

I then opened the PCAP in Wireshark and applied the display filter:

dns.qry.name == "phishing.multimilliontoken.org"

The filter matched **320 DNS packets** in our investigation.

The simulated DNS responses resolved the hostname to:

192.168.77.20

This was the REMnux address, not the genuine external C2 address.

The observation established that the configured hostname was being requested during execution and that the isolated DNS service responded.

### 4.3 Investigating TCP connections

After identifying the DNS activity, I examined TCP connections between FLARE-VM and REMnux.

I used the Wireshark filter:

ip.src == 192.168.77.10 && ip.dst == 192.168.77.20 && tcp.dstport == 443

I also opened:

**Statistics → Conversations → TCP**

The initial capture contained approximately **185 TCP conversations**.

Many of these were short connections involving destination port 443.

*Screenshot 5. Wireshark TCP Conversations showing the connections recorded during the experiment.*

A connection to port 443 does not automatically establish that the application uses HTTPS.

The actual application behavior must be determined from the exchanged data.

For that reason, I selected relevant TCP conversations and inspected their reconstructed application data.

### 4.4 Following TCP stream 39

I selected one of the relevant conversations and opened **Follow TCP Stream** in Wireshark.

The selected stream was identified as:

tcp.stream == 39

The reconstructed conversation contained structured client-identification data.

*Figure 2. Observed DNS resolution, TCP communication, and client check-in through the simulated REMnux endpoint.*

*Screenshot 6. Actual reconstructed TCP stream containing njRAT client-identification information.*

The readable data contained fields associated with the infected system, including:

- Computer name: DESKTOP-XXXXX
- Username: USER
- Windows operating-system information
- Build identifier: im523
- Additional encoded identification fields

Some fields were separated by the delimiter:

|'|'|

This matched the delimiter identified during the earlier static analysis.

The presence of structured machine and user information indicated that the malware was transmitting an initial client-identification or check-in message.

This was stronger evidence than simply observing an outbound TCP connection.

### 4.5 Investigating another TCP stream

To determine whether the message appeared only once, I examined TCP stream 40.

It contained a similar structured client-identification message.

Together with the numerous short TCP conversations, this was consistent with repeated client check-in attempts.

One possible explanation was that INetSim could accept the network connection but could not complete the protocol exchange expected by njRAT.

However, the investigation did not establish the precise reason for each repeated connection.

### 4.6 Examining data-bearing packets

I also applied the following Wireshark filter:

tcp.stream == 39 && tcp.len > 0

This displayed packets carrying TCP payload data within stream 39.

Only **two data-bearing packets** matched the filter, although the complete TCP conversation contained eight packets.

The difference was expected because TCP conversations also contain connection-establishment, acknowledgement, and connection-closure packets.

Wireshark’s Follow TCP Stream feature reconstructs the exchanged data across the packets belonging to a conversation.

The reconstructed content should not be interpreted as data contained entirely within one individual packet.

### 4.7 Network findings

The network investigation confirmed DNS requests associated with the configured hostname, responses from the simulated DNS service, repeated TCP communication to port 443, and structured client-identification data.

It did not establish a fully functioning controller session or demonstrate the execution of remote commands.

### 5. Dynamically Verifying the Keylogger

The next objective was to determine whether the keylogging functionality identified during static analysis actually operated during execution.

The relevant class was kl, and the keylogging method was WRK().

The code used Windows keyboard-state functionality, including GetAsyncKeyState, to process keypresses.

### 5.1 Initial keylogging experiment

I prepared a fresh execution in the isolated environment.

On REMnux, I started another packet capture:

sudo tcpdump -i ens33 -nn -s 0 -w \~/njrat\_keylogging\_test.pcap 'host 192.168.77.10'

On FLARE-VM, I executed the sample while Procmon monitored its activity.

I opened Notepad and typed harmless test strings, including ordinary characters, Enter, and Backspace.

The objective was to generate recognizable keyboard input that could later be compared with the malware’s behavior.

### 5.2 Searching for keylog file activity

After generating test input, I inspected the malware’s recorded Procmon events.

I found operations such as:

- CreateFile
- RegOpenKey
- RegQueryValue

However, I did not identify a convincing WriteFile event demonstrating that the sample saved the collected keystrokes to a file.

This did not prove that the keylogger was inactive.

The malware could have been accumulating keyboard input in memory instead of immediately writing it to disk.

To test that possibility, I returned to the decompiled code.

### 5.3 Identifying the in-memory buffer

Inside the kl.WRK() method, I identified the following statements:

this.Logs += this.AV();

this.Logs += text;

The second statement appended processed keyboard input to the existing Logs string.

This provided a specific location to investigate dynamically.

Rather than searching for more possible keylog filenames, I decided to observe the value of Logs inside the running malware process.

### 5.4 Attaching the dnSpy debugger

Initially, I encountered difficulty finding the malware process in dnSpy’s debugger attachment window.

After switching to **32-bit dnSpy**, the running process appeared in the available process list.

I attached the debugger and navigated to the kl.WRK() method.

I placed a breakpoint at:

this.Logs += text;

*Screenshot 8. Decompiled keylogging method and the selected breakpoint location.*

The breakpoint allowed me to pause execution when the routine reached the statement responsible for appending captured input.

*Figure 3. Keylogging flow observed during the experiment: harmless Notepad input is processed by kl.WRK() and accumulated in the in-memory Logs string.*

### 5.5 Triggering the breakpoint

After configuring the breakpoint, I resumed execution and typed more harmless text in Notepad.

The breakpoint triggered.

I opened dnSpy’s Locals window and inspected the current processed input.

At one breakpoint, the variable text contained:

"\[ENTER\]\r\n"

*Screenshot 9. dnSpy paused at this.Logs += text, with the Locals window displaying the processed Enter-key representation.*

This demonstrated that the keylogging method had processed keyboard activity during execution.

### 5.6 Inspecting accumulated keystrokes

I expanded the keylogger object, represented by this, and examined its Logs member.

The accumulated string contained previously typed test characters, key representations such as \[Back\], and window-related information.

The recorded content was consistent with the harmless input I had generated in Notepad.

*Screenshot 10. Harmless keyboard input used during the keylogging experiment.*

One detail was particularly important.

The debugger paused before the currently selected append statement completed.

Therefore, the current value of text represented input being processed at that moment, while the existing content of Logs came from earlier iterations.

This allowed me to distinguish the current input from the accumulated log buffer.

**Finding: The malware actively captured and accumulated keyboard input in memory during execution.**

This was the strongest behavioral finding of the investigation because the functionality was verified within the running process rather than inferred solely from decompiled code.

### 5.7 Investigating possible transmission

The packet capture from this experiment was saved as:

njrat\_keylogging\_test.pcap

It contained approximately 15,000 packets.

I also performed a basic Wireshark search:

frame contains "njrat"

The search returned no matching packets.

However, a literal string search is not sufficient to rule out encoded, fragmented, or controller-triggered transmission.

The decompiled OK.Ind() routine contained a branch capable of referencing the accumulated Logs data and passing it to the sample's network-sending routine.

Because our INetSim service was not a functional njRAT controller, I did not attempt controller-dependent retrieval of the captured keystrokes.

The investigation therefore established **in-memory keylogging**, not successful remote transmission of collected logs.

### 6. File-System Activity and Persistence

During the earlier static analysis, I identified configuration values suggesting that the malware supported executable relocation and Windows autostart persistence.

The configured executable filename was:

server.exe

The configured destination variable was:

TEMP

This suggested a potential file destination of:

%TEMP%\server.exe

### 6.1 Investigating the missing server.exe

I searched the TEMP directory for server.exe.

The file was not present.

I also searched the available Procmon events for the same filename but found no corresponding activity.

I therefore examined the conditions controlling the file-copying functionality.

### 6.2 Examining the installation configuration

The decompiled sample contained:

Idr = False

IsF = False

Isu = False

These flags controlled different installation and persistence branches.

Idr controlled executable relocation.

IsF controlled copying the executable into the Windows Startup folder.

Isu controlled Registry Run-key persistence.

*Figure 4. Conditional installation and persistence functionality in the analyzed sample. All three relevant flags were disabled.*

The startup method OK.ko() still called:

OK.INS();

Therefore, the installation routine itself was not necessarily skipped.

Instead, the relevant file-copying and persistence branches within the routine were disabled.

The firewall-modification code was a separate part of the same routine, which explains why the firewall command could still execute.

### 6.3 Registry and Startup-folder checks

During the investigation, I checked common Windows autostart locations, including Run and RunOnce keys and Windows Startup folders.

I also examined possible scheduled-task and service-related persistence indicators.

No successful malware autostart mechanism was confirmed.

I later searched the saved Procmon capture for:

CurrentVersion\Run

The available events did not show a corresponding Run-key modification.

These observations were consistent with the configuration values Isu = False and IsF = False.

**Finding: The malware contains persistence-related functionality, but standard Registry Run-key, Startup-folder, and self-relocation operations were disabled in this build and were not observed dynamically.**

### 7. Windows Firewall Modification Attempt

During the host investigation, I observed the malware interacting with Windows’ netsh.exe utility.

The decompiled code contained a command beginning:

netsh firewall add allowedprogram

The command referenced the executable’s path and requested a Windows Firewall exception.

I returned to the saved Procmon capture to investigate the operation more precisely.

### 7.1 Investigating netsh.exe file access

During the later execution, the malware process had PID 5488.

Procmon recorded operations involving netsh.exe.

The malware first attempted to access:

C:\Users\USER\Downloads\malwareBazar\netsh.exe

That lookup returned:

NAME NOT FOUND

It subsequently accessed:

C:\Windows\SysWOW64\netsh.exe

Those operations returned:

SUCCESS

*Screenshot 11. Procmon showing the malware accessing netsh.exe, including the unsuccessful working-directory lookup and successful access to the Windows executable.*

However, successful file access did not independently prove that the executable had started.

For that, I needed to inspect process-creation activity.

### 7.2 Confirming process execution

In Procmon, I removed the earlier restrictive filters and applied:

Operation is Process Create → Include

I searched for netsh.exe and opened the relevant event.

The event properties showed:

**Operation:** Process Create

**Result:** SUCCESS

**Path:** C:\Windows\SysWOW64\netsh.exe

**Parent process:** Hash-named malware

**Parent PID:** 5488

**Child PID:** 3640

**Command line:** netsh firewall add allowedprogram ... ENABLE

*Figure 5. The malware successfully launched netsh.exe, which attempted to add an application exception to Windows Firewall.*

*Screenshot 12. Procmon Process Create event confirming execution of netsh.exe with firewall-modification arguments.*

This was direct evidence that Windows successfully created the netsh.exe child process.

However, the successful creation of a child process does not establish that the requested firewall operation completed successfully.

### 7.3 Checking the firewall configuration

I opened Windows Defender Firewall with Advanced Security and examined the inbound rules.

I did not identify a corresponding installed rule for the malware.

I also searched the available Procmon capture for registry paths containing:

AuthorizedApplications

and:

FirewallRules

Neither search produced conclusive evidence of a successful firewall-policy modification.

### 7.4 Attempting to inspect the child process exit status

The Process Create event identified the child PID as 3640.

I attempted to filter the saved Procmon capture using this PID to find its Process Exit event.

However, no events belonging to the child process were available in the saved trace.

During our original monitoring, we had restricted Procmon’s view to the malware process. The malware and its child process had different PIDs.

The saved capture contained the parent process’s creation event but did not provide the child’s completion status.

The earlier filtering and saving configuration may have contributed to this limitation, although the precise reason could not be established.

**Finding: The malware successfully launched a command intended to add a Windows Firewall exception. The actual installation of that exception remained unverified.**

### 8. Consolidated Findings

The dynamic investigation established the following results.

**Malware execution — Confirmed**

The hash-named .NET executable ran inside FLARE-VM and was identified using Windows process-monitoring tools.

**Mutex activity — Observed**

A Mutant handle was identified during runtime inspection. Duplicate-instance prevention was supported by the code but not separately exercised.

**Registry activity — Observed**

The registry marker HKCU\di = "!" was associated with the malware's startup activity. It was not a standard Windows autostart entry.

**Network communication — Confirmed**

The malware requested its configured C2 hostname and established TCP communication with the simulated REMnux endpoint.

**Client identification — Observed**

The reconstructed TCP streams contained structured information about the Windows system and the njRAT build.

**In-memory keylogging — Dynamically verified**

A breakpoint in kl.WRK() triggered during harmless typing, and accumulated test input was observed in the malware's Logs variable.

**Firewall modification — Attempt confirmed**

Procmon showed Process Create → SUCCESS for netsh.exe with firewall-modification arguments. Successful firewall-rule creation was not confirmed.

**Self-relocation — Disabled**

The relocation flag Idr was false, and %TEMP%\server.exe was not observed.

**Autostart persistence — Disabled**

The IsF and Isu flags were false, and corresponding Startup-folder or Registry Run-key persistence was not confirmed.

**Remote command execution — Not tested**

The incoming command handler was identified statically but not exercised through a functioning controller.

**Keylog transmission — Not established**

Local collection was verified, but remote retrieval and transmission were not dynamically demonstrated.

**Protection-thread behavior — Not verified**

The sample’s configuration enabled the mgr.protect() thread, but its effects were not investigated in this analysis.

### 9. Indicators of Compromise and Relevant Artifacts

**Sample SHA-256**

ff87cd932e25b024cd10042c186f252fdabdac2c4d4cbc67f89e457697ebbc71

**Configured C2 hostname**

phishing\[.\]multimilliontoken\[.\]org

**Configured C2 port**

443/TCP

**Configured mutex identifier**

411e31664bdd9d96369d0a44d5111aef

**Observed registry marker**

HKCU\di = "!"

**Configured but unobserved executable destination**

%TEMP%\server.exe

**Laboratory addresses**

FLARE-VM: 192.168.77.10

REMnux: 192.168.77.20

The private laboratory addresses are not attacker-controlled C2 addresses.

### 10. Conclusion

This investigation examined the actual runtime behavior of a specific njRAT (Bladabindi) sample in an isolated Windows and Linux laboratory.

The network analysis identified DNS requests associated with the configured C2 hostname, repeated TCP connections to the simulated endpoint, and structured client-identification data transmitted during check-in.

The keylogging investigation provided direct evidence that the malware captured harmless keyboard input and accumulated it in memory. This was established by attaching dnSpy to the running process, triggering a breakpoint in kl.WRK(), and examining the relevant variables.

The Windows host investigation also identified mutex-related activity, a registry marker, and successful creation of a netsh.exe child process attempting to modify Windows Firewall.

At the same time, the configuration analysis established that the malware’s standard self-relocation and autostart persistence mechanisms were disabled in this build.

Not every functionality was exercised, and several limitations remained. In particular, successful firewall-rule installation, controller-dependent command execution, and keylog transmission were not established.

The main outcome of this investigation was a collection of runtime observations that could be compared directly with the sample’s decompiled functionality.

**The distinction between implemented capabilities, attempted operations, and verified behavior was essential to interpreting the results accurately.**

*All experiments were conducted inside an isolated research environment using harmless test input. The analysis did not establish a session with an external attacker-controlled controller.*
