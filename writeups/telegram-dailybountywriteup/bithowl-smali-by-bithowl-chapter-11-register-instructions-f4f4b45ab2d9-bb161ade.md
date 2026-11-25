# Smali By bithowl

- **Source URL:** https://medium.com/@bithowl/smali-by-bithowl-chapter-11-register-instructions-f4f4b45ab2d9
- **Fetched from:** https://medium.com/@bithowl/smali-by-bithowl-chapter-11-register-instructions-f4f4b45ab2d9?source=rss-87ac1fc88e11------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14917 (id 14917)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** bithowl / Sat, 19 Sep 2026 05:31:01 GMT

**“Follow the Data”**

In the previous chapter, we learned what can live inside a register.

We saw:

v0 → int

v1 → String reference

v2/v3 → long

v4 → object

v5 → array

But there is a new question.

**How does data actually move around?**

Imagine you’re investigating a suspicious Android application.

You find this:

String token = “SECRET\_TOKEN”;

Easy.

But the real application might not look like that.

Instead, Smali might show:

const-string v0, “SECRET\_TOKEN”

move-object v1, v0

invoke-static {v1}, Lcom/example/Auth;->send(Ljava/lang/String;)V

Now you need to answer:

Where did the token come from?

Which register contains it?

Where does it go next?

Does it reach the network?

Does it reach an authentication decision?

This is where **register instructions** become extremely important.

**# The Story The Warehouse Conveyor Belt**

Imagine an enormous warehouse.

There are thousands of boxes.

Each box has a small number: BOX 0, BOX 1, BOX 2, BOX 3, BOX 4

These are your registers. Now imagine workers moving boxes around.

One worker says: “Take whatever is in Box 0 and put it in Box 1.”

That’s: move v1, v0

Another worker says: “Put this new object into Box 2.”

That’s: new-instance v2, Lcom/example/User;

Another says: “Take the value from this object’s field and put it into Box 3.”

That’s: iget v3, v2, Lcom/example/User;->id:I

And another says: “Take Box 3 and put its value back into the object’s field.”

That’s: iput v3, v2, Lcom/example/User;->id:I

So Smali instructions are basically the **warehouse workers**.

Registers are the **boxes**.

Your job as a bug hunter?

**Follow the box.**

**# What Are Register Instructions?**

Register instructions manipulate the values stored in registers.

They allow Android code to:

The important idea is:

Data → Register → Instruction → Register → Method → Register

Once you understand this flow, Smali becomes much easier to read.

**1. move**

Let’s start with the simplest instruction.

move v1, v0

Meaning: Copy the value from v0 into v1.

For example:

const v0, 0x2A

Conceptually:

Before:

v0 = 42

v1 = ?

After:

v1 = 42

Notice something important. move **copies** the value. It does not empty v0.

So:

v0 → 42

v1 → 42

Both registers now contain the value.

**# move Is Your First Data-Flow Clue**

Suppose you discover:

const v0, 0x1

move v2, v1

move v3, v2

A beginner might see four unrelated instructions.

A bug hunter sees: 42?

Actually, here:

v0 = 1

↓

v1 = 1

v2 = 1

v3 = 1

The value is travelling through registers.

This is called **data flow**.

**2. move-object**

Objects use: move-object

Example: move-object v1, v0

Meaning: Copy the object reference in v0 into v1.

const-string v0, “hello”

Now:

v0 → “hello”

v1 → “hello”

Technically, for objects and strings, the register holds a **reference**, not the entire object.

That’s an important distinction.

**# move vs move-object**

Think:

move

normal 32-bit value

move-object

object/reference

might move an integer.

While: move-object v1, v0

might move:

String

User

Activity

Context

Array

Exception

and other reference types.

**3. move-wide**

Now we reach wide values. Remember Chapter 10? long and double use **two register slots**.

Example:

const-wide v0, 0x1122334455667788

The value occupies:

v0 + v1

To move it:

move-wide v2, v0

v0/v1 → long value

v2/v3 → same long value

That’s why you don’t use normal move for wide values.

**4. move-result**

This one is extremely important.

Imagine Java:

int result = calculate();

Smali might look like:

invoke-static {}, Lcom/example/Calculator;->calculate()I

move-result v0

The first instruction calls the method.

The second retrieves its result.

method()

result

v0

means:

Take the result returned by the previous method invocation and place it in v0.

**# The Important Rule**

move-result normally follows an invocation.

invoke-static {}, Lcom/example/Auth;->check()Z

The method returns:

boolean

because:

()Z

() → boolean

So now:

v0 = true/false

This becomes extremely interesting for bug hunting.

**# Security Decision Example**

Suppose you see:

