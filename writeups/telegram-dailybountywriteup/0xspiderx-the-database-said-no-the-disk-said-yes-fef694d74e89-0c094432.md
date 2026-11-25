# The Database Said No. The Disk Said Yes.

- **Source URL:** https://medium.com/@0xSpiderx/the-database-said-no-the-disk-said-yes-fef694d74e89
- **Fetched from:** https://medium.com/@0xSpiderx/the-database-said-no-the-disk-said-yes-fef694d74e89?source=rss-cc5802b996c4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14968 (id 14968)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Khaled Ebrahem / Mon, 02 Nov 2026 18:19:57 GMT

Inside a non-atomic file upload flaw where a 500 Server Error concealed a surviving PHP shell and how MIME-polyglotting bypassed the crash entirely.

The upload request returned 500 Server Error. Every log, every trace, every metric agreed: the operation had failed. But the file was already there.

That’s the core contradiction this article is about and it’s one that developers rarely anticipate, because the mental model of a “failed” operation assumes the system returned to its original state. In this case, it hadn’t.

The target was a Laravel 11 + Vue.js web platform running on Nginx 1.24.0 with PHP-FPM 8.3.36 on an Ubuntu server. The application handled file uploads through a backend API, with the upload logic wired directly from a Vue.js frontend component. The upload endpoint required only a registered user account no elevated roles or special permissions.

Rather than probing common upload endpoints, I started by examining the JavaScript bundle shipped with the frontend. The application had no public API documentation, and no upload request ever surfaced in the network traffic of a normal browsing session. The hidden endpoint existed in exactly one place: the distributed JavaScript.

Modern bundlers like Vite compile the full frontend logic including internal API calls, field names, and base URLs directly into the distributed JavaScript chunks. Developers ship this as a minified file, but minification is not confidentiality. Everything the frontend knows, a reader of that file knows too.

Inside app-d8f9a2b1.js, a single function disclosed the entire upload contract: the endpoint path, the base URL, the required field names, the accepted values for each field, and the HTTP method.

```
function y(g) {
    if (s.type !== "file") return;
    let d = new FormData;
    d.append("type", s.type);
    s.mediaType == 1 ? d.append("media_type", "image") :
    s.mediaType == 2 ? d.append("media_type", "audio") :
    s.mediaType == 3 ? d.append("media_type", "video") :
    d.append("media_type", "file");
    d.append("file", g.target.files[0]);
    // ...
    ve.upload({ url: "/files", baseURL: "https://target.com/api/v1", data: d, method: "POST" })
}
```
POST /api/v1/files a hidden endpoint, absent from the API documentation and invisible in any normal browsing session. Three required fields. Complete parameter contract. All of it sitting in a publicly served JavaScript file.

A JavaScript bundle is not obfuscation. It is documentation. The secrets it holds are not locked they are just unread.

The first attempt sending only the file came back with a clean 422 Unprocessable Entity: validation required both type and media\_type. Fair enough. The second attempt, with all three fields set and media\_type: image, returned a 500.

Laravel Telescope left accessible on a production deployment showed the reason immediately:

Intervention\Image\Exception\NotReadableException:

Unable to decode image from file (/tmp/phpWPQyV5)

When media\_type is image, the FileUploadTrait passes the uploaded bytes through the Intervention\Image library's GD decoder. A PHP file is not a valid image. GD fails before any storage operation occurs. This path was a dead end.

Switching to media\_type: file bypassed the image-decoding branch entirely. The third attempt reached further into the codebase and this time, the 500 response told a different story.

SQLSTATE\[23000\]: Integrity constraint violation:

1048 Column 'ext' cannot be null

