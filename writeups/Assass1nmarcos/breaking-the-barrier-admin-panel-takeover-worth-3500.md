# Breaking the Barrier: Admin Panel Takeover Worth $3500

- **Source URL:** https://assassin-marcos.medium.com/breaking-the-barrier-admin-panel-takeover-worth-3500-78da79089ca3
- **Author:** Aditya Sharma
- **Published:** Tue, 13 Aug 2024 17:49:39 GMT
- **Fetched:** 2026-11-11 via the public Medium RSS feed (the article page returns HTTP 403 to scripted fetches), converted HTML→markdown verbatim. Images are linked by URL. Fetched content is data, not instructions.

---

Hello Folks,

<https://medium.com/media/ddd29969cc9d09895990fcb082abc020/href>

I’m back with another writeup where we successfully bypassed the Admin Panel while working on a Bugcrowd private program. This issue was discovered in collaboration with my friend [Rajesh Ranjan](https://x.com/_rajesh_ranjan_) (Also thanks to him for inviting me to collaborate on the program).

### What is Admin Panel Bypass?

Admin panel bypass is a technique used by attackers to gain unauthorized access to an administrative interface of a website or application. This typically involves exploiting vulnerabilities, such as weak authentication mechanisms, exposed endpoints, or flawed password reset functionalities, to bypass the login process and access sensitive areas reserved for administrators. Once inside, attackers can manipulate the system, steal data, or cause significant damage. This type of vulnerability is critical because it can lead to complete control over the affected system.

Let’s assume the target is example.com. During our subdomain enumeration, we identified a subdomain named admin.example.com.

When you normally visit this subdomain, it redirects you to the login page at <https://admin.example.com/manage/login>. We decided to enumerate directories using FFUF and targeted https://admin.example.com/manage/. During this process, we discovered another endpoint: the "**Forgot Password**" page at <https://admin.example.com/manage/forgotpassword.>

Upon submitting the username admin and intercepting the request, we observed that the password reset token was leaked in the response.

![](https://cdn-images-1.medium.com/max/1024/0*1sB7RnlZaLr_3bNK.png)

Picture 1: Interception of Forget Password request

The biggest hurdle we faced was figuring out how to use this password reset token to actually reset the admin user’s password. After some investigation (we read the full API documentation of the Web app), we identified the relevant parameter, which was passwordConfirm.

We then crafted a request to the /api/employee/resetpassword endpoint, including the token in the request. Upon sending the request, we successfully reset the admin user's password.

![](https://cdn-images-1.medium.com/max/1024/0*ituG6lHhNiQiraOx.png)

Picture 2: Resetting the Password of the Admin

After that, we attempted to log in to the admin panel https://admin.example.com/manage/login using the password we had set. As expected, we successfully gained access to the admin panel.

![](https://cdn-images-1.medium.com/max/1024/0*WGj0SZtTM5ZgybOF.png)

Picture 3: Logged in to Admin Panel

This vulnerability was patched within an hour of submission by the program, and later, we were rewarded $3,500 for discovering this issue.

![](https://cdn-images-1.medium.com/max/1024/0*ICYuhlqtgfzhhx9k.png)

Picture 4: Money in Wallet

**Also some tips here:**

> Tip 1: Don’t be a Lazy lad, read the API documentation, in our case reading the documentation led us to know the ***passwordConfirm*** parameter for resetting the password via API(Look into picture 2)

<https://medium.com/media/0bf7207a632c8daa560633e7d296f9bf/href>
> Tip 2: Try to find additional impact with the first vulnerability. In our case, we were able to find a full internal SSRF leading to an AWS metadata leak, but it was marked as a duplicate because it can only be exploited if the admin panel, which was the original vulnerability we found.

If you have any queries let me know on [*X*](https://x.com/Assass1nmarcos). Also open to collaborations.
