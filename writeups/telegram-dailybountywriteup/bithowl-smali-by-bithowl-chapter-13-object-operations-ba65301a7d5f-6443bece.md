# Smali By bithowl

- **Source URL:** https://medium.com/@bithowl/smali-by-bithowl-chapter-13-object-operations-ba65301a7d5f
- **Fetched from:** https://medium.com/@bithowl/smali-by-bithowl-chapter-13-object-operations-ba65301a7d5f?source=rss-87ac1fc88e11------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14931 (id 14931)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** bithowl / Sat, 03 Oct 2026 05:31:01 GMT

**“The Register Has an Object. But What Exactly Is It?”**

In the previous chapter, we learned about constants.

We saw:

const/4

const/16

const

const-wide

const-string

const-class

We learned how values enter registers.

For example: const-string v0, “admin”

gave us: v0 → “admin”

But Android applications don’t only work with strings and numbers.

They work with **objects**.

Users.

Activities.

Services.

Intents.

URLs.

Network clients.

JSON objects.

WebViews.

Custom classes.

Exceptions.

And thousands of other object types.

So now we need to answer three important questions:

**How does Smali create an object?**

**How does it check what type an object is?**

**How does it treat an object as a specific type?**

That’s where three very important instructions enter the picture:

new-instance

instance-of

check-cast

These three instructions are simple individually. But together, they appear everywhere in real Android applications.

And for a bug hunter, they can reveal some very interesting execution paths.

**# The Hook Story**

Imagine our Android application is a giant warehouse.

Registers are storage boxes:

v0

v1

v2

v3

Now a worker says: “Create a new User object and put it in box v0.”

That’s: new-instance v0, Lcom/example/User;

Another worker asks: “Is the object inside v0 actually a User?”

That’s: instance-of v1, v0, Lcom/example/User;

And another says: “Treat the object inside v0 specifically as a User.”

That’s: check-cast v0, Lcom/example/User;

So think of the three instructions like this:

↓

Create

Check

Treat as a specific type

That’s the entire chapter in one picture. But let’s understand what is really happening.

**1. new-instance**

Let’s start with object creation.

Suppose Java contains:

User user = new User();

Smali can represent this as:

new-instance v0, Lcom/example/User;

invoke-direct {v0}, Lcom/example/User;->\<init>()V

The first instruction:

creates an instance of:

Lcom/example/User;

and puts its reference into:

So conceptually:

new User()

**Important: new-instance Does Not Finish Initialization**

This is a very important beginner concept.

When you see: new-instance v0, Lcom/example/User;

the object has been allocated, but the constructor normally still needs to run.

You’ll commonly see:

Think:

Object created

\<init>

Object initialized

In Java: new User();

looks like one operation. At the Smali level, we can see the underlying pieces.

**Why Does new-instance Matter?**

Because object creation tells you **where important objects enter the application**.

Imagine: new-instance v0, Lcom/example/ApiClient;

Now we know the application is creating an ApiClient.

Or:

new-instance v1, Landroid/webkit/WebView;

Now we have found a WebView creation point.

new-instance v2, Landroid/content/Intent;

Now we have found an Intent object.

new-instance v3, Lcom/example/AdminSession;

Now we may want to understand what that object does. The instruction itself isn’t necessarily a vulnerability.

It’s a **navigation clue**.

**# Bug Hunter Perspective**

Suppose you’re reviewing an application and searching for:

WebView

Intent

Uri

CookieManager

HttpURLConnection

OkHttp

Admin

Session

Token

You may find: new-instance v0, Landroid/webkit/WebView;

That gives you a concrete location to investigate.

Then follow the object:

WebView created

configuration

URL loaded

JavaScript enabled?

interface added?

sensitive data exposed?

The new-instance instruction is the beginning of that trail.

**# Example — Creating an Intent**

Java:

Intent intent = new Intent(this, AdminActivity.class);

At the Smali level, the creation process can involve: new-instance v0, Landroid/content/Intent;

followed by constructor/method operations.

Now you can track:

Intent object

extras / component / flags

startActivity()

This becomes especially useful when analysing Android component exposure.

**2. instance-of**

