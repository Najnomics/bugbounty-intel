# How I use to find vulnerabilities like XSS,sqli  using mixture of 3 simple tools

- **Source URL:** https://medium.com/@sreejihkn43073/how-i-use-to-find-vulnerabilities-like-xss-sqli-using-mixture-of-3-simple-tools-5108068646d2?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@sreejihkn43073
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6204)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### *How I use to find vulnerabilities like XSS,sqli using mixture of 3 simple tools*

*Hi hunters ! this is sreejith here today i am going to share to you how to find xss vulnerabilities in a web application using 3 awesome tools :*

*for more queries :*

*Follow on instagram :@sr33jith\_4\_4*

*follow on linkedin :linkedin.com/in/sreejith-kn-174b991b8/*

*Before get into it i will give you small tip to make your bug hunting easy*

*create a new directory for every target you are pentesting so that you can access the resouces and not only that it will be easy for you to analyse in future*

*Now lets get on with installation and usage of each tool and first one is,*

#### *1). PARAMSPIDER :*

#### *About:*

*paramspider allows you to fetch URLs related to any domain or a list of domains from Wayback achives. It filters out URLs, allowing you to focus on the ones that matter the most.*

*ParamSpider is a python script which is used to find parameters from web archives of the domain. Also it could mine parameters from the subdomains as well.*

*Lets see how to get it installed and its usage. It might be useful for your bug hunting journey.*

#### *INSTALLATION:*

*First clone the repository ,*

git clone https://www.github.com/devanshbatham/ParamSpider

*Then we can move on to the directory to view the contents,*

cd ParamSpider

ls

*There is a requirements.txt file which specifies the modules needed to run the script. Lets take a look at it.*

cat requirements.txt

*If you have these python modules installed, go ahead and skip the following step, but it doesn’t hurt to run the commands though you have these installed.*

pip install -r requirements.txt

*And yeah, everything is set and now we may run the python script.*

#### *python3 paramspider.py*

*Now let get on with next tool ie,*

#### *2). qsreplace:*

#### *About*

*Accept URLs on stdin, replace all query string values with a user-supplied value, only output each combination of query string parameters once per host and path. using the qsreplace tool you can encode in the payloads and all*

#### *INSTALLATION :*

*To install qsreplace tool first you need to install go language in your kali,*

*clone the repository*

git clone https://github.com/tomnomnom/qsreplace.git

*After that paste the below code and run it*

▶ go install github.com/tomnomnom/qsreplace@latest

*Now lets go on to next tool that is*

#### *3). freq*

*This is go CLI tool for send fast Multiple get HTTP request.*

#### *INSTALLATION :*

go get -u github.com/takshal/freq

or in latest version of go you can use below command

go install github.com/takshal/freq@latest

*Using qsreplace you can add your xss payload in every paremeter then you can use this tool to find vulnerablity.*

*Now lets begin how i automate the attack.*

*1 .For that i am using the domain called skullcandy.in*

*using the paramspider i collected the urls of the domain skullcandy.in and make a output as you can see below*

*2. now using the tool qsreplace you can encode the with in the all listed urls of the target domain of the endpoints*

cat www.skullcandy.in.txt| qsreplace 'payload ' | tee xss.txt

*for example i am using cat www.skullcandy.in.txt| qsreplace ‘“>\<script>alert(1)\</script>’ | tee xss.txt*

*And the output will be as shown below*

*now is the time to use last tool called freq*

cat xss.txt | freq | tee -a possible-xss.txt

*it will send multiple http request as a crafted payload*

*As you can see there is vulnerable endpoints in the target that i mentioned*

*I hope this blog help you well for your future and in bug hunting ,*

*Hope you would have learned some information from this blog if so, kindly press that follow button for further updates. Best wishes from sreejith kn .❤️*

**FOLLOW FOR MORE UPDATES**

thank you
