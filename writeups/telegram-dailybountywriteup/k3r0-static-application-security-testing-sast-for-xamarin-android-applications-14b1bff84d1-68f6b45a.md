# Static Application Security Testing (SAST) for Xamarin Android Applications

- **Source URL:** https://medium.com/@k3r0/static-application-security-testing-sast-for-xamarin-android-applications-14b1bff84d14?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250309033945/https://medium.com/@k3r0/static-application-security-testing-sast-for-xamarin-android-applications-14b1bff84d14
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9000 (id 9000)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Static Application Security Testing (SAST) for Xamarin Android Applications**

# Introduction

Android applications come in various frameworks, including Flutter, Xamarin, Cordova, React Native, and more. In this article, I will walk you through a Static Application Security Testing (SAST) approach for a Xamarin Android application by solving an HTB challenge.

# Initial Analysis

Upon launching the application, I noticed an input field that accepts a password and validates it. Entering any random password resulted in an error message.

# Examining the APK

By analyze the application further, I decompiled the APK using JADX.

I found a basic `AndroidManifest.xml` file.

However, searching for the validation logic in the source code did not yield immediate results. Instead, I observed multiple files and folders related to Xamarin.

# Understanding Xamarin.Android Architecture

Xamarin.Android allows developers to build Android applications using C# .NET. The C# code is compiled into Intermediate Language (IL), which is then Just-In-Time (JIT) compiled to a **native assembly** when the application lucnch. Below is a rough architecture of Xamarin.Android:

- Xamarin provides .NET bindings to `Android.*` and `Java.*` namespaces.
- Applications run under the Mono execution environment alongside the Android Runtime (ART).
- Managed Callable Wrappers (MCW) and Android Callable Wrappers (ACW) facilitate communication between the Mono and ART environments.

# Locating the Application Logic

Since the application logic is compiled into native libraries, I needed to find these files. Using `apktool`, I discovered the `.dll` files under `/unknown/assemblies`. With JADX, they were found in `resources/assemblies/` :

Note: The challenge name is *SeeTheSharpFlag*, hinted at investigating `SeeTheSharpFlag.dll`.


After downloading the file, I used the *file****Sony PlayStation Audio*** file.

To analyze further, I ran the `xxd` command and identified a file signature corresponding to `XALZ`, which is a compressed format used in .NET applications.

I then used the `xamarin-decompress` tool to decompress the library using LZ4 block: [https://github.com/NickstaDB/xamarin-decompress](https://github.com/NickstaDB/xamarin-decompress)

After decompression, running the `file` command again revealed it as a Portable Executable 32-bit (PE32) file.

I then opened the file using **dotPeek**, it was a .NET decompiler tool.

# Extracting the Password Validation Logic

Upon inspecting `SeeTheSharpFlag.dll` in dotPeek, I found a `MainPage` class containing a method named `Button_Clicked()`, which likely handles password validation.

## Here’s the extracted function:

```
private void Button_Clicked(object sender, EventArgs e)
    {
      byte[] buffer = Convert.FromBase64String("sjAbajc4sWMUn6HJBSfQ39p2fNg2trMQ/MmTB5mno=");
      byte[] rgbKey = Convert.FromBase64String("6F+WzEp5QXoJV+iTli4Q==");
      byte[] rgbIV = Convert.FromBase64String("DZ6YaWJlZ26VmEEQ31A==");
      using (AesManaged aesManaged = new AesManaged())
      {
        using (ICryptoTransform decryptor = aesManaged.CreateDecryptor(rgbKey, rgbIV))
        {
          using (MemoryStream memoryStream = new MemoryStream(buffer))
          {
            using (CryptoStream cryptoStream = new CryptoStream((Stream) memoryStream, decryptor, CryptoStreamMode.Read))
            {
              using (StreamReader streamReader = new StreamReader((Stream) cryptoStream))
              {
                if (streamReader.ReadToEnd() == ((InputView) this.SecretInput).Text)
                  this.SecretOutput.Text = "Congratz! You found the secret message";
                else
                  this.SecretOutput.Text = "Sorry. Not correct password";
              }
            }
          }
        }
      }
    }
```
From this code, we can see that the application uses AES encryption to validate the password through this line:

`if (streamReader.ReadToEnd() == ((InputView) this.SecretInput).Text)`
Also The decryption keys are hardcoded in the application, making it possible to decrypt the expected password.

```
byte[] buffer = Convert.FromBase64String("sjAbajc4sWMUn6HJBSfQ39p2fNg2trMQ/MmTB5mno=");
byte[] rgbKey = Convert.FromBase64String("6F+WzEp5QXoJV+iTli4Q==");
byte[] rgbIV = Convert.FromBase64String("DZ6YaWJlZ26VmEEQ31A==");
```
# Decrypting the Password

The AES encryption used in the application employs **CBC mode** with Base64-encoded components. 

Below is a Python script to decrypt the expected password:

```
import base64
from Crypto.Cipher import AES
def decrypt_aes_cbc(ciphertext_b64, key_b64, iv_b64):
    ciphertext = base64.b64decode(ciphertext_b64)
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    pad_len = decrypted[-1]
    decrypted = decrypted[:-pad_len]
    return decrypted.decode()
ciphertext_b64 = "sjAbajc4sWMUn6HJBSfQ39p2fNg2trMQ/MmTB5mno="
key_b64 = "6F+WzEp5QXoJV+iTli4Q=="
iv_b64 = "DZ6YaWJlZ26VmEEQ31A=="
plaintext = decrypt_aes_cbc(ciphertext_b64, key_b64, iv_b64)
print("========================")
print("==== Decrypted text:", plaintext)
print("========================")
```
# Extracting the Flag

Running the script successfully decrypted the flag.

I then submitted it through the mobile app and received the Congratz message.

# Conclusion

This challenge demonstrated how to analyze and reverse-engineer Xamarin applications using SAST techniques. By understanding Xamarin’s architecture and extracting native libraries.

For further reading, I highly recommend **Akshay Shinde’s** blog post on [Xamarin Reverse Engineering](https://www.appknox.com/blog/xamarin-reverse-engineering-a-guide-for-penetration-testers).

Happy hacking! 🚀

THANKS FOR READING ❤️

*If you want to connect with me, feel free to reach out to me on LinkedIn*
