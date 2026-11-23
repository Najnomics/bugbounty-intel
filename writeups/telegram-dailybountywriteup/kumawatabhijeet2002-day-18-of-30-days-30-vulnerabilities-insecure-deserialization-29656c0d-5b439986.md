# Day 18 of 30 Days — 30 Vulnerabilities | Insecure Deserialization

- **Source URL:** https://medium.com/@kumawatabhijeet2002/day-18-of-30-days-30-vulnerabilities-insecure-deserialization-29656c0d212a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240913110358/https://medium.com/@kumawatabhijeet2002/day-18-of-30-days-30-vulnerabilities-insecure-deserialization-29656c0d212a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7088 (id 7088)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 18 of 30 Days — 30 Vulnerabilities | Insecure Deserialization

**Day 18: Mastering Insecure Deserialization Vulnerability — Essential Tricks & Techniques Based on Personal Experience and Valuable POCs**

\[ In collaboration with Sunil Kumawat( his [LinkedIn](https://www.linkedin.com/in/sunill-kumawat/) | [Twitter](https://x.com/it4chis3c))\]

Hey geeks, **Abhijeet (**[Twitter](https://x.com/AbhijeetKumaw10)) here with one more write-up on tricks & tips to detect **Insecure Deserialization Vulnerability**.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

**First** of all you must know about Serialization & Deserialization process in programming to better understand the mechanics behind Insecure Deserialization Vulnerability. I had written not in-depth but essentials that you must be exposed to before hunting for Insecure Deserialization Vulnerability. If you already know about these concepts, you can move directly to the “**Where to Detect**” Section.

# How Serialization & De-serialization Works?

**Serialization** and **deserialization** are processes used in programming to convert data structures or objects into a format that can be stored, transmitted, and reconstructed later.

# Serialization:

- **Definition:** Serialization is the process of converting an object’s state (including its data and sometimes its behavior) into a byte stream or another data format, such as JSON, XML, or binary, that can be easily stored or transmitted.
- **Purpose:** The main goal of serialization is to save the state of an object so that it can be recreated later or sent over a network to another system or application.

**Example Use Cases:**

- **Persistence:** Storing an object in a file or a database.
- **Communication:** Sending objects over a network between different components of a distributed system.
- **Caching:** Storing objects in cache memory for quicker retrieval.

# Deserialization:

- **Definition:** Deserialization is the reverse process of serialization. It involves reconstructing an object from its serialized form (byte stream or data format) back into a live object in memory, restoring its original state and structure.
- **Purpose:** Deserialization allows a system to recreate and use objects that were previously stored or transmitted.

**Example Use Cases:**

- **Data Retrieval:** Loading stored data from a file or database and converting it back into usable objects.
- **Message Processing:** Receiving a serialized object from a network and converting it back into a usable format within the application.

# How They Work:

1. **Serialization Process:**

- **Object Creation:** An object is created in the application.
- **Conversion:** The object’s data and structure are converted into a format suitable for storage or transmission (e.g., binary, JSON, XML).
- **Output:** The serialized data is saved to a file, database, or transmitted over a network.

**2. Deserialization Process:**

- **Input:** The serialized data is retrieved from storage or received over a network.
- **Conversion:** The data is parsed and converted back into the original object’s structure.
- **Object Reconstruction:** The object is re-created in memory, ready for use in the application.

# Example in Different Programming Languages:

- **Java:** Uses `ObjectOutputStream` for serialization and `ObjectInputStream` for deserialization.
- **Python:** Uses `pickle` module for both serialization (`pickle.dump`) and deserialization (`pickle.load`).
- **.NET:** Uses `BinaryFormatter` for binary serialization and deserialization.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# Moving forward to hunt for Insecure Deserialization Vulnerability

# 1. Brief Description

- **Definition**: Insecure deserialization occurs when untrusted data is used to abuse the logic of an application, inflict denial-of-service (DoS) attacks, or even execute arbitrary code when deserialized.
- **Impact**: Can lead to remote code execution (RCE), privilege escalation, and other severe security breaches.
- **Examples**: Applications using JSON, XML, or binary serialization formats that fail to validate input properly.

# 2. Where to Detect

**Entry Points**:

- Web applications that accept serialized objects (e.g., cookies, API data).
- Applications using serialized data from untrusted sources.

**Common Locations**:

- **Session tokens**: Often serialized for user session management.
- **API requests**: Where data is transferred in serialized formats.
- **Inter-process communication**: Data shared between different processes in serialized form.

**Technologies to Watch**:

- **Programming languages**: Java, PHP, Python, Ruby.
- **Frameworks**: Spring, .NET, Ruby on Rails.

# 3. How to Detect

**Static Analysis**:

- **Code Review**: Look for deserialization functions, especially in places where user input is accepted.
- **Identify Libraries**: Spot libraries prone to insecure deserialization (e.g., `java.io.ObjectInputStream` in Java).

**Dynamic Analysis**:

- **Fuzzing**: Inject modified serialized objects to observe application behavior.
- **Monitoring**: Look for anomalies like exceptions or crashes during deserialization.

**Automated Tools**:

- **Burp Suite**: Deserialization scanner plugin.
- **OWASP ZAP**: Use the active scan rules.

# 4. Basic & Advanced Payloads

**Basic Payloads**:

- **Java**: Inject malicious Java objects.
- **PHP**: Inject serialized PHP objects with embedded shell commands.

**Advanced Payloads**:

- **Java**: Exploit known vulnerabilities in libraries like Commons Collections or Spring.
- **PHP**: Use `__wakeup` or `__destruct` methods to execute arbitrary PHP code.

**Language-Specific Payloads**:

- **.NET**: Inject payloads using BinaryFormatter or DataContractSerializer.
- **Python**: Exploit `pickle` deserialization by injecting malicious objects.

# 5. Defense Bypass Techniques

**Common Defenses**:

- **Input Validation**: Strictly validate all incoming serialized data.
- **Use Whitelists**: Restrict deserialization to trusted classes only.
- **Disable Deserialization**: Where possible, avoid deserialization entirely.

**Bypass Techniques**:

- **Object Tampering**: Modify objects to bypass whitelisting mechanisms.
- **Class Manipulation**: Alter class names or signatures to bypass restrictions.
- **Payload Obfuscation**: Hide malicious payloads in seemingly benign objects.

# 6. POC Section

# POC 1: Java Insecure Deserialization via Custom Deserialization Method

**A. Description:** This POC demonstrates an insecure deserialization vulnerability in a Java application where a malicious object can be serialized and deserialized, leading to arbitrary code execution. The vulnerability exists in a deserialization method that does not properly validate the object being deserialized.

**B. Steps to Reproduce:**

1. **Create a Malicious Object:**

- Develop a Java class (`VulnObj`) with a `readObject` method that executes a system command (`Runtime.getRuntime().exec("command");`).
- Serialize the `VulnObj` object using `ObjectOutputStream` and save it as a file (`vulnObj.serial`).

**2. Inject the Malicious Payload:**

- Copy the serialized file to the target system where the vulnerable Java application expects a serialized object.
- Replace the expected serialized file with the malicious `vulnObj.serial`.

**3. Trigger the Deserialization:**

- Run the vulnerable Java application, which reads the serialized file and deserializes the object.
- Observe that the command in `VulnObj` is executed upon deserialization.

**C. Impact:** Successful exploitation allows an attacker to execute arbitrary commands on the target system, leading to a complete compromise of confidentiality, integrity, and availability([thehackerish](https://thehackerish.com/insecure-deserialization-explained-with-examples/) | [PortSwigger](https://portswigger.net/web-security/deserialization)).

# POC 2: PHP Object Injection via Uncontrolled Deserialization

**A. Description:** This POC showcases a PHP object injection vulnerability, where user-controlled data is passed to the `unserialize()` function, leading to the execution of arbitrary code through a crafted payload.

**B. Steps to Reproduce:**

1. **Identify the Vulnerability:**

- Analyze the PHP code to identify instances where user input is passed directly to the `unserialize()` function.

**2. Craft the Payload:**

- Create a serialized PHP object that includes a malicious payload. For example, you can serialize an object with an `__destruct` magic method that includes malicious code.
- Example serialized string: `O:1:"A":1:{s:5:"value";s:25:"system('id');";}`.

**3. Exploit the Vulnerability:**

- Submit the serialized payload via the vulnerable input field.
- The application will deserialize the object, triggering the `__destruct` method and executing the injected code.

**C. Impact:** Exploitation can result in arbitrary code execution on the server, leading to potential data exfiltration, server compromise, or denial of service([thehackerish](https://thehackerish.com/insecure-deserialization-explained-with-examples/) | [PortSwigger](https://portswigger.net/web-security/deserialization))

# POC 3: .NET Insecure Deserialization using JSON Formatters

**A. Description:** This POC demonstrates insecure deserialization in a .NET application where JSON data is deserialized without proper validation, allowing an attacker to exploit the `ObjectDataProvider` class to execute arbitrary code.

**B. Steps to Reproduce:**

1. **Craft the Malicious JSON Payload:**

- Create a JSON payload that leverages the `ObjectDataProvider` class to execute a command:

```
{
  "__type": "System.Windows.Data.ObjectDataProvider, PresentationFramework",
  "MethodName": "Start",
  "ObjectInstance": {
    "__type": "System.Diagnostics.Process, System",
    "StartInfo": {
      "FileName": "cmd.exe",
      "Arguments": "/c calc.exe"
    }
  }
}
```
2\. **Inject the Payload:**

- Send the crafted JSON payload to the vulnerable endpoint of the .NET application that deserializes JSON data.

**3. Trigger the Vulnerability:**

- The application deserializes the JSON data and executes the command specified in the `ObjectDataProvider`, launching the calculator application as a demonstration.

**C. Impact:** By exploiting this vulnerability, an attacker can execute arbitrary code on the server, leading to a complete system compromise. The impact depends on the privileges of the application running the vulnerable code([thehackerish](https://thehackerish.com/insecure-deserialization-explained-with-examples/) | [PortSwigger](https://portswigger.net/web-security/deserialization))..

# 7. Conclusion

**Summary**: Insecure deserialization is a critical vulnerability that can lead to severe security breaches if not properly managed.

**Best Practices**:

- **Avoid Deserialization**: If possible, avoid deserialization altogether.
- **Implement Strong Validation**: Always validate and sanitize data before deserializing.
- **Use Secure Libraries**: Employ libraries known for secure deserialization practices.

**Final Thought**: Stay updated with the latest vulnerabilities and patches related to deserialization in the technologies you use.

…………………………………………………………………………………………………

Thank you for reading the blog!!!

You can also follow me on [Twitter](https://x.com/AbhijeetKumaw10) & [LinkedIn](https://www.linkedin.com/in/abhijeet-kumawat-a6b019230/) for more write-ups

**Follow & subscribe for daily write-up updates via mail on Medium**

**Stay tuned for Day 19, where we’ll dive into another vulnerability!**

…………………………………………………………………………………………………