Now imagine we already have an object.

Maybe: v0 → some object

But we don’t know exactly what type it is.

Smali provides: instance-of

Example: instance-of v1, v0, Lcom/example/User;

Conceptually: v1 = v0 instanceof User;

The result is a boolean.

So: v1 = 1

means the object is compatible with that type.

And: v1 = 0

means it isn’t.

**The Basic Pattern**

instance-of v1, v0, Lcom/example/User;

Break it down:

result

object being checked

type being tested

So:

**Java Equivalent**

Smali: instance-of v1, v0, Lcom/example/User;

Java-style thinking: boolean result = v0 instanceof User;

That’s the easiest way to remember it.

**Why instance-of Matters**

Applications frequently receive objects through:

Intent extras

callbacks

framework APIs

interfaces

collections

generic containers

reflection

Android lifecycle methods

The actual object type may not be obvious.

So developers may check:

if (object instanceof User) {

…

}

Smali represents that logic with:

**Example — Security-Sensitive Type Check**

Imagine:

instance-of v1, v0, Lcom/example/AdminUser;

if-eqz v1, :not\_admin

Now we have:

“Is this an AdminUser?”

if-eqz

security branch

This is interesting during reverse engineering.

Why?

Because you’ve discovered a **type-based security decision**.

You should now inspect:

Where did v0 come from?

Who controls it?

How is the object created?

Can another object type reach this point?

What happens in the AdminUser branch?

Again:

The instruction is a clue, not automatically a vulnerability.

**3. check-cast**

Now we reach the third instruction.

Suppose we have: v0 → object

and we know or expect that it is a particular type.

We can see: check-cast v0, Lcom/example/User;

Conceptually: (User) v0

In other words: Treat the reference in v0 as a User reference.

**Why Is check-cast Needed?**

Imagine Java:

Object obj = getObject();

User user = (User) obj;

The object is initially treated as: Object

Then the application casts it to: User

Smali can represent the cast with: check-cast v0, Lcom/example/User;

After that, the code can use v0 in operations that require a User reference.

**A Simple Example**

invoke-static {}, Lcom/example/Manager;->getObject()Ljava/lang/Object;

move-result-object v0

check-cast v0, Lcom/example/User;

Follow the flow:

getObject()

Object reference

User reference

The register itself didn’t suddenly become a different physical object. The reference is being checked/cast so subsequent operations can treat it as the specified type.

**What Happens If the Cast Is Wrong?**

Suppose: v0 → String

but the application executes: check-cast v0, Lcom/example/User;

If the runtime object isn’t compatible with User, the cast can fail with a: ClassCastException

This matters when understanding application behaviour.

**# instance-of vs check-cast**

These two instructions are easy to confuse.

Remember: **instance-of**

**Ask a question.**

Meaning: “Is v0 a User?”

Result: true / false

**Perform a cast/check.**

Meaning:

“Treat v0 as a User reference.”

If incompatible: ClassCastException

**The Classic Pattern**

You’ll often see these instructions together:

if-eqz v1, :not\_user

invoke-virtual {v0}, Lcom/example/User;->getToken()Ljava/lang/String;

This is beautiful from a reverse-engineering perspective.

Let’s translate it.

**Step 1**

Ask:

Is v0 a User?

**Step 2**

If the answer is false:

go to :not\_user

**Step 3**

Now treat v0 as a User.

**Step 4**

Call:

User.getToken()

So the entire flow becomes:

Now you’re thinking like a reverse engineer.

**# Object Data Flow**

Let’s connect this to the previous chapter.

Suppose:

move-object v1, v0

instance-of v2, v1, Lcom/example/User;

check-cast v1, Lcom/example/User;

Follow the object:

v2 = true

v1 treated as User

Now we can continue following:

invoke-virtual {v1}, Lcom/example/User;->getToken()Ljava/lang/String;

And the chain becomes:

new User

check type

cast

getToken()

**Bug Hunter Example — Intent Extras**

This pattern becomes especially interesting around Android Intent data.

Imagine an application receives an object:

invoke-virtual {p0}, Landroid/content/Intent;->getSerializableExtra(Ljava/lang/String;)Ljava/io/Serializable;