invoke-static {p0}, Lcom/example/Auth;->isLoggedIn(Landroid/content/Context;)Z

if-eqz v0, :not\_logged\_in

Follow the data:

isLoggedIn()

move-result

if-eqz

security decision

That’s exactly the kind of flow a bug hunter wants to identify.

**5. move-result-object**

What if the method returns an object?

Java:

String token = getToken();

Smali:

invoke-static {}, Lcom/example/Auth;->getToken()Ljava/lang/String;

move-result-object v0

Here:

getToken()

String reference

Because the return type is:

Ljava/lang/String;

we use:

move-result-object

**# Example: Token Tracking**

Imagine:

invoke-static {}, Lcom/example/Session;->getToken()Ljava/lang/String;

invoke-static {v0}, Lcom/example/Network;->send(Ljava/lang/String;)V

Your eyes should immediately notice:

send(v0)

You’ve discovered a potential **token data flow**.

That’s far more useful than simply reading individual instructions.

**6. move-result-wide**

What if the method returns a long or double?

long timestamp = getTimestamp();

invoke-static {}, Lcom/example/Time;->getTimestamp()J

move-result-wide v0

The J tells us:

long

Therefore:

move-result-wide

is used.

The result occupies:

**7. const**

Now let’s create values.

This places a constant integer value into v0.

Another example:

const v0, 0x0

v0 = 0

You will see these everywhere.

**# Security Flags Hide Here**

followed by:

if-eqz v0, :disabled

The register contains:

1

which may represent:

enabled

true

allowed

authenticated

debug mode

feature enabled

But don’t assume the meaning from 1 alone. You need to trace where the value is used.

That’s an important reverse-engineering habit:

**Don’t guess what a value means. Follow its data flow and context.**

**8. const-string**

This is one of the most interesting instructions for Android bug hunters.

const-string v0, “admin”

v0 → “admin”

Another:

const-string v1, “https://api.example.com"

v1 → URL

const-string v2, “Authorization”

v2 → HTTP header name

**# Why Bug Hunters Love const-string**

Because strings often reveal application behaviour.

Search for:

http

https

api

token

password

secret

Authorization

Bearer

admin

debug

internal

You may discover:

const-string v0, “https://api.example.com"

const-string v1, “Authorization”

const-string v2, “Bearer “

Then follow those registers.

const-string v0, “Bearer “

move-result-object v1

v0 → “Bearer “

v1 → token

The next instructions may combine them.

That’s where the investigation gets interesting.

**9. new-instance**

Now let’s create an object.

User user = new User();

new-instance v0, Lcom/example/User;

v0 → new User object

Usually you’ll then see a constructor invocation:

invoke-direct {v0}, Lcom/example/User;->\<init>()V

new-instance

object created

constructor

object initialized

**# Why new-instance Matters**

When reverse engineering an app, object creation tells you where important structures are born.

You may see:

new-instance v0, Lcom/example/ApiClient;

or:

new-instance v1, Lcom/example/User;

new-instance v2, Ljava/net/URL;

These are clues about what the application is doing.

**10. iget / iput**

Now we access object fields.

Suppose Java contains:

String token = user.token;

iget-object v0, v1, Lcom/example/User;->token:Ljava/lang/String;

Break it down:

iget-object

read an object field

destination register

v1

object register

User;->token

field being read

v1.user.token

**# iget = Read Instance Field**

Object

field

register

iget v0, v1, Lcom/example/User;->id:I

Means approximately:

v0 = v1.id;

For an object field, you’ll commonly encounter the object form:

For wide fields, corresponding wide forms are used.

**# iput = Write Instance Field**

Now reverse the direction.

user.token = token;

iput-object v0, v1, Lcom/example/User;->token:Ljava/lang/String;

object field

v0 → token

User.token

**# This Is Extremely Useful for Data Tracking**

Suppose:

const-string v0, “SECRET”

You can trace:

“SECRET”

Later:

iget-object v2, v1, Lcom/example/User;->token:Ljava/lang/String;

v2

The value has travelled:

const-string

iput-object

That’s the kind of chain you want to build during reverse engineering.

**11. sget / sput**

What if the field is static?

String token = Session.token;

sget-object v0, Lcom/example/Session;->token:Ljava/lang/String;

This means:

Read a static field.

**sget = Read Static Field**

Static Field

Register

sget v0, Lcom/example/Config;->DEBUG:I

v0 = Config.DEBUG;

**sput = Write Static Field**

sput-object v0, Lcom/example/Session;->token:Ljava/lang/String;

Session.token = v0;

Now the flow becomes:

Session.token

**# Instance vs Static Fields**

Remember this simple rule:

**Instance field**

Belongs to an object:

