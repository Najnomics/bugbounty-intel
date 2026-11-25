# Smali By bithowl

- **Source URL:** https://medium.com/@bithowl/smali-by-bithowl-chapter-17-method-calls-9ac5725e5afa
- **Fetched from:** https://medium.com/@bithowl/smali-by-bithowl-chapter-17-method-calls-9ac5725e5afa?source=rss-87ac1fc88e11------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14975 (id 14975)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** bithowl / Mon, 09 Nov 2026 06:52:15 GMT

**“Who Is Calling Whom? Follow the Instructions, Find the Logic.”**

In the previous chapter, we explored return instructions.

We learned how methods finish their work and send values back using:

We also learned how a returned value can influence what happens next.

But here’s an important question: **How does one method actually call another method?**

Imagine an Android application as a company.

One department handles authentication. Another manages user accounts. Another communicates with the server. Another handles encryption.

When the authentication department needs a token, it doesn’t perform every operation itself. It calls the session manager.

When the session manager needs to send a request, it calls the network client. Methods work in a similar way. They communicate through method calls.

In Smali, these calls are represented by instructions beginning with invoke-.

In this chapter, we’ll explore five important instructions:

We’ll also understand:

By the end, we’ll be able to follow a method call from its caller to its implementation and understand what information travels between them.

**# The Story (Hook)**

Imagine you’re investigating an Android banking application.

You discover a method called: login(username, password);

But the interesting question isn’t just what the method is called.

You want to know:

A single method call may connect several different parts of the application.

For example:

LoginActivity

|

v

AuthManager.login()

CredentialValidator.verify()

NetworkClient.authenticate()

Server Response

In Smali, each connection can appear as an invoke-\* instruction.

**A method call is not just an instruction. It’s a doorway into another part of the application.**

Let’s learn how to open those doors.

**1. What Is a Method Invocation?**

A method invocation is an instruction that tells the runtime to execute another method.

Consider this Java code:

int result = calculate(10, 20);

A simplified Smali representation could look like:

const/16 v0, 0xa

const/16 v1, 0x14

invoke-static {v0, v1}, Lcom/example/Calculator;->calculate(II)I

move-result v2

Let’s understand what happens:

The basic structure is:invoke-type {registers}, Lpackage/Class;->methodName(parameters)returnType

Let’s break it down:

This complete description is called a **method signature**. We’ll explore it in detail later.

**2. invoke-static — Calling a Static Method**

Let’s begin with one of the easiest invocation instructions.

invoke-static

A static method belongs to a class rather than a particular object instance.

In Java:

