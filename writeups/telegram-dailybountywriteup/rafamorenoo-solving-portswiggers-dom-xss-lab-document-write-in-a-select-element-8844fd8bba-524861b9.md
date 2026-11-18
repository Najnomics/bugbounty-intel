# Solving PortSwigger’s DOM XSS Lab

- **Source URL:** https://medium.com/@rafamorenoo/solving-portswiggers-dom-xss-lab-document-write-in-a-select-element-8844fd8bba89?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@rafamorenoo
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9811)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
In this write-up, I’ll explain how to solve the Burp Suite lab as part of my preparation for the Burp Suite Certified Practitioner.

### Step 1: Inspect the target element

Scroll down to the element in question.

We can observe the name of the element involved in the vulnerability.

Podemos ver el nombre del elemento

### Step 2: Analyze the URL

This is the URL when accessing the product page:

Now, we add the storeId parameter and assign it a value:

### Step 3: Analyze the URL

The value has been successfully added!

If we inspect the HTML, we can see that our value appears inside a \<select> element as an \<option>.

### Step 4: Find a valid XSS payload

The next step is to find a suitable payload for this context.

There are several possible options — in my case, I used AI to help me generate a working XSS payload.

Payload used:

\</option>\<script>alert(1)\</script>

Pum!
