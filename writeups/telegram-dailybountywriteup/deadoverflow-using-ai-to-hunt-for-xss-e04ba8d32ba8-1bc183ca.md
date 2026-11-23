# Using AI to hunt for XSS.

- **Source URL:** https://medium.com/@deadoverflow/using-ai-to-hunt-for-xss-e04ba8d32ba8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240703085550/https://medium.com/@deadoverflow/using-ai-to-hunt-for-xss-e04ba8d32ba8
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6550 (id 6550)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Using AI to hunt for XSS.

Before I start, I must say that the [https://hackrhub.com](https://hackrhub.com) has been updated. In case you don’t know, that is my free platform where I teach people how to hunt for vulnerabilities and more and now you can even hire me to be your personal teacher. There is a free plan on it so make sure to check it out as well!

Socials:

**Instagram**: [https://instagram.com/deadoverflow](https://instagram.com/deadoverflow)

**Youtube**: [https://youtube.com/@deadoverflow](https://youtube.com/@deadoverflow)


# Using AI to hunt for XSS

AI is a powerful tool almost everyone uses nowadays. That’s why I just decided to test and see if AI or ChatGPT can find vulnerabilities. Vulnerability that I choose is XSS since I can give Chat GPT JS code and let him analyze it to see if there are any potential vulnerabilities. So let’s test out the theory and maybe we can prove today that AI can be used as another powerful tool for hacking!

# Testing the AI

I will be using practitioner Portswigger’s labs to see if AI can solve them maybe. I will also be using Chat GPT 3.5 which is a Free version and then comparing it to the Chat GPT 4 which is a paid version to see who will preform better.

# Lab to solve

I will be using the following lab to see if AI is capable of finding vulnerabilities. As I have not solved this challenge myself, this will be very interesting. So let’s just start.

# The challenge

After the lab has loaded there is a search functionality. So let’s test that out. I will copy and paste the JS code to see if AI can find an XSS. The code I will be giving to AI is this:

```
function search(path) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            eval('var searchResultsObj = ' + this.responseText);
            displaySearchResults(searchResultsObj);
        }
    };
    xhr.open("GET", path + window.location.search);
    xhr.send();
    function displaySearchResults(searchResultsObj) {
        var blogHeader = document.getElementsByClassName("blog-header")[0];
        var blogList = document.getElementsByClassName("blog-list")[0];
        var searchTerm = searchResultsObj.searchTerm
        var searchResults = searchResultsObj.results
        var h1 = document.createElement("h1");
        h1.innerText = searchResults.length + " search results for '" + searchTerm + "'";
        blogHeader.appendChild(h1);
        var hr = document.createElement("hr");
        blogHeader.appendChild(hr)
        for (var i = 0; i < searchResults.length; ++i)
        {
            var searchResult = searchResults[i];
            if (searchResult.id) {
                var blogLink = document.createElement("a");
                blogLink.setAttribute("href", "/post?postId=" + searchResult.id);
                if (searchResult.headerImage) {
                    var headerImage = document.createElement("img");
                    headerImage.setAttribute("src", "/image/" + searchResult.headerImage);
                    blogLink.appendChild(headerImage);
                }
                blogList.appendChild(blogLink);
            }
            blogList.innerHTML += "<br/>";
            if (searchResult.title) {
                var title = document.createElement("h2");
                title.innerText = searchResult.title;
                blogList.appendChild(title);
            }
            if (searchResult.summary) {
                var summary = document.createElement("p");
                summary.innerText = searchResult.summary;
                blogList.appendChild(summary);
            }
            if (searchResult.id) {
                var viewPostButton = document.createElement("a");
                viewPostButton.setAttribute("class", "button is-small");
                viewPostButton.setAttribute("href", "/post?postId=" + searchResult.id);
                viewPostButton.innerText = "View post";
            }
        }
        var linkback = document.createElement("div");
        linkback.setAttribute("class", "is-linkback");
        var backToBlog = document.createElement("a");
        backToBlog.setAttribute("href", "/");
        backToBlog.innerText = "Back to Blog";
        linkback.appendChild(backToBlog);
        blogList.appendChild(linkback);
    }
}
```
Now If AI finds an actual vulnerability here then this is amazing and quite useful in real world scenarios. This is too much for Chat GPT to handle therefore I will be giving him function after function to analyze. You could just copy and paste some code that you found on a webpage and **ChatGPT** will handle the rest. So let’s waste no further time and let’s ask AI to help us find a vulnerability here.

# The response

After I asked AI and gave him the context of the function usage, he was able to give me some nonsense.

I was really concerned will Chat GPT even be able to pull through it so I decided to give him a bit of a reality check. I just said to him that putting HTML into eval function is just not gonna do anything really.

Now he was on the right track. He knew that he had to escape the JSON object since it was inside the eval() function to potentially execute some code.

Now he was really close to solve this lab. This is now the problem:

AI was able to escape the JSON object however instead of ; there should be } since this is displayed in the console:

He was really close and I will try to guide him just a bit now by giving him an error to see if he can figure it out.

# The result

Unfortunatly he was not able to get it right. He was so close just one character away from exploiting this and I am so pissed off that it was so close yet so far away. You can see my frustration in the chat here: [https://chatgpt.com/share/bb1274d4-b507-4853-955b-79a490c29505](https://chatgpt.com/share/bb1274d4-b507-4853-955b-79a490c29505)

Chat GPT 3.5 was very close and I will in the next blog post see if Chat GPT 4.0 can do any better. That blog post you will be able to find on my official platform called [https://hackrhub.com/](https://hackrhub.com/). Here is a proof that he indeed was just one character away from solving this lab:

# Summary

AI now cannot do tasks for you without your monitoring and help. That’s why I still recommend you asking AI some things that aren’t quite clear in your head. AI can even lead you into right direction if you are stuck somewhere since it’s better than nothing! In the next blog post I will be seeing how Chat GPT 4.0 can handle it so make sure to check it out tomorrow when it goes out on [https://hackrhub.com](https://hackrhub.com)!
