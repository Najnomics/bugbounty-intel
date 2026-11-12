# 🛡️ How We Were Almost Hacked at Ethereum Argentina 2023

- **Source URL:** https://blog.theredguild.org/you-were-not-pwned-the-red-guild-ethereum-argentina-2023
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/330 (id 330)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Crypto conferences aren't only about the buzz and the networking. If you pay attention, you'll quickly realize what a hostile environment they really are. Attackers don't lose their time - they are there to try to scam and hack you. How? Perhaps using [social engineering](<https://en.wikipedia.org/wiki/Social_engineering_(security)>) techniques on you, or tampering and compromising your devices once they have physical access.

But we don't learn until something bad happens to us, do we? It's like we're waiting to be pwned to learn how to not be pwned.

Perhaps if someone *almost* pwned you – but really didn't – and told you how, you'd have a taste for the experience, without the harmful consequences. Sounds good?

Great, because that's what we're beginning to do. **At The Red Guild, we run security awareness campaigns in IRL events we attend.** We want you to learn first-hand about how you *could* be attacked, and the proactive measures you can take to prevent some of the threats.

Soooo... do we pwn people to teach them stuff?

No! Relax. The Red Guild isn't pwning anyone. We *never* do anything that could compromise anyone's security.

We simply take some liberties during events, to showcase threats that you and your friends may be exposed to. Without any harmful consequences.

In August 2023 we ran our first IRL campaign at Ethereum Argentina. This is what we did:

- Dropped USB devices.
- Hanged QR codes with redirects.
- Ran a phishing campaign including fake on-site flyers, a deceiving coding challenge, and a copycat website sharing fake agendas and calendars.
- Downloaded a little gift to our workshop's attendees.
- Played with the WiFi APs.
- Spotted and flagged unattended and unlocked laptops.

At the end of this article you'll also **find safety tips** to put into practice the next time you attend a conference.

## Dropping USB devices

USB dropping can be a fairly common technique that attackers may use to spread malware and gain access to your laptop in a conference. After infecting the device, they'll drop the USB somewhere in the conference, and wait for someone to pick it up and connect it to their device.

To replicate the experience without harming anyone, we decided to drop USB devices throughout the place, but with a twist. Instead of spreading malware, we put harmless files in the devices.

We not only used the opportunity to share security advice with whomever picked up our USBs. We also wanted to make it a memorable experience! And ideally have new adepts join our campaign. So we included some cool stuff for them.

README-FIRST.txt was such a beauty. It was an e-zine!

This is how The Red Guild pays respect to all those hackers and curious people who came before us. These little things are a gesture, a humble contribution to keep whatever is left of that flame alive.

Here's the full e-zine: [https://theredguild.org/ezines/1.html](https://theredguild.org/ezines/1.html)

