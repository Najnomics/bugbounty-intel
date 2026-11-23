# The File Upload Check That 90% of Hunters Forget (And How I Got $1500 From a JPEG)

- **Source URL:** https://medium.com/@userwithheart/the-file-upload-check-that-90-of-hunters-forget-and-how-i-got-1500-from-a-jpeg-008774a1e9b1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260602080903/https://medium.com/@userwithheart/the-file-upload-check-that-90-of-hunters-forget-and-how-i-got-1500-from-a-jpeg-008774a1e9b1
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14013 (id 14013)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
I used to test file uploads the same way everyone does.

Rename a PHP file to .jpg. Try to upload an .svg with script tags. See if I can bypass the filter with double extensions.

Basic stuff. And mostly useless on modern sites.

Then I found a file upload bug that paid $1500. Not because I did something clever. Because I tested something most people skip entirely.

Here’s what I changed.

– -

What Everyone Tests (And Why It Barely Works Anymore)

Most sites today aren’t dumb. They check file extensions. They scan for magic bytes. They even run antivirus on uploads.

So you try to upload shell.php.jpg and it blocks you. You try a polyglot file and it blocks you. You spend an hour and get nothing.

I’ve been there. It’s frustrating.

But here’s the thing – you’re testing the upload. The real bug is usually hiding after the upload.

– -

The Check That 90% of Hunters Forget

Once a file is uploaded, the server has to do something with it.

Serve it from a CDN. Generate a thumbnail. Resize it. Extract metadata. Rename it. Move it.

Every single one of those “something” actions is a potential bug.

Here’s what I test now, every single time.

First – Can I access the original file after upload?

Upload a normal image. Check where it’s stored. Is it /uploads/random-name.jpg? Is it https://cdn.target.com/images/user123/photo.jpg?

Now upload the same image again. Same URL? Different? Can you guess the pattern?

I once found a site that stored uploads at /files/userid/timestamp.jpg. I could change the userid in the URL and see anyone’s uploads. No auth check on the file serving endpoint. That was the bug. Not the upload itself.

Second – What happens when the server processes the file?

Upload an image with a really long filename. Like 500 characters. Does it error? Does it truncate? Can you inject path traversal into the filename?

Upload an image with metadata. Exif data, comments, artist name. Does the server render any of that metadata anywhere? If it shows the “artist” field on the profile page without sanitizing, that’s stored XSS waiting to happen.

Upload a valid image but with an invalid extension. Like a real JPEG saved as test.php. Does the server reject it based on content or just extension? If it only checks extension, you have a bypass.

Third – What happens when the file is deleted or replaced?

Upload a file. Delete it. Can you still access it via the old URL? If yes, the server isn’t properly cleaning up. Sometimes you can find deleted files from other users this way.

Upload a file. Upload another file with the same name. Does it overwrite? Can you overwrite someone else’s file if you know their filename pattern?

– -

The $1500 Bug – A JPEG That Wasn’t Just a JPEG

I was testing a site that let users upload profile pictures.

Normal stuff. Only JPEG and PNG. Max size 2MB. File name was hashed and stored in a CDN.

I uploaded a normal photo. Nothing happened. No bypass. No injection.

But then I noticed something weird. After uploading, the site displayed a thumbnail of my photo on the profile page. The thumbnail was generated on the fly – I could see a parameter in the image URL like /thumbnail?path=myhashedphoto.jpg&size=small.

I changed size=small to size=../../../etc/passwd.

The server tried to resize a file that didn’t exist and threw an error. The error message showed the full file system path. Not a bug yet, but interesting.

Then I tried path=../myhashedphoto.jpg. It worked. The thumbnail loaded.

That meant the server wasn’t sanitizing the path parameter. It was just joining strings.

I spent another hour testing path traversal. Eventually I found that I could access any file in the CDN bucket if I knew the hashed filename. But I didn’t know anyone else’s filename.

Then I realized – the site had a public profile directory. Every user’s hashed filename was exposed in the page source.

I grabbed another user’s hash, put it in the thumbnail endpoint with path=../../uploads/theirhash.jpg, and got their private photo.

That was the report. IDOR via path traversal in an image thumbnail endpoint. $1500.

The upload itself was completely secure. The thumbnail generator was the problem.

– -

What I Learned

Stop testing only the upload button.

Test everything that happens after. Where is the file stored? How is it accessed? Is there an image processor? A thumbnail generator? A metadata extractor? A CDN with weak permissions?

The upload is just the door. The real bugs are inside the house.

– -

If this helped you see file uploads differently, clap and follow. Tomorrow I’m breaking down how I test GraphQL endpoints – including the one query that finds IDORs in seconds.
