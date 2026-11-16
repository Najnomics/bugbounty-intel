# P4 Anonymous S3 Bucket Object Listing Leading to Cloud Storage Information Disclosure

- **Source URL:** https://medium.com/@akashmotkar001/p4anonymous-s3-bucket-object-listing-leading-to-cloud-storage-information-disclosure-555ee8a3e796
- **Fetched from:** https://medium.com/feed/@akashmotkar001
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14985 (id 14985)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Severity:** P4 — Low

**Vulnerability Type:** Misconfigured Cloud Storage / Information Disclosure

**Bugcrowd VRT:** Server Security Misconfiguration → Misconfigured S3 Bucket → Readable/Listable Bucket

**CWE:**

- CWE-548 — Exposure of Information Through Directory Listing
- CWE-200 — Exposure of Sensitive Information to an Unauthorized Actor
- CWE-668 — Exposure of Resource to Wrong Sphere

**CVSS v3.1:** 3.7 (Low)

**CVSS Vector:** AV/AC/PR/UI/S/C/I/A

### 1. Description

During external security testing, an insecure cloud storage configuration was identified in an application-associated Amazon S3 storage environment.

The storage bucket permits unauthenticated users to perform object-listing operations through the S3 ListBucket API.

As a result, an external user can send a request to the bucket’s root endpoint and retrieve an XML response containing the names of stored objects, directory prefixes, object metadata, and the bucket owner’s canonical identifier.

The listing operation is accessible without authentication or valid AWS credentials.

Testing revealed that the bucket returns up to 1,000 object keys in a single response and supports pagination through continuation tokens. This allows an unauthenticated user to enumerate the available object namespace.

The exposed objects primarily consisted of publicly intended documentation, PDF files, CSS resources, regional documents, and product-related downloadable materials.

Although no sensitive credentials, customer information, database backups, or private signing material were identified during testing, exposing the complete storage namespace provides unnecessary infrastructure information to external users.

The vulnerability represents an insecure cloud storage permission configuration that allows anonymous users to enumerate stored objects.

### 2. Affected Component

**Component:** Amazon S3 Cloud Storage

**Service:** S3 Object Storage

**Affected Functionality:** Anonymous Object Listing

**Authentication Required:** No

**Permission Involved:** s3:ListBucket

### 3. Steps to Reproduce

### Prerequisites

- Linux environment (Kali Linux recommended).
- curl.
- xmllint (optional, for formatting XML responses).

Install the required utility:

sudo apt update

sudo apt install curl libxml2-utils -y

### Step 1 Check anonymous access to the storage endpoint

Send an unauthenticated HTTP request to the affected storage endpoint:

curl -sS -i "https://\<affected-storage-host>/?list-type=2"

Observe the HTTP response.

The server responds successfully without requiring AWS credentials or an authenticated session.

### Step 2 Retrieve the anonymous object listing

Execute:

curl -sS "https://\<affected-storage-host>/?list-type=2" | xmllint --format -

Observe the returned XML response.

The response contains an S3 ListBucketResult structure with information about the available objects.

### Step 3 Examine the exposed storage information

Review the XML response for the following information:

- Object keys and filenames.
- Directory prefixes.
- Last-modified timestamps.
- Object sizes.
- ETags.
- Storage class information.
- Bucket owner canonical identifier.

The response demonstrates that an unauthenticated user can enumerate the storage bucket’s object namespace.

### Step 4 Verify object-listing pagination

Inspect the XML response for the following fields:

\<IsTruncated>true\</IsTruncated>

\<NextContinuationToken>...\</NextContinuationToken>

If the response indicates that additional objects are available, the listing can be continued using the returned continuation token:

curl -sS "https://\<affected-storage-host>/?list-type=2&continuation-token=\<TOKEN>"

This allows additional object keys to be enumerated without authentication.

### Step 5 Review the exposed object inventory

Inspect the returned object keys and identify the types of resources exposed.

During the assessment, the listing included documentation directories, PDF documents, CSS resources, regional documents, and product-related downloadable files.

No sensitive credentials, customer records, database backups, or private signing materials were identified in the reviewed object inventory.

### 4. Security Impact

The vulnerability allows unauthenticated external users to enumerate the contents of the cloud storage bucket.

Potential security implications include:

**1. Storage Namespace Disclosure**

An attacker can identify the names and directory structure of stored objects without requiring authentication.

**2. Infrastructure Information Disclosure**

The exposed object inventory may reveal internal naming conventions, resource organization, documentation structures, and storage patterns.

**3. Increased Reconnaissance Capabilities**

An attacker can use the discovered object keys to identify interesting resources and understand how the application’s downloadable content is organized.

**4. Future Exposure Risk**

If sensitive files are accidentally uploaded to the publicly listable bucket in the future, their filenames and locations could become discoverable by external users.

**5. Unnecessary Cloud Resource Exposure**

Allowing anonymous users to enumerate the complete object namespace exposes storage metadata that may not need to be publicly accessible.

**Impact limitation:** During this assessment, the enumerated content was primarily public download material. No confirmed exposure of sensitive customer data, credentials, or confidential backups was identified. Therefore, direct data compromise is not claimed.

### 5. Root Cause Analysis

The root cause is an overly permissive Amazon S3 bucket access policy or access-control configuration.

The bucket permits anonymous principals to execute the s3:ListBucket operation.

This allows external users to enumerate stored object keys without authentication.

Public access to individual downloadable files, where required for business purposes, should not automatically grant anonymous users permission to enumerate the entire bucket.

### 6. Remediation

The following remediation measures are recommended:

1. Remove anonymous s3:ListBucket permissions from the affected bucket.
2. Review the bucket policy and access-control lists for unintended public permissions.
3. Enable Amazon S3 Block Public Access wherever public access is not required.
4. If public downloads are necessary, permit access to specific objects without allowing anonymous bucket listing.
5. Consider serving public resources through CloudFront with Origin Access Control.
6. Restrict direct access to the underlying S3 bucket where appropriate.
7. Review existing object permissions to ensure confidential resources are not publicly accessible.
8. Periodically audit bucket policies and permissions to prevent accidental exposure.

### 7. Classification

AttributeClassificationVulnerabilityAnonymous S3 Bucket Object ListingSeverityP4 — LowBugcrowd VRTMisconfigured S3 Bucket — ListableCVSS v3.13.7 — LowCWECWE-548, CWE-200, CWE-668CategoryCloud Security MisconfigurationAttack VectorNetworkPrivileges RequiredNoneUser InteractionNoneStatusConfirmed
