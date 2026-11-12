# Root Cause Analyses for 0-day In-the-Wild Exploits - Project Zero

Source: https://projectzero.google/2020/07/root-cause-analyses-for-0-day-in-wild.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

# Posted by Maddie Stone, Project Zero


When a 0-day is exploited in the wild AND it is detected, we need to use that as an opportunity to learn as much as possible about the vulnerability and the exploit if we hope to make 0-day hard. One of the main methods to do that is to perform a root cause analysis (RCA) on the 0-day.


Our effort on this began in earnest in the last quarter of 2019. Today we are beginning to publish the root cause analyses for 0-days exploited in the wild that we have completed. While we’re publishing some in bulk now to play “catch-up”, in the future we plan to post each one in a timely manner after it’s detected and disclosed. We think publishing technical details in a timely manner is important for transparency and so that the whole of the security community can make informed decisions and actions.


We’ve added a new column to the [“0day In the Wild” tracking spreadsheet](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/edit#gid=0) that will link to any RCAs that we publish. We will also continue to update the following page on our blog as we publish additional RCAs.



For each of these root cause analyses, we are using a template. We developed this template based on what we, at Project Zero, find important and actionable about 0-days exploited in-the-wild, but we’d love your feedback on what other information would help you! We welcome any researchers and vendors who want to use our [template](https://docs.google.com/document/d/1z1s__qj16DdhRvAg_TJlmRrXKosUSWfpm463Mjk24Vs/view) and publish this information about 0-days they detect and/or analyze!


When completing a root cause analysis we focus on the following areas.

- Bug class
- Details of the vulnerability, such as how to trigger, what it allows, etc.
- Exploit method and whether or not it’s a known method
- Hypothesis of how the vulnerability was found (code audit, fuzzing, variant analysis, etc.)
- Any historical, present, and future bug context such as previous related bugs
- Areas for variant analysis and any found variants
- Structural improvements
- Can you also kill the entire bug class?
- Is there a way to make it much harder to exploit?
- Potential detection methods for similar 0-days
- Brainstorming ways that this 0-day exploit could have been caught while it was still a 0-day. Please note that this is different from “indicators of compromise” because we’re focusing on detecting while it’s still a 0-day.


We selected these areas because the vulnerability details and exploit method provide in-depth explanation of facts of the exploit: what is the vulnerability, how does it work, and how was it exploited. Once we have the facts documented, we can then use those facts to inform our hypotheses and brainstorm how we can prevent the attackers from being able to do it again. While some of these ideas may be considered infeasible by vendors or not work well in practice, some will be (and already have been) reasonable and able to be launched. The overarching goal is to force brainstorming in the hope of taking actions informed by the detected 0-day: actions to better detect, actions to better lockdown, actions to prevent new vulnerabilities from being introduced, actions to make 0-day hard.


Out of the 20 0-days for 2019 (more on what we decided to include/exclude in our tracking here), we completed 8 root cause analyses that we’re publishing here today. These are 5 out of the 6 of the 0-days detected in August or later of 2019 (when I joined the team and started this initiative 🙂 ). In addition, we’re publishing the two iOS 0-days from February 2019 that Project Zero reported to Apple in partnership with [Google's Threat Analysis Group](https://blog.google/threat-analysis-group), and a Firefox 0-day that Project Zero had reported to Firefox, that was also discovered independently in-the-wild.


- [CVE-2019-7286](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-7286.html): iOS use-after-free in CFPrefsDaemon
- [CVE-2019-7287](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-7287.html): iOS buffer overflow in ProvInfoIOKitUserClient
- [CVE-2019-1107](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-11707.html): Firefox type confusion in Array.pop
- [CVE-2019-1367](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-1367.html): JScript use-after-free in Internet Explorer
- [CVE-2019-2215](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-2215.html): Android use-after-free in Binder
- [CVE-2019-13720](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-13720.html): Chrome use-after-free in webaudio
- [CVE-2019-1458](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2019/CVE-2019-1458.html): Windows win32k uninitialized variable in task switching


These RCAs provide technical details on what the vulnerability is and how it is exploited. We then hypothesize and brainstorm based on these details from our perspective as offensive security researchers.

Our hope is that these analyses are helpful for others in the security and tech communities to act on data gleaned from detected 0-day exploits and help determine ways to make it more costly, more time consuming andmore difficult for attackers to use 0-days in the wild. Please [reach out](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/edit#gid=0&range=A18) with any feedback and/or suggestions and we hope that others will also begin publishing information from the [RCA template](https://docs.google.com/document/d/1z1s__qj16DdhRvAg_TJlmRrXKosUSWfpm463Mjk24Vs/view) in the future.
