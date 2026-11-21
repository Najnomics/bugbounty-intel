# Account Takeover via Cookie Attribute Manipulation — A Unique Method

- **Source URL:** https://medium.com/@pauldipesh29/account-takeover-via-cookie-attribute-manipulation-a-unique-method-ea66a78cdb06?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250201051653/https://medium.com/@pauldipesh29/account-takeover-via-cookie-attribute-manipulation-a-unique-method-ea66a78cdb06
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8647 (id 8647)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover via Cookie Attribute Manipulation — A Unique Method

*📌about-me‼️*


Hello guys, I am Dipesh Paul (aka thegenetic), a dedicated cybersecurity professional and part-time bug hunter🫠. With expertise in uncovering vulnerabilities like injections, sensitive information disclosures, and broken access controls, I’ve helped multiple organization secure there online assets by reporting multiple vulnerabilities till date.🥷

I came across this vulnerability during a pentesting engagement while performing grey-box testing for a client. It was an incredible moment — stumbling upon something so unique that it stood out even among seasoned professionals🎯. The find was rewarding enough on its own, but earning recognition at Deloitte for discovering such a distinctive flaw made it all the more special✨. It’s moments like these that reaffirm why I love what I do😊.

Now let’s roll into the bug…

*The Hack 🥷*

During the engagement, I had access to two accounts with the same privilege levels. Let’s assume the user IDs for these accounts are `testA` (attacker) and `testB` (victim). While logged in as `testA`, I began examining various functionalities to see if the session was being properly managed.

While doing so, a cookie named `user_info` caught my attention. Its value appeared to be URL-encoded. Using Burp Suite’s decoder, I decoded the value and discovered it contained all the Personally Identifiable Information (PII) of the user associated with the account. This included the `user_id`, email, name, and other sensitive details.

Note: All cookies used here are sample cookies and not the actual ones, ensuring the privacy and security of clients.


Here is the cookie format :

`user_info = %7B%22sub%22%3A%22123abc456-1234-1234-ac12-789abc012%22%2C%22email_verified%22%3Atrue%2C%22name%22%3A%22John%20Doe%22%2C%22preffered_username%22%3A%22testA%22%2C%22given_name%22%3A%22John%22%2C%22family_name%22%3A%22Doe%22%2C%22email%22%3A%22johndoe%40example.com%22%7D`
After decoding, it revealed:

```
{
  "sub":"123abc456-1234-1234-ac12-789abc012",
  "email_verified":true,
  "name":"John Doe",
  "preffered_username":"testA",
  "given_name":"John",
  "family_name":"Doe",
  "email":"johndoe@example.com"
}
```
🔍Upon experimenting with the value of this cookie, I discovered that the login session could be manipulated using the `user_info` cookie. Interestingly, while the application also used an access token, it wasn’t bound to the session or other cookies, which allowed for this exploitation.

Initially, I tried altering the `prefferred_username` and `email` fields to random gibberish. This resulted in an error indicating that the user did not exist. Then, I modified the values to match those of the victim’s account (`testB`). Here's how the manipulated cookie looked

```
{
  "sub":"123abc456-1234-1234-ac12-789abc012",
  "email_verified":true,
  "name":"John Doe",
  "preffered_username":"testB",
  "given_name":"John",
  "family_name":"Doe",
  "email":"victimaccount@example.com"
}
```
I then encoded the modified cookie back to its original format and replaced the existing cookie in the browser. After refreshing the page — *voilà!* 🎉 I gained access to the victim’s account. From there, I was able to navigate the site and access all functionalities as if I were the victim. 🕵️♂️💻

There was also a `user-id` in the request header that confirmed the identity of the logged-in user. 🔑 In the attacker’s case, its value was `testA`. However, after successfully taking over the victim’s account, the value changed to `testB`, allowing me full access to all the details and functionalities of the victim’s user account. 🎯💻

*Mitigation🦺*

To address this vulnerability, the following measures are recommended:

1. **Proper Session Handling:** Implement session expiration and re-authentication mechanisms to reduce the risk of session hijacking⏳
2. **Input Validation and Integrity:** Avoid storing sensitive data in cookies and Ensure proper encryption and implement integrity checks for cookie values to prevent tampering. 🔐✅
3. **Use Token-Based Authentication:** Adopt secure, token-based authentication methods (e.g., JWT or OAuth) to manage user sessions effectively. 💾🔑
4. **Monitor for Suspicious Activity:** Implement robust logging and monitoring systems to detect unusual access patterns and potential account takeover attempts. 📊🚨

In conclusion, this vulnerability highlights the importance of robust session management and secure handling of sensitive user data. By implementing the recommended measures, such issues can be effectively mitigated, ensuring a safer environment for users.

That’s all for now, but this is just the beginning of many more exciting discoveries! Until next time, stay curious and keep learning. 😊🔍

Connect with me on [LinkedIn](https://www.linkedin.com/in/the-genetic/) and also on [Twitter](https://x.com/DipeshPaul19)

*Thank you for reading! If my content has helped you in any way, consider buying me a coffee to show your support* [***here***](https://buymeacoffee.com/thegenetic)!
