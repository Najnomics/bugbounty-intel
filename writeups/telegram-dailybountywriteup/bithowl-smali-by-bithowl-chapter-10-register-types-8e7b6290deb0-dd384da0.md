# Smali By bithowl

- **Source URL:** https://medium.com/@bithowl/smali-by-bithowl-chapter-10-register-types-8e7b6290deb0
- **Fetched from:** https://medium.com/@bithowl/smali-by-bithowl-chapter-10-register-types-8e7b6290deb0?source=rss-87ac1fc88e11------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14908 (id 14908)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** bithowl / Sat, 12 Sep 2026 05:31:01 GMT

*(“What’s Actually Inside the Register?”)*

In the last chapter, we learned about:

v0

v1

v2

p0

p1

We learned that registers are the tiny storage locations used by Smali methods. But there’s a question we haven’t answered yet:

**What can actually be stored inside those registers?**

The answer is: Almost everything a method needs.

Numbers.

Booleans.

Objects.

Strings.

Arrays.

And even values that require **two registers**. That’s where register types become important.

Because when you’re reading Smali, you shouldn’t just ask: “What’s in v0?”

You should ask: “What type of value is v0 holding?”

That one question can completely change how you interpret the next instruction.

Let’s break it down.

**# The Story (Hook)**

Imagine a warehouse with identical storage boxes. Every box looks exactly the same from the outside.

But inside, one box contains: 5

Another contains: “admin”

Another contains: User object

Another contains: \[10, 20, 30\]

And one particularly large item needs **two boxes**. The boxes themselves don’t tell you what they’re holding. You need to understand how the program is using them.

That’s essentially what happens with registers.

Register

↓

Value

Type determines how the value is interpreted

So:

v0 → int

v1 → String reference

v2 → array reference

The register name doesn’t tell you the type. The **instructions and surrounding code do**.

**# Register Types — The Big Picture**

For beginners, divide register values into these categories:

A useful simplified rule is:

**Single-width values** — Usually occupy **one register**. Examples: int, float, Boolean, byte, char, short, object references, array references, String references

**Wide values —** Occupy **two consecutive registers**. Examples: long**,** double

This distinction becomes extremely important when reading register layouts.

**1. Single-Width Registers**

A single-width value occupies one register.

For example: const/4 v0, 0x5

Conceptually: v0 = 5

Only one register is required.

Another example: const/4 v1, 0x1

Conceptually: v1 = 1

v0 → 5

v1 → 1

These are single-width values.

**1.1 Integer Values**

Integers are among the most common values you’ll encounter. Smali represents the Java int type using: I

Example method: .method public calculate()I

The I at the end means: Return type = int

An integer can be stored in a single register.

Example: const/4 v0, 0x5

You might then see: add-int v2, v0, v1

Conceptually: v2 = v0 + v1

For a bug hunter, integer registers commonly appear in:

**1.2 Boolean Values**

A boolean also fits in a single register. Smali uses: Z for the Java boolean type.

For example: .method public isAuthenticated()Z

means: Returns boolean

You may encounter:

const/4 v0, 0x1

return v0

Conceptually:

return true;

And:

const/4 v0, 0x0

conceptually means:

return false;

This pattern is particularly interesting when analysing authentication or authorization logic.

**1.3Float Values**

The Java float type uses: F and occupies one register.

Example: const/high16 v0, 0x3f800000

The exact encoding can look unfamiliar at first, but the important concept is:

float → single-width value

Floating-point operations have their own Smali instructions, such as:

add-float

sub-float

mul-float

div-float

You don’t need to memorize every instruction yet.

The important thing is recognizing the type.

**2. Wide Values**

Now we reach something different. Some values require **two consecutive registers**. These are called **wide values**.

The two main examples are:

long

double

So instead of:

v0 → value

you may have:

v0 + v1 → one long value

or:

v2 + v3 → one double value

Think of it like storing a large object across two boxes:

│ part 1 ││ part 2 │gives one value

This matters enormously when counting registers.

**2.1 Long**

Java’s long type is represented by: J and uses two register slots.

For example: .method public getTimestamp()J

The J means: Return type = long

Conceptually, you might encounter a pair such as: v0 + v1 representing one long value.

Don’t interpret this as:

v0 = first number

v1 = second number

They’re together representing **one wide value**.

**2.2 Double**

Java’s double type is represented by: D and also occupies two registers.

For example: .method public calculate()D

means the method returns a double.

Conceptually: v0 + v1 → double

Again, the two registers together represent one value.

