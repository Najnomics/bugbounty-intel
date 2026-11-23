# Some XSS Situation

- **Source URL:** https://medium.com/@haticezkmnl/some-xss-situation-31fa64e113fe?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241003110513/https://medium.com/@haticezkmnl/some-xss-situation-31fa64e113fe
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7447 (id 7447)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Some XSS Situation 👾

## Steps to create a website with simple php codes + What is XSS + XSS injection attempts

**⚔️ My work summary for our Gallipoli community’s mission to create and exploit XSS vulnerabilities. 📝**

After completing the VPS installation process, here are a few configuration steps we need to do in order to use the [👉🏻HERE👈🏻](/@haticezkmnl/vps-virtual-private-server-f37ffab2f3f1) php file.

## ***PHP*-*FPM Installation***

sudo apt update

sudo apt install php-fpm

sudo nano /etc/nginx/sites-available/default


## It should be like:

```
server {
    listen 80;
    server_name your_domain_or_IP;
    root /var/www/html;
    index index.php index.html index.htm;
    location / {
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
    location ~ /\.ht {
        deny all;
    }
}
```
***for changes in our starting php file:***
sudo nano /var/www/html/info.php


Here I gave examples of 3 different vulnerability methods (GET, POST, HEADER) for 3 types of XSS.

Before preparing the vulnerability codes, let’s learn XSS in detail.

# WHAT IS XSS?

XSS is an exploit where the attacker attaches code onto a legitimate website that will execute when the victim loads the website.

XSS occurs when a web application converts user input into its own output without validation or coding.


## REFLECTED XSS

It arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.

## STORED XSS

This occurs when an application receives data from an untrusted source and insecurely inserts that data into subsequent HTTP responses. These are cases where the injected script is permanently stored on the target servers, for example in a database, a message forum, a visitor log, a comment area, etc.

## DOM-BASED XSS

In DOM XSS, an application processes user-provided data (from an untrusted source) directly in the browser, manipulating the Document Object Model (DOM) in an insecure way. This allows an attacker to inject malicious scripts or code that can be executed in the user’s browser.It arises when an application contains some client-side JavaScript that processes data from an untrusted source in an unsafe way, usually by writing the data back to the DOM.

The Document Object Model (**DOM**) is a programming interface that represents HTML and XML documents as a structured tree of objects. It allows developers to interact with the content and structure of web pages dynamically using languages like JavaScript.


## ***Reflected XSS → GET***

```
<body>
    <h1>Feedback Form</h1>
    <div class="feedback-box">
        <form method="get" action="">
            <label for="feedback">Leave your feedback:</label><br>
            <textarea id="feedback" name="feedback" placeholder="Enter your feedback here..."></textarea><br>
            <button type="submit">Submit Feedback</button>
        </form>
    </div>
    <?php
    // XSS vulnerability: Data coming from the user is printed directly to the screen.
    if (isset($_GET['feedback'])) {
        $feedback = $_GET['feedback'];
        echo "<div class='result'><p>Your feedback: " . $feedback . "</p></div>";  // Reflected XSS açığı
    }
    ?>
</body>
</html>
PAYLOAD ->> <script>alert('THERE IS A XSS')</script>
```
## Reflected XSS → POST

```
<body>
    <h1>Leave a Comment</h1>
    <div class="form-container">
        <form method="POST" action="">
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" placeholder="Enter your name">
            <label for="comment">Your Comment:</label>
            <textarea id="comment" name="comment" placeholder="Write your comment"></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>
    <?php
      if ($_SERVER['REQUEST_METHOD'] === 'POST') {
          $name = $_POST['name'];
          $comment = $_POST['comment'];
  
         // XSS vulnerability: Data coming from the user is printed directly to the screen.
          echo "<div class='result'>";
          echo "<p><strong>$name</strong> commented: </p>";
          echo "<p>$comment</p>";
          echo "</div>";
      }
    ?>
</body>
</html>
PAYLOAD ->> <script>alert('THERE IS A XSS')</script>
```
## Reflected XSS → HEADER

