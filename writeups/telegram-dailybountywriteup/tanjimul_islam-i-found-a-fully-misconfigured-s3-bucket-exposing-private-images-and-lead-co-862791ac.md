# I Found a Fully Misconfigured S3 Bucket Exposing Private Images and Lead Complete Takeover

- **Source URL:** https://medium.com/@tanjimul_islam/i-found-a-fully-misconfigured-s3-bucket-exposing-private-images-and-lead-complete-takeover-8e24320e612a
- **Fetched from:** https://medium.com/@tanjimul_islam/i-found-a-fully-misconfigured-s3-bucket-exposing-private-images-and-lead-complete-takeover-8e24320e612a?source=rss-6c861fc0bcb4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14886 (id 14886)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Md Tanjimul Islam Sifat / Sat, 29 Aug 2026 00:01:01 GMT

**By Md Tanjimul Islam Sifat (TI Sifat)** *Cybersecurity Researcher | Bug Bounty Hunter | Founder of SftSec Tim*

“The most dangerous misconfigurations aren’t the ones hidden in the code. They’re the ones sitting in plain sight on the infrastructure layer — waiting for someone to simply ask.”

I discovered that the Amazon S3 bucket prism-uploads — belonging to PRISM (an OYO platform) — was publicly accessible to **any unauthenticated user on the internet**. No credentials. No tokens. No exploits. Just a single AWS CLI command gave me the ability to:

I uploaded a test file, confirmed it was publicly served, discovered GPS metadata embedded in user photos, and then found evidence that the bucket had been discovered and abused by others for months — yet remained completely unpatched.

**CVSS Score: 9.3 — Critical.**

This is the full story of how I found it, how I proved it, and what it means.

PRISM is a platform under the OYO ecosystem — one of the world’s largest hospitality technology companies. Their infrastructure handles property management, bookings, user data, and content assets at enormous scale.

They run a Vulnerability Disclosure Program (VDP) on HackerOne with an important policy clause:

“Accepts reports for all owned assets based on impact, even if not listed in scope.”

That clause matters — because what I found wasn’t in their explicit asset list. But it was very clearly theirs.

I’ll be honest about my methodology: cloud asset discovery is a discipline I’ve been building into my recon process. When I target a company with a VDP, I don’t just test the web app. I enumerate their cloud footprint too — S3 buckets, exposed Azure blobs, Firebase databases, open GCP buckets.

The naming convention for S3 buckets is predictable. Companies tend to name their buckets after their brand:

```
{company-name}-uploads
{company-name}-assets
{company-name}-static
{company-name}-media
```
For PRISM, prism-uploads was an obvious candidate. One command confirmed it existed and was accessible:

aws s3 ls s3://prism-uploads/ --no-sign-request

The --no-sign-request flag is the key part. It tells the AWS CLI to send the request without any authentication credentials. If the bucket has public permissions, it responds. If it doesn't, you get an AccessDenied error.

It responded. And what it returned took my breath away.

**Output:**

PRE api/

PRE events/

PRE incoming/

PRE lambda/

PRE pending/

PRE processed/

PRE queue/

PRE triggers/

PRE uploads/

PRE webhooks/

2026-08-17 23:50:55 2446 codebuff-xss-verify-7a3f9.svg

2026-05-12 15:30:02 971 xss-poc-realvivek.svg

Let me highlight a few things about this output that immediately told me how serious this was:

**1. The directory structure is a full system map.** Directories like lambda/, triggers/, webhooks/, processed/, and queue/ don't look like static frontend assets. These look like **backend pipeline directories** — files being passed between internal services, Lambda functions, and event-driven workflows. Exposing this structure is like handing an attacker your entire system architecture diagram.

**2. The SVG files at the root level are alarming.** xss-poc-realvivek.svg — uploaded in May 2026. codebuff-xss-verify-7a3f9.svg — uploaded in August. These are clearly test files from **other security researchers** who had already discovered this bucket and were using it to host XSS proof-of-concept payloads.

Here’s what that means: this bucket has been open, discoverable, and actively writable by external parties for **at least three months** — and it was still fully unpatched when I found it.

That’s not a theoretical risk anymore. That’s proof of ongoing exploitation.

I dug into the uploads/ directory to understand what kind of data was stored there.

curl -I https://prism-uploads.s3.amazonaws.com/uploads/6784cdcef3417a3ee635240e/1758267786804-8529365.jpg

HTTP/1.1 200 OK

Content-Length: 20332

Last-Modified: Fri, 19 Sep 2025 07:43:07 GMT

Accept-Ranges: bytes

Server: AmazonS3