**# Why Wide Registers Matter**

Imagine: **.method public calculate(J)V**

The method accepts one long.

A beginner might think: One parameter = one register

But that’s not true here. A long occupies two register slots.

So parameter layout can become: p0 + p1 → long for a static method.

For an instance method, the implicit this reference comes first, so the layout conceptually becomes:

p0 → this

p1 + p2 → long

This is one reason register counting can become tricky.

**Always consider the type descriptor.**

**3. References**

**3.1 Object References**

Now we leave primitive values. Smali registers can also hold **references to objects**.

For example: const-string v0, “hello”

places a String reference into v0.

You might then see:

invoke-virtual {v0}, Ljava/lang/String;->length()I

v0.length();

The important distinction is: Register does not contain the entire object.

Register contains a reference to the object.

Think of it like an address card:

┌─────────┐

│ String object │

│ “ hello ” │

└─────────┘

This is a fundamental concept.

**Object Descriptors**

From Chapter 6, you learned that object descriptors look like:

Lpackage/ClassName;

For example: Ljava/lang/String;

represents: java.lang.String

And: Lcom/example/User;

represents: com.example.User

So if you see:

iget-object v0, p0, Lcom/example/User;->username:Ljava/lang/String;

you can understand:

Read an object field

Store its reference in v0

**3.2 Strings**

Strings are objects in Java. That means a String is not a primitive type.

The descriptor is: Ljava/lang/String;

For example: const-string v0, “admin”

Conceptually: String value = “admin”;

Now: v0 → String reference

This distinction is important.

Don’t think: v0 = raw string bytes

Instead: v0 → reference to String object

**Why Strings Matter to Bug Hunters**

Strings are everywhere in Android applications.

You may find: URLs, API endpoints, Feature flags, Error messages, File paths, Intent actions, Database names, Configuration values, Potential secrets

For example:

const-string v0, “https://api.example.com"

const-string v1, “debug\_mode”

const-string v2, “Authorization”

These strings can provide excellent reconnaissance clues.

But again:

**Finding a string isn’t automatically finding a vulnerability.**

You need to understand how the application uses it.

**3.3 Arrays**

Arrays are also represented by references.

For example: int\[\] values;

The register contains a reference to the array.

┌──────────┐

│ Array │

├──┬──┬──┬─┤

│ 10 │ 20 │ 30 │40│

└──┴──┴──┴─┘

The register itself isn’t storing every element. It holds a reference to the array object.

**Array Descriptors**

