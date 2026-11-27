# Race Condition on Change Email Leads to Arbitrary Email Forgery

- **Source URL:** https://medium.com/@blackarazi/race-condition-on-change-email-leads-to-arbitrary-email-forgery-741b720ac840?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240530061545/https://medium.com/@blackarazi/race-condition-on-change-email-leads-to-arbitrary-email-forgery-741b720ac840
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5886 (id 5886)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Race Condition on Change Email Leads to Arbitrary Email Forgery**

Hello everyone,

In this post, I will show you how I discovered a vulnerability that allows a malicious user to change their email to an unregistered email that belongs to someone else & perform the email verification without consent from the legitimate owner of the email. The attack can be done by sending multiple requests in parallel with 2 different emails in the request body, also known as a `single packet attack`. This attack will result in the new email address (pending) being set to the victim email but the confirmation email will be sent both to the victim & attacker email, the attacker then can click the confirmation email (with the valid token) and claim the victim email.

This attack is heavily inspired by a post from James Kettle about [Smashing the state machine: the true potential of web race conditions](https://portswigger.net/research/smashing-the-state-machine).


## What is Race Condition?

According to PortSwigger Web Security Academy, Race conditions are a common type of vulnerability closely related to business logic flaws. They occur when websites process requests concurrently without adequate safeguards. This can lead to multiple distinct threads interacting with the same data at the same time, resulting in a “collision” that causes unintended behavior in the application. A race condition attack uses carefully timed requests to cause intentional collisions and exploits this unintended behavior for malicious purposes.

The period of time during which a collision is possible is known as the “race window”. This could be the fraction of a second between two interactions with the database, for example.

Like other logic flaws, the impact of a race condition is heavily dependent on the application and the specific functionality in which it occurs.

Some real-life cases of race condition attacks:

You can also check “[Top Race Condition reports from HackerOne](https://github.com/reddelexc/hackerone-reports/blob/master/tops_by_bug_type/TOPRACECONDITION.md)”.

## Who is the target?

Vidio is one of Indonesia’s most popular news and entertainment websites, with live streaming channels, critically acclaimed original content, real-time audience involvement, and talent spotting competitions. Users can enjoy live streaming, watch TV and anytime, as well as other exclusive shows on Vidio.com anytime and anywhere.


Vidio has a Bug Bounty Program (BBP), you can check it on their page [VIDIO BUG BOUNTY PROGRAM](https://www.vidio.com/pages/vidio-bug-bounty-program) for more details on the program scope, rules, etc.

I had a positive impression of Vidio security team swift response to my bug report submissions. They consistently demonstrates excellent communication. Their prompt responses, clear explanations, and proactive updates contribute significantly to our collaborative efforts in maintaining a secure environment. I’d like to also highlight their help & feedback to this writing, their expertise and insights greatly enhanced the final piece, and I’m truly appreciative of the time and effort they dedicated to helping me.


## Limitation

Please note that the reproduction steps might not work on the first try, this is due to the nature of the race condition itself. Although we send the requests simultaneously in a single TCP packet & arrive at the server simultaneously, but we can’t control how the server processes the requests. In order to be successful, a race condition vulnerability requires a ‘collision — two concurrent operations on a shared resource. So we might

want to retry the steps if isn’t working on the first try.

## **Steps To Reproduce**

Before started, make sure you already have Burp Suite & Turbo Intruder Extension installed.


\[1\] Create a `attacker` user & make sure that the email is already verified.

\[2\] Find a `victim` email that never registers to Vidio.

\[3\] Prepare a secondary email for the `attacker` that never register to Vidio, this email will be the one that receives the confirmation email.

\[4\] Log in to the `https://www.vidio.com/users/login` as `attacker`

\[5\] Go to the Email Setting page `https://www.vidio.com/dashboard/setting/email`

\[6\] Turn on the Burp Proxy Intercept.

\[7\] Put the victim's email in the form & then click Submit.

\[8\] Go to Burp & search for the URL `PATCH` [https://www.vidio.com/dashboard/setting/email](https://www.vidio.com/dashboard/setting/email`)

\[9\] Select the victim email on the request body & right click then select `Extensions` > `Turbo Intruder` > `Send to turbo intruder`

\[10\] It will open a new window dialog for Turbo Intruder. In the top section, it will show the request, make sure the URL is correct & the request body looks like this:

`user%5Bemail%5D=%s`
- `user%5Bemail%5D` is the request key, if we url-decode it, it becomes `user[email]`
- `%s` is the request value, in this case, the email address, Turbo Intruder automatically changed it to `%s` variable so that we can control it via script.

\[11\] Now in the Script section below, click on the script dropdown & select the`examples/race-single-packet-attack.py`, we need to modify the script to suit our needs. It should look like this:

```
def queueRequests(target, wordlists):
    # if the target supports HTTP/2, use engine=Engine.BURP2 to trigger the single-packet attack
    # if they only support HTTP/1, use Engine.THREADED or Engine.BURP instead
    # for more information, check out https://portswigger.net/research/smashing-the-state-machine
    engine = RequestEngine(endpoint=target.endpoint,
                        concurrentConnections=1,
                        engine=Engine.BURP2
                        )
    # the 'gate' argument withholds part of each request until openGate is invoked
    # if you see a negative timestamp, the server responded before the request was complete
    engine.queue(target.req, 'victim@example.com', gate='race1')
    engine.queue(target.req, 'attacker@example.com', gate='race1')
    # once every 'race1' tagged request has been queued
    # invoke engine.openGate() to send them in sync
    engine.openGate('race1')
def handleResponse(req, interesting):
    table.add(req)
```
\[12\] Now click on the `Attack` button below to launch the attack.

\[13\] After it is finished, it will show the result & we can see there are 2 requests. Make sure that the HTTP response is `200`.

\[14\] Next, we can open the `attacker` secondary email & see if we receive the `Confirmation Email`. Open the email & observe that the recipient & email mentioned in the email content is actually different. This means that our attack is successful.

\[15\] Now we can click on the `Verify victim@example.com` button to claim the `victim` email.

\[16\] Go to the Email Setting page `https://www.vidio.com/dashboard/setting/email` again & observe that the `victim` email is listed there & verified.

## Impact

1. Attackers could change their Vidio account’s email using an unregistered email that they don’t own, resulting in a legitimate owner of the email couldn’t register their own email to Vidio. This could cause missed opportunities for new Vidio users that could lead to financial losses.
2. It can also result in “spam” activity to the legitimate email owner since they never register to Vidio but they will receive marketing/ promo emails from Vidio. This could cause reputational losses for Vidio.

## Mitigation

According to Infosec on [How to mitigate Race Conditions vulnerabilities,](https://www.infosecinstitute.com/resources/secure-coding/how-to-mitigate-race-conditions-vulnerabilities/) the simplest ways to eliminate race conditions are to remove the potential for parallel processing within an application or to ensure that different threads of execution do not share resources.

However, this is not an option in some cases and can negatively impact program performance in others. Two options for fixing the issue are the use of **thread-safe programming** and **randomization**.

In Vidio's case, the mitigation is based on thread-safe programming:

\[1\] Atomic; a function or a particular set of instructions can be designed to be atomic (uses database transaction, locking mechanism, mutexes, or similar tools). An atomic operation is one that is always run as a whole, i.e., no other threads of execution can interrupt its processing. By marking a block of code containing a race condition vulnerability as atomic, the potential vulnerability can be eliminated, since two threads cannot execute the instructions it contains at the same time.

Some articles I found that hopefully could help:

- [\[FastRuby.io\] An introduction to race condition](https://www.fastruby.io/blog/rails/code-quality/An-introduction-to-race-condition.html)
- [\[Honeybadger\] How to Avoid Race Conditions in Rails](https://www.honeybadger.io/blog/avoid-race-condition-in-rails/)
- [\[Redis\] Distributed Locks with Redis](https://redis.io/docs/manual/patterns/distributed-locks/)\]

\[2\] Parallel processing; designing a function so that multiple instances of the function can be executed in parallel without any interference with one another. Such a design enables the application to take full advantage of parallel processing.

If database transactions & locking mechanism mitigation already exist, there’s also a chance that the vulnerability relies on how the confirmation email is being sent. This is the same vulnerability as Gitlab has & [they already patched it](https://gitlab.com/gitlab-org/gitlab/-/commit/e4d8d4f818275d42469d154b72fc6367b2b86bbb).

The vulnerability arises in an inconsistency between how Devise knows where to send the email, and how it knows what to put inside the email. The email is sent to a variable passed directly in an argument to \`send\_devise\_notification\`. However, the variables used to populate the email body, including the \`confirmation\_link\`, are retrieved from the database using a server-side template engine. This creates a race window between \`send\_devise\_notification\` being invoked, and the email body being generated, where another thread can update \`user.unconfirmed\_email\` in the database.


## Conclusion

In summary, the exploration of the race condition vulnerability within the email change functionality highlights the intricate dance between user convenience and system security. This case study not only sheds light on a specific security challenge but also serves as a cautionary tale that underscores the ongoing battle in cybersecurity. It reminds us that vigilance and continuous improvement are paramount in the digital age, where security is not just about protecting data but also about maintaining user trust and the integrity of digital platforms. I’d like to also recommend fellow security researcher to continue their research in this specific area since it has many hidden opportunities, including vulnerabilities that were previously near-impossible to detect or exploit.

Spotting anomalies is the single most important skill for finding race condition

— *James Kettle*


## Timeline

- \[16/11/2023\] Report by email to the Vidio security team [security@vidio.com](mailto:security@vidio.com)
- \[20/11/2023\] Acknowledgement of the receipt of security disclosure
- \[05/12/2023\] The results of the Vidio team verify that the report is valid and categorize the report as **informational** because they are aware of how the current system works and is in accordance with the business process design that has already been implemented. However, the finding is very useful for the further development of Vidio. As a form of appreciation for the report, Vidio gave a 6 month Platinum voucher that can be used to watch interesting shows on Vidio.
- \[07/12/2023\] Asking permission for public disclosure & Hall of Fame.
- \[28/12/2023\] Accept Hall of Fame request. For public disclosure, ask to follow the [Coordinated Vulnerability Disclosure (CVD)](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) principles, as explained. Vidio would appreciate it if it could wait up to 90 days before publishing.
- \[31/12/2023\] Receive Hall of Fame.
- \[19/03/2024\] Submit the first draft of the public disclosure
- \[25/03/2024\] Received feedback
- \[02/04/2024\] Submit the second draft
- \[08/04/2024\] Received feedback
- \[08/04/2024\] Submit the final version
