# Riddle Registry ~ CyLab Security Academy Write-up | Finding Hidden Clues in PDF Metadata

- **Source URL:** https://medium.com/@affanhaxor/riddle-registry-cylab-security-academy-write-up-finding-hidden-clues-in-pdf-metadata-2c8378d382d1
- **Fetched from:** https://medium.com/@affanhaxor/riddle-registry-cylab-security-academy-write-up-finding-hidden-clues-in-pdf-metadata-2c8378d382d1?source=rss-a70f2c751bb6------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14969 (id 14969)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Affanhaxor / Wed, 04 Nov 2026 05:33:22 GMT

**Author:** Affanhaxor

**Platform:** CyLab Security Academy

**Category:** Forensics / Information Disclosure

**Challenge:** Riddle Registry

**Topic:** PDF Metadata Analysis, Base64 Decoding, and Hidden Information

The **Riddle Registry** challenge on CyLab Security Academy demonstrates how important it is to examine file metadata during a security investigation.

At first glance, the challenge provides a PDF document named confidential.pdf. The document contains a short story and several suspicious-looking details. However, the actual flag is not clearly visible in the main content.

The challenge encourages us to look beyond what is displayed inside the PDF and inspect the document’s metadata.

In this write-up, I will explain how I reviewed the PDF, discovered an encoded value in its author metadata, and decoded it to reveal the flag.

I started by opening the provided confidential.pdf file in the browser's PDF viewer.

The document contained the title:

**The Ultimate Guide to Flag Hunting**

It also included a welcome message and a short story suggesting that something might be hidden inside the document.

The text included clues such as:

These messages suggested that the visible content might not contain the complete answer.

Instead of spending too much time searching through the visible text, I decided to inspect the document’s properties and metadata.

PDF files contain metadata that describes the document. Depending on how the file was created, metadata may include:

This information is commonly used for document management, but it can also contain hidden clues or accidentally exposed information.

I opened a PDF metadata viewer and uploaded confidential.pdf for analysis.

The metadata showed several details, including the file name, file size, PDF version, and producer.

The most interesting field was **Author**.

Instead of a normal author name, the field contained a long encoded-looking string.

This was a strong indication that the metadata contained information that needed further analysis.

The Author field contained the following Base64-looking value:

YWNnZGVteXtwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV80NzcwZDRlY30=

At this point, the value did not look like readable text.

Base64 is a common encoding format used to represent binary data as text. It is not encryption and does not require a secret key to decode.

Since the value appeared to use Base64 encoding, I decided to decode it.

I copied the encoded value from the PDF’s Author field and used a Base64 decoder.

The decoding process converted the encoded text into a readable string.

The output revealed the challenge flag:

`academy{puzzl3d_m3tadata_f0und!_4770d4ec}`
This confirmed that the PDF metadata contained the hidden information required to complete the challenge.

The important part of this challenge was recognizing that the information was not hidden in the visible PDF content.

Instead, the flag was stored inside the document’s metadata, specifically the Author field.

The process involved three main steps:

This approach is useful in digital forensics and security assessments because files can contain information that is not immediately visible to users.

PDF metadata is information stored within a document that describes its properties.

For example, a PDF may contain an author name, document title, creation date, or application information.

Metadata can be useful for identifying how a document was created and who may have created it. However, developers and users sometimes forget to remove sensitive information before sharing files.

In this challenge, the Author field was deliberately used to store the encoded flag.

Base64 is an encoding scheme that converts data into a text representation using a set of printable characters.

It is frequently used when data needs to be represented in text-based systems.

Base64 is **not encryption**. Anyone who obtains the encoded value can decode it without a password or secret key.

For example, on Linux, a Base64 string can be decoded using:

echo 'BASE64\_VALUE' | base64 -d

Replace BASE64\_VALUE with the encoded string.

This is useful when investigating suspicious strings found in metadata, configuration files, or application responses.

Metadata can reveal information that developers did not intend to expose.

Examples include:

Although metadata is often overlooked, it should be included in security reviews and forensic investigations.

This challenge provides several important lessons:

The **Riddle Registry** challenge was a useful exercise in document analysis and information discovery.

The PDF appeared to contain a simple story, but the real clue was hidden in its metadata. By examining the Author field, identifying the Base64-encoded value, and decoding it, I was able to retrieve the flag.

The main takeaway is that **a file’s visible content does not always reveal everything it contains**.

For security professionals, metadata analysis is an important part of reconnaissance and digital forensics. For developers and document creators, this challenge highlights the importance of reviewing file properties before sharing documents publicly.

**Thanks for reading!**

**LinkedIn:** [https://www.linkedin.com/in/affanhaxor](https://www.linkedin.com/in/affanhaxor)

**Instagram:** [https://instagram.com/affan\_haxor](https://instagram.com/affan_haxor)

*Follow me for more CTF write-ups, web security labs, and AppSec content.*
