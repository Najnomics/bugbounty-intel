# How Android Broke Me into Tech

- **Source URL:** https://medium.com/@UnfilteredInk/how-android-broke-me-into-tech-from-bricking-phones-to-bounty-hunting-1ed674170559?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905085207/https://medium.com/@UnfilteredInk/how-android-broke-me-into-tech-from-bricking-phones-to-bounty-hunting-1ed674170559
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10084 (id 10084)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How Android Broke Me into Tech: From Bricking Phones to Bounty Hunting

Look, I’m gonna be real with you — this whole thing started because I was broke, sleep-deprived, and desperately needed something to keep me sane while my twins screamed at 3 AM. That something turned out to be a Motorola Droid RAZR and an unhealthy obsession with making it run shit it was never supposed to run.

## The RAZR That Started a Thousand Bricks

Two newborn babies. Zero sleep. One locked-down RAZR that Verizon had neutered worse than a shelter dog. I’d just discovered XDA-Developers, which — if you’ve never been there — is basically crack cocaine for phone nerds. Pages and pages of people arguing about kernels, governors, and whether Project Butter actually made anything smoother (spoiler: it didn’t on the RAZR).

My first root was with motofail. If you know, you know. If you don’t, imagine typing commands into a terminal while your phone does absolutely nothing for 10 minutes, then suddenly springs to life with superuser access. First thing I did? Froze all of Verizon’s bloatware with Titanium Backup. NFL Mobile? Gone. VZ Navigator? See ya. That stupid Blockbuster app they were still shipping in 2012? Deleted with extreme prejudice.

But freezing apps got boring fast. The real drug was custom ROMs.

## Flashing Myself into Oblivion

AOKP. CyanogenMod. MIUI (before it became the bloated mess it is now). Eclipse. Liquid Smooth. I flashed them all. Sometimes twice in one night. My poor RAZR probably thought it was having an identity crisis. “Am I stock Android? Am I iOS-themed? Why does my camera app keep force closing?”

Then I got cocky. Tried to downgrade my bootloader from .181 to .173 because some dude on XDA said it would give me better battery life. Pro tip: When Motorola burns those qfuses, they mean it. That phone turned into the world’s thinnest cutting board.

But here’s where it gets good — I refused to accept defeat. Started researching Motorola factory cables, which force the phone into Qualcomm’s emergency download mode by shorting pin 4 to ground. Couldn’t afford the $25 eBay special, so I made my own. Dollar store micro-USB cable, X-Acto knife, 30-watt RadioShack soldering iron, and more burnt fingers than I care to admit.

First time I got a bricked RAZR to show up in RSD Lite after using my janky homemade cable? Better than sex. Well, not really, but my wife was pretty tired of me yelling “IT’S ALIVE!” from the garage at midnight.

## Becoming the Neighborhood Phone Dealer

Here’s how you accidentally start a business: You unbrick one phone at work. Just one. Next thing you know, everyone’s cousin’s girlfriend’s brother is showing up at your door with a Galaxy S3 that’s stuck on the Samsung logo because they tried to flash an AT&T ROM on a T-Mobile device.

My garage became Phone ER. I had milk crates full of USB cables (because Samsung needed different ones than HTC, and don’t even get me started on Sony’s flashtool driver requirements). Three laptops — Windows 7 for Samsung stuff, a beaten-up ThinkPad running Ubuntu for when Heimdall was more reliable than Odin, and a Mac Mini for the occasional iPhone jailbreak.

The money wasn’t bad either. $40 to unbrick a soft brick. $60 if I had to hunt down specific firmware. $100+ if your phone required me to dive into QPST or LGUP territory. I was making more fixing phones on weekends than I was at my day job.

Best customer story? This kid — couldn’t have been more than 16 — shows up with a Verizon Galaxy Note 2. He’d tried to flash an international ROM and killed his IMEI. Phone worked but no cell service. Most shops would’ve sent him packing. Me? I spent six hours teaching myself how to use QPST, found his original IMEI on the box he smartly kept, and rebuilt his EFS partition from scratch. Kid’s mom tried to tip me an extra $100. I took $20 and told her to buy him a backup phone.

## Knox: Samsung’s Middle Finger to Modders

Then Samsung dropped Knox. If you weren’t around for this, imagine Samsung basically putting a tamper-evident seal inside your phone’s bootloader. Trip it once by installing custom recovery or rooting, and boom — WARRANTY VOID 0x1 burned into your bootloader forever. No Samsung Pay. No KNOX apps. No warranty service.

But the modding community doesn’t just roll over and die. When geohot released towelroot (the futex exploit, not the modstring one), we could root without tripping Knox. FOR A WHILE. Samsung patched that shit quick, but there was a golden window where you could have your cake and eat it too.

The real holy grail was bootrom exploits. See, Knox lived in the bootloader, but the bootrom — that’s burned into the chip. Can’t patch hardware. The Galaxy S5 had this beautiful vulnerability where if you timed things just right during boot, you could inject unsigned code before the bootloader even loaded. Samsung couldn’t patch it without replacing every S5 on the planet.

