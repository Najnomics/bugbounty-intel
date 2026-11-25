# Smali By bithowl

- **Source URL:** https://medium.com/@bithowl/smali-by-bithowl-chapter-14-fields-6e455999a654
- **Fetched from:** https://medium.com/@bithowl/smali-by-bithowl-chapter-14-fields-6e455999a654?source=rss-87ac1fc88e11------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14941 (id 14941)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** bithowl / Sat, 10 Oct 2026 07:15:47 GMT

**“The Data Is There. But Who Put It There?”**

In the previous chapter, we learned about object operations.

We explored:

new-instance

instance-of

check-cast

We learned how objects are created, checked, and treated as specific types.But creating an object is only the beginning. Imagine an Android application creates a User object.

What happens next?

Where does the user’s name go?

Where is the authentication token stored?

Where does the application keep the login status?

And when the application needs that data again, how does it retrieve it?

Consider this Java code:

User user = new User();

user.name = “bithowl”;

user.isAdmin = false;

The object exists, but it also has **fields** that hold its data. In Smali, four important instructions help us read and write those fields:

iget

sget

iput

sput

One important detail: you’ll often encounter variants such as iget-object, sget-object, iput-object, and sput-object. These handle object references, including strings.

Let’s understand them.

**# The Story — The Apartment With Two Kinds of Storage**

Imagine an Android application is an apartment building. Each apartment represents an object.

Inside each apartment, you have storage compartments:

User Object

├── name

├── token

└── isAdmin

These compartments are called **instance fields**.

Every User object can have its own name, email, token, and admin status.

For example:

User A

├── name = “Alice”

└── isAdmin = false

User B

├── name = “Bob”

└── isAdmin = true

Now imagine the building also has a shared noticeboard. It belongs to the entire building, not to any single apartment. That represents a **static field**.

Session Class

└── currentToken

The difference is simple:

And Smali gives us different instructions to access them.

**# What Is a Field?**

A field is a variable declared inside a class but outside its methods.

public class User {

String name;

String token;

boolean isAdmin;

static String appVersion;

}

Here:

In Smali, fields are commonly declared like this:

.field public name:Ljava/lang/String;

.field public token:Ljava/lang/String;

.field public isAdmin:Z

.field public static appVersion:Ljava/lang/String;

Remember the descriptors from Chapter 6:

Ljava/lang/String; → String

Z → boolean

I → int

J → long

Now let’s learn how to access these fields.

**1. iget — Read an Instance Field**

The iget family reads a field belonging to an object.

Suppose Java contains:

String name = user.name;

Smali might contain: iget-object v0, v1, Lcom/example/User;->name:Ljava/lang/String;

Let’s decode it.

iget-object

↓

Read an object-reference field

v0

Destination register

v1

Register containing the User object

User;->name

Field being read

The result:

v1.name

In Java-style thinking:

v0 = v1.name;

The register v0 now contains the reference stored in the name field.

**What about a normal integer field?**

Java:

int age = user.age;

Smali:

iget v0, v1, Lcom/example/User;->age:I

Conceptually:

user.age → v0

The instruction variant depends on the field’s type.

Common examples:

iget # Single-width primitive

iget-object # Object or String reference

iget-wide # long or double

**# Bug Hunter Perspective**

Imagine you find:

iget-object v0, v1, Lcom/example/Session;->token:Ljava/lang/String;

You have discovered a token being read from a Session object.

Now ask:

The field read is a clue. The surrounding code tells you whether there’s a security issue.

**2. sget — Read a Static Field**

Now let’s look at the shared noticeboard.

String token = Session.currentToken;

sget-object v0, Lcom/example/Session;->currentToken:Ljava/lang/String;

Notice the difference.

There is no register holding a particular Session object.

Why?

Because currentToken is a **static field**.

It belongs to the class.

v0 = Session.currentToken;

The data flow is:

Session.currentToken

For an integer static field:

int debug = Config.DEBUG;

Smali might contain:

sget v0, Lcom/example/Config;->DEBUG:I

Common variants include:

sget # Single-width primitive

sget-object # Object or String reference

sget-wide # long or double

**Why Is This Interesting?**

Suppose you discover:

sget-object v0, Lcom/example/Session;->accessToken:Ljava/lang/String;

You now know that the application reads a static field named accessToken.

Trace where the value goes next.

invoke-static {v0}, Lcom/example/Api;->send(Ljava/lang/String;)V

Session.accessToken

Api.send()

That gives you a concrete place to investigate token handling.

But remember: a static field isn’t automatically insecure. The question is how the value is protected, accessed, and used.

**3. iput — Write an Instance Field**

So far, we’ve only read data.

What if the application needs to save a value inside an object?

user.age = 25;

const/16 v0, 0x19

iput v0, v1, Lcom/example/User;->age:I

Value being written: 25

Object receiving the value

User;->age

Destination field

The flow is:

