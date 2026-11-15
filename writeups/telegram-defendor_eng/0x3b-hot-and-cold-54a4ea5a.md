# 🔍 The "Hot" State Is the Most Underrated Edge in Security Research

- **Source URL:** https://paragraph.com/@0x3b/hot-and-cold
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1638 (id 1638)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
If I ask you what is the most important way to improve your auditing **right now** what will you say? Maybe you would say to try different methods like to audit top to bottom, or follow user flows,  or tell me to try AI or the most common - "just read code".

What I would say is to **audit while hot**, so go and increase your AC temperatures, because it will help!

go on, do it before you continue reading, just trust me

...

Now for all of you who trusted me, thanks... and **never trust anyone** (especially me) because that's not what I meant by auditing hot.

By auditing hot I mean to have X time of auditing (be it a few hours or a day or 2) before you are "hot", and when you are hot you would notice an improvement in your ability to understand and break code.

This may seem a bit off topic, but trust me it's important to know it.

In sales you have the term "hot" and it's when your sales guy gets into the mood of selling and he is performing at it's best. His close rate increase, by 20%, 30% sometimes 50% or even 2x and he becomes a "selling machine".

But why is that?

There are multiple factors and multiple prerequisites in order for this to happen, each playing a different role. But it usually goes like:

1. Bob has a good sales call, he feels confident in the product and himself
2. He tries to sell the product a bit more, he asks more questions and fights more no's
3. Bob gets the sale
4. Bob is now even more confident in what he is doing, he truly knows he is doing gods work
5. You can notice that in the tone he uses, the words, the amount of questions he ask, the hunger to make the sale

Where am I getting with this...?

Well it is the same here, usually how it goes is:

1. You find something interesting
2. You think it's an issue and you start diving deeper
3. You find a High or an interesting Med and adrenaline hits you
4. You are now more curious and start looking further and further
5. You find a few more interesting edge cases, the spiral continues

Sounds familiar ?

Do you know how to ruin your streak? Take a break after the first finding since "you've earned it". And if you are the one that would take the break, then try not to do it

Similarly you may have noticed that if you break your audit with a break for 2 or maybe 3 days then the code feels off, the issues don't pop out, you are slower or even tired. You think to yourself "I've already looked at this" or even if you dive deeper it still takes you more time (to find something interesting) than before the break.

Maybe it's my terrible memory, but if you have felt this after taking a few days off then you know exactly what I mean. The context you built up in your head - the relationships between contracts, the assumptions you were questioning, the edge cases you were tracking - all of it fades. And rebuilding that context is never as fast as building it the first time.

But do you know what the worst part is? Some of those questions you had in mind before the break, you may have explored them to a point and your brain will think they are answered... however that is never the case. The hard to find, interesting bugs come from constant back and forth pushing between you and the code.

You go for the bug, but X stops you, you try another path, but Y stops you, you try to configure Y and move past it and you do, but Z stops you... The difference between finding something rare and thinking this path is secure is the ability to push forward, challenge obstacles and overcome them.

A junior will check and step after the first require or if. A senior will always try to find a way to move past it. And due to this "break" your brain may think that since X was there then this bug is invalid...

So the advice here is simple. Don't take multi-day breaks during an active audit. If you have a 2-week audit, treat it like a 2-week sprint, not a marathon with rest stops. The "hot" state is fragile, and a 3-day break in the middle can cost you more time than the break saved you.

So I just told you not to take breaks, but let's be real... You probably can't audit for 2 weeks straight without breathing (unless you are like me of course, cuz I am better). You are a human, not a machine. So how do you take a break without killing your streak?

Half days.

Wake up early, get your focused hours in while your brain is fresh and you actually have the will to do it. This is when you are sharpest. No distractions, no fatigue, just you and the code.

After that, the rest of the day is yours. Go outside, touch some grass (or women, consensually of course), do whatever you want. If someone sends you a message you can always respond, but don't go opening Cursor and start verifying that edge case "real quick". That's not a break, that's a half ass audit session.

Why mornings? Because your brain is fresh and you actually want to work. Try auditing at 9pm after a full day of hiking or going out. You'll be reading the same function 3 times and still not getting it. Your focus is a limited resource, spend it when you have the most of it.

This is where it all comes together.

When you find your first bug in a codebase, something shifts. Before that first finding, you're reading code. After it, you're hunting. The code is no longer "probably fine", it's proven to be breakable. And if it broke once, it can break again.

That's the confidence boost that makes you hot. You stop giving the developer the benefit of the doubt. You stop skimming over that weird edge case because "they probably handled it". You start pulling on every thread because you've already proven that threads lead somewhere. You start digging deeper and deeper and maybe coming back to old invalid issues with a new knowledge of how everything moves around.

The more bugs you find, the hungrier you get. Bug number one makes you curious. Bug number two makes you suspicious. By bug number three you are looking at every function like it owes you money. The code didn't change, you did.

This is why auditing while hot matters so much. It's not about being smarter or knowing more. It's about being in the state where your confidence and curiosity are both maxed out, and every line of code feels like it's hiding something from you.

Next time you find something interesting, don't reward yourself with a break. Reward yourself by going deeper. That first finding is not the finish line, it's the starting gun.

Stay in the code. Stay suspicious. Stay hot.

**Because at the end of the day, it's not how many bugs you find. It's how many are left after you.**

Thanks for reading this far and as always a shameless plug:

Founders and builders if you are looking for an audit you can check us out at: [https://phagesecurity.com/](https://phagesecurity.com/)
