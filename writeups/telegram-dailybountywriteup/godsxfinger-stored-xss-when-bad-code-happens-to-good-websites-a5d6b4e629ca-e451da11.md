# Stored XSS

- **Source URL:** https://medium.com/@godsxfinger/stored-xss-when-bad-code-happens-to-good-websites-a5d6b4e629ca?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@godsxfinger
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6854)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Today, we’re tackling one of the nastiest: Stored Cross-Site Scripting (XSS). This little bugger doesn’t just crash the party it moves in, trashes the place, and makes sure everyone gets a nasty surprise when they least expect it.

#### What the Hell is Stored XSS?

Stored XSS is like a bad houseguest that never leaves. It’s when an attacker injects a malicious script into a target server, and that script gets stored somewhere (a database, message forum, visitor log, you name it). The script sits there, waiting for an unsuspecting user to stumble upon it. Unlike Reflected XSS, which needs a crafted link to spread its chaos, Stored XSS is like a landmine any user who visits the booby-trapped page triggers the payload. No fancy link-clicking required.

### How Stored XSS Works

1. **Injection**: The attacker finds a vulnerable input field on a website and injects their malicious script. This could be a comment box, a profile bio, whatever.
2. **Storage**: The server, none the wiser, stores the malicious script in its database.
3. **Retrieval**: When a user requests the page with the infected content, the server dutifully retrieves the data and sends it to the user’s browser.
4. **Execution**: The user’s browser processes the content and, surprise, executes the malicious script.
5. **Impact**: The script can do pretty much anything the user can: steal cookies, redirect them, deface the page — basically, it’s a digital free-for-all.

### Example Scenario: The Comment Section from Hell

Imagine a web application with a comment feature. Users submit comments, which get stored in a database and displayed on the page without any sanitization. Here’s what that mess looks like:

#### Vulnerable Code (Server-Side)

Storing Comment:

// Assume $\_POST\['comment'\] is user input from a form submission

$comment = $\_POST\['comment'\];

// Store the comment in the database without sanitization

mysqli\_query($conn, "INSERT INTO comments (comment) VALUES ('$comment')");

Displaying Comment:

\<html>

\<head>\<title>Comments\</title>\</head>

\<body>

\<h1>User Comments\</h1>

\<?php

$result = mysqli\_query($conn, "SELECT comment FROM comments");

while ($row = mysqli\_fetch\_assoc($result)) {

echo "\<p>" . $row\['comment'\] . "\</p>";

}

?>

\</body>

\</html>

#### Malicious Input

An attacker, with mischief in their heart, submits a comment with a script:

`<script>alert('XSS');</script>`
#### Stored and Executed

Every time a user views the comments page, the stored script executes:

\<html>

\<head>\<title>Comments\</title>\</head>

\<body>

\<h1>User Comments\</h1>

\<p>\<script>alert('XSS');\</script>\</p>

\</body>

\</html>

The unsuspecting user’s browser runs the script, and boom — there’s an alert box screaming ‘XSS’. It’s not just annoying; it’s dangerous.

### Conclusion: The Art of Not Screwing Up

Stored XSS is a nasty piece of work. It’s not just a security hole; it’s a chasm. It can lead to all sorts of havoc: stolen sessions, defaced content, hijacked accounts. So, if you’re running a web application, do yourself a favor: validate and escape user input like your digital life depends on it — because it does.

And if you’re just here for the chaos? Well, enjoy the show. Just remember, with great power comes great responsibility or at least, a really good story.