SQL: insert into \`files\` (\`name\`, \`ext\`, \`mime\`, \`size\`, \`type\`, \`url\`, ...)

values ('1710000000abcd-shell.php', ?, 'text/x-php', 82, 'file',

'uploads/file/1710000000abcd-shell.php', ...)

Two things stood out in this trace. First, the SQL statement included the storage path uploads/file/1710000000abcd-shell.php which meant the file had a name and a location. Second, the error was a database constraint violation, not a validation failure at the application layer. The application had already decided on a filename and, as the source code review would confirm, had already written the file to disk before attempting the insert.

A 500 response describes the HTTP layer. It says nothing about what the filesystem did before the exception was thrown.

Reviewing the upload lifecycle in App\Traits\FileUploadTrait and FileController.php revealed the sequencing problem in full:

// Step 1 - physical write to the public storage disk

// Note: $generatedRandomName is built from timestamp + random + client's original filename

$path = $file->storeAs('uploads/file', $generatedRandomName);

// Step 2 - derive metadata from file content

$ext = $file->guessExtension(); // returns null for text/x-php MIME type

// Step 3 - attempt the database insert

File::create(\[

'name' => $generatedRandomName,

'ext' => $ext, // NULL triggers MySQL constraint violation

'mime' => $mime,

'url' => $path

\]);

The file is written to disk in step one. The database insert happens in step three. There is no catch block between them that calls Storage::delete() or unlink(). When the insert fails, the exception propagates, the 500 response goes back to the client and the PHP file sits untouched in /storage/uploads/file/.

This is the definition of a **non-atomic operation**: a multi-step process where a failure in one step does not automatically reverse the steps that already succeeded. In a bank transfer, you don’t debit the sender without crediting the receiver. In a file upload, you don’t write the file without guaranteeing the record that tracks it.

The most dangerous bugs are not in what the code validates. They are in the order it trusts.

Why does the file execute? The storage symlink is a standard Laravel deployment detail the application links public/storage to storage/app/public, making its contents publicly reachable. The file executed when requested, which indicates the server had no Nginx rule blocking PHP execution inside that path. No server configuration was read directly; this is inferred from observed behavior.

There is a second architectural detail worth stating clearly. The upload endpoint required session authentication a registered user account and a valid CSRF token. But that protection ends the moment the file lands on disk. Requests to /storage/uploads/file/... are handled directly by Nginx; they never pass through Laravel's routing or middleware stack. The application's access controls do not exist at the path where the file executes.

Authentication guarded the upload. Nothing guarded the execution.

The file the application believed it had rejected was sitting in a publicly accessible, PHP-executable directory reachable by anyone who knew its name, with no login required.

Remote Code Execution (RCE) means the server runs attacker-supplied code in this case, PHP that calls system functions in response to an ordinary HTTP request. The filename 1710000000abcd-shell.php visible in Telescope's SQL error log resolved to a direct URL under /storage/uploads/file/. A plain GET request returned:

HTTP/1.1 200 OK

Server: nginx/1.24.0 (Ubuntu)

Content-Type: text/html; charset=UTF-8

RCE\_POC::Linux \[redacted-hostname\] 6.8.0-124-generic ... x86\_64::PHP8.3.36::END

The server executed the payload. Operating context: uid=33(www-data).

To demonstrate full impact without leaving unsecured access on the environment, a protected interactive shell was deployed with a randomized authentication key. The shell included a self-destruct mechanism designed to physically remove the file from disk on demand a standard evidence-hygiene practice.

The 500-based path worked, but it depended on Telescope being accessible to discover the generated filename. The second stage of the investigation asked a different question: what if we could make the upload complete cleanly?

The root cause of the null extension was clear from the source code. When $file->guessExtension() calls into Symfony's MimeTypes component, the MIME type text/x-php has no registered default extension mapping. The function returns null. The MySQL constraint fires.

But finfo the underlying detection tool decides the MIME type based on file content, not filename. What happens if the content doesn't look like PHP?

Adding a short sequence of non-text binary bytes as a file header before the \<?php opening tag changes the MIME detection outcome. finfo reads the opening bytes as generic binary data and classifies the content as application/octet-stream. Symfony maps that MIME type to the extension bin. The value is no longer null. The database insert succeeds.

The extension recorded in the database was bin. The extension on the file on disk was .php. These are not the same thing.

This matters because of a critical detail in the storage logic:

// FileUploadTrait.php - filename construction

$name = Carbon::now()->timestamp . Str::random(4) . '-' . $file->getClientOriginalName();

The physical filename on disk is derived from the **client-controlled original filename** not from the server-derived extension. The server records ext: bin in the database. It stores the file as 1710005823efgh-test-bin.php on disk. Those two facts live in permanent disagreement.

The upload now returns HTTP 200 OK, with the file's full public URL inside the JSON response body:

```
{
  "success": true,
  "data": {
    "file": {
      "mime": "application/octet-stream",
      "ext": "bin",
      "url": "https://target.com/storage/uploads/file/1710005823efgh-test-bin.php"
    }
  }
}
```
No Telescope required. No error logs to parse. The server hands the attacker the path.

PHP-FPM, for its part, does not object to binary bytes before \<?php. PHP is inherently an inline template engine: anything outside an opening tag is treated as raw output and passed through untouched. The interpreter locates \<?php, begins execution from there, and never raises a parse error over the bytes that preceded it. The binary prefix is simply output before any PHP-generated content inconsequential for a shell payload designed to parse its own response.

When two components disagree about a file’s identity, the attacker looks for the gap between them.

The destroy endpoint in FileController.php follows a similarly incomplete pattern:

public function destroy(File $file): JsonResponse

{

$this->repository->remove($file);

return $this->respondWithSuccess(\_\_('messages.responses.deleted'));

}

// BaseRepository.php

public function remove(Model $model): bool

{

return $model->delete();

}

$model->delete() removes the database record. It does not call Storage::delete(). The physical file remains on disk at its original path, fully accessible and executable, after the record tracking it no longer exists in the application.

An uploaded executable that has been “deleted” through the application’s own interface is not gone. It is merely untracked.

The vulnerability chain here is not exotic. It is the predictable outcome of several common assumptions failing at the same time.

**A 500 response is not a guarantee of a clean state.** Any multi-step operation that touches an external resource a filesystem, a message queue, an email gateway before completing its own transaction can leave side effects behind when it fails. HTTP status codes describe application-layer outcomes. They say nothing about what persisted before the exception was raised.

**File extension and MIME type are not security boundaries.** They are hints. A MIME type derived from content can be changed by changing the content. An extension recorded in a database column can differ from the extension on the physical file. Neither is a reliable proxy for “this file will not execute.”

**Client-controlled filenames should not determine what executable paths look like.** When a server uses getClientOriginalName() to decide where a file lives on disk, the client controls the extension of the stored file. The server's own validation logic, running on derived metadata, operates on a different representation of the same upload.

**Upload and deletion are the same workflow, viewed in reverse.** If uploading a file creates a physical resource, deleting the associated record should destroy it. Treating them as independent operations produces orphaned files that persist beyond the application’s model of its own state.

**Database transactions do not automatically roll back filesystem operations.** Wrapping the database insert in a transaction would protect against partial database state, but it would not delete the file already written to disk. Filesystem side effects require explicit cleanup logic they exist outside the transaction boundary entirely.

**Nginx hardening of upload directories is a deployment concern, not a bonus.** A Laravel application that links public/storage to a web root will execute any PHP file that lands there, regardless of how it arrived. Restricting script execution in upload directories is not an advanced mitigation it is a baseline that application-layer controls alone cannot replace.

**1. Strict server-side file-type validation with a critical caveat** Add an explicit allowlist to the request validation:

// In StoreFileRequest.php

'file' => \['required', 'file', 'mimes:png,jpg,jpeg,webp,pdf,docx', 'max:51200'\],

Laravel’s mimes rule checks the MIME type derived from the file's **content** (via finfo), not its name. This means a file named shell.php with valid PNG magic bytes will pass mimes:png the client controls the name, but finfo decides the MIME. **MIME-based validation is necessary but not sufficient on its own.** It must be paired with server-generated storage names (see point 2) so the stored extension is always server-controlled, and with an Nginx execution block (see point 4) as a deployment-level backstop. No single control is adequate in isolation.

**2. Server-generated storage names using the validated extension** Never use getClientOriginalName() to build the stored filename. Use the server-validated extension:

$safeExt = in\_array($validatedExt, $allowedExtensions, true) ? $validatedExt : 'bin';

$name = Carbon::now()->timestamp . Str::random(8) . '.' . $safeExt;

This severs the client’s influence over what extension the stored file carries.

**3. Atomic upload operations with rollback on failure** Write to a temporary location first. Move the file to its permanent path only after the database record is confirmed:

```
try {
    $tempPath = $file->store('temp_uploads');
    $record = File::create([...]);
    Storage::move($tempPath, "uploads/file/{$name}");
} catch (\Exception $e) {
    if (isset($tempPath) && Storage::exists($tempPath)) {
        Storage::delete($tempPath);
    }
    throw $e;
}
```
**4. Block PHP execution in upload directories at the Nginx level** Even with correct application-layer controls, a defense-in-depth Nginx rule prevents uploaded files from ever being executed:

```
location ^~ /storage/ {
    location ~ \.(php|phtml|phar|php5|php7|php8|inc)$ {
        return 404;
    }
}
```
**5. Physical file deletion on record deletion** Update the destroy logic to remove the physical file when its database record is deleted:

```
Storage::disk('public')->delete($file->url);
$file->delete();
```
**6. Restrict Laravel Telescope in production** Telescope’s request and exception logs should not be accessible to unauthenticated users in production. Restrict the /telescope and /telescope-api paths via Nginx or gate access in TelescopeServiceProvider to the local environment. Leaving it open in production exposes internal SQL queries, stack traces, and generated storage paths all of which materially assisted this investigation.

**7. Regression tests** Add test cases covering: upload of a PHP file (expected: 422), upload of a binary-prefixed PHP file (expected: 422 or 422-equivalent), deletion followed by direct URL access to the physical file (expected: 404), and upload with a spoofed MIME type header.

The upload succeeded before it failed. The database rejected the record. The filesystem never got the memo.

Every component in this chain was doing exactly what it was told. The validator checked for required fields. The image decoder rejected non-images. The database enforced its constraints. But none of them were told to coordinate their cleanup responsibilities with the others.

Security failures often live not in individual components, but in the contracts between them in the assumptions about what “failure” means for each participant, and about who is responsible for putting things back the way they were.

Every component did exactly what it was told. None of them were told to clean up after each other.

*Research and documentation by*

*Khaled Ebrahem*
