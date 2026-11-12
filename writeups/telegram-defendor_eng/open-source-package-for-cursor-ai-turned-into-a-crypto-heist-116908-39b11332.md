# 🛡️ Fraudulent Solidity Extension Stole $500K from a Developer

- **Source URL:** https://securelist.com/open-source-package-for-cursor-ai-turned-into-a-crypto-heist/116908
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/273 (id 273)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Attacks that leverage malicious open-source packages are becoming a major and growing threat. This type of attacks currently seems commonplace, with [reports of infected packages](https://www.kaspersky.com/blog/supply-chain-attacks-in-2024/52965/) in repositories like PyPI or npm appearing almost daily. It would seem that increased scrutiny from researchers on these repositories should have long ago minimized the profits for cybercriminals trying to make a fortune from malicious packages. However, our investigation into a recent cyberincident once again confirmed that open-source packages remain an attractive way for attackers to make easy money.

## Infected out of nowhere

In June 2025, a blockchain developer from Russia reached out to us after falling victim to a cyberattack. He’d had around $500,000 in crypto assets stolen from him. Surprisingly, the victim’s operating system had been installed only a few days prior. Nothing but essential and popular apps had been downloaded to the machine. The developer was well aware of the cybersecurity risks associated with crypto transactions, so he was vigilant and carefully reviewed his every step while working online. Additionally, he used free online services for malware detection to protect his system, but no commercial antivirus software.

The circumstances of the infection piqued our interest, and we decided to investigate the origins of the incident. After obtaining a disk image of the infected system, we began our analysis.

## Syntax highlighting with a catch

As we examined the files on the disk, a file named `extension.js` caught our attention. We found it at %userprofile%\.cursor\extensions\solidityai.solidity-1.0.9-universal\src\extension.js. Below is a snippet of its content:

This screenshot clearly shows the code requesting and executing a PowerShell script from the web server `angelic[.]su`: a sure sign of malware.

It turned out that `extension.js` was a component of the Solidity Language extension for the Cursor AI IDE, which is based on Visual Studio Code and designed for AI-assisted development. The extension is available in the Open VSX registry, used by Cursor AI, and was published about two months ago. At the time this research, the extension had been downloaded 54,000 times. The figure was likely inflated. According to the description, the extension offers numerous features to optimize work with Solidity smart contract code, specifically syntax highlighting:

We analyzed the code of every version of this extension and confirmed that it was a fake: neither syntax highlighting nor any of the other claimed features were implemented in any version. The extension has nothing to do with smart contracts. All it does is download and execute malicious code from the aforementioned web server. Furthermore, we discovered that the description of the malicious plugin was copied by the attackers from the [page of a legitimate extension](https://open-vsx.org/extension/juanblanco/solidity), which had 61,000 downloads.

## How the extension got on the computer

So, we found that the malicious extension had 54,000 downloads, while the legitimate one had 61,000. But how did the attackers manage to lull the developer’s vigilance? Why would he download a malicious extension with fewer downloads than the original?

We found out that while trying to install a Solidity code syntax highlighter, the developer searched the extension registry for `solidity`. This query returned the following:

In the search results, the malicious extension appeared fourth, while the legitimate one was only in eighth place. Thus, while reviewing the search results, the developer clicked the first extension in the list with a significant number of downloads – which unfortunately proved to be the malicious one.

## The ranking algorithm trap

How did the malicious extension appear higher in search results than the legitimate one, especially considering it had fewer downloads? It turns out the Open VSX registry ranks search results by relevance, which [considers multiple factors](https://github.com/eclipse/openvsx/blob/master/server/src/main/java/org/eclipse/openvsx/search/RelevanceService.java), such as the extension rating, how recently it was published or updated, the total number of downloads, and whether the extension is verified. Consequently, the ranking is determined by a combination of factors: for example, an extension with a low number of downloads can still appear near the top of search results if that metric is offset by its recency. This is exactly what happened with the malicious plugin: the fake extension’s last update date was June 15, 2025, while the legitimate one was last updated on May 30, 2025. Thus, due to the overall mix of factors, the malicious extension’s relevance surpassed that of the original, which allowed the attackers to promote the fake extension in the search results.

The developer, who fell into the ranking algorithm trap, didn’t get the functionality he wanted: the extension didn’t do any syntax highlighting in Solidity. The victim mistook this for a bug, which he decided to investigate later, and continued his work. Meanwhile, the extension quietly installed malware on his computer.

## From PowerShell scripts to remote control

As mentioned above, when the malicious plugin was activated, it downloaded a PowerShell script from `https://angelic[.]su/files/1.txt`.

The script checks if the ScreenConnect remote management software is installed on the computer. If not, it downloads a second malicious PowerShell script from: `https://angelic[.]su/files/2.txt`. This new script then downloads the ScreenConnect installer to the infected computer from `https://lmfao[.]su/Bin/ScreenConnect.ClientSetup.msi?e=Access&y=Guest` and runs it. From that point on, the attackers can control the infected computer via the newly installed software, which is configured to communicate with the C2 server `relay.lmfao[.]su`.

## Data theft

Further analysis revealed that the attackers used ScreenConnect to upload three VBScripts to the compromised machine:

- `a.vbs`
- `b.vbs`
- `m.vbs`

Each of these downloaded a PowerShell script from the text-sharing service `paste.ee`. The download URL was obfuscated, as shown in the image below:

The downloaded PowerShell script then retrieved an image from `archive[.]org`. A loader known as [VMDetector](https://www.sonicwall.com/blog/vmdetector-based-loader-abuses-steganography-to-deliver-infostealers) was then extracted from this image. VMDetector attacks [were previously observed](https://www.ibm.com/think/x-force/dcrat-presence-growing-in-latin-america) in phishing campaigns that targeted entities in Latin America. The loader downloaded and ran the final payload from paste.ee.

Our analysis of the VBScripts determined that the following payloads were downloaded to the infected computer:

- Quasar open-source backdoor (via `a.vbs` and `b.vbs`),
- Stealer that collected data from browsers, email clients, and crypto wallets (via `m.vbs`). Kaspersky products detect this malware as `HEUR:Trojan-PSW.MSIL.PureLogs.gen`.

Both implants communicated with the C2 server `144.172.112[.]84`, which resolved to `relay.lmfao[.]su` at the time of our analysis. With these tools, the attackers successfully obtained passphrases for the developer’s wallets and then syphoned off cryptocurrency.

## New malicious package

The malicious plugin didn’t last long in the extension store and was taken down on July 2, 2025. By that time, it had already been detected not only by us as we investigated the incident but also by [other researchers](https://secureannex.com/blog/these-vibes-are-off/). However, the attackers continued their campaign: just one day after the removal, they published another malicious package named “solidity”, this time exactly replicating the name of the original legitimate extension. The functionality of the fake remained unchanged: the plugin downloaded a malicious PowerShell script onto the victim’s device. However, the attackers sought to inflate the number of downloads dramatically. The new extension was supposedly downloaded around two million times. The following results appeared up until recently when users searched for `solidity` within the Cursor AI development environment (the plugin is currently removed thanks to our efforts).

The updated search results showed the legitimate and malicious extensions appearing side-by-side in the search rankings, occupying the seventh and eighth positions respectively. The developer names look identical at first glance, but the legitimate package was uploaded by `juanblanco`, while the malicious one was uploaded by `juanbIanco`. The font used by Cursor AI makes the lowercase letter `l` and uppercase `I` appear identical.

Therefore, the search results displayed two seemingly identical extensions: the legitimate one with 61,000 downloads and the malicious one with two million downloads. Which one would the user choose to install? Making the right choice becomes a real challenge.

## Similar cyberattacks

It’s worth noting that the Solidity extensions we uncovered are not the only malicious packages published by the attackers behind this operation. We used our [open-source package monitoring tool](https://www.kaspersky.com/open-source-feed?icid=gl_securelist_acq_ona_smm__onl_b2c_securelist_lnk_sm-team_______da69c993382d038a) to find a malicious npm package called “solsafe”. It uses the URL `https://staketree[.]net/1.txt` to download ScreenConnect. In this campaign, it’s also configured to use `relay.lmfao[.]su` for communication with the attackers.

We also discovered that April and May 2025 saw three malicious Visual Studio Code extensions [published](https://securitylabs.datadoghq.com/articles/mut-9332-malicious-solidity-vscode-extensions/): solaibot, among-eth, and blankebesxstnion. The infection method used in these threats is strikingly similar to the one we described above. In fact, we found almost identical functionality in their malicious scripts.

In addition, all of the listed extensions perform the same malicious actions during execution, namely:

- Download PowerShell scripts named `1.txt` and `2.txt`.
- Use a VBScript with an obfuscated URL to download a payload from `paste.ee`.
- Download an image with a payload from `archive.org`.

This leads us to conclude that these infection schemes are currently being widely used to attack blockchain developers. We believe the attackers won’t stop with the Solidity extensions or the solsafe package that we found.

## Takeaways

Malicious packages continue to pose a significant threat to the crypto industry. Many projects today rely on open-source tools downloaded from package repositories. Unfortunately, packages from these repositories are often a source of malware infections. Therefore, we recommend extreme caution when downloading any tools. Always verify that the package you’re downloading isn’t a fake. If a package doesn’t work as advertised after you install it, be suspicious and check the downloaded source code.

In many cases, malware installed via fake open-source packages is well-known, and [modern cybersecurity solutions](https://www.kaspersky.com/premium?icid=gl_securelist_acq_ona_smm__onl_b2c_securelist_lnk_sm-team___kprem____3b7590825188da5e) can effectively block it. Even experienced developers must not neglect security solutions, as these can help prevent an attack in case a malicious package is installed.

## Indicators of compromise

Code highlighting with Cursor AI for $500,000

Neel

Amazing report! Now the question we have, as the era of Vibe coding and use of agentic tools expands. How do we make sure such cases and threats are eliminated currently.

For the case in point, thankfully the users were developers so that had a sense of what they were downloading the system extension still backfired!

What if a person with no knowledge take recommendations ,downloads this as vibe coding is all abt end goal with knowing majority what flow or what backend is doing and faces severe financial losses.

Is there a way to solve this truely. I would have suggested creating another extension for checking the and validating the packages.

once in package and is installed before moving forward I hope you see the irony :p

Securelist

Hi Neel,

To protect against such threats, we recommend staying cautious and double-checking any open-source extensions you download. At Kaspersky, we provide a dedicated data feed that flags known malicious packages in various popular repositories (including npm that was affected in the described incident). This tool requires no technical expertise, making it a valuable addition to your overall protection. If you wish to learn more, follow the link: https://www.kaspersky.com/open-source-feed

We appreciate your commitment to building a safer community.

Ben

Thank you for publicising these events. It makes me a lot more vigilant when dealing with extensions. Anything not verified I stay away from.
