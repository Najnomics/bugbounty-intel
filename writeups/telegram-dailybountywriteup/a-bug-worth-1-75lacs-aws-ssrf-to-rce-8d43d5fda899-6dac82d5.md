# A bug worth 1.75Lacs — AWS SSRF to RCE

- **Source URL:** https://logicbomb.medium.com/a-bug-worth-1-75lacs-aws-ssrf-to-rce-8d43d5fda899?source=rss------bug_bounty-5
- **Fetched from:** https://logicbomb.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 612)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### AWS SSRF to Root on production instance — A bug worth 1.75Lacs

It’s been some time since I blogged mainly because there was not something new I could find in the last 6–7 months of bug bounty. Fortunately, this month started with a nice bug that I discovered in a Trading Platform. Let’s get straight away to the vulnerability writeup, would try to keep it short and crisp so here you go. This is about —

### **How I escalated well-known AWS SSRF to perform Remote Code Execution (RCE) in one of India’s growing Trading startups.**

I was manually traversing to different sections of the app to look for some sensitive API endpoints and parallelly I added the target scope to “Crawl and Audit” in Burpsuite. In the app, there was a usual “Password Reset” functionality. Looking closely at the endpoint, there was a parameter **“return\_url”**. Such parameters always have the potential of carrying some easy-find bugs. And my expectations proved right when Burpsuite discovered an **“External service interaction (DNS)”** vulnerability in the same endpoint. While checking different HTTP request headers, it was clear that the application was over AWS since I could see the Response Header as X-Amz-Cf-Id and there was also an S3 bucket interaction for fetching profile photos.

The next move was clear to check if there is any SSRF possible or not. I tried accessing the AWS metadata URL (http://169.254.169.254/latest/meta-data/)and below was the response to the CURL request —

Fetching security credentials from instance metadata —

and that confirmed the SSRF for me.

Now it’s time to extend it further and this is what one should always try to do —

Escalate the vulnerability by trying out every possibility associated with it. That will increase the impact of the bug and also fetch much better rewards.

AWS provides a service called **AWS System manager** to manage applications and infrastructure running in the AWS Cloud which can be used by command-line tools as well. Ref — [https://docs.aws.amazon.com/cli/latest/reference/ssm/index.html](https://docs.aws.amazon.com/cli/latest/reference/ssm/index.html)

*The one thing that ran in my favor here was in order to run remote commands in the instance via SSM, it should have a relevant role attached to the instance.*

1. Install and configure AWS CLI by using the above security credentials.

$ *export AWS\_ACCESS\_KEY\_ID=*
$ *export AWS\_SECRET\_ACCESS\_KEY=*
$ *export AWS\_DEFAULT\_REGION=*
$ *export AWS\_SESSION\_TOKEN=*

2\. Below command can be used to find the region used in the 1st step- [http://169.254.169.254/latest/meta-data/placement/availability-zone](http://169.254.169.254/latest/meta-data/placement/availability-zone)

3\. Use send-command to execute the command, the query looks like this-

$ aws ssm send-command --document-name "AWS-RunShellScript" --comment "AnyComment" --instance-ids="\[Instance-id\]" --parameters "commands=whoami"

The output of this command provides a CommandId

4\. To get the instance ID used in the 3rd step- [http://169.254.169.254/latest/meta-data/instance-id](http://169.254.169.254/latest/meta-data/instance-id)

5\. Final step to see the output of the command executed (as used in step 3 “whoami”)-

$ aws ssm list-command-invocations --command-id="\[Command\_Id\]" --details

Pheww and finally I was able to get the command executed. One can see the output as “root”! And this is how I was able to escalate AWS SSRF to RCE. That’s it from this short writeup.

*Report details-*

8-Oct-2022 — Bug reported to the concerned company.

12-Oct-2022 — Bug was marked fixed.

15-Oct-2022 — Re-tested and confirmed the fix.

23-Oct-2022 — Rewarded.

Thanks for reading!

Twitter \~ [logicbomb\_1](https://twitter.com/logicbomb_1)

Site \~ **https://logicbomb.in/**