if-eqz v1, :invalid

Now you know:

Intent data

Serializable object

instance-of User

check-cast User

As a bug hunter, this tells you where to investigate.

Questions include:

Where does the Intent come from?

Can another application send it?

Is the receiving component exported?

What data can the sender control?

What happens after the cast?

Are security-sensitive fields taken from the object?

The object operations help you reconstruct that path.

**Bug Hunter Example — WebView**

Suppose you find:

new-instance v0, Landroid/webkit/WebView;

invoke-direct {v0, p0}, Landroid/webkit/WebView;->\<init>(Landroid/content/Context;)V

You’ve found a WebView creation point.

Now you might trace:

settings

JavaScript

URL

loadUrl()

The interesting security behaviour may happen **after** new-instance. That’s why object creation is a starting point rather than the conclusion.

**Bug Hunter Example — Custom Security Object**

new-instance v0, Lcom/example/SecurityManager;

invoke-direct {v0}, Lcom/example/SecurityManager;->\<init>()V

invoke-virtual {v0}, Lcom/example/SecurityManager;->isSecure()Z

move-result v1

Now you can trace:

SecurityManager created

isSecure()

security decision

If you’re auditing authentication or security controls, this is exactly the kind of flow worth following.

**# A Key Difference: Object vs Class**

This is another concept worth locking into memory.

const-class v0, Lcom/example/User;

Gives you:

User.class

Creates:

Asks:

Treats/checks:

v0 as User

Four different operations.Don’t mix them.

**#One Mental Model**

Imagine a package arriving at a warehouse.

BUILD A NEW PACKAGE

WHAT KIND OF PACKAGE IS THIS?

HANDLE THIS PACKAGE AS THIS SPECIFIC TYPE

Simple.

**Practice — Convert Java to Smali Thinking**

Let’s practice.

**Example 1 — Object Creation**

Smali:

Register:

v0 → User object

**Example 2 — Type Check**

if (obj instanceof User) {

v1 → true/false

**Example 3 — Cast**

Now subsequent operations can use v0 as a User reference.

**#Practice — Follow the Whole Flow**

Look at this:

if-eqz v2, :invalid

move-result-object v3

Let’s trace it.

v1 → same User reference

v2 → true

assuming the object is actually a User.

Now v1 is treated as a User.

**Step 5**

The User object provides a token.

**Step 6**

Now:

v3 → token

Complete flow:

This is exactly the kind of object/data flow you should learn to recognize.

**# Bug Hunter Checklist**

When you encounter an object operation, ask:

What object is being created?

Why is it being created?

Where is the reference stored?

What happens immediately after construction?

What type is being checked?

Where did the object come from?

Does the result control a security-sensitive branch?

What type is the object being cast to?

Could the object originate from external input?

Which methods or fields are accessed next?

**Search Strategy**

When reviewing Smali, searching for these instructions can quickly reveal object-related behaviour.

Search for: new-instance

to find object creation.

Search for: instance-of

to find runtime type checks.

Search for: check-cast

to find type assumptions.

Then investigate the surrounding code.

For example:

is much more interesting than:

by itself.

Context is everything.

**Quick Reference**

Mental model:

CREATE

CHECK

CAST

**# Quick Recap**

Today we learned three important object operations.

Creates an object reference.

Think: new User()

Checks whether an object is compatible with a particular type.

Think: v0 instanceof User

Checks/casts a reference so subsequent instructions can treat it as the specified type.

Think: (User) v0

If the runtime object isn’t compatible, the cast can throw ClassCastException.

**#Final Thought**

When you see: new-instance

don’t just think: “An object was created.”

Think: **“A new object has entered the data flow.”**

When you see: instance-of

don’t just think: “The app is checking a type.”

Think: **“This type check might control where execution goes.”**

And when you see: check-cast

think: **“The application now expects this object to behave like this specific type.”**

Put the three together:

USE

And suddenly a block of strange looking Smali starts telling a story. Because reverse engineering isn’t about memorizing instructions. It’s about following the story of the objects.

**Create the object. Identify the object. Follow the object.**

By — bithowl
