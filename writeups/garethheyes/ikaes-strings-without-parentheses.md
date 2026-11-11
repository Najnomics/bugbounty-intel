# ikaes-strings-without-parentheses

- **Source URL:** https://blog.ikaes.de/generating-strings-without-parentheses-in-javascript/
- **Fetched:** 2026-11-11
- **Researcher:** garethheyes
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

# generating strings without parentheses in javascript

everyone knows [js fuck](https://github.com/aemkei/jsfuck) - the javascript trick to generate arbitrary strings and code without using any alphanumeric characters.

in this article i will present how to achieve the exact opposite - a way to generate arbitrary strings in javascript without using any special characters (except `+`,`=`, `,` and `.`)

## abusing errors

this trick heavily relies on the `Error` function and error objects, so first we need to recap errors in javascript.

### anatomy of the error

an error in javascript consists of a `name` and a `message`. the `name` is typically something like `ParseError` or `SyntaxError`, … while the `message` is the actual error message.

these values are used in the `toString()` function of the `Error` object, which overrides the `Object.prototype.toString()` function.

we can see that it essentially just returns the `name` and `message`. we can set arbitrary values to these variables by overwriting the prototype.

that way, the `toString` function becomes just the constant function of the `name` or `message` if either one is not defined

this is how the actual javascript payload was snuck into the `Function` body in my [discovered way to invoke arbitrary functions in javascript](https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/).

it will become relevant later that `Error.toString` is not the same as `Error.prototype.toString`, since `Error` refers to the error function and `Error.prototype` to the error object.

### looking inside the stack trace

the `Error` function has a member function `prepareStackTrace` which is meant to format stack traces. i showed in [my previous article](https://blog.ikaes.de/yet-another-way-to-invoke-functions-without-parentheses/) how it can be used to generate arbitrary javascript functions.

it turns out it is not the only superpower this function provides.

in order to understand how we can bend the function to our will, we must know more about how it actually works.

the following function can be used to peek inside `prepareStackTrace`

```
Error.prepareStackTrace = function (...args) {
  console.log('--- prepareStackTrace called ---');
  console.log('this:     ' + typeof this + ' -> ' + inspect(this));
  console.log('argCount: ' + args.length);
  args.forEach((a, i) => console.log(`arg${i}:     ` + typeof a + ' -> ' + inspect(a)));
  return 'this becomes the stack'; 
};
```
this is what the function outputs after we run it with a generic error and access its stack

### what is this?

`prepareStackTrace` is called on each error instance upon accessing the `stack` attribute. its `this` is simply the global `Error` function. it makes sense, because `prepareStackTrace` is a member of this function

we can confirm this by overwriting the functions’ `toString` method. we also see many invocations of `prepareStackTrace` after overwriting the `toString` function, but it’s just the browser console throwing errors in the background while i typed out the function.

### other arguments

the remaining inputs are, as per the documentation, the thrown error and the ‘structured stack trace’, which is essentially an array. we can confirm this by overwriting their respective `toString` methods

### all together

putting the information we have about the inputs of the `prepareStackTrace` function, we see that it can essentially be rewritten as

```
(prepareStackTrace).call(Error, e, Array)
```
which is great because it seems that it would allow us to invoke 2-ary functions without parentheses on an object!

## there is no free lunch

sadly, as with most cool exploits, we can not abuse this possibility of invoking arbitrary functions in every scenario. as we saw before, it is possible to influence what is accessed within the function, by modifying the default `toString` methods of the inputs’ prototypes,. this trick sadly does not always work.

consider the following example:

here we overwrite `prepareStackTrace` with the `String.prototype.concat` function. all other functions which we hooked before also have a `console.log` statement which confirms that the respective `toString` function is indeed invoked.

and as we see, each function is invoked and `this` together with the two arguments are indeed concatinated. this happens because we’re in a `String` “context” which invokes `toString` internally.

now look what happens if we use a different prototype

when passing our elements into an `Array` function, the `toString` functions are not invoked.

sadly there is not much we can do to inject our functions in this, or any other context. one option would be to use a `Proxy`, however we can not define a custom `get` function without using parentheses.

## pulling the strings

luckily for us, this scenario is enough to generate arbitrary strings. after all, the only object we need is `String` and using the trick above we can essentially call every function of the `String` prototype.

the general idea of the trick is to construct a `Strings.fromCharCode` expression which will return our wanted string from numbers. this expression can be injected into a `Function` constructor, which can be invoked without parenthesis. our new function will then return our desired function.

that way we only have to worry about generating numbers, some letters and special characters to generate the expression, rather than ripping all characters manually.

### getting what we need

in order to construct our generator expression, i used some established tricks to getting arbitrary characters from [jsfuck](https://github.com/aemkei/jsfuck/blob/main/jsfuck.js).

for example, we can get the brackets or parentheses by invoking the `toString` on any functions and getting the respective indices

while this works on paper, you notice that it will not work in our scenario, because we’re not allowed to use brackets.

luckily we can use a workaround for this:

- we can first transform a string into an array of characters
- and then get elements at arbitrary position using the `shift` function.

### string to array

we need to figure out how to split a string into an array. this is where `prepareStackTrace` trick comes to play!

as we saw before, we can use `prepareStackTrace` to invoke any `String` function and pass string arguments to it by overwriting the `toString` methods of the `Error` function, an `Error` object and the `Array` prototype.

in this case, the return value of `Error.toString` is our `this`, i.e. the string which will be splitted, `toString` of our error will be the delimeter, and return value of `Array.prototype.toString` will be the optional limit, which must be an integer.

generally, to split a string into an array we need an expression like this:

```
String.prototype.split.call('our string', '', -1 or n>length of our string)
```
as we see, two new challenges emerge - we need an empty string, and a number greater than the length of our string or -1.

luckily, these values very easy to get with the help of the `Array` prototype.

finally we arrive at the following code snippet:

```
// set message and create a constant string
delete Error.name;
Error.message = "no params here" ;
Error.toString = Error.prototype.toString;
// set the 2nd parameter to -1 
Array.prototype.toString = Array.prototype.lastIndexOf;  
// overwrite prepareStackTrace
Error.prepareStackTrace = String.prototype.split;
// create the new error instance
err = new Error;
// set the first parameter to ''
err.toString = Array.prototype.join;
// invoke String.prototype.split.call
result = err.stack;
```
### shift at work

our goal is to create an expression which does not use any parentheses or brackets which returns an arbitrary index of an array. something like this `arr[i]` .

it turns out that it is actually quite simple and the `Array` prototype brings a method which does almost exactly what we need

by calling shift a few times in a row, we can eventually get to the character of the string which we need. obviously the above example is illegal in our scenario, but we can use the `valueOf` trick to invoke `shift` without parentheses

if we want to get other values than numbers, we need to implicitly convert the return value to a string by adding it to an empty string. we can get it from a dummy object with its `valueOf` function overwritten by `Array.prototype.join` . here as an example i choose `BigInt`, but it can be any object.

### numbers

now we have everything we need for our generator expression and all is left is to fill it with charcodes.

to generate arbitrary string integers, we can again use the `Array.prototype.indexOf -> -1` trick to generate arbitrary digits.

for example, we can generate a zero by subtracting the `Array.prototype.indexOf` return values from each other, since it results in `-1 - -1 = 0` . we can subtract further `toString()` expressions to eventually get all digits

then all is left is to convert the digits to a string. this can be done by using our another `Array` trick - `Array.prototype.join → ''` .

finally we end up with the following code snippet which generates all digits as strings

```
// initialize any object (here for example Set) 
x=Set,x.toString=Array.prototype.indexOf,
// generate all integer digits
a=x+-x,b=a+-x,c=b+-x,d=c+-x,e=d+-x,f=e+-x,g=f+-x,h=g+-x,i=h+-x,j=i+-x,
// overwrite valueOf to return an empty string
x.valueOf=Array.prototype.join,
// convert all digits to strings
a+=x,b+=x,c+=x,d+=x,e+=x,f+=x,g+=x,h+=x,i+=x,j+=x
```
## all together

finally, combining the techniques described so far, the final trick to generate arbitrary strings without using parentheses is as follows

1. we obtain the characters necessary for the `fromCharCode` decoder using jsfuck tricks
2. to get the characters we first split the strings using the `prepareStackTrace` method
3. and then use `shift` to get the individual characters
4. we combine the obtained characters into the following expression
5. `return String["fromCharCode"](65)`
6. then we inject it into the `Function` constructor and get a constant function which returns our desired string

the final payload is quite long and hard to read, and honestly not spectacular, so i will not go into the details of how every step is achieved. the full commented code and a generator function is available at [my github repository](https://github.com/skarn958/no-param.js) and in the source code of this article.

you can use the `generate_payload` function to generate payloads which generate your desired string.

## executing javascript without quotes

we can take the trick further and instead of generating random strings, we can execute arbitrary code by evaluating our payload instead of just returning it.

the adjusted payload simply passes the charcode-encoded javascript into `eval` instead of returning it.
