# IDOR lead to unauthorized Access Organizations function

- **Source URL:** https://medium.com/@HBlackGhost/idor-lead-to-unauthorized-access-organizations-function-0dc707011dd1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251105001231/https://medium.com/@HBlackGhost/idor-lead-to-unauthorized-access-organizations-function-0dc707011dd1
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11312 (id 11312)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR lead to unauthorized Access Organizations function

بسم الله الرحمن الرحيم

«اللَّهُمَّ صَلِّ عَلَى محَمَّدٍ وَعَلَى آلِ محَمَّدٍ كَمَا صَلَّيْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ إِنَّكَ حَمِيدٌ مَجِيدٌ، اللَّهُمَّ بَارِكْ عَلَى محَمَّدٍ وَعَلَى آلِ محَمَّدٍ كَمَا بَارَكْتَ عَلَى إِبْرَاهِيمَ وَعَلَى آلِ إِبْرَاهِيمَ إِنَّكَ حَمِيدٌ مَجِيدٌ».

Hello friends. After my absence, I’m back with juicy writeups

In this writeup I will show how I chained an IDOR with an information disclosure to raise it’s severity, turning a single IDOR into a high-severity issue and earning a larger bounty.

One day I woke up, had breakfast with a cup of tea, then started hunting for a privilege-escalation bug in the program’s role logic. While hunting, I discovered an important endpoint and saved it to my notes. After finishing the hunt Form Privilege Escalation , I returned to that endpoint.

**This is the request I saved to my notes.**

This endpoint creates flows on the website. A flow is a sequence of actions

Yea , this request Have Id’s let’s Test IDOR Here …. :

I created another account and quickly navigated to the “Create Flow” function, where I obtained the `project_id` and `env_id` values.

let’s replace `project_id` and `env_id` values and hack this function

Boom. Boom. Boom. I created the flow in another account i created it

But my mind didn’t stop there. After some thought, I came up with a way to increase the severity of this issue: search for leaked IDs in Waybackurls .

OMG, I found it! , i will extrect this from using this command

`echo "https://sub.site.com" | waybackurls | grep -Po 'c-[a-zA-Z0-9]+' | cut -d '-' -f 2 | anew`
Using this command, I was able to extract other users’ IDs from the site

Let’s Improve Severity Of IDOR with Information Disclosure :

I copied the IDs, opened Intruder, selected a Pitchfork attack, chose the sample list payload, and pasted the copied IDs into it and put filter to get 2xx Status Code then click Start Attack

Is this real? I was able to create flows for these IDs.

وابللللللع 🔥😎

[LinkedIn Profile](https://www.linkedin.com/in/pt-ahmed-alaa/) : [https://www.linkedin.com/in/pt-ahmed-alaa/](https://www.linkedin.com/in/pt-ahmed-alaa/)

[YouTube Channel](https://www.youtube.com/@PT-ahmed-alaa) : [https://www.youtube.com/@PT-ahmed-alaa](https://www.youtube.com/@PT-ahmed-alaa)

والسلام عليكم ورحمه الله وبركاته
