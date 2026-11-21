# Humorous XSS Vulnerabilities in a Movie Website

- **Source URL:** https://medium.com/meetcyber/humorous-xss-vulnerabilities-in-a-movie-website-3600d7828661?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250816232843/https://medium.com/meetcyber/humorous-xss-vulnerabilities-in-a-movie-website-3600d7828661
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8418 (id 8418)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Humorous XSS Vulnerabilities in a Movie Website

Here’s another follow-up article. I’ll be sharing more vulnerabilities I discovered on a popular Turkish movie website, which I mentioned in my previous post. This website attracts mora than **10 million unique** monthly visitors.

Vulnerabilities can sometimes bring huge **surprises**. Although they pose a significant security risk, they can occasionally be a source of amusement.

I want to discuss how the feature that allows users to add movies to their profiles is susceptible to manipulation.

The system’s logic involves creating a new list from the “Create New List” section in the user profile, naming it, and then adding movies and TV series to curate a personalized list. This list is then published on your profile. However, due to a critical oversight by the developers, it’s possible to upload XSS payloads into the list’s title field using a simple trick.

In the first example, I attempted to play an audio file from a remote site — and succeeded. The lack of a character limit for the list title made my task even easier. Using the payload below, I managed to add a funny sound from the [**myinstants**](https://www.myinstants.com/) website.

```
<script>
document.body.addEventListener('click', () => 
    setTimeout(() => 
        new Audio('https://www.myinstants.com/media/sounds/among-us-role-reveal-sound.mp3').play(), 2000), 
    { once: true });
</script>
```
For the sound to play, the user needs to click anywhere on the body of the page. Modern…