```
<body>
    <h1>Custom Header Example</h1>
    
    <?php
    if (isset($_SERVER['HTTP_CUSTOM_HEADER'])) {
        $customHeader = $_SERVER['HTTP_CUSTOM_HEADER'];
        echo "<p>You sent a custom header: " . $customHeader . "</p>";
    }
    ?>
</body>
</html>
PAYLOAD ->>  <script>alert('xss');</script>
In this example, the exploit was performed using burpsuite and replacing
the referer content in the request with the payload.
```
⇢ The HTTP\_REFERER header is checked on the server side to retrieve the URL the user came from and is placed directly in the HTML. However, if the data retrieved from the user (in this case, the referrer information) is not properly sanitized in such a process, it could allow a malicious user to inject and execute JavaScript code.


## Stored XSS → POST

```
<body>
    <h1>Leave a comment</h1>
    <!-- Comment Form -->
    <form action="stored_post.php" method="POST">
        <label for="comment">Your Comment:</label>
        <textarea id="comment" name="comment"></textarea>
        <input type="submit" value="Submit">
    </form>
    <?php
    // File to store comments
    $file = 'comments.txt';
    // Check if a comment is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST['comment'])) {
        $comment = $_POST['comment'];
        // Save comment to the file
        file_put_contents($file, $comment . PHP_EOL, FILE_APPEND);
        echo "<p>Comment saved!</p>";
    }
    // Display stored comments
    if (file_exists($file)) {
        echo "<h2>Comments:</h2>";
        $comments = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        foreach ($comments as $comment) {
            // Display the comment directly (XSS vulnerability here if unsanitized)
            echo "<p>" . $comment . "</p>";
        }
    }
    ?>
</body>
</html>
```
**Form Submission**: This file has a form where users can submit their comments.

**Storing the Comment**: When the form is submitted, the comment is written to a text file (`comments.txt`).

**Displaying Comments**: All comments are read from the file and displayed on the page. Since the comments are displayed directly without any sanitization, any script injected into the comment will be executed.


## Stored XSS → GET

```
<body>
    <h1>Update your bio</h1>
    <!-- Form to update bio -->
    <form action="stored_get.php" method="GET">
        <label for="bio">Update your bio:</label>
        <textarea id="bio" name="bio"></textarea>
        <input type="submit" value="Update">
    </form>
    <?php
    // Check if a bio is submitted via GET
    if (isset($_GET['bio'])) {
        $bio = $_GET['bio'];
        // Save the bio to a file (could be database)
        file_put_contents('bio.txt', $bio . PHP_EOL);
        // Display the bio directly (vulnerable to XSS)
        echo "<div class='bio'><h2>Your Bio:</h2><p>" . $bio . "</p></div>";
    }
    ?>
</body>
</html>
```
**Form Submission**: The form uses the **GET** method to submit the bio.

**GET Request Handling**: When the form is submitted, the `$_GET['bio']` value is retrieved and saved to a file called `bio.txt`.

**Bio Display**: The bio is displayed directly on the page without sanitization, which leaves it vulnerable to XSS attacks if malicious content is entered.

**XSS Payload**: `<script>alert('XSS');</script>`


## Stored XSS → HEADER

```
<body>
    <h1>Leave a Review</h1>
    <!-- Review Form -->
    <form action="stored_header.php" method="POST">
        <label for="review">Leave a review:</label>
        <textarea id="review" name="review"></textarea>
        <input type="submit" value="Submit">
    </form>
    <?php
    // Check if the review is submitted via POST form
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['review'])) {
        $review = $_POST['review'];
        // Store the review in a file (vulnerable to XSS)
        file_put_contents('reviews.txt', $review . PHP_EOL, FILE_APPEND);
        echo "<p>Review submitted!</p>";
    }
    // Capture the review from a custom header ('X-Review')
    if (isset($_SERVER['HTTP_X_REVIEW'])) {
        $headerReview = $_SERVER['HTTP_X_REVIEW'];
        // Store the header review in a file
        file_put_contents('reviews.txt', $headerReview . PHP_EOL, FILE_APPEND);
        echo "<p>Review submitted via header!</p>";
    }
    // Display stored reviews
    if (file_exists('reviews.txt')) {
        echo "<div class='reviews'><h2>Stored Reviews:</h2>";
        $reviews = file('reviews.txt', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        foreach ($reviews as $storedReview) {
            // Display the reviews directly (unsanitized, XSS vulnerability here)
            echo "<p>" . $storedReview . "</p>";
        }
        echo "</div>";
    }
    ?>
</body>
</html>
```
**Form Submission**: Users can submit reviews via the form, and the review is stored in `reviews.txt`.