Array descriptors begin with: \[

Examples: \[I

means: int\[\]

And: \[Ljava/lang/String;

means: String\[\]

For example: .method public getUsers()\[Ljava/lang/String;

means:

Method:

getUsers()

Returns:

String\[\]

**Reading Array Operations**

You may encounter instructions such as: aget, aput

These are commonly used to read from and write to arrays.

Conceptually: aget v0, v1, v2

means: v0 = array\[index\]

where:

v1 → array

v2 → index

Similarly: aput v0, v1, v2

conceptually means: array\[index\] = value

The exact instruction variant depends on the element type.

**# Object vs Primitive — The Important Difference**

Consider these two:

I

Ljava/lang/String;

They represent very different things.

int

Primitive value

Whereas:

String

Object reference

This difference affects the instructions used.

For example: add-int works with integers.

While: invoke-virtual may operate on an object reference.

Similarly: return is commonly used for primitive values.

While: return-object is used for object references.

Recognizing these patterns makes Smali much easier to decode.

**# A Register Can Change What It Holds**

Here’s a subtle but important concept. A register isn’t permanently assigned one type for the entire method.

For example: const/4 v0, 0x1

At this point: v0 → integer value

Later: const-string v0, “hello”

The same register has been reused.

So don’t say: “v0 is an integer register.”

Instead say: “At this point in execution, v0 contains an integer.”

Later, it may contain something completely different.

**# Type Is Determined by Usage**

Suppose you see: move-object v0, p1

The object suffix tells you that the operation is moving an object reference.

Compare: move v0, p1

and: move-object v0, p1

The instruction itself gives you valuable information about how the register is being interpreted.

Similarly:

move

move-object

move-wide

represent different categories of values.

This is why understanding instructions and register types together is so powerful.

**# Method Calls Reveal Types**

Consider:

move-result v1

What do we know?

The method being called is:

String.length()

and it returns: I

Therefore: v1 → int

Now consider:

invoke-virtual {v0}, Lcom/example/User;->getName()Ljava/lang/String;

move-result-object v1

The return descriptor is:

Therefore: v1 → String reference

This is one of the easiest ways to infer register types while reverse engineering.

**# A Complete Example**

.method public getUserInfo(Ljava/lang/String;)Ljava/lang/String;

.locals 3

const-string v0, “Hello”

invoke-virtual {p1}, Ljava/lang/String;->length()I

invoke-static {v1}, Ljava/lang/Integer;->toString(I)Ljava/lang/String;

move-result-object v2

return-object v2

.end method

Let’s trace the registers.

**Parameter**

p1 → String

**First instruction**

Therefore: v0 → String reference

**Method call**

The String length is calculated.

**Result**

Therefore:

v1 → int

**Next call**

The integer is converted into a String.

v2 → String reference

Finally:

The method returns the String reference.

The flow becomes:

│

▼

length()

Integer.toString()

return

That’s register-type tracing.

**# Bug Hunter Perspective**

This isn’t just theory.

When hunting Android vulnerabilities, knowing register types helps you understand what data is moving through security-sensitive code.

Imagine:

p1 → user-controlled String

validation()

authorization check

Now you can ask: What type is p1?

Where did it come from?

Was it validated?

What does v1 represent?

Does the result control access?

Or:

v0 → Content URI

ContentResolver

database query

Now you’ve identified a potential data-flow path.

v0 → String URL

WebView.loadUrl()

Now you can investigate how that URL is constructed and whether it is attacker-controlled.

The register type gives you the first piece of the puzzle.

**# Bug Hunter Pattern — Primitive to Security Decision**

invoke-virtual {p1}, Lcom/example/Auth;->isAdmin(Ljava/lang/String;)Z

move-result v0

if-eqz v0, :cond\_0

We can decode:

p1 → input

isAdmin()

boolean

conditional branch

Here v0 isn’t just some random register. It’s carrying a **security decision**.

That’s exactly the kind of data flow a bug hunter should pay attention to.

**# Bug Hunter Pattern — Object Reference**

iget-object v0, p0, Lcom/example/User;->token:Ljava/lang/String;

Now:

p0 → User object

v0 → token String reference

Then:

So the type changes as the value moves through the program:

User object

This is exactly why type awareness is essential for reverse engineering.

**# Quick Type Reference**

Keep this table nearby while reading Smali:

Remember: **Object and array values are references.**

They occupy one register in this model, regardless of the size of the object they refer to.

**# Practical Exercise Become a Register Detective**

Extract an APK: apktool d app.apk

Pick a small Smali class. Find a method containing several registers.

For every register, create a simple map:

p0 → ?

p1 → ?

v0 → ?

v1 → ?

v2 → ?

Then determine the type from:

v1 → String

v2 → boolean

Then follow each value through the method.

Your goal isn’t to understand the entire application.

Your goal is to answer:

**What type of value is moving through this register right now?**

**# Mini Challenge**

Decode this:

.method public check(Ljava/lang/String;)Z

.locals 2

const/4 v1, 0x5

if-ge v0, v1, :cond\_0

:cond\_0

Let’s reason through it.

p1.length()

returns an:

**Next value**

**Comparison**

The code compares two integers.

**Return**

v0 = 0 → false

v0 = 1 → true

So the conceptual Java is:

public boolean check(String input) {

if (input.length() >= 5) {

}

You just performed:

Register identification

Type identification

Data flow

Control-flow interpretation

Java reconstruction

That’s the foundation of Smali analysis.

**# One Important Rule**

Never identify a register’s type just because of its name.

There is no:

v0 = int register

v1 = String register

v2 = object register

Instead:

What instruction wrote to it?

What type did that instruction produce?

How is v0 used afterward?

That’s the correct way to reason about registers.

**# Quick Recap**

**# Final Thought**

When you first learned registers, you saw:

They looked like empty boxes. Now you know they aren’t just boxes. They’re carrying information.

v0 → 42

v1 → “admin”

v2 → User object

v3 → int\[\]

v4 + v5 → long

And the real skill isn’t memorizing which register contains what.

It’s learning to follow the value.

When you see:

move-result-object v0

you should immediately ask:

**What object just came back?**

When you see: move-result v1

ask: **What primitive value was returned?**

When you see: move-wide v2, v4

ask: **What wide value is moving through these registers?**

Because once you can identify **what is inside the register**, Smali stops being a collection of mysterious v0s and v1s.

It becomes a trail of data.

And for a bug hunter…

**following that trail is where the interesting stuff begins.**

BY — bithowl
