# I Asked Them To delete The Account ------ They Told Me Yes

- **Source URL:** https://medium.com/@Yahia_Ramadan/i-asked-them-to-delete-the-account-they-told-me-yes-f4d87001a7c1
- **Fetched from:** https://medium.com/@Yahia_Ramadan/i-asked-them-to-delete-the-account-they-told-me-yes-f4d87001a7c1?source=rss-a1fe31dce74a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14893 (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Yahia Ibrahim khamis / Tue, 01 Sep 2026 20:48:14 GMT

قال الله تعالي: ﴿ قُلْ مَنْ يَرْزُقُكُمْ مِنَ السَّمَاوَاتِ وَالْأَرْضِ قُلِ اللَّهُ وَإِنَّا أَوْ إِيَّاكُمْ لَعَلَى هُدًى أَوْ فِي ضَلَالٍ مُبِينٍ ﴾ \[سبأ: 24\].

Hello Guys long time no see .

Today I will talk about my **first Critical report on HackerOne**. 🎉

Before we start, let’s call our target example.com.

example.com is an e-commerce website that sells 3D-printing models. It also hosts another domain called example2.com, which is used if you want to become a merchant and sell 3D-printing models.

If you create an account on example.com, an account using the same email address is also created on example2.com. You can then access your account on example2.com if you are authenticated on example.com.

Okay, now let’s get into the interesting part.

On example.com and example2.com , you cannot directly delete your account. Instead, you have to contact the AI chatbot, which will eventually connect you with a human support agent who can handle the account deletion request.

I was authenticated as koko@test.com, and I wanted to delete toto@test.com.

So, I asked the human support agent to delete the account, and he told me:

Then, I gave him toto@test.com.

He realized that koko@test.com was the account talking to him, not toto@test.com.

So, he told me that he had sent an email to toto@test.com, and if I replied to that email, he would delete the account.

At this point, I surrendered and thought there was no bug. 😢😢😢😢

I came back to test the domain again, and I was still thinking about the previous attempt.

I wanted to make the human support agent not suspicious about the fact that koko@test.com was talking to him.

I wanted to make him believe that toto@test.com was the one talking to him.

So, I tested the same functionality again, but this time **without being authenticated**.

When I asked the AI chatbot to make an account deletion request, it asked me to provide an email address:

So, I entered:

toto@test.com

And it accepted it.

Then, the human support agent told me that they were sad to see me leave and thanked me for using their service. He also told me that the account would be deleted after 24 hours.

Some other human support agents told me that it would take 48 hours or even a few days.

But there was a problem.

The whole conversation was also sent to the victim’s email address.

So, if I waited for 24 hours or more, the victim would be able to see what was going on from their email.

Then I thought:

***Why wait?***

So, I asked every human support agent to delete the account immediately.

And surprisingly, they all told me that they had deleted the account and wished me a nice day.

And the victim’s email received the final message:

***We have deleted your account and have a nice day.***

😆😆😆😆😆😆

So lets do it as a steps report :

1- Open the application’s main page while unauthenticated.

2- Start a conversation with the chatbot and request to delete an account.

3- The chatbot asks for an email address.

4- Provide the email address of a victim account that is not controlled by the attacker.

5- The chatbot transfers the conversation to a human support agent.

6- The human support agent receives the conversation and sees the victim’s email address as the email associated with the deletion request.

7- Notice that the support agent does not request any proof of ownership, authentication, verification code, or other confirmation that the requester controls the provided email address or account.

8- Ask the support agent to delete the account.

9- Depending on the support agent’s handling, the account may initially be scheduled for deletion. For example, one agent stated:

“We will delete your account 1–2 business days from this notice.”

10- Reply to the agent requesting that the account be deleted immediately.

The support agent will proceed with the deletion without performing any additional identity verification.

11- The support agent confirmed that the account had been deleted:

“Ok no problem. Your account has been deleted.”

12- In another test, the support agent initially provided a 24-hour cancellation period and, after the attacker requested immediate deletion, confirmed:

“we have deleted your account as requested.”

13- Try to login again after the account has been deleted.

14- observe that account has been deleted and can not access it anymore.

Thank you for your time. I hope you found this write-up useful.

**Big thanks to my company and my amazing team:** [Rootxsecurity](https://medium.com/u/56d6dda3b729)

My linkedin : [https://www.linkedin.com/in/yahia-ramadan-](https://www.linkedin.com/in/yahia-ramadan-/)

**ومتنساش تصلي على النبي ﷺ ❤️**
