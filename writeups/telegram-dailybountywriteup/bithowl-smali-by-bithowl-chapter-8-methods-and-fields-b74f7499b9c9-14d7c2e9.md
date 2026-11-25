# Smali By bithowl

- **Source URL:** https://medium.com/@bithowl/smali-by-bithowl-chapter-8-methods-and-fields-b74f7499b9c9
- **Fetched from:** https://medium.com/@bithowl/smali-by-bithowl-chapter-8-methods-and-fields-b74f7499b9c9?source=rss-87ac1fc88e11------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14886 (id 14886)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** bithowl / Sat, 29 Aug 2026 05:31:01 GMT

*(“The Memory and Machinery Inside Every Android Class”)*

A class without data is just an empty box. A class without behaviour is just a blueprint. Put them together, and you get something useful.

In Java, you already know them as:

Smali has the same concepts.

But the way they’re represented is much closer to the underlying bytecode. For an Android reverse engineer, understanding methods and fields is essential.

Because when you’re hunting for a vulnerability, you’re often asking two simple questions:

**What does this class store?**

and

**What can this class do?**

Fields answer the first question.

Methods answer the second.

Let’s break them apart.

**# The Story (Hook)**

Imagine you discover a locked room inside an Android application.

Inside the room you find:

A safe

A control panel

A telephone

A filing cabinet

The safe contains information.

The control panel performs actions.

The filing cabinet stores records.

The telephone communicates with other systems.

In programming terms:

**Fields** → Things the class stores

**Methods** → Things the class does

A field might contain:

username

token

API\_URL

isLoggedIn

A method might:

login()

logout()

verifyToken()

sendRequest()

When reverse engineering an application, these two pieces often reveal the purpose of a class before you even understand its entire implementation.

**# What Is a Method?**

A method represents a behaviour or operation.

Java:

public boolean verifyToken(String token) {

…

}

Smali:

.method public verifyToken(Ljava/lang/String;)Z

.end method

From Chapter 6, we can decode the signature:

verifyToken

│

├── Parameter: String

└── Return: boolean

The method signature tells us **what goes in and what comes out**.

The instructions inside the method tell us **what actually happens**.

**# Static Methods**

A static method belongs to the class itself rather than a particular object.

