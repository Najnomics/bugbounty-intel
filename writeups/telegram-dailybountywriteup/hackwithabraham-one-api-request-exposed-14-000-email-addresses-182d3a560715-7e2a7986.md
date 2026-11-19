# One API Request Exposed 14,000+ Email Addresses

- **Source URL:** https://medium.com/@hackwithabraham/one-api-request-exposed-14-000-email-addresses-182d3a560715
- **Fetched from:** https://medium.com/feed/@hackwithabraham
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14989 (id 14989)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### One API Request Exposed 14,000+ Email Addresses

*What initially looked like a small information disclosure turned into something much bigger. The interesting part wasn’t just finding the bug, but figuring out how easily anyone could exploit it.*

While testing an online internship and training platform, I came across a feature that allowed enrolled users to interact through course discussions.

As usual, I started inspecting the background API requests using Burp Suite.

One request caught my attention. It was responsible for loading discussion-related information.

I sent it to Repeater and started examining the JSON response.

### The first clue

The request looked like this:

**Request**

POST /api/v1/discussions/loadStreams.do HTTP/1.1

Host: \[REDACTED\]

Cookie: \[REDACTED SESSION COOKIES\]

Nothing particularly unusual about the request itself.

But the response was a different story.

**Response (sanitized excerpt)**

```
{
  "usersInfo": [
    {
      "name": "[REDACTED]",
      "id": "[REDACTED]",
      "type": "C",
      "hasCustomImage": "false",
      "imageUrl": "[REDACTED]",
      "email": "[REDACTED]"
    },
    {
      "name": "[REDACTED]",
      "id": "[REDACTED]",
      "type": "CL",
      "hasCustomImage": "false",
      "imageUrl": "[REDACTED]",
      "email": "[REDACTED]"
    }
  ]
}
```
The usersInfo array contained full email addresses and internal numeric user IDs..

Initially, I assumed this information belonged only to people who had participated in discussions.

But I wanted to verify that assumption.

### The first assumption was wrong

After examining the response more closely, I realised the exposure wasn’t limited to people who had posted comments.

The API was returning information about users enrolled in the course, even if they had never interacted with the discussion feature.

And it didn’t stop at learners.

Email addresses and internal IDs belonging to trainers and administrators were also exposed.

No comments. No interaction. Just the API request.

### Finding a way to exploit it at scale

Finding exposed information is one thing. Demonstrating how an attacker could realistically access it is another.

I started looking at the registration and enrollment process.

Account registration didn’t require email verification. That immediately made me question whether an attacker even needed an existing relationship with the platform.

I explored the available courses and found something interesting: freely accessible courses that anyone could enroll in after creating an account.

That was the missing piece.

I could simply:

1. Register a fresh account using an unverified email address.
2. Find a freely accessible course.
3. Enroll in the course.
4. Open its discussion section.
5. Inspect the corresponding API response in Burp Suite.

The interesting part was that users didn’t need to participate in discussions for their information to appear.

I repeated the investigation across freely accessible courses to understand the overall exposure.

**The total came to more than 14,000 unique email addresses.**

The exposed information included learners, trainers, and administrators.

What started as a seemingly ordinary information disclosure had turned into a large-scale personal data exposure.

### Why does this matter?

An attacker could potentially use this information for:

- **Targeted phishing:** Build lists of actual platform users and send convincing emails.
- **Social engineering:** Identify trainers and administrators for targeted attacks.
- **Email harvesting:** Collect thousands of addresses for spam campaigns.
- **Further enumeration:** Use exposed internal IDs while investigating other endpoints for potential access-control weaknesses.

The users had no reason to expect their personal email addresses to be accessible to other course participants.

### Reporting the vulnerability

I submitted the finding through the platform’s responsible disclosure program.

As I investigated further, I provided additional updates explaining that:

- User interaction was completely unnecessary.
- Trainers and administrators were affected too.
- Freely accessible courses made exploitation possible for practically anyone.
- The overall exposure exceeded 14,000 unique email addresses.

I also attached a proof-of-concept video demonstrating the exploitation process, starting with a fresh account.

### Report Timeline

- **May 2026:** Vulnerability reported.
- **Within a week:** Vulnerability fixed by the platform.
- **July 2026:** Reward received.

### A small lesson from this finding

One thing I enjoy about bug bounty hunting is that the initial vulnerability is not always the complete story.

Sometimes, the real work starts after discovering the bug.

Instead of stopping at an exposed email address, I questioned how an external attacker could reach the data, explored the platform’s registration and enrollment flow, and found a practical way to demonstrate the actual scale.

**Don’t just find what is exposed. Understand how an attacker can reach it, how far the exposure goes, and what the real-world consequences could be.**

Sometimes, the most interesting part of a vulnerability isn’t the API request itself.

It’s what happens when you start asking the right questions.

If you enjoyed this write-up, please consider leaving a like and sharing your thoughts.

For more security research and bug bounty write-ups, you can connect with me:
