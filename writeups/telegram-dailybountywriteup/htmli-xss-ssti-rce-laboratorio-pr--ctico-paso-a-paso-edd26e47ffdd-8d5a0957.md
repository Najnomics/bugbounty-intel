# HTMLI → XSS → SSTI → RCE — Laboratorio práctico paso a paso

- **Source URL:** https://gorkaaa.medium.com/htmli-xss-ssti-rce-laboratorio-pr%C3%A1ctico-paso-a-paso-edd26e47ffdd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251018160204/https://gorkaaa.medium.com/htmli-xss-ssti-rce-laboratorio-pr%C3%A1ctico-paso-a-paso-edd26e47ffdd?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11136 (id 11136)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔗 HTMLI → XSS → SSTI → RCE — Laboratorio práctico paso a paso

💞 Mi canal de Youtube: Bug Bounty & Pentesting y Hacking Web [https://www.youtube.com/@0xGorka](https://web.archive.org/web/20251018160204/https://www.youtube.com/@0xGorka)

🧠 Aprende en nuestra comunidad de Discord: [https://discord.gg/RNexFUsM](https://web.archive.org/web/20251018160204/https://discord.gg/RNexFUsM)

En el nuevo vídeo del canal analizo un laboratorio práctico donde **encadeno varias vulnerabilidades hasta lograr una ejecución remota de comandos (RCE)**. La cadena es directa: **HTML Injection → XSS → SSTI → RCE**. Aquí te dejo un resumen técnico y didáctico para entender por qué funciona y qué debes fijarte cuando haces bug bounty o pentesting.

*Aviso legal: Todo lo mostrado está en un entorno controlado. No realices pruebas intrusivas en sistemas sin autorización.*


## 🔍 ¿Por qué esta cadena importa?

Cada uno de estos fallos por separado puede parecer de menor impacto si se analiza fuera de contexto. Sin embargo, la **combinación** es lo que convierte un problema en un compromiso completo:

- **HTML Injection (HTMLI)** suele revelar puntos donde la entrada de usuario no se normaliza correctamente. Es una señal: algo en el pipeline de salida está roto.
- **XSS** permite ejecutar código en el navegador de la víctima; sirve como pivot inicial para obtener contexto o forzar acciones.
- **SSTI (Server-Side Template Injection)** eleva el ataque al servidor: plantillas mal gestionadas pueden ejecutar código en el backend.
- **RCE** es el objetivo final: ejecutar comandos en el servidor, obtener shells, leer archivos sensibles.

Entender la progresión lógica entre estas etapas es clave para pensar en cadenas reales, no solo en fallos aislados.

## 🧭 Flujo didáctico del laboratorio (qué hago y por qué)

1. **Detección de HTMLI**

- Busco puntos donde la entrada se refleja en HTML sin escapar.
- Anoto parámetros, rutas y contextos (atributos, texto, atributos JS).

1. **Pivot a XSS**

- Aprovecho la reflexión para insertar payloads que ejecuten JS en el navegador.
- Uso XSS para obtener cookies, tokens o para forzar requests desde el navegador de un usuario (CSRF-like).

1. **Búsqueda de SSTI**

- Revisando respuestas y comportamiento del backend, busco plantillas que procesen datos del usuario.
- Pruebo cargas que puedan ser interpretadas por motores de templates (por ejemplo Jinja2, Twig, etc.).

1. **Explotación SSTI → RCE**

- Una SSTI bien explotada puede permitir evaluar expresiones en el servidor.
- Construyo payloads que llamen funciones del runtime (p. ej. subprocess en Python) para ejecutar comandos remotos en el entorno aislado.

1. **Control y seguridad**

- Mantengo la explotación en modo controlado (comandos no destructivos) y documentando cada paso.
- Evito acciones que dañen datos o infraestructuras reales.

## 🧰 Técnicas y recursos prácticos que muestro en el vídeo

- Cómo identificar contextos vulnerables (atributo HTML, text node, JS eval).
- Payloads de XSS básicos para pivotar reconnaissance desde el navegador.
- Heurísticas para detectar SSTI según el motor de templates y su sintaxis.
- Construcción gradual de un payload SSTI que permita ejecución limitada y posterior escalado.
- Buenas prácticas al probar RCE en laboratorios: comandos seguros, registros y limpieza.

## ⏱️ Capítulos del vídeo (para que vayas directo a lo que te interesa)

00:00 INTRO

00:27 Laboratorio

00:50 HTMLI

01:10 XSS

02:15 SSTI

04:18 RCE

📺 Mira el vídeo completo aquí: [https://youtu.be/nOX7HoCiqmM](https://web.archive.org/web/20251018160204/https://youtu.be/nOX7HoCiqmM)

## 🎯 ¿Para quién es este contenido?

- Hunters que quieren ver cómo se encadenan vectores hasta llegar a RCE.
- Pentesters que buscan un walkthrough práctico y razonado.
- Estudiantes de seguridad web que quieran interiorizar la lógica ofensiva (no solo payloads).

Si valoras entender **por qué** se elige una técnica en cada paso y cómo pivotar con criterio, este laboratorio está hecho para ti.

## ✅ Conclusión práctica

No busques solo fallos aislados. Aprende a **leer el flujo**: una pequeña HTMLI puede ser la primera pista que te lleve, con paciencia y razonamiento, a un RCE. La clave está en la mentalidad ofensiva: ver las dependencias entre capas, probar con lógica y encadenar pruebas de forma escalonada.

💬 ¿Te gustaría un vídeo adicional con las payloads comentadas o un tutorial sobre SSTI en distintos motores de templates? Dímelo en los comentarios o en la comunidad.

#BugBounty #SSTI #RCE #XSS #HTMLI #ExploitDev #Laboratorio #HackingEtico #Ciberseguridad #WebSecurity #InfoSec #0xGorka #GorkaElBochiMorillo