**Header Injection**: If a custom HTTP header (`X-Review`) is present in the request, its content is also stored as a review in `reviews.txt`.

**XSS Injection**: An attacker can inject a payload such as `<script>alert('XSS');</script>` either through the form or by setting a custom HTTP header using tools like **Burp Suite** or **cURL**.

**Display Reviews**: When the page is loaded, all stored reviews are displayed without sanitization, making it vulnerable to XSS.


## DOM-Based XSS → GET

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM XSS Using GET</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000; /* Black background */
            color: #E0E0E0; /* Soft gray text */
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #B2DFDB; /* Soft teal heading */
        }
    </style>
</head>
<body>
    <h1>DOM XSS Using GET Method</h1>
    <p id="output"></p>
    <script>
        var query = document.location.search;
        document.getElementById("output").innerHTML = "You searched for: " + query;
    </script>
</body>
</html>
```
***PAYLOAD***: http://your-server/path/to/dom\_get.php?search**\<script>alert('XSS');\</script>**


**→** The JavaScript on the page retrieves this input from `document.location.search` and directly adds it to the DOM, leading to script execution.

## DOM-Based XSS → POST

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOM XSS Using POST</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000; /* Black background */
            color: #E0E0E0; /* Soft gray text */
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #B2DFDB; /* Soft teal heading */
        }
        textarea {
            width: 300px;
            height: 100px;
            background-color: #444; /* Darker area for input */
            color: #E0E0E0; /* Soft gray text */
            border: 1px solid #B2DFDB; /* Soft teal border */
            border-radius: 5px;
            padding: 5px;
        }
    </style>
</head>
<body>
    <h1>DOM XSS Using POST Method</h1>
    <form action="" method="POST">
        <label for="comment">Leave a comment:</label><br>
        <textarea id="comment" name="comment"></textarea><br>
        <input type="submit" value="Submit">
    </form>
    <div id="display"></div>
    <?php
    // Check for POST submission
    if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['comment'])) {
        $comment = $_POST['comment'];
        // Display the comment directly (XSS vulnerability)
        echo "<script>document.getElementById('display').innerHTML = 'User input: " . $comment . "';</script>";
    }
    ?>
</body>
</html>
```
***PAYLOAD***: *\<script>alert('XSS');\</script>*

## DOM-Based XSS → HEADER

*Here are the main reasons why headers are not typically used for injection in DOM XSS attacks:*

→ **Nature of DOM XSS:**

Client-Side Execution: DOM XSS relies on manipulating the DOM using JavaScript running in the user’s browser. The attack focuses on how the web page processes and displays data from sources like URLs or user input fields, not the server response headers.

→ **Headers Are Server-Side:**

Different Context: HTTP headers are part of the server’s response and are not directly accessible by client-side JavaScript. While you can read certain headers using JavaScript (like document.referrer or AJAX), headers generally do not serve as the primary entry vector for DOM XSS.

**→ Input Vectors:**

Common Vectors: Common sources for DOM XSS include URL parameters (query strings), fragments (hashes), or form inputs. These are simpler for a user to manipulate and directly affect the DOM without involving server-side operations.

**→Script Context:**

JavaScript Execution: JavaScript executed in the DOM context can easily manipulate elements based on user input or URL parameters. Injecting malicious payloads via headers does not trigger the same DOM manipulation because the execution context (browser environment) is not directly affected by headers.

In summary, DOM XSS attacks focus on exploiting how a web application processes and displays data in the browser, specifically via user input and URL parameters, rather than HTTP headers, which are server-side constructs that are not directly manipulated by client-side scripts.

THANK YOU FOR READING

⚔️⚔️ **If you want to try** ⚔️⚔️ **http://52.54.217.140/info.php** ⚔️⚔️


⚔️⚔️ FOR CODE CLICK [HERE](https://github.com/Zehrakmnl/xssInjections-1)
