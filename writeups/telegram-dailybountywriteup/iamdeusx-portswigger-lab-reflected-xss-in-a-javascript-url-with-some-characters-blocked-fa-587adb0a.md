# Portswigger Lab

- **Source URL:** https://medium.com/@iamdeusx/portswigger-lab-reflected-xss-in-a-javascript-url-with-some-characters-blocked-fa15ae95d90e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241102224000/https://medium.com/@iamdeusx/portswigger-lab-reflected-xss-in-a-javascript-url-with-some-characters-blocked-fa15ae95d90e
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7694 (id 7694)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Portswigger Lab: Reflected XSS in a JavaScript URL with some characters blocked

Lab description: This lab reflects your input in a JavaScript URL, but all is not as it seems. This initially seems like a trivial challenge; however, the application is blocking some characters in an attempt to prevent [XSS](https://portswigger.net/web-security/cross-site-scripting) attacks.

To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function with the string `1337` contained somewhere in the `alert` message.

I was able to understand the concept behind solving this lab thanks to [z3nsh3ll’s](https://www.youtube.com/watch?v=bCpBD--GCtQ&list=PLWvfB8dRFqbZG5cw2OrnEmzSzorxRuxFV&index=27) explanation on YouTube, so huge shout out to him.

Here is the payload used to solve the lab, but how does this even work. I will try my best to explain that in this post.

`&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`
# Detecting the XSS vulnerability

First thing to do is to detect where the XSS vulnerability is on the website.

Well from the name of the lab we already have an idea of it being in the URL. Viewing any post on the site, we can see how the URL adds a **postId** parameter which accepts a value.

Looking at the page source for where the **postId** parameter is reflected.

`<a href="javascript:fetch('/analytics', {method:'post',body:'/post/postId=5'}).finally(_ => window.location = '/')">Back to Blog</a>`
The ‘Back to Blog’ button at the bottom of the page is inside of an anchor tag, and this anchor tag has a href attribute which uses JavaScript fetch API to send a post request to the endpoint **/analytics** and then finally redirects the user to the home page **/****/post/postId=5****javascript:**

# Escaping the fetch API argument

Next up is to try and see if there are any filters to worry about and how our input will be reflected.

This is the reason the payload starts with an `&` . Next up is to escape the `{` and `'` .

The fetch API accepts 2 arguments, One is required and the other is optional. The first argument is path to the resource you want to fetch, in this case `/analytics` the second is argument is an array of properties like the Method (e.g GET, POST, PUT etc.), Headers, Body etc.

We have effectively escaped the second argument. Which means our actual payload will be contained in the subsequent arguments. But that raises the question, doesn’t the fetch API only accept 2 arguments? How can we supply more than 2 and still get it to execute our payload?

Now traditionally we can only add 2 arguments to the fetch API but we can actually add more by just separating all the arguments by a comma.

`fetch('/path', {method:'post',body:'hello'}, argument3, argument4, ...)`
And these arguments can even modify the code like for example reassigning a variable.

so after escaping the `'`and `}`, we can separate it by a comma and start injecting our malicious JavaScript code as arguments to the fetch API

`/post?postId=1&'},argument2,argument3`
The next part of the payload is this

`x=x=>{throw/**/onerror=alert,1337}`
# The throw Statement

The `throw` statement allows you to create a custom error. It’s a statement that **throws an exception**. The exception can be a JavaScript String, a Number, a Boolean or an Object.

Using the throw statement

This will log an error 1337 in the console

The throw statement will also only return the last value passed to it.

We can see it logs 1338 and doesn’t display 1337. We can pass as many values in the throw statement and only the last one will be returned. Which means we can use the other values to perform other functions we want.

For example:

Here we are assigning the variable `var1`, the value of `1339` and passing it as the last argument to the throw statement. This value is then logged as an error by the console.

What happens when we reassign the variable `var1` inside the throw statement?

`var1` was reassigned from `1339` to `1000` and the error logged was `1000` and not `1339` . So even though the throw statement only logs the last argument, the rest can still be used to do things like variable reassignment.

This brings us to this portion of the payload

`throw/**/onerror=alert,1337`
The `onerror` in JavaScript is an event handler and `alert` is a function to create pop-ups on a web page. The first value being passed to the throw statement is `onerror=alert` and the second is `1337` . We already know that the throw statement will always execute the last argument, but the other arguments can still be used for assigning values. The `/**/` is used to create a space using comments due to the fact that we can’t use actual spaces because they’ll get filtered out. The `onerror` attribute is used for handling errors and in this case it is going to override part of the throw statement’s behavior and execute whatever it was given, which is the alert function in this case. The `onerror` attribute normally has it’s own behavior towards handing errors but this time we are setting it’s behavior to be an alert pop-up. So now instead of throwing the error to the console like the regular throw statement would, this time it’ll pass the error to the alert pop-up.

For example:

The variable `var1` is assigned a value of `1339` while `onerror` is assigned the value of alert. The throw statement has 2 arguments `onerror` and `var1`. When the error is thrown, it’ll be passed to the alert function and pop-up the value of of the last argument `var1` which results in:

# Arrow function in JavaScript

The next part of the payload to discuss is the arrow function.

`x=x=>`
Regular function in JavaScript:

Here we have a function called add that accepts 2 parameters `a & b` and returns the addition of these parameters. The function is then called `add(1,3)` , and the result is logged to the console `console.log` .

Arrow functions allow us to write shorter function syntax. For example, the above function can be written as this in arrow function:

`let add = (a,b) => a + b;`
We can display the result using console.log

Going back to our payload

`x=x=>{throw/**/onerror=alert,1337}`
The name of the function in this case is `x` and we are giving it a parameter `x`, the `x` parameter is not actually used, but it allows the function to be executed when needed. Then the last portion is the content to be executed by our function when it is called.

This is how the payload would look like in a proper format

The function is being called at the end `x();` .

The problem though with the code above is that the brackets `(x)`are going to be filtered out or blocked which was discovered after some testing.

So they can be removed and it’ll still be a valid function

We are almost at the end. The next section to discuss is the `toString` method.

# toString in JavaScript

`toString=x`
toString is a method in javascript that converts a datatype to a string. We are overwriting this method and setting it to the function `x` which contains our payload.

rather than calling the function `x` , we are assigning the function to the method `toString` and calling the it at the end.

Now why are we using the `toString` method? When does JavaScript make use of the default `toString` method?

Because when the method is actually used, our function will be executed and so will our alert pop-up.

Well that brings us to the next part of the payload

# window+’’

The `window` object is supported by all browsers. It represents the browser's window.

The reason it’s being used in our payload is this, the window object is concatenated with an empty string `window+’’`. In JavaScript, when you use the `+` operator with a non-string value `window` and a string `''` , JavaScript will try to convert the non-string value `window` into a string and this will cause JavaScript to invoke or make use of the `toString` method. Remember the `toString` method has been assigned to the function `x` which stores our XSS payload to pop an alert, so when the method is called our payload gets executed.

For example:

Instead of calling the function using \`toString()\`, we use the \`window + ‘’\` to make javascript call the toString method automatically executing our payload.

Finally, the last portion of the entire payload

`{x:'`
is just to close out the function to prevent any errors from occuring.

putting it all together

`&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:'`
It triggers when we click on the `Back to Blog` button because that is where it is reflected

Thanks for reading, hope you enjoyed it. Stay tuned for more 🫡
