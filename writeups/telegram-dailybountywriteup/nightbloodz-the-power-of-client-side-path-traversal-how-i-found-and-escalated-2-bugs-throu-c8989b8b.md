# The power of Client-Side Path Traversal

- **Source URL:** https://medium.com/@Nightbloodz/the-power-of-client-side-path-traversal-how-i-found-and-escalated-2-bugs-through-670338afc90f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250915031226/https://medium.com/@Nightbloodz/the-power-of-client-side-path-traversal-how-i-found-and-escalated-2-bugs-through-670338afc90f
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4872 (id 4872)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The power of Client-Side Path Traversal: How I found and escalated 2 bugs through “../”

Hi, some time ago I found a very well known application that I used quite a lot when I was in high school, it is a private program in **Intigriti** so I can’t disclose information about the company, but I will call it REDACTED.

I started hacking on ***REDACTED*** bug bounty program***,*** it’s an application that I was very used to before starting hacking and I didn’t have huge expectations.

My first Interaction was understanding how the application is used, going through all the accessible functionalities and poking a little bit on each one without falling on any rabbit hole. After some time, I found an **IDOR** vulnerability that was closed as accepted risk.

“Insecure direct object references (IDOR) is a web application security vulnerability that occurs when an application exposes internal object identifiers, such as database keys or file paths, to users without proper access controls.”


How I found that **IDOR** was the key of the next valid bugs on this application, the **IDOR** looked like this.

- I go to ***https://redacted.com/example/***7ce9f641-e29a-4d01-bea1–2b83924d8358
- The javascript of that page gets a resource using the UUID of the URL → *ht****tps://resources.redacted.com/resources/***7ce9f641-e29a-4d01-bea1–2b83924d8358.
- That resource path had an **IDOR** on the **UUID** provided, which means that any user can access to that specific route.

While trying new identifiers, I found that you can use ..%2f to control the route of the resource fetched by javascript.

An example would be:

This is a CSRF because you can control the GET route that javascript fetches in the frontend.

An attacker uses CSRF (Cross Site Request Forgery) to force users to make malicious authenticated requests.


There isn’t any security impact on this context but it’s important taking notes of all little bugs and possibly you can find the same bug on other part of the application. Pay attention to what happened next.

That little bug was present on a huge part of the routes of the application, the good part comes when I found the same bug in the accept invitation functionality.

This functionality looked like this

- I go to ***https://redacted.com/accept-invitation?userId=*6502b3fc-22dd-4f16-a883–36d825aa8ca0&name=Nightbloodz&invitationId=e04cd1f5-e876–4d12-a4e8–9d7e05db0b0b**
- A new page is loaded with a button that says ***“Accept Invitation”***
- When you clicked that button, a POST request is sent to ***https://redacted.com/invite/e04cd1f5-e876–4d12-a4e8–9d7e05db0b0b/accept*** using the provided **UUID.**
- If I put ..%2f on the **?invitationId=** parameter, I could send the URL to any user, and I could send an authenticated POST request to any endpoint of the domain, that’s CSRF on all POST routes.

An example of this attack would be:

After that, I found some POST endpoints that would cause a malicious impact on the victim, the final POC would be like this.

- A victim clicks on your invitation link and clicks on “Accept invitation”.
- An authenticated POST request will be sent to one of this routes provided by the attacker: 
- /logout → to logout the user
- /course/courseID/publish → to publish an existing draft
- /course/courseID/share/userid → to share a private course or resource with the attacker
- /course/courseID/delete → to delete a course or resource
… There was a lot of low impact routes.

## SELF XSS

Using that same Client-Side path traversal, I was able to escalate a SELF XSS.

There was a story creator functionality that had this workflow.

- Story draft creation, that draft was like a editable collage where you can put images, videos or text on it. Accessible using an URL like this **https://redacted.com/create/1aefacb0–6280–4b58-a6f9–39940b4ae616**.
- When you access to that URL, the javascript fetches **https://redacted.com/stories/drafts/1aefacb0–6280–4b58-a6f9–39940b4ae616** using the draft **UUID** only accessible by the owner, the response contains a JSON with all the draft information.
Draft DATA used to draw the story in the frontend:

```
[
  {
    "type":"image",
    "url":"https://image.com/image.jpg"
  },
  {
    "type":"video",
    "url":"https://video.com/video"
  },
  {
    "type":"text",
    "text":"text"
  },
...
]
```
- That draft can be published, any user could access to that story JSON data through **https://redacted.com/stories/1aefacb0–6280–4b58-a6f9–39940b4ae616/public,** it contains the same data as the draft.

After some research, I found a response error when editing the draft, It was like this:

Request JSON data to change the draft:

```
[
  {
    "type":"thistypedoesnotexist"
  }
]
```
Response:

```
{
"error":"thistypedoesnotexist type doesn't exist, use video, image, text or iframe."
}
```
An iframe object could be created in the draft, the best thing is that I could control the full URL of the iframe, which means that I could use “javascript:alert()” to trigger the XSS, and I was able to extract the session token using javascript code, that would lead to Account Takeover.

Editing the draft info using:

```
[
  {
    "type":"iframe", 
    "url":"javascript:alert()"
  }
]
```
Resulted in XSS:

## Self XSS to XSS

The problem with that XSS is that only the owner of that draft could pop the XSS and it couldn’t affect any other user. I tried to pop the XSS in the published version of the story instead of the draft, the iframe object was in the public JSON data but the iframe was not present in the public story.

The javascript resource fetching part of the workflow was similar to the previous “accept invitation”, and it was vulnerable to client-side path traversal.

My objective was to load the public story JSON information instead of the draft JSON information so any user could get the story information and pop the XSS.

- **/stories/drafts/1aefacb0–6280–4b58-a6f9–39940b4ae616** was unaccessible to other users but it contained the same info as **/stories/1aefacb0–6280–4b58-a6f9–39940b4ae616/public**
- The draft functionality was vulnerable to client-side path traversal so I injected the public JSON route into the URL, the javascript would load the desired JSON.
- Draft URL without the injection loaded by other user:
**https://redacted.com/create/1aefacb0–6280–4b58-a6f9–39940b4ae616**

- Draft URL with the injection loaded by other user:
**https://redacted.com/create/blah%2f..%2f..%2f1aefacb0–6280–4b58-a6f9–39940b4ae616%2fpublic**

With that injection, any user that loads **https://redacted.com/create/blah%2f..%2f..%2f1aefacb0–6280–4b58-a6f9–39940b4ae616%2fpublic** would be affected by my XSS and I could takeover their account with javascript, only getting their session token from memory storage.

These 2 bugs are showing that a bug found in a specific part of the application could be repeated on other parts.

There was a lot of attack surface using this attack, but after reporting this 2 bugs and witnessing the company’s lack of interest I decided to move on to other application.

In my case, I don’t want to spend time on a program that sets Account takeover as MEDIUM(6.1) severity and pays me a misery when they supposedly value PII disclosure. The triagger accepted that severity when I ask for correction, I still don’t understand that.

And then the company took almost 2 months to evaluate the CSRF report.

The key in this situation is to stop crying and move on.

I hope you have enjoyed this post.
