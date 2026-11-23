# Getting RCE — Challenge #1025 by Intigriti

- **Source URL:** https://hamzaavvan.medium.com/getting-rce-challenge-1025-by-intigriti-b3d0033a286d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251022003909/https://hamzaavvan.medium.com/getting-rce-challenge-1025-by-intigriti-b3d0033a286d
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11277 (id 11277)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Getting RCE — Challenge #1025 by Intigriti

So I got a notification from discord about an amazing **Remote Code Execution (RCE)** challenge from the Intigriti platform created by , and decided to give it a try.

Let’s get started…

After digging into this challenge for a few minutes, I found that the backend sends a curl request to any URL provided by the user (me)

I decided to check if the request made by the server discloses any critical information, like an authentication header or something, but the request did not disclose any sensitive information, as we can see in the screenshot of my netcat listener.

There were some restrictions in placed, I wasn’t able to make a request to localhost, 127.0.0.1, but it was possible to bypass the restriction by giving http://0.0.0.0 or [http://127.127.127.127](http://127.127.127.127), but these bypasses served only the default challenge page. Afterwards, I tried checking for AWS metadata endpoint and ended up finding google cloud internal metadata that we could access through: [https://challenge-1025.intigriti.io/challenge.php?url=http://metadata/computeMetadata/](https://challenge-1025.intigriti.io/challenge.php?url=http%3A%2F%2Fmetadata%2FcomputeMetadata%2F)

And after checking the [https://challenge-1025.intigriti.io/challenge.php?url=http://metadata/computeMetadata/v1](https://challenge-1025.intigriti.io/challenge.php?url=http%3A%2F%2Fmetadata%2FcomputeMetadata%2Fv1) endpoint, I found out that it was a dead end for me

Then I switched my strategy to check for other common protocols supported by curl. I tried to use `file://` and ended up getting this error (shown in screenshot):

Thanks to my experience with curl due to my programming background, I appended `%23http` or `(#http)` as a bypass. Because it looked like the backend didn’t care where http appeared within the `?url=` parameter, and just like that, BOOM! The restriction was bypassed.

Bypass: [https://challenge-1025.intigriti.io/challenge.php?url=file:///%23http](https://challenge-1025.intigriti.io/challenge.php?url=file%3A%2F%2F%2F%23http)

The file `93e892fe-c0af-44a1–9308–5a58548abd98.txt` contained the flag for this challenge ;)


Payload: `file:///93e892fe-c0af-44a1-9308-5a58548abd98.txt%23http`

Payload Url: [https://challenge-1025.intigriti.io/challenge.php?url=file:///93e892fe-c0af-44a1-9308-5a58548abd98.txt%23http](https://challenge-1025.intigriti.io/challenge.php?url=file%3A%2F%2F%2F93e892fe-c0af-44a1-9308-5a58548abd98.txt%23http)

Flag: **INTIGRITI{ngks896sdjvsjnv6383utbgn}**

But the real challenge was getting a **reverse shell** on the server. So, let me share my story of how I got a reverse shell through a 403 bypass. So after digging hard with open eyes, I found another hidden php file (not that hidden if you look with open eyes)`upload_shoppix_images.php`

Looking into its source code, I was assured that I could upload a PHP shell disguised as an image and successfully obtain a reverse shell.

From the source code analysis, it indicates that the file type checking mechanism (lines 61–63) is permissive and does not restrict uploads by file extension. The main obstacle to exploitation is the prior `mime_content_type()` check, which validates the file's actual MIME type and presents a significant challenge.

1. [mime_content_type()](https://www.php.net/manual/en/function.mime-content-type.php)
[Reference: mime\_content\_type](https://www.php.net/manual/en/function.mime-content-type.php)
2. the whitelisted filename includes `.png`, `.jpg` or `.jpeg`

The `mime_content_type()` check can be bypassed by embedding a malicious PHP payload within a file that has a valid image signature, and renaming the extension, also including whitelisted ones like `shell.jpg.php`Or create a polyglot file by prepending a valid image header (e.g., `GIF87a`) to a PHP reverse shell payload. The `mime_content_type()` function will identify the file as a GIF, while the PHP engine will still execute the malicious code.

After concluding all the results, when I tried to open the file, I got a 403 error 😲

The hint I got from the error is Apache. Since I share a long, sweet journey working with Apache applications, it wasn’t an issue for me to figure out what to do. I immediately started looking into Apache2 config files, and after analysing a few files, I went straight to the main culprit `000-default.conf`(according to my knowledge). And I knew it!! I found my final answer to the question:`is-shoppix-admin` header and the secret to the 403 page bypass.

By looking at the syntax, I realized it would be a header, so without wasting any time, I quickly added the header with the`is-shoppix-admin: true` into the request headers, sent the request, and received a 200 OK response.

## Before

## After Adding “**is-shoppix-admin"** header

Then I just picked up the php reverse shell code from [Online — Reverse Shell Generator](https://www.revshells.com/), edited it, and uploaded it to the server.

The first attempt gave me an error due to incorrect image bytes. After removing the trailing bytes of the image from the request body and re-uploading, the payload executed successfully.

BINGO! and I got the reverse shell.

If you like my content, don’t forget to **clap** and **comment** on this article, and also support me by subscribing to my [YouTube](https://www.youtube.com/@hamzaavvan) channel. I upload cool videos like challenges wakthrough and video related to my bug bounty journey.