iget

iput

user.token

**Static field**

Belongs to a class:

sget

sput

A simple mental model:

INSTANCE

│

└── field

STATIC

Class

**# The Real Skill: Follow the Data**

Knowing individual instructions is useful.

But memorizing instructions isn’t the real goal.

The real goal is:

**# DATA-FLOW ANALYSIS**

Suppose you find:

invoke-static {v1}, Lcom/example/Network;->connect(Ljava/lang/String;)V

Don’t read it as three separate lines.

Read it as:

URL

connect()

That’s the mindset.

**# Bug Hunter Example #1 — Password**

const-string v0, “password123”

invoke-static {v1}, Lcom/example/Auth;->login(Ljava/lang/String;)V

Your data flow is:

“password123”

login()

Now investigate:

Don’t immediately call every hardcoded string a vulnerability.

**Trace it first.**

**#Bug Hunter Example #2 — API Token**

invoke-static {v1}, Lcom/example/Api;->request(Ljava/lang/String;)V

Follow it:

Api.request()

Now you know:

A static token field reaches an API request.

That’s a meaningful lead.

**# Bug Hunter Example #3 — URL**

You find:

const-string v0, “https://internal.example.com"

invoke-static {v0}, Lcom/example/Api;->open(Ljava/lang/String;)V

Flow:

internal URL

open()

Who controls the URL?

Can it be modified?

Is it trusted?

Is it used for redirects?

Is it used for API communication?

Is certificate validation performed?

The register instruction itself isn’t necessarily the vulnerability.

It is the **trailhead**.

**# Bug Hunter Example #4 — Security Flag**

Consider:

if-eqz v0, :normal

invoke-static {}, Lcom/example/Debug;->enable()V

Data flow:

Config.DEBUG

condition

security-sensitive branch

Now investigate where:

is written.

You might find:

const v1, 0x1

sput v1, Lcom/example/Config;->DEBUG:I

Now you’ve connected:

branch

debug functionality

This is how a few register instructions can reveal an entire execution path.

**# The Register Tracking Technique**

When analysing Smali, make a tiny table.

**Value**

API URL

authentication result

v3

User object

Then update it as you read.

You write:

v0 = API URL

Then:

Update:

v1 = API URL

invoke-static {v1}, Lcom/example/Api;->connect(Ljava/lang/String;)V

API URL → connect()

This simple technique becomes incredibly powerful with larger methods.

**# Practice — Objects**

Register map:

v0 → User object

**# Practice — Field Access**

iget-object v1, v0, Lcom/example/User;->token:Ljava/lang/String;

v1 = user.token

\# **Practice — Method Result**

boolean authenticated = checkAuth();

invoke-static {}, Lcom/example/Auth;->checkAuth()Z

v0 → authenticated

**# Practice — Put Everything Together**

send(token);

invoke-static {v0}, Lcom/example/Api;->send(Ljava/lang/String;)V

send()

This is the exact mental model you should develop.

**# Quick Reference**

And remember the basic direction:

A → B

object.field → register

register → object.field

Class.field → register

register → Class.field

method() → register

register ← new Object

**# Bug Hunter Checklist**

When you encounter an interesting value, ask:

**1. Where was it created?**

Look for:

const

**2. Which register contains it?**

**3. Where does the register go?**

invoke-\*

**4. Does it enter an object field?**

**5. Does it come from a field?**

sget-object

**6. Does it reach a method?**

**7. Does it influence a security decision?**

if-\*

if-nez

packed-switch

sparse-switch

Those control-flow instructions will become much more important in the next chapters.

**# Quick Recap**

You now know how Smali moves data.

moves normal values.

moves references.

move-wide

moves wide values.

captures normal method results.

captures object results.

captures wide results.

creates numeric constants.

loads strings.

creates objects.

iget / iput

read and write instance fields.

sget / sput

read and write static fields.

But the most important lesson isn’t any individual instruction.

It’s this: **Follow the data.**

**# Final Thought**

A Smali method can look terrifying at first.

Hundreds of registers.

Dozens of instructions.

Strange descriptors.

Labels everywhere.

But don’t try to understand everything at once.

Pick one interesting value.

Maybe: password

Maybe: token

Maybe: API URL

Maybe: isAdmin

Then follow it.

Where was it created?

Which register holds it?

Where is it moved?

Which field stores it?

Which method receives it?

Does it influence a security decision?

That is the beginning of real Smali analysis.

Because when you’re hunting bugs, you don’t need to understand **every box in the warehouse**.

You just need to know:

**Which box contains the valuable package and where that package is going.**

**Next chapter:** Control Flow in Smali **“Which Door Does the Code Take?”**

BY — bithowl
