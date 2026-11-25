# White Pixels, Big Problems

- **Source URL:** https://medium.com/@prabaswaradaffa2/white-pixels-big-problems-an-image-decompression-bomb-case-study-b832b442f2de
- **Fetched from:** https://medium.com/@prabaswaradaffa2/white-pixels-big-problems-an-image-decompression-bomb-case-study-b832b442f2de?source=rss-5dcc53ddc0b1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14982 (id 14982)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mephisto / Fri, 13 Nov 2026 07:19:29 GMT

While testing a profile picture upload feature on a web application, one simple question came to mind: *“Does the server actually validate image dimensions, or does it only check file size?”*

Turns out my suspicion was right and the result was pretty interesting. With a PNG file that was only 1.5 MB, I managed to make the server take **over 22 seconds** to process a single request. In this write-up, I’ll walk through how I did it, why it happens, and why it’s still worth discussing even though the bug bounty program rejected the report.

Before diving into the technical details, let’s align on the concept first.

Image formats like PNG use compression. So an image filled with a solid color (say, pure white) can be compressed into a very small file, even though the image’s pixel dimensions are enormous.

A simple analogy: imagine you have a blank canvas the size of a football field, but since it’s just plain white, you can describe the entire thing with one sentence: “white canvas, 100x50 meters.” Simple, right? That’s roughly how image compression works under the hood.

The problem arises when a server receiving that image immediately decodes it fully into memory without first checking how large the actual dimensions are. The server will try to “redraw” every single pixel from that short description — and if the dimensions are absurdly large, it will consume a massive amount of RAM, even though the file sent was tiny.

This is called a decompression bomb — in the context of images, sometimes referred to as a “pixel flood.”

I found a profile picture upload endpoint:

PUT /rest/users/profile-picture

Content-Type: application/json

{"image": "data:image/png;base64,\<data>"}

The first thing I noticed: the server accepts the image as **base64 inside a JSON body**, not a regular multipart upload. This means there’s no filename or extension validation at this layer — the only thing checked is the MIME type embedded in the data URI itself.

That made me suspicious: if only the MIME type is checked, what about validation of the file’s actual **content** — specifically, its dimensions?

The payload is surprisingly easy to generate, just a few lines of Python:

from PIL import Image

import base64

import io

dimension = 20000

img = Image.new('RGB', (dimension, dimension), color='white')

buffer = io.BytesIO()

img.save(buffer, format="PNG")

raw\_size = len(buffer.getvalue())

b64\_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

print(f"Dimensi: {dimension}x{dimension}")

print(f"Ukuran file mentah: {raw\_size / 1024:.2f} KB")

print(f"Ukuran Base64 (payload): {len(b64\_str) / 1024:.2f} KB")

if len(b64\_str) \< 2000000:

with open("payload\_bomb\_20k.txt", "w") as f:

f.write(f'{{"image":"data:image/png;base64,{b64\_str}"}}')

print("Berhasil dibuat dan disimpan ke payload\_bomb\_20k.txt")

else:

print("Terlalu besar, coba turunkan dimensinya.")

The trick lies in two key things:

I gradually increased the dimensions while measuring response time using Burp Suite. Here’s what I found:

Take a close look: the payload only grew from a few KB to 1.5 MB (a few hundred times larger, at most), but the response time increased **34x** compared to the baseline. That’s clearly disproportionate — the only reasonable explanation is that the server was struggling to allocate memory for decoding an image of that size.

I reported this finding to the relevant bug bounty program, but it was rejected because the “DoS/resource exhaustion” category falls outside their scope. Fair enough — that policy makes sense from the program’s perspective, since testing DoS on production carries real risk to availability for other users.

That said, from a technical standpoint, I still wanted to share this as a learning point — this kind of bug (missing dimension validation) is fairly common in image upload features, and often gets overlooked because validation efforts typically focus on file type or byte size, not the actual content/dimensions of the file itself.

Thanks For Reading :)
