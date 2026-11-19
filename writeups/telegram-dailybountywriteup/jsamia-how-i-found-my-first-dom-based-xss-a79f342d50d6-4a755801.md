# How I found my first DOM based XSS

- **Source URL:** https://medium.com/@jsamia/how-i-found-my-first-dom-based-xss-a79f342d50d6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251020214713/https://medium.com/@jsamia/how-i-found-my-first-dom-based-xss-a79f342d50d6
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5621 (id 5621)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found my first Reflected XSS

The website we will refer to as target.com, this was a VDP not a BBP unforuntately with a few things on the unfortunate side but we will get into that later.

## Recon

Like always I started out with recon, I am still perfecting my process but for this one we started by looking for sub-domains. I like to use crtsh.py as well as subfinder. I save both of these to the same list, then run a quick python script to remove duplicates. I was feeling extra lazy so I had ChatGPT create this for me, feel free to use it. I will eventually update this myself and post it on my GitHub (now posted, link at bottom)

```
def remove_duplicates(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    # Removing duplicates
    unique_lines = list(set(lines))
    with open(input_file, 'w') as f:
        f.writelines(unique_lines)
if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")
    remove_duplicates(input_file)
    print("Duplicates removed successfully in the input file!")
```
Once I had the cleaned up list, I ran httpx

./ httpx -l targetStart.txt -status-code -title


I like to run a few other things as well, but for the sake of this story it isn’t neccessary. Usually it’s helpful to manually check out quite a bit, if not all of the domains and sort it into my own notes, doing so, I stumbled upon *sub.target.com*

On this site there are statistics, articles, and a search. I quickly inputted “XSStest” in the search to see if the parameter was reflected, but it wasn’t, so I moved on. I then wanted to play around with what happens when I click on some stats, so thats what I did and intercepted it with Burp.

This is the request, which has a significant amount of spots we can try to inject a payload into, so I sent into the repeater.

In the repeater, the XSS won’t actually pop-up when you hit render but, in this case it was very obvious still. I decided to start simple and replace the name parameter and put in a basic payload:

`<script>alert(1)</script>`
This is what the response was, clearly this is not the normal response, I then copied the link over to my browser and noticed no payload was going off so I decided to inspect it.

When inspecting I noticed it was being reflected in 3 different spots! One of which was in a \<script> like

```
<script> 
  var queryString = {"data":"data", "data2":"data2", "name":"<script>alert(1) 
</script>
```
I realized all I had to do was close that script tag at the start so I added that to my payload :

`</script><script>alert(1)</script>`
The final link looked like:

`sub.target.com/data?data=123&data2=456&name=</script><script>alert(1)</script>`
I then submitted this to the VDP, this is where it went a bit sour sadly. Once reported the next day they got back to me saying the scope was updated at some point during the day of discovery and XSS is not accepted, along with a large list of other vulnerabilites. This was frustrating due to when it was found nothing in the scope had mentioned this, but theres only so much you can do, I thanked the person from the bounty website and moved on.

Being an unpaid program it wasn’t worth trying to elevate the bug to something else or arguing, it was at least good practice and I am hoping they still fix it.

Thank you so much for reading, don’t forget to follow and clap if you enjoyed/learned anything!

Duplicate remove: [https://github.com/JSamia36/RemDup](https://github.com/JSamia36/RemDup)
