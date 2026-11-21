# Bug Bounty Broken Access Control

- **Source URL:** https://gorkaaa.medium.com/bug-bounty-broken-access-control-la-vulnerabilidad-que-abre-m%C3%A1s-puertas-de-las-que-imaginas-52ede8b6bc4a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250830223146/https://gorkaaa.medium.com/bug-bounty-broken-access-control-la-vulnerabilidad-que-abre-m%C3%A1s-puertas-de-las-que-imaginas-52ede8b6bc4a
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10861 (id 10861)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty Broken Access Control: la vulnerabilidad que abre más puertas de las que imaginas

💞 **Si quieres contenido REAL de bug bounty**, no te puedes perder mi canal de YouTube: [https://www.youtube.com/@0xGorka](https://www.youtube.com/@0xGorka)

El **Broken Access Control** (BAC) es una de las vulnerabilidades más frecuentes y críticas en bug bounty.

Se produce cuando una aplicación no valida correctamente qué usuario puede acceder a qué recurso.

👉 Dicho de otra forma: el sistema te deja entrar a lugares donde **no deberías estar**.

En este artículo te explico cómo identificarlo, ejemplos prácticos y comandos útiles para tu investigación.

## 🧩 ¿Qué es exactamente Broken Access Control?

Es un fallo en la lógica de permisos.

Aunque el usuario no tenga privilegios, el sistema **no verifica bien su rol** y permite acciones indebidas.

Ejemplos:

- Un usuario normal accediendo a un panel de administrador.
- Un IDOR que deja ver los datos de otro cliente cambiando el parámetro user\_id=123.
- Modificar una petición para ejecutar acciones restringidas.

## 🛠️ Metodología para detectarlo

## 1. Mapear roles y permisos

Hazte preguntas clave:

- ¿Qué ve un usuario anónimo?
- ¿Qué ve un usuario autenticado?
- ¿Qué debería ver un admin?

## 2. Probar manipulación de parámetros

Endpoints como:

`GET /api/user/12345`
Cámbialo a:

`GET /api/user/12346`
Si devuelve datos de otro usuario → tienes un **IDOR** (Insecure Direct Object Reference).

## 3. Reutilizar peticiones con tokens distintos

Intercepta con BurpSuite y cambia cookies o JWT de un usuario por las de otro.

Si aún así accedes → **Broken Access Control** confirmado.

## 4. Jugar con métodos HTTP

Algunas veces:

`GET /admin`
bloquea…

pero

`POST /admin`
o

`PUT /admin`
funcionan.

## 5. Revisar el “front” contra el “back”

Muchos desarrolladores **ocultan botones en la interfaz**, pero no protegen la lógica en el backend.

👉 Lo que no aparece en el panel, puede seguir siendo accesible vía request directa.

## 📂 Ejemplo práctico

Un sitio tiene:

`https://target.com/api/deleteUser?id=42`
- Usuario normal: **no debería** poder borrar a nadie.
- Si al interceptar la petición con Burp puedes borrar usuarios → acceso roto.

Impacto: escalada de privilegios y control sobre cuentas ajenas.

## 📌 Cómo reportarlo

Un buen informe de Broken Access Control incluye:

- **Contexto**: qué usuario/rol usaste.
- **Pasos reproducibles**: petición interceptada, parámetro modificado, respuesta del servidor.
- **Impacto**: acceso a datos sensibles, acciones administrativas, manipulación de recursos.
- **Recomendación**: (en bug bounty no siempre obligatorio, pero ayuda) → validación de permisos en backend.

## 🧭 Reflexión final

El Broken Access Control no suele necesitar payloads sofisticados ni fuzzing avanzado.

Necesita **mentalidad analítica**: pensar como un usuario que intenta colarse por las grietas de la lógica.

👉 Recuerda: la seguridad no es solo autenticarse, es **validar que cada acción corresponde al rol correcto**.

#BugBounty #BrokenAccessControl #Ciberseguridad #InfoSec #BugBountyHunter #Pentesting #HackingEtico
