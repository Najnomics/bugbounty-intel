# BAC (Authorization Bypass Allows Former Owner to Add Teachers After Role Downgrade)

- **Source URL:** https://medium.com/@HBlackGhost/bac-authorization-bypass-allows-former-owner-to-add-teachers-after-role-downgrade-d346fc051fca?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905210518/https://medium.com/@HBlackGhost/bac-authorization-bypass-allows-former-owner-to-add-teachers-after-role-downgrade-d346fc051fca
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10200 (id 10200)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# BAC (Authorization Bypass Allows Former Owner to Add Teachers After Role Downgrade)

بسم الله الرحمن الرحيم , اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كما صليت على إبراهيم، وعلى آل إبراهيم، إنك حميد مجيد، اللَّهُمَّ بَارِكْ عَلَى مُحَمَّدٍ وَعَلَى آلِ مُحَمَّدٍ، كما باركت على إبراهيم وعلى آل إبراهيم، إنك حميد مجيد , اللهم لك الحمد كما ينبغي لجلال وجهك وعظيم سلطانك االلهم لك الحمد حمداً كثيراً طيباً مباركاً فيه

Let’s start our scenario today. This is a useful scenario that teaches us how to dive into requests and check the functionality, even when it does not appear in the UI.

This target is a teaching platform that can be used to create virtual schools and classes. After spending some time exploring and understanding the program, I was able to extract this information about the target and how it works

```
   
    
    
    3.Parent
    4.Student
```
**The types of accounts available on this website are:****1.School Leader / Admin****2.Teacher**
After exploring the website, I found the following:

- A **School Leader** can create a school , Class and invite teachers to join The Class .
- A **School Leader** can assign any **Teacher** as the **Owner** of a class but teacher can’t do this .
- Teacher can Accept The invite and have access on this Class

let’s start to hack this website :

I created **Account A** as a **School Leader**, then created a **school** and a **class**.

After that, I created **Account B** as a **Teacher**, and accepted the invitation to join **Account A’s** class.

During this process, I discovered that adding other teachers is **restricted** for the Teacher role — only the **School Leader** has permission to add teachers

You can’t add or remove other teachers ????? . Okay this is my **favorite message** to try and break your function, baby☠️❤️!

Let’s try to break this function:

I returned to **Account A** and set myself as the **owner**. I tried to **add and remove a co-teacher**, and I **intercepted the requests** using Burp Suite then send to Repeater .

from **Account B**, I transferred the ownership **back to Account A**.

Now, I’m teacher and haven’t access to delete or add Co- Teacher , when I try to **remove any teacher** by resend the requestI had saved in Repeater

**OMG, “403 Forbidden”!**

No problem — let’s test the function.

After I become a teacher (not an owner), I’ll go to Repeater and try sending the request again.

**BOOOOOM! 200 OK** — that’s what we like to see! 💥✅

The invitation is sent to the email I specified in the request, even though I’m only a **teacher**, and this functionality **is not available in the UI** for my role.

وابلللللللع يا نجم!! 💥🔥

والسلام عليكم ورحمه الله وبركاته