class Calculator {

static int add(int a, int b) {

return a + b;

}

You can call this method directly through the class:

int result = Calculator.add(10, 20);

You don’t need to create a Calculator object first.

**Smali example**

invoke-static {v0, v1}, Lcom/example/Calculator;->add(II)I

What’s happening?

Notice something important: There is no p0 receiver being passed automatically.

A static method doesn’t receive an instance reference as its implicit first argument.

**Another example: Security-related method**

Java:

boolean isDebugEnabled() {

return SecurityConfig.isDebugMode();

Smali:

invoke-static {}, Lcom/example/SecurityConfig;->isDebugMode()Z

move-result v0

return v0

The empty braces mean the method receives no arguments. The method returns a boolean, which is captured in v0.

**Bug Hunter Perspective**

Static methods are common in Android applications.

During security analysis, search for calls involving:

invoke-static {v0}, Lcom/example/CryptoUtils;->encrypt(Ljava/lang/String;)Ljava/lang/String;

move-result-object v1

This tells you that a string reference in v0 is passed to encrypt(). But don’t assume encryption is secure just because the method is named encrypt.

Open the implementation and investigate:

**Bug-hunting lesson:** A method name tells you where to investigate. Its implementation tells you what it actually does.

**3. invoke-direct — Calling Constructors and Direct Methods**

Next comes: invoke-direct

This instruction is commonly used for:

Let’s understand constructors first.

class User {

String name;

User(String name) {

this.name = name;

When you create an object:

User user = new User(“Alex”);

Java calls the constructor.

In Smali, the constructor is represented by:

\<init>

new-instance v0, Lcom/example/User;

const-string v1, “Alex”

invoke-direct {v0, v1}, Lcom/example/User;->\<init>(Ljava/lang/String;)V

Let’s break it down.

**Step 1: Create the object**

A new User object is created, with its reference placed in v0.

**Step 2: Prepare the constructor argument**

The string reference is placed in v1.

**Step 3: Call the constructor**

Here:

The constructor initializes the object.

**What about private methods?**

Consider:

class AuthManager {

private boolean validatePassword(String password) {

return password.length() >= 8;

A call to this private method can use invoke-direct.

Illustrative Smali:

invoke-direct {p0, v0}, Lcom/example/AuthManager;->validatePassword(Ljava/lang/String;)Z

move-result v1

Constructors are interesting because sensitive objects and configuration values are often initialized there.

Look for constructors that receive:

invoke-direct {v0, v1}, Lcom/example/ApiClient;->\<init>(Ljava/lang/String;)V

This tells you that a string is passed into the ApiClient constructor. Investigate what the constructor does with that string.

Is it a base URL? An API key? A configuration value? Follow the argument into the constructor and trace its subsequent use.

**Remember:** invoke-direct is not automatically suspicious. It simply identifies a direct method invocation.

**4. invoke-virtual — Calling an Instance Method**

Now let’s explore one of the most common instructions you’ll encounter: invoke-virtual

It is used to invoke an instance method with virtual dispatch. In simple terms, it calls an instance method on an object.

String getName() {

return “Alex”;

Calling the method:

User user = new User();

String name = user.getName();

A simplified Smali representation:

invoke-virtual {v0}, Lcom/example/User;->getName()Ljava/lang/String;

Unlike invoke-static, an instance method requires an object receiver.

**Understanding virtual dispatch**

Imagine a parent class:

class Animal {

void sound() {

System.out.println(“Animal sound”);

And a child class:

class Dog extends Animal {

@Override

System.out.println(“Bark”);

Now:

Animal animal = new Dog();

animal.sound();

Although the reference is declared as Animal, the actual object is a Dog.

Virtual dispatch allows the overridden Dog.sound() implementation to be selected at runtime.

This is one reason why understanding inheritance is important when analysing Android applications.

The method reference you see in a Smali invocation doesn’t always tell the whole story about which implementation executes.

invoke-virtual is particularly useful when tracing application behaviour.

Look for calls involving:

invoke-virtual {v0}, Lcom/example/Session;->getToken()Ljava/lang/String;

You can identify:

Next, open the method implementation.

A method named getToken() might read a field, retrieve a value from storage, or call another method.

Don’t stop at the invocation. Follow the chain.

**5. invoke-interface — Calling an Interface Method**

Now imagine your application uses an interface. An interface defines methods that implementing classes must provide.

interface PaymentProcessor {

boolean processPayment(int amount);

A class implements that interface:

class CardPayment implements PaymentProcessor {

public boolean processPayment(int amount) {

return true;

The application might call:

PaymentProcessor processor = new CardPayment();

boolean result = processor.processPayment(500);

The method is called through the interface reference.

In Smali, this can appear as:

invoke-interface {v0, v1}, Lcom/example/PaymentProcessor;->processPayment(I)Z

Let’s understand the registers:

**Why is this different?**

The caller uses the interface method declaration. The runtime dispatches the call to the appropriate implementation for the actual object.

That means you may need to find which class implements the interface to understand the actual behaviour.

Interfaces are common in applications with layered architecture.

PaymentProcessor

Implemented by

\+ — — CardPayment

\+ — — UpiPayment

\+ — — WalletPayment

A call to PaymentProcessor.processPayment() might lead to different implementations depending on the actual object.

During an audit:

This can be especially useful when reviewing:

**Important:** Finding an interface declaration doesn’t prove that every implementation is used. Trace the object creation and assignment to understand the actual execution path.

**6. invoke-super — Calling a Parent Class Method**

Let’s now look at inheritance.

Suppose we have:

class Parent {

void display() {

System.out.println(“Parent method”);

class Child extends Parent {

super.display();

System.out.println(“Child method”);

The child method calls the parent implementation using:

invoke-super {p0}, Lcom/example/Parent;->display()V

The instruction invokes the appropriate superclass implementation of the method.

**Understanding the example**

Parent

| display()

Child

\+ — — invoke-super

Parent.display()

The important distinction:

Parent classes often contain shared application behaviour.

For example, an Android activity may extend another activity:

class LoginActivity extends BaseActivity {

protected void onCreate(Bundle savedInstanceState) {

super.onCreate(savedInstanceState);

// Login screen setup

A Smali call may look like:

invoke-super {p0, p1}, Lcom/example/BaseActivity;->onCreate(Landroid/os/Bundle;)V

Why should you care?

The parent class might initialize:

If you inspect only LoginActivity, you might miss important behaviour inherited from BaseActivity.

**Bug-hunting lesson:** When a method calls its parent implementation, inspect the parent method too.

**7. Method Parameters — What Information Enters a Method?**

Now that we understand the five invocation types, let’s explore parameters.

A parameter is information passed into a method when it is called.

void login(String username, String password) {

// Authentication logic

The method receives two parameters:

In Smali, parameters are represented through registers.

Remember our earlier chapter about register architecture?

We learned that:

Let’s see this in action.

**Java example**

// Login logic

.method public login(Ljava/lang/String;Ljava/lang/String;)V

.locals 0

\# p0 = this

\# p1 = username

\# p2 = password

return-void

.end method

The method signature is:

login(Ljava/lang/String;Ljava/lang/String;)V

Let’s decode it:

Now imagine the method is called:

invoke-virtual {v0, v1, v2}, Lcom/example/AuthManager;->login(Ljava/lang/String;Ljava/lang/String;)V

Inside the called instance method, those arguments correspond to:

p0 = AuthManager object

p1 = username

p2 = password

The caller’s v registers and the callee’s p registers are different register frames. They are not the same physical registers.

**What about static methods?**

A static method has no implicit this parameter.

static boolean verify(String username, String password) {

.method public static verify(Ljava/lang/String;Ljava/lang/String;)Z

.locals 1

\# p0 = username

\# p1 = password

const/4 v0, 0x1

Notice:

There is no instance receiver occupying p0.

**What about wide parameters?**

Remember long and double occupy two register slots.

void updateBalance(long amount) {

In an instance method, the register layout is conceptually:

p0 = this

p1, p2 = amount

The wide parameter uses two consecutive register slots.

When reading method parameters, always account for the type and width of each parameter.

**8. Return Values — What Information Comes Back?**

Parameters enter a method. Return values leave a method.

Let’s connect this with our previous chapter.

int add(int a, int b) {

.method public static add(II)I

add-int v0, p0, p1

The method receives two integers and returns one integer.

Now look at the caller:

invoke-static {v1, v2}, Lcom/example/Calculator;->add(II)I

move-result v3

The sequence is:

Arguments

Method invocation

Method executes

Return instruction

move-result

Caller receives value

**Return instruction depends on the return type**

Remember: the appropriate move-result instruction must immediately follow the invocation that produces the result.

invoke-virtual {p0}, Lcom/example/AuthManager;->isAuthorized()Z

Do not insert another instruction between the invocation and its corresponding move-result.

**9. Method Signatures — Reading the Complete Method Identity**

Now comes one of the most important concepts in Smali.

A method signature describes:

login(Ljava/lang/String;Ljava/lang/String;)Z

login(

String,

String

)

returns boolean

The method accepts two strings and returns a boolean.

**Common type descriptors**

Examples:

\[I

Integer array.

\[Ljava/lang/String;

String array.

**Understanding complete method references**

Lcom/example/AuthManager;->login(Ljava/lang/String;Ljava/lang/String;)Z

Break it into four pieces:

This complete method reference tells you exactly which class and method the invocation targets.

**Why signatures matter during reverse engineering**

Imagine you find these two methods:

login(Ljava/lang/String;)Z

And:

Both methods are named login. But they have different parameter lists. They are different method signatures. This is called method overloading.

When searching for a method in JADX or Smali, don’t rely only on the method name. Check the complete signature.

**10. The Five Invocation Instructions Side by Side**

Let’s summarize the differences.

A quick memory trick:

There are also range variants, such as:

invoke-static/range {v0 .. v5}, Lcom/example/Helper;->process(IIIIII)V

The /range form passes a consecutive range of registers. It is useful when register numbers or the number of argument words make the ordinary register-list form unsuitable.

You may encounter these variants while examining real APKs.

**11. Bug Hunter Lab: Follow a Login Method Call**

Now let’s put everything together.

Imagine an application contains this Java-like code:

AuthManager auth = new AuthManager();

boolean result = auth.login(username, password);

if (result) {

openDashboard();

A simplified Smali caller might look like:

new-instance v0, Lcom/example/AuthManager;

invoke-direct {v0}, Lcom/example/AuthManager;->\<init>()V

invoke-virtual {v0, v1, v2}, Lcom/example/AuthManager;->login(Ljava/lang/String;Ljava/lang/String;)Z

if-eqz v3, :login\_failed

invoke-virtual {p0}, Lcom/example/Dashboard;->openDashboard()V

:login\_failed

Let’s investigate.

**Step 1: Find the object creation**

The application creates an AuthManager object.

**Step 2: Find the constructor**

**Step 3: Find the login invocation**

This is the important method call.

It passes:

The method returns a boolean.

**Step 4: Capture the return value**

The returned boolean is placed in v3.

**Step 5: Understand the branch**

If v3 is zero, execution jumps to :login\_failed.

If it is nonzero, execution continues to the dashboard call.

**Step 6: Open the implementation**

Now locate:

Investigate:

You have followed the method call from object creation to parameter passing, return value, and control-flow decision.

That’s a complete starting point for a security investigation.

**12. Practical Exercises**

**Exercise 1: Identify the invocation type**

invoke-static {}, Lcom/example/Config;->getVersion()I

Questions:

**Answer:**

**Exercise 2: Understand constructor invocation**

invoke-direct {v0}, Lcom/example/User;->\<init>()V

**Answer:** new-instance creates the object, invoke-direct calls the constructor, and V means the constructor returns no value.

**Exercise 3: Decode a method signature**

Lcom/example/Auth;->verify(Ljava/lang/String;I)Z

Identify:

**Exercise 4: Trace the parameters**

invoke-virtual {v0, v1, v2}, Lcom/example/User;->update(Ljava/lang/String;I)V

What does each register represent?

The method returns void.

**Exercise 5: Follow a returned value**

invoke-static {v0}, Lcom/example/Auth;->check(Ljava/lang/String;)Z

if-eqz v1, :denied

**Answer:** A string reference is passed to check(). It returns a boolean, received in v1. Execution branches to :denied when v1 is zero.

**13. Bug Hunter Checklist**

Whenever you encounter an invoke-\* instruction, ask:

One more important habit:

**Always inspect both sides of a method call.** The caller tells you what information is supplied. The callee tells you what happens to that information.

Together, they reveal the actual data flow.

**# Quick Recap**

In this chapter, we learned five important method invocation instructions:

We also explored:

The most important thing to remember:

**An invocation tells you where execution goes. The method signature tells you what information travels there. The return value tells you what comes back.**

**# Final Thought**

When you first open a Smali file, you might see hundreds of method calls. They may look like unrelated instructions.

But start following them.

One method retrieves a token. Another validates it. Another creates a request. Another sends the request. Another processes the response.

Suddenly, the application stops looking like a collection of random instructions.

It becomes a connected system of decisions and data flows. And that’s exactly what a bug hunter needs to understand.

**Don’t just find the method. Follow the call.**

By — bithowl