The path structure uploads/{24-character-hex-string}/ is immediately recognizable to anyone who has worked with MongoDB. These are **MongoDB ObjectIds** — the unique identifiers assigned to each user or entity in a MongoDB database.

This means:

A single aws s3 ls --recursive command could enumerate every user directory in the bucket. That's mass PII extraction, fully automated, at zero cost.

A readable bucket is bad. A writable bucket is a weapon.

I created a harmless test file and uploaded it:

echo "PRISM-Security-Test-POC" > test-poc.txt

aws s3 cp test-poc.txt s3://prism-uploads/test-poc.txt --no-sign-request

upload: ./test-poc.txt to s3://prism-uploads/test-poc.txt

No authentication. No error. One command, and I had written a file into a production S3 bucket belonging to a company serving millions of users.

I then verified the file was publicly served:

curl https://prism-uploads.s3.amazonaws.com/test-poc.txt

PRISM-Security-Test-POC

Confirmed. My file was now live on PRISM’s production S3 bucket, served under the amazonaws.com domain.

After the initial report was filed, I ran one more test that escalated the severity further:

aws s3 rm s3://prism-uploads/test-upload.txt --no-sign-request

delete: s3://prism-uploads/test-upload.txt

s3:DeleteObject — also publicly accessible.

This means an attacker doesn’t just have **read/write** access. They have **full CRUD**: Create, Read, Update, Delete.

A single malicious script could recursively wipe the entire bucket:

\# This command would destroy everything — do NOT run this

aws s3 rm s3://prism-uploads/ --recursive --no-sign-request

1,800+ files. User photos. Backend configs. Event data. Everything — gone in seconds. Irreversibly.

This is the finding within the finding — and the one that differentiates this report from any previous discovery of the same bucket.

While reviewing the JPEG files in the uploads/ directory, I checked the EXIF metadata embedded in user-uploaded photos. Modern smartphones embed GPS coordinates directly into photos unless the user or the application strips this data.

What I found in several JPEGs:

Latitude:  31.39°

Longitude: 74.36°

These coordinates resolve to a real, specific location. And they’re embedded inside photos uploaded by real PRISM users — photos that any anonymous internet user can now download and read.

This isn’t just a file exposure issue anymore. This is **location surveillance at scale** — a GDPR/CCPA violation exposing the physical whereabouts of users who never consented to their location data being made public.

Previous researchers who found this bucket likely focused on the XSS vector (uploading a malicious SVG). No one had flagged the GPS PII angle. That made my report a distinct finding with a higher and broader impact profile.

The uploads/{userId}/ path structure, combined with public ListBucket access, means an attacker can enumerate and download every user's uploaded content without any authentication. User photos, property documents, profile images — all of it is exposed. Given the bucket's association with a hospitality platform like OYO/PRISM, this could include passport scans, ID documents, and property records submitted during booking.

The amazonaws.com domain is trusted by virtually every corporate firewall, email filter, and endpoint detection system on the planet. Hosting phishing pages or malicious binaries at prism-uploads.s3.amazonaws.com/phishing-page.html would bypass most security controls that a victim company has in place. The brand legitimacy of amazonaws.com makes these attacks substantially more effective.

S3 costs money per GB stored and per GB transferred. An attacker with anonymous write access can upload unlimited data — terabytes, petabytes — directly into PRISM’s bucket. The resulting storage and egress fees would be charged to PRISM’s AWS account, with no cap, resulting in potentially catastrophic unplanned infrastructure costs.

With s3:DeleteObject confirmed publicly accessible, an attacker could delete the entire bucket's contents in a single recursive command. If PRISM lacks versioning or cross-region backup on this bucket, that data is permanently and irreversibly lost. This is the cloud equivalent of a ransomware attack — except there's no decryption key to negotiate over. The data is simply gone.

A complete S3 bucket takeover would allow an attacker to **delete the entire bucket and its contents**, resulting in total loss of availability and potentially permanent data destruction.

But I think , The bucket has been known to the security research community since at least May 2026 — **three months before my report**. Prior researchers tested it and moved on. The vulnerability sat unpatched, fully exploitable, the entire time.

The presence of those test files wasn’t a sign of prior remediation. It was a **receipt** proving sustained, ongoing exposure.

**Block all public access at the bucket level:**

aws s3api put-public-access-block \

--bucket prism-uploads \

--public-access-block-configuration \

BlockPublicAcls=true,\

IgnorePublicAcls=true,\

BlockPublicPolicy=true,\

RestrictPublicBuckets=true

