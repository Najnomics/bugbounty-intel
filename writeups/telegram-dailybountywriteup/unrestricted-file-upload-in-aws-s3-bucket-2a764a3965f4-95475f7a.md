# Unrestricted File Upload in AWS S3 Bucket

- **Source URL:** https://infosecwriteups.com/unrestricted-file-upload-in-aws-s3-bucket-2a764a3965f4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20261116211027/https://infosecwriteups.com/unrestricted-file-upload-in-aws-s3-bucket-2a764a3965f4
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7481 (id 7481)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Discovering an Unrestricted File Upload in AWS S3 Bucket

AWS S3 Bucket Misconfiguration


I was recently exploring🔍 a web application for vulnerabilities and came across an issue that could seriously compromise the security of AWS S3 buckets 🪣. While I was initially searching for a SQL injection 💉 vulnerability due to the **PHP** extension and the presence of an **id** parameter in the URL, I stumbled upon something unexpected—a misconfigured AWS S3 bucket.

## Let’s Go🚶♂️

Here’s a detailed 👌 breakdown of the vulnerability, how I found it, and its potential impact.

## Vulnerability:

Unrestricted Remote File Upload and Deletion.

The vulnerability I found allows anyone with the correct S3 bucket URL to upload and delete files without authentication ☠️ This can be dangerous as it exposes the bucket to unauthorized users, allowing them to manipulate files, upload malicious content, or even delete crucial data.


## Steps to Reproduce✨️

1\. Inspect the Page Source: I started by viewing the page source of the gallery page:

*view-source:http://www.example.com/gallery.php?id=10*

Here, I noticed a reference to an S3 bucket URL(images of the website are hosted on this aws s3 bucket):

*https://bucketname.s3-ap-south-1.amazonaws.com/*

2\. Set Up AWS CLI: To interact with the bucket, I set up the AWS Command Line Interface (CLI) using Kali Linux. If you’re unfamiliar with AWS CLI installation, here’s a helpful guide:

*https://www.cyberciti.biz/faq/how-to-install-aws-cli-on-linux/*

3\. List the Bucket's Contents: Once AWS CLI was ready, I ran the following command to check the files in the bucket:

**aws s3 ls s3://bucketname/ --no-sign-request**

4\. Upload a Test File: I created a simple text file called testput.txt and used the following command to upload it:

## Get viperx9’s stories in your inbox

Join Medium for free to get updates from this writer.

**aws s3 cp testput.txt s3://bucketname/testput.txt --no-sign-request**

5\. Verify the Upload: To confirm the file was successfully uploaded, I accessed it directly via the S3 bucket URL:

*https://bucketname.s3-ap-south-1.amazonaws.com/testput.txt*

6\. Delete the File: Finally, I deleted the file using this command:

**aws s3 rm s3://bucketname/testput.txt --no-sign-request**

## Impact 😈

This vulnerability opens up several potential risks:

**Unauthorized File Uploads:** Attackers can upload malicious files to the S3 bucket, which could be used for phishing, malware distribution, or other harmful purposes.

**Data Loss:** Important files could be deleted or replaced, resulting in the loss of critical data.

**Malicious Hosting:** The bucket could be exploited to host malicious content, turning it into a platform for cyberattacks.

## Conclusion 🥸

By failing to properly configure the S3 bucket's permissions, the web application exposed sensitive file operations to unauthorized users. This vulnerability can have severe consequences, and it’s crucial for developers to always ensure their S3 buckets are secured against such threats.

## Reference:

*https://medium.com/@janijay007/s3-bucket-misconfiguration-from-basics-to-pawn-6893776d1007*

Special thanks 😊 to [Jay Jani](https://medium.com/u/507f41b869c9) 🙏 for his detailed write-up on AWS S3 bucket 🪣 exploitation. Without his article, I wouldn’t have been able to discover this vulnerability.

🫂
