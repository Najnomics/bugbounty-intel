# Bug Bounty

- **Source URL:** https://gorkaaa.medium.com/bug-bounty-de-htmli-a-rce-gu%C3%ADa-pr%C3%A1ctica-y-paso-a-paso-d6d499c8ef68?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251006062752/https://gorkaaa.medium.com/bug-bounty-de-htmli-a-rce-gu%C3%ADa-pr%C3%A1ctica-y-paso-a-paso-d6d499c8ef68
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11171 (id 11171)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔥 Bug Bounty: De HTMLI a RCE — Guía práctica y paso a paso

💞 Mira el vídeo completo: [https://www.youtube.com/watch?v=nOX7HoCiqmM](https://www.youtube.com/watch?v=nOX7HoCiqmM)

En el vídeo del canal analizo un laboratorio práctico donde encadeno varias vulnerabilidades hasta conseguir una **ejecución remota de comandos (RCE)**. La cadena es clara: **HTML Injection → XSS → SSTI → RCE**. Aquí tienes un resumen técnico y accionable para entender por qué funciona y cómo pensar cuando te enfrentas a estas combinaciones en bug bounty o pentesting.

*Aviso legal: Todo lo mostrado está en un entorno controlado. No realices pruebas intrusivas en sistemas sin autorización.*


## 🔎 Por qué esta cadena tiene sentido

Una vulnerabilidad aislada suele parecer “limitada”. El verdadero poder ofensivo aparece cuando entiendes **cómo conectar puntos**:

- **HTML Injection (HTMLI)** revela que la entrada del usuario se refleja sin normalizar. Es una pista de que el pipeline de salida falla.
- **XSS** te permite ejecutar código en el navegador de la víctima: perfecto para pivotar, obtener contexto o forzar acciones desde el cliente.
- **SSTI** eleva la inyección al servidor: plantillas mal saneadas pueden ejecutar expresiones en el runtime del servidor.
- **RCE** es el objetivo final: ejecutar comandos en la máquina objetivo, obtener shells o acceder a datos sensibles.

Entender la progresión lógica entre estas etapas transforma hallazgos “pequeños” en compromisos reales.

## 🧭 Flujo práctico (qué hago y por qué)

1. **Detectar HTMLI**

- Buscar entradas que se reflejan en HTML sin escape.
- Identificar el contexto (atributo, text node, etc.) y anotar parámetros.

1. **Pivotar a XSS**

- Insertar payloads ligeros para confirmar ejecución de JS.
- Usar XSS para recolectar información del navegador, cookies o forzar peticiones desde el contexto de un usuario legítimo.

1. **Buscar SSTI**

- Observar respuestas y comportamiento del backend: ¿se evalúan plantillas?
- Probar payloads que coincidan con la sintaxis de motores comunes (Jinja2, Twig, etc.).

1. **Explotar SSTI → RCE**

- Construir payloads que permitan evaluar funciones del runtime (ej. subprocess, os.system, etc.).
- Escalar paso a paso, usando comandos seguros y limitados antes de intentar shells interactivos.

1. **Control y seguridad**

- Ejecutar comandos no destructivos. Registrar todo y limpiar artefactos del lab.

## 🧰 Técnicas y heurísticas claves que muestro

- Detección de contextos vulnerables en HTML.
- Payloads XSS para pivot y reconnaissance desde navegador.
- Heurísticas para identificar motor de templates y su sintaxis.
- Construcción gradual del payload SSTI (de pruebas seguras a ejecución limitada).
- Buenas prácticas al probar RCE en laboratorio (comandos seguros, rollback, logging).

## ⏱ Capítulos (ve al bloque que te interesa)

00:00 INTRO

00:27 Laboratorio

00:50 HTMLI

01:10 XSS

02:15 SSTI

04:18 RCE

🎯 Para quién es esto

- Hunters que desean aprender a encadenar vectores hasta llegar a RCE.
- Pentesters que buscan walkthroughs reproducibles y razonados.
- Estudiantes que prefieren comprender la lógica ofensiva, no solo copiar payloads.

## ✅ Conclusión práctica

No busques solo fallos aislados. Aprende a **leer el flujo**: una HTMLI puede ser la pista que, con paciencia y criterio, te lleve a un RCE. La diferencia entre lanzar payloads y explotar con criterio está en la mentalidad: mapear dependencias entre capas, probar con método y escalar de forma controlada.

💬 ¿Quieres que publique las payloads comentadas en detalle o un tutorial sobre SSTI en motores específicos (Jinja2, Twig, etc.)? Dímelo en los comentarios o pásate por la comunidad.

💞 Mi canal de Youtube: Bug Bounty & Pentesting y Hacking Web [https://www.youtube.com/@0xGorka](https://www.youtube.com/@0xGorka)

🧠 Aprende en nuestra comunidad de Discord: [https://discord.gg/Dkq6924asp](https://discord.gg/Dkq6924asp)

#BugBounty #SSTI #RCE #XSS #HTMLI #ExploitDev #Laboratorio #HackingEtico #WebSecurity #InfoSec #0xGorka #GorkaElBochiMorillo