**Audit the bucket policy** and remove any statement with "Principal": "\*". Every legitimate use case for serving user-uploaded content can be replaced with CloudFront signed URLs or S3 pre-signed URLs that expire after a defined window.

Adopt a proper signed URL pattern for serving user content:

User uploads file → Backend generates pre-signed URL → URL expires in 15 min → No public bucket needed

This pattern gives users access to their own content without exposing the bucket to the world.

**Enable S3 Versioning** — so that if files are accidentally or maliciously deleted or overwritten, previous versions can be restored.

**Enable S3 Server Access Logging** — so there’s an audit trail of who accessed what, when. This is critical for forensic analysis of what may have already been downloaded by unauthorized parties.

**Strip EXIF metadata server-side** — When users upload photos, process them through an image normalization pipeline (e.g., ImageMagick, Sharp) that strips all embedded metadata before storing to S3. Users should never expose their GPS coordinates through a platform that doesn’t make this a deliberate, informed choice.

**Rotate any exposed credentials** — Audit the bucket for .env, .json, and config files that may have been uploaded (intentionally or accidentally) by internal teams. If any AWS keys, API tokens, or database credentials were stored there, rotate them immediately.

**1. Cloud infrastructure is the largest attack surface most bug hunters ignore.** The web app might have rate limiting, WAFs, and solid authentication. But the S3 bucket behind it might be completely open. Always extend your recon to cloud assets.

**2. --no-sign-request is one of the most powerful reconnaissance flags you have.** Every AWS CLI command supports it. It tells you immediately whether a bucket has public permissions. Make it part of your standard recon checklist.

**3. Naming conventions are exploitable.** {company}-uploads, {company}-assets, {company}-static, {company}-cdn, {company}-media — test them all. Companies are predictable with their naming, and S3 bucket names are globally unique (which means you can directly probe them without any prior knowledge of the company's infrastructure).

**4. Existing test files in a bucket aren’t a sign it’s already been reported and fixed.** Those SVG files from other researchers? They were proof the bucket was known and unpatched — not proof it had already been closed. Unpatched vulnerabilities are valid. If a bug is still exploitable today, it’s a valid finding today.

**5. PII angle differentiates your report from duplicates.** When you suspect a bucket might have already been reported, dig deeper for a unique impact dimension. GPS metadata in user photos, .env files in a config directory, credentials in JSON files — these elevate an "already reported" finding into a distinct, higher-impact submission.

**6. Read the scope policy line by line.** PRISM’s VDP explicitly stated they accept reports on all owned assets based on impact, even unlisted ones. That clause is what validated my submission. Many programs have similar language — don’t dismiss a finding just because the specific asset isn’t in the scope table.

**7. Document everything before you touch anything.** Screenshots, command outputs, HTTP responses, timestamps. When a triage team reviews your report, they’re trusting your documentation. The cleaner and more detailed your evidence, the faster and smoother the process.

**It’s NA Because S3 Bucket not real PRISM Official owned Bucket. But Bug’s Is Real in Even it’s not owned into PRISM.**

This finding is a perfect example of why cloud security deserves as much attention as web application security. There was no injection, no bypass, no authentication flaw to exploit. The vulnerability was simply a misconfigured IAM policy — a checkbox someone forgot to uncheck during setup.

And yet the blast radius was enormous: thousands of users’ private content exposed, production infrastructure writable by anyone, backend pipeline directories enumerable, and GPS coordinates leaking the physical location of real people.

The bucket had been open for months. Other researchers had found it. Yet it remained unfixed — sitting there, fully accessible, waiting for someone with worse intentions than mine to come along.

That’s the real reason bug bounty programs exist. Not to be a game, but to create a reliable channel for researchers who find things like this to report them safely — before the wrong person does.

If you’re a security researcher, build cloud enumeration into your recon flow. If you’re a developer, check your S3 buckets right now. The AWS console makes it embarrassingly easy to block all public access with a single toggle. There’s no reason this should ever happen.

Hunt ethically. Disclose responsibly. Keep learning.

**Md Tanjimul Islam Sifat**, known online as **TI Sifat**, is a Cybersecurity Researcher, Bug Bounty Hunter, and Offensive Security Expert based in Bangladesh. He specializes in penetration testing, API security, cloud infrastructure vulnerabilities, and responsible vulnerability disclosure — helping organizations identify and fix real security weaknesses before malicious actors can exploit them.

He is the founder of **SftSec Tim**, a fast-growing cybersecurity Discord community dedicated to practical bug bounty education, real-world research, and building the next generation of ethical hackers through technical content, shared methodology, and collaborative learning.

*Hack ethically. Learn with consistency.*