I taught myself ARM assembly to understand how it worked. Not gonna lie, most of it went over my head at first. But when you’re debugging at 2 AM with a crying baby in a bouncer next to your desk, you get really good at reading hex dumps.

## iOS: The Other Side of the Fence

iPhones were different. Android modding was like working on a hot rod — messy but straightforward. iOS jailbreaking was like defusing a bomb where Apple kept changing the wire colors.

evasi0n for iOS 6. Pangu for iOS 7. TaiG dropping untethered jailbreaks like it was Christmas. The drama when certain teams would burn exploits before major iOS releases. The Chinese jailbreaks that came bundled with pirate app stores you had to carefully remove.

I got scary good at putting iPhones into DFU mode. Hold power and home for exactly 10 seconds, release power while holding home for exactly 15 more seconds. Mess up by even a second? Start over. Your computer makes the USB disconnect sound? You’re in. No sound? You’re probably in recovery mode instead, try again.

SHSH blobs, anyone? Back when you could actually downgrade iOS if you saved them. I had a folder with hundreds of blob files for customers’ phones. Apple killed that party eventually, but for a while, you could run whatever iOS version you wanted.

## School: Learning the Why Behind the How

Here’s the thing — I was good at using exploits, but I didn’t really understand them. Like, I knew buffer overflows were bad, but I couldn’t tell you why strcpy was dangerous or what a NOP sled actually did.

Cape Fear Community College. Not exactly MIT, but their InfoSec program was legit. First day of Assembly Language class, professor writes on the board: “mov eax, 1; int 0x80”. I’m thinking “holy shit, that’s a Linux system call for exit!” Half the class is wondering why we’re learning a dead language.

Hardest part wasn’t the material — it was the logistics. Ever try to debug segfaults while bottle-feeding twins? Or write a paper on return-oriented programming while Peppa Pig plays on repeat in the background? My laptop had more formula spills than a daycare center.

But it clicked. That Samsung bootrom exploit I’d been using? Classic stack buffer overflow leading to PC control. The Android property service vulnerability in motofail? Race condition combined with improper permission checking. It wasn’t black magic — it was just C programmers being lazy with bounds checking.

## From Script Kiddie to Bug Hunter

First real bug I found was embarrassing in its simplicity. Popular Android app with 10 million downloads. Had a broadcast receiver that accepted intents with root commands and… just ran them. As system. No validation. Nothing.

Sent a PoC to Google’s VRP. Two weeks later, $5,000 in my account. More than I’d made in two months of phone repairs.

That hooked me harder than custom ROMs ever did. Set up a proper lab — old phones running every Android version from Gingerbread to Nougat. Some with UART cables soldered to the board for kernel debugging. Others with custom kernels compiled with every debug flag enabled.

Started specializing in Android app vulnerabilities. You’d be amazed how many apps with millions of downloads have exported activities with no permission checks. Or content providers that dump their entire database if you query them right. Or — my personal favorite — apps that use predictable values for their “secure” random number generators.

## Today’s Game

Now? I’m hunting bugs in places that make Android look fort knox. IoT devices with hardcoded credentials. Smart home hubs running ancient kernels with known CVEs. Medical devices that accept firmware updates over unencrypted Bluetooth.

Last month, found an authentication bypass in a popular smart doorbell. The API endpoint for viewing video feeds checked if you had a valid session token… but not if that token belonged to YOUR account. Basically, any valid user could watch any other user’s doorbell. Reported it, got paid, they patched it in 48 hours.

But I still keep that original RAZR. Still boots, running LineageOS 14.1 (shoutout to stargo for maintaining that ancient device tree). Sometimes I fire it up just to remember. The screen’s cracked from when I threw it against the wall after the fifth failed kernel compile. The USB port is loose from the thousands of times I plugged it in. But it works.

## What Android Taught Me

Every security system is just a series of assumptions. Find where the assumptions are wrong, and you’ve found your bug. Android taught me that before I knew what threat modeling was.

The community taught me more. Those old XDA arguments about whether governors actually did anything? That’s basically kernel scheduling theory. Fights about whether to use F2FS or EXT4? That’s filesystem design. We were getting computer science educations and didn’t even know it.

To anyone thinking about starting: just start. Grab an old phone off eBay. Something already deprecated, so you can’t make it worse. Learn fastboot and ADB. Brick it. Unbrick it. Brick it again. Each time you’ll understand a little more.

And when you’re sitting there at 3 AM, staring at a bootlooping phone while your family sleeps, remember — you’re not wasting time. You’re learning how technology actually works, not just how it’s supposed to work. That difference? That’s where all the interesting stuff happens.

Now if you’ll excuse me, I’ve got a smart fridge that’s inexplicably running a four-year-old Android kernel with netfilter disabled. The bug bounty on this one’s gonna be good.

Still breaking things. Still learning. Still can’t believe I get paid for this.