public static boolean isValid(String token) {

.method public static isValid(Ljava/lang/String;)Z

Notice: **public static**

The static keyword is part of the method’s access flags. A static method can be called without creating an instance of the class.

For example: **AuthUtils.isValid(token);**

In Smali, you will commonly see static method calls using: **invoke-static**

Example: **invoke-static {v0}, Lcom/example/AuthUtils;->isValid(Ljava/lang/String;)Z**

This is an important distinction when reading bytecode.

**# Instance Methods**

Instance methods belong to a particular object.

public boolean verify(String token) {

.method public verify(Ljava/lang/String;)Z

Notice there is no: **static**

An instance method operates on an object instance.

For example:

AuthManager manager = new AuthManager();

manager.verify(token);

In Smali, instance method calls commonly use:

invoke-virtual

or:

invoke-direct

depending on the method and access context.

You’ll learn these invocation instructions in much greater detail later.

**# Static vs Instance Methods**

The difference is simple:

Example**: MathUtils.calculate();**

This doesn’t require an object.

But: **user.getToken();**

operates on a particular user object.

Understanding this distinction becomes extremely important when tracing execution through Smali.

**# Constructors**

Constructors are special methods.

In Java:

public AuthManager() {

In Smali:

.method public constructor \<init>()V

The unusual part is: \<init>

That’s the constructor name in Smali.

The return type is: V meaning void.

Constructors initialize objects.

public AuthManager(String token) {

this.token = token;

could appear conceptually as:

.method public constructor \<init>(Ljava/lang/String;)V

Constructors are particularly interesting during reverse engineering because initialization logic can reveal:

**# Static Constructors**

There’s another special method: \<clinit>

Example:

.method static constructor \<clinit>()V

This is the class initializer. It is commonly used to initialize static fields.

static {

API\_URL = “https://api.example.com";

may be represented through \<clinit>.

When you see \<clinit>, pay attention to what it initializes.

It can provide useful clues about how the application configures itself.

**# Method Signatures**

A method signature tells you:

.method public login(Ljava/lang/String;Ljava/lang/String;)Z

Decode it:

Name: login

Parameter 1: String

Parameter 2: String

Return: boolean

Equivalent Java: public boolean login(String username, String password)

Another: .method public getToken()Ljava/lang/String;

means: public String getToken()

And: .method private calculate(II)I

means: private int calculate(int a, int b)

Once you become comfortable with descriptors, method signatures become surprisingly easy to read.

**# Parameters**

Methods can accept parameters.

Example: .method public login(Ljava/lang/String;)Z

The method accepts one String.

Multiple parameters appear sequentially: .method public login(Ljava/lang/String;Ljava/lang/String;)Z

That’s: String

String

↓

boolean

In the method body, parameters are commonly represented using **parameter registers** such as:

p0

p1

p2

For instance methods, p0 commonly represents this reference.

So when you see: p0

don’t automatically assume it is the first declared method argument. For an instance method, it generally represents the current object.

This distinction becomes critical when analysing registers.

**# Return Values**

Methods can return different types.

**Void**

.method public logout()V

V means the method returns nothing.

The method typically ends with:

return-void

**Integer / Boolean**

.method public isValid()Z

The result is returned using an instruction such as:

return v0

**Object**

.method public getToken()Ljava/lang/String;

An object return commonly uses: return-object v0

Understanding return types helps you follow data through the application.

**# What Is a Field?**

A field is data associated with a class or an object.

Java: private String token;

Smali: .field private token:Ljava/lang/String;

The field contains:

Access: private

Name: token

Type: String

Fields can store almost anything: Strings, Integers, Booleans, Objects, Arrays, Collections, References

**# Static Fields**

A static field belongs to the class rather than individual objects.

Java: public static String API\_URL;

Smali: .field public static API\_URL:Ljava/lang/String;

There is only one class-level value rather than one value per object instance.

Static fields are often used for:

For a bug hunter, static fields can be interesting because developers sometimes place sensitive configuration there.

For example: .field private static API\_KEY:Ljava/lang/String;

This is worth investigating.

But remember: **A suspicious field name is not automatically a vulnerability.**

You need to determine what the value contains and how it is used.

**# Instance Fields**

Instance fields belong to individual objects.

.field private username:Ljava/lang/String;

.field private token:Ljava/lang/String;

.field private loggedIn:Z

Equivalent Java:

private String username;

private String token;

private boolean loggedIn;

Imagine two objects:

User A

├── username = “alice”

├── token = “…”

└── loggedIn = true

User B

├── username = “bob”

└── loggedIn = false

Each object has its own copy of the instance fields.

**# Static vs Instance Fields**

This distinction is fundamental.

Static Field

▼

Belongs to the class

└── One shared class-level value

Instance Field

Belongs to an object

└── Each object has its own value

.field public static APP\_VERSION:Ljava/lang/String;

The first is class-level.

The second belongs to an instance.

**# Accessing Fields in Smali**

Smali uses specific instructions to read and write fields.

For instance fields, you’ll commonly encounter:

iget

iput

For static fields:

sget

sput

iget-object v0, p0, Lcom/example/User;->token:Ljava/lang/String;

This means:

Read the token field from the object represented by p0 and place the result into v0.

And:

sget-object v0, Lcom/example/Config;->API\_URL:Ljava/lang/String;

means:

Read the static API\_URL field and place it into v0.

We’ll study these instructions in detail when we get into Smali operations.

For now, remember the pattern:

iget / iput → instance fields

sget / sput → static fields

**# Field Access Modifiers**

Fields can have access modifiers.

Example: .field public username:Ljava/lang/String;

Public means the field is accessible according to normal Java visibility rules.

Private: .field private token:Ljava/lang/String;

Protected: .field protected sessionId:Ljava/lang/String;

Static: .field private static API\_URL:Ljava/lang/String;

Final: .field private static final VERSION:I = 0x1

These modifiers tell you how the field is intended to be used.

**# Bug Hunter Perspective**

This is where methods and fields become especially interesting for security research.

Imagine you find:

Don’t immediately conclude:

“Token vulnerability!”

Instead, trace the field.

Ask:

Where is token initialized?

Where is token written?

Where is token read?

Is it stored securely?

Is it sent over the network?

Can an attacker influence it?

The same approach applies to methods.

Suppose you find: .method public resetPassword(Ljava/lang/String;)V

The method name sounds sensitive.

But you need to investigate:

This is the difference between **finding interesting code** and **finding a vulnerability**.

**# A Realistic Example**

Consider:

.class public Lcom/example/app/AuthManager;

.super Ljava/lang/Object;

.method public isAuthenticated()Z

We can immediately build a mental model:

AuthManager

├── Field

│ └── token : String

├── Constructor

│ └── Receives String

├── isAuthenticated()

│ └── Returns boolean

├── getToken()

│ └── Returns String

└── logout()

└── Returns void

We haven’t read the method bodies yet. But we’ve already learned a lot about the class.

That’s the power of understanding structure.

**# Practical Exercise Method & Field Mapping**

Take an APK and choose a security-sensitive class.

Good candidates include classes containing words such as:

Auth

Login

Token

Crypto

Network

Api

WebView

Database

Security

Open the corresponding Smali file.

Create a simple table:

Then choose one interesting field and one interesting method.

Trace where they are used.

Don’t try to understand the entire application. Learn to follow **one piece of data or one action** through the code. That skill will become extremely valuable later.

**# Quick Recap**

**# Final Thought**

When you open a Smali class, don’t immediately chase instructions.

First ask two questions: **What does this class remember?**

Look at the fields.

**What does this class do?**

Look at the methods.

Then connect the two.

A field stores the data.

A method changes, reads, validates, or sends that data.

And somewhere between those two…

is often where the vulnerability lives.

Because security bugs aren’t just hidden in instructions.

They’re hidden in the **relationship between data and behaviour**.

By — bithowl
