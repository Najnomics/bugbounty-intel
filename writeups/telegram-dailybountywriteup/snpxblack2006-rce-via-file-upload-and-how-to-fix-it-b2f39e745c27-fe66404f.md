# RCE Via File upload And How To Fix It

- **Source URL:** https://medium.com/@snpxblack2006/rce-via-file-upload-and-how-to-fix-it-b2f39e745c27?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250328002125/https://medium.com/@snpxblack2006/rce-via-file-upload-and-how-to-fix-it-b2f39e745c27?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9187 (id 9187)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# RCE Via File upload And How To Fix It

# What is a File Upload Vulnerability?

A File Upload Vulnerability is a type of security flaw found in websites or applications that allow users to upload files (such as images, videos, or documents). The danger arises when an attacker uploads a malicious file instead of a legitimate one, such as uploading a shell script to gain control over the server.

# What This Article Covers:

- The scenario I encountered and how I analyzed the website
- How developers can fix the vulnerability.
- Strong resources for learning about this vulnerability (both in Arabic and English).

# Discovery of the Vulnerability

I found a page that allowed me to upload an image as my profile picture.

1. **First Attempt:** I uploaded a `.png` image, and it was accepted normally.
2. **Second Attempt:** I tried uploading a PHP file with the following content:

```
<?php 
if(isset($_REQUEST['cmd'])){
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
}?>
```
This script executes commands passed as a parameter in the URL and returns the result.

**Example Usage:**

`https://victim.com/uploads/shell.php?cmd=whoami`
However, the server rejected the upload and returned a **403 Forbidden** status code.

# Bypassing Upload Restrictions

# 1. Testing File Extensions

I suspected that the server was blocking PHP files. I tried renaming the file to:

`file.png.php`
This method failed, suggesting that the server was checking for the full extension, not just the presence of `.png`.

# 2. Null Byte Injection

I attempted using a null byte (`%00`) to bypass the extension check:

`file.php%00.png`
The idea was that some servers might truncate the filename at the null byte, effectively making it a PHP file. However, this attempt also failed.

# 3. Manipulating the Content-Type Header

The **Content-Type** header indicates the MIME type of a file (e.g., `image/jpeg` for JPEG images, `image/png` for PNGs). I tried removing it from the request, but the server still rejected the upload.

# Exploiting the Vulnerability

After multiple failed attempts, I decided to explore **Magic Numbers**.

# What is a Magic Number?

A **Magic Number** is a unique sequence of bytes at the beginning of a file that identifies its type. Even if a file’s extension is changed, the Magic Number helps the system recognize the actual file format.

## Examples:

- PNG files start with: `89 50 4E 47 0D 0A 1A 0A`
- PDF files start with: `%PDF-1.7`

I uploaded a normal `.jpg` image, and the server accepted it, returning a **200 OK** status.

## Exploit Attempt:

I re-sent the exact same request, but this time, I modified the image content by embedding the PHP shell code inside it.

*But I sent the request and changed the file extension to PHP.*


**Result:** The server accepted the modified file and returned **200 OK**!

To confirm execution, I accessed the file and executed a command.

`https://victim.com/uploads/shell.php`
**Boom!** The command executed successfully, proving that the server only relied on the Magic Number to validate files.

# Why Did This Happen?

“The server only checked the Magic Number **but did not verify** whether the uploaded **file contained harmful content or if the filename matched** the file type. It only validated the allowed Magic Numbers, such as PNG and JPG, but did not prevent embedding malicious code within these files. The developer assumed that verifying the Magic Number alone was enough to prevent attacks, but as demonstrated, it was bypassed.”

# How to Fix the Vulnerability?

## Security Measures for Developers:

- **Monitor file upload logs** to detect suspicious activities.
- **Change directory permissions** to prevent execution of uploaded files.
- **Improve the PHP upload validation process.**

## Secure File Upload Code in PHP



<?php

// Define the directory where uploaded files will be stored (outside public_html for security)

$uploadDir = __DIR__ . '/../your_dir_here/';


// Allowed file extensions and MIME types

$allowedExtensions = ['jpg', 'jpeg', 'png' ];

$allowedMimeTypes = [

'jpg'  => 'image/jpeg',

'jpeg' => 'image/jpeg',

'png'  => 'image/png',

];


// Maximum file size (5 MB)

$maxFileSize = 5 * 1024 * 1024;


if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['uploadedFile'])) {

$file = $_FILES['uploadedFile'];


// Check for upload errors

if ($file['error'] !== UPLOAD_ERR_OK) {

die('An error occurred while uploading the file.');

}


// Check file size

if ($file['size'] > $maxFileSize) {

die('The file size exceeds the allowed limit.');

}


// Get file extension

$fileInfo = pathinfo($file['name']);

$fileExtension = strtolower($fileInfo['extension'] ?? '');


// Validate file extension

if (!in_array($fileExtension, $allowedExtensions)) {

die('File extension is not allowed.');

}


// Validate MIME type

$finfo = finfo_open(FILEINFO_MIME_TYPE);

$mimeType = finfo_file($finfo, $file['tmp_name']);

finfo_close($finfo);


if (!in_array($mimeType, $allowedMimeTypes)) {

die('The file type does not match the extension.');

}


// Additional validation for images using exif_imagetype()

if (in_array($fileExtension, ['jpg', 'jpeg', 'png'])) {

$imageType = exif_imagetype($file['tmp_name']);

if ($imageType === false) {

die('The uploaded file is not a valid image.');

}

}


// Generate a secure file name

$newFileName = bin2hex(random_bytes(16)) . '.' . $fileExtension;

$destination = $uploadDir . $newFileName;


// Ensure the upload directory is writable

if (!is_writable($uploadDir)) {

die('Upload directory is not writable.');

}


// Move the uploaded file to the destination directory

if (move_uploaded_file($file['tmp_name'], $destination)) {

echo 'File uploaded successfully.';

} else {

die('An error occurred while saving the file.');

}

} else {

echo 'No file was uploaded.';

}

?>
# References

By following these security measures, developers can prevent attackers from exploiting file upload vulnerabilities and ensure safer web applications.