v0 = 25

user.age = 25

v1.age = v0;

The exact register names depend on the method. The important point is that iput writes a value into an instance field.

**Writing a String Field**

user.token = token;

iput-object v0, v1, Lcom/example/User;->token:Ljava/lang/String;

The flow:

Token in v0

iput-object

User.token

Other common variants include:

iput # Single-width primitive

iput-object # Object or String reference

iput-wide # long or double

**# Bug Hunter Perspective — Find Where Sensitive Data Is Stored**

Suppose you see:

invoke-static {}, Lcom/example/Auth;->getToken()Ljava/lang/String;

move-result-object v0

Follow it:

getToken()

You’ve discovered where a returned token is assigned to a field.

our next task is to find where that field is read and whether the token is exposed, persisted insecurely, or sent to an unintended destination.

**4. sput — Write a Static Field**

Now let’s update the shared noticeboard.

Session.currentToken = token;

sput-object v0, Lcom/example/Session;->currentToken:Ljava/lang/String;

Session.currentToken = v0;

The data flow:

sput-object

Config.DEBUG = 1;

Smali could look like:

const/4 v0, 0x1

sput v0, Lcom/example/Config;->DEBUG:I

Now the value 1 is written into Config.DEBUG.

sput # Single-width primitive

sput-object # Object or String reference

sput-wide # long or double

**Why Does This Matter?**

const-string v0, “example-token”

You’ve discovered a string being assigned to a static field.

Questions worth investigating:

Static storage and secure storage are not the same thing. A static field is a memory location associated with the class; it does not provide encryption or persistent storage by itself.

**# Instance vs Static: The Four Instructions**

Here’s the simplest way to remember them.

\<text color=”secondary” size=”sm”>Read data from a particular object.\</text>

\`\`\`smali

\`\`\`

\</box>

\<text color=”secondary” size=”sm”>Read data associated with a class.\</text>

\<text color=”secondary” size=”sm”>Save a value inside a particular object.\</text>

\<text color=”secondary” size=”sm”>Save a value into a class-level field.\</text>

One-line memory trick:

i = instance

s = static

get = read

put = write

Therefore:

iget → instance read

sget → static read

iput → instance write

sput → static write

**# Follow the Field: A Realistic Bug Hunter Workflow**

Let’s put all four instructions together. Imagine an application stores a session token.

First, the application receives it:

Then it saves the token:

Later, another method retrieves it:

sget-object v1, Lcom/example/Session;->currentToken:Ljava/lang/String;

Finally, it passes the token to a request:

invoke-static {v1}, Lcom/example/Api;->send(Ljava/lang/String;)V

The full story:

sget-object

This is **field-based data-flow analysis**.

You are connecting the places where data is created, stored, retrieved, and used. When investigating a suspected issue, you can now ask whether the token is handled safely throughout that journey.

**# Practical Exercise — Trace the Fields**

Study this example:

.class public Lcom/example/Session;

.super Ljava/lang/Object;

.field public static currentToken:Ljava/lang/String;

.field public username:Ljava/lang/String;

.field public age:I

Imagine a method contains:

const-string v0, “demo-token”

new-instance v1, Lcom/example/Session;

invoke-direct {v1}, Lcom/example/Session;->\<init>()V

const-string v2, “Alice”

iput-object v2, v1, Lcom/example/Session;->username:Ljava/lang/String;

const/16 v3, 0x19

iput v3, v1, Lcom/example/Session;->age:I

**Step 1 — Create the token string**

v0 → “demo-token”

**Step 2 — Store the static token**

Session.currentToken = “demo-token”

**Step 3 — Create the object**

v1 → Session object

**Step 4 — Write the username**

v1.username = “Alice”

**Step 5 — Write the age**

v1.age = 25

The final state is conceptually:

Session class

└── currentToken = “demo-token”

Session object (v1)

├── username = “Alice”

└── age = 25

Notice the distinction: currentToken belongs to the class, while username and age belong to the object.

**# Bug Hunter Checklist**

Whenever you find a field access, ask these questions:

**When you see iget:**

**When you see sget:**

**When you see iput:**

**When you see sput:**

And always search for both sides of the field:

WRITE → FIELD → READ → USE

A field’s name can be helpful, but it isn’t proof of what the application actually does. Follow the instructions and examine the surrounding control flow.

**# Quick Recap**

For reference types, you’ll often see the corresponding -object variants. For long and double, you’ll often see -wide variants.

Remember:

**# Final Thought**

When you first open a Smali file, a field instruction might look like another strange line of machine code.

But now we can read:

and understand the story:

The class has a token.

The application reads it.

The token enters v0.

The next instruction determines where it goes.

That’s a big step toward understanding an unfamiliar Android application.

Because when you’re hunting bugs, **finding where data is stored is only half the job. Finding who can write it, who can read it, and what they do with it is where the investigation gets interesting.**

By — bithowl
