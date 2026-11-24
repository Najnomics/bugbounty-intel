# portswigger-talk-css-bomb-inside-your-inbox

- **Source URL:** https://portswigger.net/research/talks?talkId=39
- **Fetched:** 2026-11-24
- **Researcher:** garethheyes
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

**Researcher:** 
                    [Zakhar Fedotkin](/research/zakhar-fedotkin)

We've all heard of well-known misconfigurations causing breaches - but what about those nobody even realised are dangerous? Websites are now built from dozens of infrastructure components, each accompanied by copious vendor guidance. Each system may be secure in isolation but vulnerable when deployed, and vendors 'patch' vulnerabilities by adding notes to docs that nobody actually reads - their way of saying it's your problem now.


In this session, I'll share novel techniques backed up by real-world case studies with impacts including arbitrary read/write access to cloud storage, disclosure of sensitive secrets including encryption keys, widespread XSS, cache-poisoning, and severe single-request DoS attacks.


You don't need a bug to compromise that system - you just need to understand it.

**Researcher:** 
                    [Gareth Heyes](/research/gareth-heyes)

You might think it's safe to open an email in 2026. After all, it's only HTML, right? Turns out, we forgot about CSS. In this talk, I'll introduce multiple novel techniques for compromising email accounts by ripping apart trust boundaries, using nothing but CSS and HTML. I'll show you how to weave vectors past defence layers, including CSS sanitization, hardened CSP, and the HTML filtering library everyone trusts. I'll start with a simple attack that deanonymizes users of a "privacy-first" encrypted email provider. Then I'll show just how much damage CSS can do, with end-to-end account takeovers on multiple major email providers, including an enterprise giant. I'll also share an alternative angle of attack, targeting third-party websites by turning a classic non-issue into a genuine threat. This attack works regardless of which webmail the victim is using.


You'll leave with an open-source CSS weaponization toolkit, a honed methodology, and a permanent distrust of every email in your inbox.

**Researcher:** James Kettle

**Conferences:** DEF CON 34, 07 Aug 2026 | Black Hat USA 2026, 05 Aug 2026

**Conferences:** Black Hat USA 2026, 05 Aug 2026

**Conferences:** Black Hat Europe, 10 Dec 2025

**Conferences:** NDC Manchester, 04 Dec 2025

**Conferences:** RomHack, 27 Sept 2025 | DEF CON 33, 08 Aug 2025 | Black Hat USA 2025, 06 Aug 2025

**Researcher:** Martin Doyhenard

**Conferences:** Black Hat USA Arsenal, 06 Aug 2025

**Conferences:** Steelcon, 12 Jul 2025

**Conferences:** PortSwigger Discord, 07 Nov 2024

**Conferences:** DEF CON 32, 11 Aug 2024 | Black Hat USA 2024, 07 Aug 2024

**Conferences:** DEF CON 32, 09 Aug 2024 | Black Hat USA 2024, 07 Aug 2024

**Conferences:** Nullcon Goa 2023, 23 Sept 2023 | DEF CON 31, 12 Aug 2023 | Black Hat USA 2023, 09 Aug 2023

**Conferences:** Nullcon Berlin 2023, 09 Mar 2023 | OWASP 2023 Global AppSec Dublin, 15 Feb 2023

**Conferences:** DEF CON 30, 12 Aug 2022 | Black Hat USA 2022, 10 Aug 2022

**Conferences:** Nullcon Berlin, 08 Apr 2022

**Conferences:** Black Hat Europe, 10 Nov 2021 | DEF CON 29, 06 Aug 2021 | Black Hat USA, 05 Aug 2021

**Conferences:** Black Hat Europe 2020, 10 Dec 2020

**Conferences:** Black Hat USA 2020, 05 Aug 2020

**Conferences:** Global AppSec Allstars, 26 Sept 2019

**Conferences:** Black Hat USA 2019, 07 Aug 2019

**Conferences:** LevelUp 0x03, 25 Jan 2019

**Conferences:** Black Hat USA 2018, 09 Aug 2018

**Conferences:** AppSec Europe, 06 Jul 2018

**Conferences:** BSides Manchester, 17 Nov 2017

**Conferences:** Black Hat USA 2017, 27 Jul 2017

**Conferences:** OWASP AppSec EU 2017, 12 May 2017

**Conferences:** Black Hat Europe 2016, 05 Dec 2016

**Conferences:** OWASP London , 24 Nov 2016

**Conferences:** 44Con 2015, 15 Sept 2015

**Conferences:** Black Hat USA 2015, 05 Aug 2015
