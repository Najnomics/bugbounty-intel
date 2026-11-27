# Bypass Android Applications Debug and Root Detection via debugger.

- **Source URL:** https://medium.com/@shubhamsonani/hacking-with-precision-bypass-techniques-via-debugger-in-android-apps-27fd562b2cc0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260220014420/https://medium.com/@shubhamsonani/hacking-with-precision-bypass-techniques-via-debugger-in-android-apps-27fd562b2cc0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4250 (id 4250)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Bypass Android Applications Debug and Root Detection via debugger.**

Hi Everyone,

I was going through OWASP [*MASTG*](https://github.com/OWASP/owasp-mastg/releases) for Android/iOS pentesting techniques. For learning Android/iOS pentesting, one can refer to this e-book. While reading, I came up with debug techniques to bypass root detection or modify the hidden variables.

Other Interesting Blogs -

## ***What is Debugging and how it helps in security testing?***

Debugging means finding and fixing errors, commonly known as “bugs,” in software, systems, or mobile apps to make them work correctly. It is a tiring process, needs focus and requires a great amount of patience. For developers, a normal bug which affects other lines of code, uses debuggers to stop the execution of the program, analyze variable values, execute line of code step by step, set breakpoints and can modify the values during runtime. Hence, it helps to solve the error or bug that affects other lines of code. Now, you can think this can bring malicious practices from the perspective of hackers.

*Bypass the debug and root detection of application.*

*Continuing….*

I was seeing debug technique to bypass root detection of an android application — *Uncrackable1*. This application implements protection against debugging and root detection.

*Tools -*

1. Android Studio — 3.6 (for best and easiest approach)
2. [APK-Gui Tool](https://github.com/AndnixSH/APKToolGUI) — for decompiling and recompiling the application.
3. Any android emulator

*In the book, this caught my eye.*

Now, the application was allowing me to bypass root detection, but I was not able to bypass debug message from the application. Once the user clicks “OK”, the application exits. I tried various methods and did research for multiple days, and the result was null. But one variable got my attention and then I was able to bypass the debug and root protection.

Let’s Bypass -

*Note — I will be showing 2 methods. First is detailed method to see what and which variables or values are called and second is fast-paced method.*

Step 1 — Decompile the APK using APK-GUI tool. Edit the *android-manifest* file and add *android:debuggable=true,* to make the application debuggable. Recompile, sign and zipalign the application.

Step 2 — Install the application via -

*adb install \<application\_name>.*

Step 3 — Get the package name using *-*

***adb shell pm list packages –3*** (to list the 3rd party applications.

Step 4 — Now make the application wait for debugger via this command — ***adb shell am setup-debug-app –w \<package\_name>***.

**Note —** You will require to run this command every time, before you start the application, so that application waits for debugger.

To make it persistent you can use –

*adb shell am setup-debug-app –w -–persistent \<package\_name>.*

To clear all the flags –

*adb shell am clear-debug-app \<package\_name>.*

Step 5 — Open the ***Android Studio -> File -> Open Profile or APK*** -> Open the recompiled APK.

Step 6 — Add breakpoints to the java files as mentioned below.

- ***MainActivity.java — onCreate method, b.java, ContextWrapper.java***

This method checks for root and debug detection. There are few conditional checks -

1\. ***c.a() / c.b() / c.c()*** — method checks if the device contains “***su***” binary or “***su***” file access. If the application can find these files, then the condition will return ***true*** which will trigger ***root detection*** alert dialog.

2\. ***b.a(getApplicationContext())*** — method gets the ***applicationInfo*** class and it contains various properties and methods to manage and retrieve information about an APK. If the application contains the debug property which it retrieves from ***android-manifest*** file and it will return true, which again will trigger the alert box.

3\. ContextWrapper.java — will return the ***applicationInfo*** value with its properties and configuration.

## ***Now real hectic work begins….***

Now open the application and it should show “***wait for debugger***”. Connect android studio debugger with the current process of the application and the application should pause at ***ContextWrapper.java*** file *-> getApplicationContext()* method*.*

*Before proceeding two things to understand -*

*a. In b.java file -*

*Method “a” is used to access application-specific resources and information.*

*Then it gets the application specific flags mentioned in applicationInfo file. Then android system will combine all the flags (Binary Bits) and change it to the decimal value and perform “AND” operator with “0x2” which is 2 in decimal value. This method returns true if the binary bit contains 2 and if it contains then it will return TRUE which will not allow user to access the application.*

*b. Buttons used in the debug console.*

*→ Step-over -> move to next method.*

*→ Step into -> move inside the function or method.*

*→ Force step into -> list all variables and classes names once inside the method or function.*

*→ Step out -> if not needed then exit out of the function.*

*NOTE — you can use terminal to connect with JDB (Java Debugger). Java application uses JDWP (JAVA DEBUG WIRE PROTOCOL) for debugging. But, in windows JDB doesn’t work properly as expected, so my best call was to use IDE and the same I will suggest.*

So, when the application starts and android-studio’s debugger is attached to the application, initially it will check if debugging value is set in ***android-manifest*** file. So as said above, in the debugger we can see the flag value in decimal.

Step 1 — Under the variable section of the debugger console, navigate to “***this mLoadedAPK -> mApplicationInfo -> flags = 814267974***”

*Note: flags = 814267974 in binary bits is 11000011100111011110. This means “Flag\_debuggable” is set.*

Step 2 — Change the flag value to 814267972. Binary bits conversion — 110000101101000000100010100.

*Note — If the android device is not rooted, the values will be different. Just subtract 2 from whatever the value you are seeing in flags variable, as condition will perform AND operation with 2.*

Step 3 — Click “***Force Step In***” and then “***Step Out***” button 3 times to reach to ***onCreate()*** method. Once reached, click “***Force Step Into***” to enter the ***onCreate*** method.

Step 4 — First, “***Step Out***” -> “***Force Step In***” -> “***Step Out***” -> “***Force Step In***”. You will reach where application will check for “***su***” binary. Change the value to “***notsu***”.

Step 5 — After changing the value of “***child***” local variable -> ***Force Step In -> (Step Out) x 2 times -> Force Step In***. Repeat this for 17–18 times. You will get a similar console view.

Step 6 — ***Force Step In -> Step Out -> (Force Step In) x 2 times***.

Step 7 — ***(Step out -> Force Step In) X 14 times.*** This will skip the ***For Loop*** which contains list of ***root directory paths*** and check if that path exists in the device. This is the bypass for **root detection** check.

Step 8 — ***Force Step In***. Navigate to this -> ***mActivityInfo -> applicationInfo -> flags = 814267974***. Modify the current value as mentioned before.

Step 9 — ***Force step in -> Force Step In -> Step Out -> Force Step In -> Force Step In***. You will reach to condition where ***debug method*** is checked. Check whether the modified value is present or not by navigating to “***ContextImpl.getApplicationContext() -> mApplicationinfo”***.

Step 10 -> ***Force Step In -> Step Out -> Force Step In -> Step Out***. Check again the modified value is present or not.

Step 11 -> ***Step Out -> Force Step In -> Force Step In.*** Release the debugger.

## Now, we have successfully bypassed the root and bypass detection and can access the application.

**SECOND METHOD —**

Step 1 — Connect the android studio debugger and attach the breakpoints as mentioned above. If everything goes right, you will reach to this type of debug console.

Step 2 — Expand the right drop box, navigate to ***mApplicationInfo*** and in it set the ***flags*** value from “814267974” to “814267972”.

*Note — If the android device is not rooted, the values will be different. Just subtract 2 from whatever the value you are seeing in flags variable, as condition will perform AND operation with 2.*

Step 3 — Click “S***tep Out***” until you reach to ***onCreate*** method.

Step 4 — Click “***Force Step In -> Step Out -> Force Step In -> Step Out***” until you reach to “***su***” binary checks. Change the value to “***notsu***”

Step 5 — Click “***Step Out -> Step Out -> Force Step In***” until you reach to second checks.

Step 6 — Again, “***Step Out -> Step Out -> Force Step In***”, this will skip the method and you can save some time. The debug console then will reach to 3rd condition for checking if android device has “***su/root***” directories.

Step 7 — Again, “***Step Out -> Step Out -> Force Step In***”, this will reach to “***debug***” checks. Click “***Force Step In***”, expand “***mPackageInfo -> mApplicationInfo -> flags”*** for checking the modified flags value.

Step 8 -> For final verification, again “***Step Out -> Force Step In***”. Expand the right panel and find “***flags under mApplicationInfo***”. Check the value and release the debugger, you will be able to bypass both the detection i.e root and debug detection.

Thank you for reading this blog. Happy Hacking!!
