# Unrestricted File Upload Walkthrough — VulnLab by Yavuzlar

- **Source URL:** https://medium.com/@muhammadriva/unrestricted-file-upload-walkthrough-vulnlab-by-yavuzlar-76854ebafe84?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240716184933/https://medium.com/@muhammadriva/unrestricted-file-upload-walkthrough-vulnlab-by-yavuzlar-76854ebafe84
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6498 (id 6498)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Unrestricted File Upload Walkthrough — VulnLab by Yavuzlar

Unrestricted File Upload is a vulnerability where an application allows users to upload files without proper validation or security checks. This can lead to serious security issues because attackers can exploit it to upload malicious files, such as scripts or executable files, onto the server. Once uploaded, these files can be used to:

1. **Execute Malicious Code**: Attackers can upload scripts or executable files that, when executed on the server, can perform unauthorized actions like data theft, server takeover, or spreading malware.
2. **Gain Unauthorized Access**: By uploading files like web shells or backdoors, attackers can gain persistent access to the server, bypassing normal authentication mechanisms.
3. **Host Malware**: Malicious files can be hosted on the server and distributed to other users, infecting their systems when downloaded.
4. **Abuse Server Resources**: Uploading large or numerous files can consume server resources, leading to denial of service for legitimate users.

To mitigate this vulnerability, applications should implement strict file upload validation and enforce restrictions on file types, sizes, and locations. They should also perform server-side checks to verify the integrity and safety of uploaded files before allowing them to be accessed or executed. Regular security audits and updates are essential to ensure ongoing protection against such threats.

# 1. Unrestricted

In this first part, we can upload files of any type, and we can obtain the file storage path for exploitation.In this first part, we can upload files of any type, and we can obtain the file storage path for exploitation.

# 2. MIME Type

In this part, the MIME type is used to filter which types of uploaded files are allowed. Unlike in part 1 where any file type could be uploaded, here we will attempt to bypass the filtering process using BurpSuite.

Prepare any backdoor file, you can get them from GitHub where there are plenty of options available. For example, the backdoor file I’m using can be found at the following [GitHub](https://github.com/backdoorhub/shell-backdoor-list/blob/master/shell/php/p0wny-shell.php)

Open Burp Suite and intercept the upload of the backdoor file as shown below.

Now let’s change the Content-Type based on the allowed filters only. You can visit the following link to see a summary of the code for [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)

It’s time to manipulate the Content-Type using Burpsuite

Congratulations, the backdoor file has been successfully uploaded, and now it’s time to go surfing.

Klik link on File Path to run Backdoor

Thank you for following this article. I hope it has helped you understand better. I apologize if anything was unclear.