In another file [matta](https://twitter.com/mattaereal) wrote about ideas on how to reuse the pendrive for personal use. Such as turning it into a key to open your own password manager database. Here it is:

Finally, t3m4rd0.mp3. What. A. Trackkkk. The coolest 8-bit-style cyberpunk song you'll ever listen to. We had a local producer made it specially for the occasion. Enjoy:

## Planting QR codes in the wild

We wouldn't advise scanning whatever QR code you see in a conference. It may be the entrypoint that leads you into a phishing site, or have you download harmful stuff that could put your device at risk.

To teach attendees about this risk, we planted QR codes everywhere we could. Just harmless codes that would link to a redirect in our site `https:://theredguild.org/r/curiosity`. The redirect would finally point people here:

We had an absurd amount of QR codes printed as stickers. 50? 100? Lost count.

We carried them around the whole time, and pasted them whenever we saw a good spot.

Like on all tables of the co-working space:

Or in the main room's map:

Or, well, anywhere really:

## Phishing flyers

We wanted include realistic assets as part of the campaign. After some discussions, we decided to hang phishing flyers in the main room.

This was tricky. We wanted the flyers to be noticed by attendees, but that meant they had to be well designed. They had to look "official". Luckily, our design skills are the envy of the web3 space. Check these babies out.

One flyer had a QR code as if it was sharing the event's main agenda:

The other flyer promoted a coding challenge to "win a hardware wallet".

We had them printed in pro quality, and hanged them around the conference.

They look nice, don't they? Just as if they belonged to the official organization. See for yourself where we placed them:

At some point the organization started to notice. All of a sudden they were bringing down our beloved flyers. We may have seen one or two ugly faces on those trying to find the culprits 😄

One fun moment was when someone shared a "SCAM ALERT" in the main Telegram group of the event mentioning our QR codes and fake flyers:

## Fake site and GitHub org

Our flyers linked to a website for the agenda, as well as to a GitHub repository where we hosted the challenge. To do make them even more deceiving, we needed to establish a minimum online presence.

First, we mirrored the official site of the conference. The original was hosted at `ethereumargentina.org`. We bought `ethereumargentina.xyz`, and hosted a similar site.

Here's the code for ours:

We even managed to get the same IP address of the official site! 😎

If you're wondering how, we can only tell you that magicians never reveal all their tricks 🫢

On top of the original one, our site included a link to the fake agenda. If clicked, would automatically download a PDF to your device. Without any prompt. Here's the actual link used:

If you clicked on it, you'd have the """agenda""" automatically downloaded and opened. Which looked like this:

The phishing site also had some easter eggs. For example, we listed ourselves as sponsors:

As said, this was hosted in a public repository. To make them more realistic, we created a [fake organization in GitHub](https://github.com/ethereum-argentina) called "ethereum-argentina".

## A dangerous coding challenge

This one's another gem of our campaign. You saw earlier that we had a flyer promoting a "coding challenge". If you scanned the QR code, it would take you to this repository:

At first it looks like a real challenge. The prompt reads:

The repository contains a real Foundry project, with instructions to install dependencies and run the code. Ideally, participants should be able to find a vulnerability in one of the Solidity smart contracts that would allow them to pass the challenge. Must say: the thing is real! You can actually attempt to solve the challenge.

Buut of course there's a twist. Upon being run, the code silently fetches and downloads a PDF to your machine. In theory, this would be the "ticket" to participate in the raffle for a hardware wallet that would take place during Ethereum Argentina.

Although there was no real raffle. If you opened the PDF, this would pop up:

The magic is in how we accomplished to embed an automatic PDF download in the coding challenge, without having any noticeable URL in plaintext in the code. Can you figure it out? That's the meta-challenge for you, anon.

## Almost pwning our own workshop

Some members of The Red Guild delivered a smart contract security hands-on workshop. For almost two hours we showed the basics on how to do security testing with Foundry.

Of course we didn't mean to hack any of the workshop attendees... Although, it was too tempting.

We just left a little thing hidden in the repository, that would be run locally in the machines of anyone following the workshop.

Nothing harmful! We just took advantage of Foundry's ffi to silently drop the same PDF we showed earlier to their machines.

Oh, btw, the reverse shell is commented out, just in case you were wondering about it 😇

## Flagging unattended laptops

You must NEVER leave your laptops unattended during a conference. Let alone leave them unattended AND unblocked. Surprisingly or not, we saw many instances of this during Ethereum Argentina.

We knew this would happen, and we were ready. We printed *lots* of pretty cards to flag any unattended computer. We always had a bunch in our pockets, and dropped them whenever we ran into a pwnable device.

At some point it became too easy:

We won't spoil you what the card looks like in detail. It's super pretty, and definitely feels like a cool collectible for our followers.

But please don't start leaving your laptops alone just to get our cards! 😊

## Playing with WiFis

Have you ever been advised to avoid connecting to suspicious WiFis during an event? Probably.

Well, we wanted to recreate that experience at Ethereum Argentina. So together with some frens we brought some cool WiFi toys to the conference.

We spinned up garbage and fake APs, to create noise and disturb visually anyone trying to use the WiFis.

We also tried to clone some of the event's official networks, simulating MAC addresses and passwords. Some users may have erroneously connected to ours.

Worth stressing: we only played around during some very brief periods of time. We *never* messed up with the WiFi networks nor affected the overall experience of the people participating in the conference.

## Security awareness article

We not only wanted to trick people. We also wanted them to learn. That's why we published this unlisted article during Ethereum Argentina:

The QR code in the cards, the fake agenda, the ticket of the coding challenge, the files in the USB devices, etc. In some way or another, they would all end up pointing attendees to this article.

In it we shared more details about our ongoing security awareness campaign, asked them to keep it a secret between us, and advised them on how to better stay safe during the conference.

## What's next?

This was incredibly fun. With little resources but lots of creativity, we ended up running what felt like a red teaming exercise in an IRL event. None of our activities were actually harmful for any of the attendees, but still were able to showcase and teach people relevant safety lessons.

We also want to bring to the crypto world part of the hacking culture that exists in more traditional security conferences. Think [DEFCON](https://defcon.org/), [BlackHat](https://blog.theredguild.org/blackhat.com), [Ekoparty](https://blog.theredguild.org/ekoparty.org), etc. where the environment can be, to put it nicely, a bit more hostile among participants.

This was just our first time! We see ourselves repeating these activities in other conferences, next time with more experience, preparation and surprises.

**If you're an event organizer and wish to have The Red Guild run a security awareness campaign in your next event, get in touch!**

### **How do you stay safe during your next event?**

There's no silver bullet. Other than not attending 😆

Attackers and criminals can be far more sophisticated that what we've shown. An attacker won't be as noisy and evident as us. We only had time to prepare our campaign for one or two weeks, and we rushed to execute everything while we prepared our [talk](https://www.youtube.com/watch?v=6YxWTxVkp4A&t=1s) and workshop.

In real life, attackers may hide for days, months or years before actually making a noticeable move. That's why we must strive to be proactive in our security practices.

Yes, it's hard, and you never know what's gonna happen. Yet, there're a few basic things we can bear in mind to lower the chances of getting pwned:

- Never leave unattended nor unlocked devices.
- Find private places to use your laptops, have calls, etc. Wherever you can avoid [shouldersurfing](<https://en.wikipedia.org/wiki/Shoulder_surfing_(computer_security)>) and [eavesdropping](https://en.wikipedia.org/wiki/Eavesdropping).
- Don't bring your main crypto wallets. If you do, which you shouldn't, just don't show nor use them.
- Don't mindlessly sign transactions to participate in airdrops, POAPs, etc. Always verify the data you're signing. And do so with low-value wallets.
- Use privacy-enhancing screen protectors.
- Don't connect strange external devices (such as USB flash drives) to your laptop.
- Consider using an alternative laptop that doesn't store sensitive information (personal or work-related). For instance, you could carry around a cheap Chromebook.
- Avoid scanning suspicious QR codes that can redirect you to malicious sites. Always double-check the URL, particularly if you're going to introduce sensitive information or sign transactions.
- Don't connect to open WiFis that are not setup by the organizer.
- Don't run untrusted code in a non-isolated environment.
- Don't disclose sensitive details to people who claim to be interested in your projects. First, seek referrals, double-check information, do some [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) on their online presence, and gradually build trust over time.

## Want more stories?

Subscribe to the blog!

It's cool. It's free. And we don't spam. Too lazy to do that.

[i'm a subscriboooooor](https://blog.theredguild.org#/portal/signup/)
