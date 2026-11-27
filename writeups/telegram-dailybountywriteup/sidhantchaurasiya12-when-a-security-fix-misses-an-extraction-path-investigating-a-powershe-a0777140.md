# When a Security Fix Misses an Extraction Path

- **Source URL:** https://medium.com/@sidhantchaurasiya12/when-a-security-fix-misses-an-extraction-path-investigating-a-powershell-windows-cab-path-02369e81239a
- **Fetched from:** https://medium.com/feed/@sidhantchaurasiya12
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### When a Security Fix Misses an Extraction Path: Investigating a PowerShell Windows CAB Path Traversal Vulnerability

**A vulnerability research case study involving PowerShell, Windows Cabinet (CAB) extraction, FDI callbacks, Update-Help, and an incomplete security boundary**

**Researcher:** Sidhant Kumar Chaurasiya

**Research area:** Vulnerability Research | Windows Internals | Application Security | Responsible Disclosure

**Vendor:** Microsoft

**Affected component:** PowerShell / System.Management.Automation

**Microsoft case:** 142705

**Submission ID:** VULN-219264

**CWE:** CWE-22 — Improper Limitation of a Pathname to a Restricted Directory

**Disclosure status:** Vendor-confirmed behavior; fix released; report closed as duplicate.

### 1. Introduction

Security vulnerabilities are not always introduced by completely new features or previously unknown programming mistakes. Sometimes, a security issue survives because an existing mitigation protects one execution path but does not cover another path that reaches the same sensitive operation.

That was the central idea behind my investigation into Microsoft’s PowerShell help-content extraction mechanism.

In September 2026, I submitted a vulnerability report to the Microsoft Security Response Center (MSRC) describing a potential path traversal issue in the Windows-native Cabinet (CAB) extraction implementation used by PowerShell.

The investigation focused on a specific component:

System.Management.Automation/help/CabinetNativeApi.cs

More specifically, I examined the FdiNotify callback implementation and its handling of archive entry paths during CAB extraction.

My investigation identified a potential gap between two extraction mechanisms:

- The managed ZIP extraction path, which relies on archive extraction protections.
- The Windows-native CAB extraction path, which processes archive entry names through native FDI callbacks.

The concern was that the security validation applied to one extraction mechanism was not equivalently enforced in the other.

If an archive entry could influence the destination path without proper canonicalization and containment validation, the extraction process could potentially write files outside its intended directory.

This is particularly important because archive extraction is a security-sensitive operation. An archive should never be allowed to decide where files are written outside the directory explicitly authorized by the application.

I reported the issue as a potential incomplete remediation related to the historical PowerShell Remote Code Execution vulnerability, CVE-2022–41076.

Microsoft subsequently confirmed the reported behavior, investigated the issue, released a fix, and published an acknowledgement on the associated CVE. My submission was ultimately closed as a duplicate because the same underlying issue had already been reported by another researcher.

This article documents the technical reasoning, investigation, security implications, and responsible disclosure process behind the research.

### 2. Background: Understanding CVE-2022–41076

Before examining the new finding, it is important to understand the security context.

CVE-2022–41076 is a PowerShell Remote Code Execution vulnerability disclosed by Microsoft in December 2022.

The original vulnerability involved PowerShell’s help-content processing functionality and was assigned a CVSS 3.1 score of 8.5 (High).

Microsoft released security fixes for affected PowerShell versions, including:

- PowerShell 7.2.8
- PowerShell 7.3.1

The original vulnerability demonstrated that processing untrusted help content could introduce a security risk when archive contents were not handled safely.

For an application that downloads, processes, and extracts archive files, path validation is a critical security requirement.

Consider a simple example.

An application intends to extract files into:

C:\Application\Help\

A normal archive entry might be:

en-US\about\_Command.help.txt

The application should resolve this entry to a location inside the intended extraction directory.

However, an attacker-controlled archive entry containing parent-directory traversal components can attempt to escape the extraction directory.

Conceptually:

..\..\outside.txt

If the application combines this entry with the extraction directory without validating the final resolved destination, the resulting path may point somewhere outside the authorized directory.

This vulnerability class is known as **Path Traversal**, classified under CWE-22.

The important security principle is:

*An application must validate the final resolved filesystem destination, not simply trust the path supplied by an archive entry.*

The original CVE provided the context for my investigation. I wanted to understand whether the security protections introduced around help-content extraction were consistently applied across all extraction implementations.

Reference: [https://nvd.nist.gov/vuln/detail/CVE-2022-41076](https://nvd.nist.gov/vuln/detail/CVE-2022-41076)

### 3. The investigation: Looking beyond the ZIP extraction mechanism

One of the most important steps in vulnerability research is understanding how a security-sensitive operation is actually implemented.

Rather than treating archive extraction as a single operation, I examined the different mechanisms used by PowerShell.

My investigation focused on two distinct extraction paths.

### 3.1 Managed ZIP extraction

The first path uses the managed archive extraction functionality.

The relevant implementation was associated with:

UnzipHelpContentand: ExpandArchive

This path uses .NET archive-processing functionality.

The important observation was that the managed ZIP extraction mechanism benefits from built-in protections against certain archive path traversal scenarios.

In other words, archive entry paths are not necessarily treated as unrestricted filesystem destinations.

### 3.2 Windows-native CAB extraction

The second path was more interesting.

Windows supports Cabinet archive files, commonly identified by the .cab extension.

CAB archives are frequently used by Windows components and software distribution mechanisms.

PowerShell supports CAB processing through Windows-native functionality, including the File Decompression Interface (FDI).

The implementation I investigated was:

System.Management.Automation/help/CabinetNativeApi.cs

Unlike the managed ZIP extraction mechanism, this implementation interacts with the Windows-native FDI API through callback functions.

The relevant callback was:

FdiNotify

This callback receives notifications from the FDI extraction process and handles operations such as creating files and closing extracted files.

The important question was:

**Does the CAB extraction implementation enforce the same filesystem containment guarantees as the ZIP extraction implementation?**

My investigation suggested that it did not.

### 4. Understanding Windows FDI and FdiNotify

To understand the reported issue, it helps to understand the role of FDI.

The File Decompression Interface is a Windows API used to decompress files from Cabinet archives.

It allows an application to provide callback functions that handle different extraction events.

Instead of treating extraction as a simple managed operation, the application participates in the extraction process through callbacks.

The PowerShell implementation uses a notification callback to process these events.

Two notification operations were particularly relevant to my investigation:

1. FdintCOPY\_FILE
2. FdintCLOSE\_FILE\_INFO

### 4.1 FdintCOPY\_FILE

This notification is associated with creating or opening an extracted file.

In the implementation examined during my research, the archive entry name was used to derive filesystem path components.

The relevant operations included:

- Obtaining the filename using Path.GetFileName.
- Obtaining the directory portion using Path.GetDirectoryName.
- Combining the directory portion with the extraction destination using Path.Combine.
- Creating the resulting directory.
- Constructing the final filename.
- Opening the destination through the native file-opening operation.

The security concern was that the archive-provided path influenced the destination directory.

Path combination alone does not establish that the resulting path remains inside the intended extraction directory.

For example, consider the following conceptual operation:

string destination = Path.Combine(

extractionDirectory,

archiveEntryDirectory

);

This operation constructs a path. It does not independently establish a security boundary.

If the second argument contains traversal components, the resulting path can escape the intended directory after filesystem path resolution.

This is the fundamental distinction between path construction and path validation.

### 4.2 FdintCLOSE\_FILE\_INFO

The second relevant notification was:

FdintCLOSE\_FILE\_INFO

This callback handles file metadata and closing-related processing after extraction.

My investigation also identified another path construction operation in this callback.

The destination was reconstructed using the extraction destination and the archive entry path.

This raised an additional concern.

Even if an earlier stage validates a path, reconstructing it later without applying equivalent validation can introduce a second opportunity for an unsafe destination to be used.

This is why security checks must be consistently enforced at every filesystem operation that relies on untrusted path data.

It is not sufficient to validate a path once and assume that all subsequent operations are automatically safe.

### 5. Root cause: Missing filesystem containment validation

The central issue identified in my report was the absence of an effective containment check in the Windows-native CAB extraction path.

The relevant distinction is between these two operations:

**Path construction:**

Path.Combine(baseDirectory, archiveEntryName);

**Path containment validation:**

Path.GetFullPath(candidatePath);

followed by a comparison against the canonical extraction directory.

The first operation combines path components.

The second helps determine where the resulting path resolves.

However, canonicalization by itself is also insufficient. The application must verify that the resolved destination is actually contained within the authorized extraction directory.

For example, suppose the intended extraction directory is:

C:\Temp\HelpExtraction

A safe destination should resolve to a location beneath that directory.

An unsafe destination might resolve to:

C:\Temp\Outside.txt

The security boundary has been violated even though the original path was constructed using Path.Combine.

The important missing property is **directory containment**.

### 5.1 Why Path.Combine is not a security control

Developers sometimes assume that combining a trusted base directory with an untrusted filename automatically constrains the result.

That assumption is incorrect.

Path-combination APIs are not authorization mechanisms.

An attacker-controlled path may contain:

- Parent-directory traversal components.
- Rooted paths.
- Drive-qualified paths.
- Platform-specific path separators.
- Alternative path representations.

Applications must account for the filesystem’s actual path semantics.

For this reason, archive extraction implementations should validate the canonical destination before creating directories or opening files.

### 5.2 Why validating only after extraction is insufficient

Another important part of my investigation involved the validation process performed after extraction.

The relevant PowerShell functionality included:

ValidateAndCopyHelpContent()

The concern was that this validation occurred after the extraction stage and inspected files within the expected temporary extraction directory.

This creates a potential blind spot.

If an extraction operation has already written a file outside that directory, inspecting only the files remaining inside the directory cannot establish that all extracted files were safe.

The distinction is important:

- Pre-extraction validation can prevent an unsafe destination from being used.
- Post-extraction validation can inspect the results that remain within the inspected location.
- Post-extraction validation cannot reliably undo or detect every filesystem side effect that already occurred outside that location.

The correct security model is to prevent unauthorized writes before they happen.

### 6. Why the issue mattered: Potential arbitrary file write

A path traversal vulnerability in an archive extraction mechanism can have consequences beyond writing an unexpected file.

If an attacker can control the destination path, the application may write data outside its intended extraction directory.

The potential impact depends on several conditions:

- Whether an attacker can supply or influence the archive.
- Whether the extraction operation processes the archive.
- Which directories are writable by the extracting process.
- Whether the resulting file is subsequently loaded or executed.
- Whether the process runs with elevated privileges.

In my report, I described the issue as a potential arbitrary file write with possible code-execution consequences.

### 6.1 Arbitrary file write

The most direct security impact is the ability to cause a file to be written outside the intended extraction directory.

This violates the filesystem boundary that the extraction process is expected to enforce.

Depending on the process permissions, the consequences could include:

- Writing files into user-writable application directories.
- Modifying files used by PowerShell modules.
- Placing content in locations that influence later script execution.
- Modifying files in other writable locations accessible to the extracting process.

An arbitrary file write is particularly serious when the destination is a location that another application or component automatically loads.

### 6.2 Potential code execution

The next stage of impact depends on where the attacker-controlled file can be written.

For example, a malicious file placed in a location that PowerShell subsequently loads as a script or module component could potentially result in code execution when the relevant loading mechanism is triggered.

This is a conditional impact, not an automatic consequence of every successful file write.

The following conditions must be considered:

1. The attacker must be able to influence the archive content.
2. The vulnerable extraction operation must process that content.
3. The extracting process must have permission to write to the selected destination.
4. The destination must be consumed by a relevant loading or execution mechanism.
5. Any additional application-specific security controls must not prevent execution.

The severity therefore depends on the actual execution context.

### 6.3 Elevated execution context

Another important consideration is the privilege level of the extraction process.

If an administrator or another privileged process performs the vulnerable extraction, an attacker-controlled write may have greater consequences than the same operation performed by an unprivileged user.

This is a general security principle:

**The impact of a filesystem path traversal vulnerability is strongly influenced by the permissions of the process performing the operation.**

### 7. Attack surface and security assumptions

The research also raised questions about how PowerShell help-content processing should be treated from a security perspective.

The relevant functionality includes:

- Update-Help
- Save-Help
- Help-content archive processing.
- CAB extraction.
- Local and remote help-content sources.

The security concern is not that every invocation of these commands is inherently vulnerable.

The relevant condition is whether an attacker-controlled or compromised archive can reach the vulnerable extraction implementation.

Potential sources of untrusted input include:

- A compromised help-content distribution source.
- An attacker-controlled local archive supplied through a configured source path.
- A compromised distribution or update infrastructure.
- Other scenarios in which an attacker can influence the archive being processed.

The remote-execution implications require additional conditions.

For example, a remote attacker would need an applicable way to cause the vulnerable operation to process attacker-controlled archive content. An authenticated remoting session, an exposed management interface, or a privileged automation workflow could change the practical attack surface.

I did not establish that every PowerShell remoting configuration exposed this issue to unauthenticated network attackers.

That distinction is important when evaluating the real-world exploitability of a vulnerability.

### 8. Investigation methodology

This research involved examining the implementation rather than relying solely on the existence of an earlier security advisory.

The investigation followed several stages.

### Stage 1: Reviewing the original vulnerability

I started by examining the original CVE-2022–41076 security context.

The objective was to understand:

- What functionality had originally been affected.
- Which extraction mechanisms were involved.
- What security protections had been introduced.
- Whether different extraction implementations followed equivalent security assumptions.

This provided the basis for investigating the possibility of an incomplete remediation.

### Stage 2: Identifying separate extraction paths

The next step was to trace the help-content extraction functionality.

I examined the managed ZIP extraction implementation and compared it with the Windows-native CAB implementation.

This comparison was important because two code paths can perform logically similar operations while relying on entirely different security controls.

A fix applied to one implementation does not automatically protect another.

### Stage 3: Reviewing the FDI callback implementation

I then focused on:

CabinetNativeApi.cs

The relevant code paths were:

- FdiNotify
- FdintCOPY\_FILE
- FdintCLOSE\_FILE\_INFO

I examined how archive entry names were transformed into destination paths and how those paths were used during filesystem operations.

The main security question was whether the final destination was constrained to the intended extraction directory.

### Stage 4: Evaluating path traversal behavior

My analysis focused on the relationship between:

- Archive-provided entry names.
- Path.GetFileName.
- Path.GetDirectoryName.
- Path.Combine.
- Directory creation.
- Native file-opening operations.

I evaluated the path-resolution and containment assumptions deterministically.

One important limitation should be stated clearly: my research environment was Linux-based. I did not complete a full end-to-end Windows reproduction using a crafted ANSI-FDI CAB archive and the actual PowerShell Update-Help workflow.

The investigation therefore distinguished between the source-level behavior and the final Windows exploitation chain.

A Windows-based reproduction would be needed to independently demonstrate every stage of the complete attack chain.

### Stage 5: Preparing the security report

After identifying the issue, I prepared the report with:

- The affected source-code component.
- The relevant callback operations.
- The suspected missing validation.
- The security implications.
- The relationship to the earlier CVE.
- Suggested remediation.
- Reproduction limitations and outstanding validation requirements.

I also made it clear that the research had not been publicly released or weaponized.

### Stage 6: Responsible disclosure

I submitted the report to Microsoft through the MSRC researcher portal on September 2, 2026.

The report was tracked under:

- Submission: VULN-219264
- MSRC case: 142705
- External tracking reference: VULN-001

The investigation continued through Microsoft’s coordinated vulnerability disclosure process.

### 9. Suggested remediation

The primary remediation is to ensure that every archive entry is resolved and validated against the intended extraction directory before any filesystem operation is performed.

A robust implementation should:

1. Establish a trusted extraction root.
2. Canonicalize the extraction root.
3. Resolve the archive entry against that root.
4. Canonicalize the resulting destination.
5. Verify that the destination remains inside the extraction root.
6. Reject rooted paths and drive-qualified paths where they are not permitted.
7. Apply the validation consistently to all extraction callbacks.
8. Account for filesystem reparse points and symbolic links where relevant.

### 9.1 Canonicalization

A simplified conceptual example is:

string extractionRoot =

Path.GetFullPath(destinationDirectory);

string candidatePath =

Path.GetFullPath(

Path.Combine(extractionRoot, entryName)

);

At this stage, the application has a canonical candidate path.

However, canonicalization alone does not guarantee safety.

The application must still verify that the candidate is contained within the extraction root.

### 9.2 Boundary-aware containment

A simplistic string comparison can introduce another vulnerability.

For example, if the extraction root is:

C:\Temp\Help

A candidate path such as:

C:\Temp\Help-Evil\file.txt

starts with the same character sequence but is not inside the intended directory.

Therefore, containment checks must be directory-boundary-aware.

Conceptually:

string root = Path.GetFullPath(destinationDirectory);

string candidate = Path.GetFullPath(

Path.Combine(root, entryName)

);

string rootPrefix = Path.EndsInDirectorySeparator(root)

? root

: root + Path.DirectorySeparatorChar;

if (!candidate.StartsWith(

rootPrefix,

StringComparison.OrdinalIgnoreCase

) &&

!string.Equals(

candidate,

root,

StringComparison.OrdinalIgnoreCase

))

{

throw new SecurityException(

"Archive entry escapes extraction directory."

);

}

This is illustrative defensive logic, not a complete cross-platform or race-free extraction implementation.

A production implementation must also account for:

- Windows path comparison semantics.
- Alternate separators.
- Drive-relative and rooted paths.
- UNC paths.
- Filesystem reparse points.
- Symbolic links.
- Time-of-check-to-time-of-use (TOCTOU) races.

### 9.3 Validate both callback paths

One of the most important recommendations from my report was that validation must not be limited to a single callback.

Both of the following operations require equivalent protection:

- FdintCOPY\_FILE
- FdintCLOSE\_FILE\_INFO

Every filesystem operation must use a destination that has been validated against the trusted extraction root.

### 9.4 Avoid trusting post-extraction validation

Validation should occur before a file is created or opened.

A post-extraction inspection can be useful as an additional security measure, but it should never replace validation at the point where the destination path is selected.

The overall principle is simple:

**Do not allow untrusted archive metadata to determine a filesystem destination without enforcing containment at the point of use.**

### 10. Responsible disclosure timeline

The disclosure process was an important part of this research.

Below is the timeline based on the MSRC activity feed.

DateEventSeptember 2, 2026Vulnerability submitted to Microsoft MSRC.September 2, 2026MSRC created case 142705.September 2, 2026Initial research archive uploaded.September 2, 2026Additional research material uploaded.November 13, 2026Microsoft confirmed the reported behavior.November 13, 2026Microsoft informed me that the underlying issue had already been reported by another researcher.November 13, 2026I acknowledged the duplicate determination and expressed appreciation for the recognition.November 24, 2026Microsoft confirmed that the fix had been released and my acknowledgement had been published on the CVE.November 24, 2026Case closed as Complete — Duplicate.

### 10.1 Microsoft confirmed the behavior

On November 13, 2026, MSRC provided an important update:

Microsoft confirmed the behavior described in my report and stated that its investigation would continue to determine how to address the issue.

This was an important validation milestone.

It established that the behavior I had identified was not simply a theoretical concern raised through source-code inspection.

### 10.2 Duplicate classification

Microsoft subsequently informed me that the same underlying issue had already been reported by another researcher.

Consequently, my submission was not eligible for a bounty under Microsoft’s Bounty Program terms.

The case was therefore classified as:

**Complete — Duplicate**

This does not mean that the reported behavior was invalid.

It means that the underlying vulnerability had already entered Microsoft’s reporting process through another submission.

### 10.3 Fix released and acknowledgement published

On November 24, 2026, Microsoft sent the final update:

The fix for the report had been released, and my acknowledgement had been published on the CVE.

This was the most important outcome of the disclosure process.

Although the report did not qualify for a bounty, the issue was addressed and the research received acknowledgement through Microsoft’s coordinated disclosure process.

### 11. What I learned from this research

This investigation reinforced several important lessons for vulnerability researchers and software developers.

### 11.1 Security fixes must cover every implementation

A security patch should not be evaluated only by examining the code that was changed.

Researchers should also identify alternative implementations that perform the same security-sensitive operation.

A vulnerability may survive when one code path receives a security improvement but another path continues using the original unsafe assumptions.

### 11.2 Archive extraction is a security boundary

Archive extraction should never be treated as a simple file-management operation.

Archive entry names are untrusted input.

The application must ensure that extracted files remain inside their intended destination directory.

### 11.3 Path construction is different from path authorization

Using a path-combination API does not establish that a destination is safe.

Security requires canonicalization, containment validation, and appropriate handling of filesystem behavior.

### 11.4 Validation must happen before side effects

Checking files after extraction is not an adequate substitute for preventing unauthorized writes.

Security validation should occur before creating or opening the destination file.

### 11.5 Native and managed APIs require separate security reviews

Managed APIs may provide protections that developers do not automatically receive when using native interfaces.

When applications mix managed .NET code with Windows-native APIs, the security assumptions of each layer must be examined independently.

### 11.6 A duplicate report can still represent meaningful research

One of the more important professional lessons was understanding the distinction between a valid vulnerability report and bounty eligibility.

A report can be technically meaningful, independently investigated, and confirmed by a vendor while still being classified as a duplicate.

Vulnerability research is not only about receiving a CVE or bounty.

It is also about identifying security weaknesses, communicating them responsibly, and helping vendors improve their products.

### 12. Conclusion

This investigation began with a relatively simple question:

**If PowerShell had introduced security protections for archive extraction, were all of its extraction mechanisms actually enforcing the same security boundary?**

Examining the Windows-native CAB extraction implementation led me to investigate the FDI callback mechanism, particularly FdiNotify, and the way archive entry names influenced filesystem destinations.

The resulting report described a potential path traversal issue involving missing destination containment validation in the CAB extraction path.

I submitted the findings to Microsoft on September 2, 2026.

Microsoft confirmed the reported behavior on November 13, 2026, subsequently released a fix, and published my acknowledgement on the CVE on November 24, 2026.

The report was closed as a duplicate, so it did not qualify for a bounty. Nevertheless, it represented an important research experience: investigating a security boundary in a widely used development and automation environment, reporting the issue responsibly, and receiving vendor confirmation and acknowledgement.

The broader lesson extends beyond PowerShell.

Whenever software extracts untrusted archives, processes external file metadata, or translates user-controlled paths into filesystem operations, every execution path must enforce the same security guarantees.

A security fix is only as strong as the least-protected path that reaches the sensitive operation.

### References and further reading

1. **NIST National Vulnerability Database — CVE-2022–41076**
[https://nvd.nist.gov/vuln/detail/CVE-2022-41076](https://nvd.nist.gov/vuln/detail/CVE-2022-41076)
2. **Microsoft Security Response Center — CVE-2022–41076**
[https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41076](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41076)
3. **Microsoft Security Update Guide**
[https://msrc.microsoft.com/update-guide/](https://msrc.microsoft.com/update-guide/)
4. **MITRE CWE-22 — Improper Limitation of a Pathname to a Restricted Directory**
[https://cwe.mitre.org/data/definitions/22.html](https://cwe.mitre.org/data/definitions/22.html)
5. **Microsoft .NET — Path.GetFullPath documentation**
[https://learn.microsoft.com/en-us/dotnet/api/system.io.path.getfullpath](https://learn.microsoft.com/en-us/dotnet/api/system.io.path.getfullpath)
6. **Microsoft .NET — Path.Combine documentation**
[https://learn.microsoft.com/en-us/dotnet/api/system.io.path.combine](https://learn.microsoft.com/en-us/dotnet/api/system.io.path.combine)
7. **Microsoft Learn — File Decompression Interface (FDI)**
[https://learn.microsoft.com/en-us/windows/win32/devnotes/file-decompression-interface](https://learn.microsoft.com/en-us/windows/win32/devnotes/file-decompression-interface)

**Disclosure note:** This article documents my independent research and the information made available to me through Microsoft’s MSRC disclosure process. The report was closed as a duplicate, and I do not claim to be the first researcher to report the underlying issue. The complete Windows end-to-end exploitation chain was not independently reproduced in my Linux-only research environment. Technical descriptions of potential exploitation should therefore be distinguished from the behavior Microsoft confirmed and the fix Microsoft released.
