# ️ Charla + laboratorio

- **Source URL:** https://gorkaaa.medium.com/%EF%B8%8F-charla-laboratorio-c%C3%B3mo-se-encontr%C3%B3-un-idor-real-hackerone-y-c%C3%B3mo-mitigarlo-5ebbe8868a37?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126144017/https://gorkaaa.medium.com/%EF%B8%8F-charla-laboratorio-c%C3%B3mo-se-encontr%C3%B3-un-idor-real-hackerone-y-c%C3%B3mo-mitigarlo-5ebbe8868a37
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11291 (id 11291)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🎙️ Charla + laboratorio: cómo se encontró un IDOR real (HackerOne) y cómo mitigarlo

📺 Ver el vídeo completo: 👉 [https://youtu.be/kA4bpJX\_pFg](https://youtu.be/kA4bpJX_pFg)

En este nuevo vídeo traigo algo diferente: una **charla con un hunter real** que nos cuenta cómo encontró un **IDOR** en un programa de **HackerOne**, y cómo lo resolvió desde el punto de vista técnico y ético.

Lo mejor es que no se queda en la historia: lo **reproducimos en laboratorio**, analizamos el código vulnerable y mostramos la **mitigación correcta** en detalle.

📺 Puedes verlo aquí 👉 [https://youtu.be/kA4bpJX\_pFg](https://youtu.be/kA4bpJX_pFg)

## 🔍 Qué vas a ver en el vídeo

- **Historia real:** cómo identificó el fallo y qué señales le llevaron al IDOR.
- **Laboratorio reproducible:** demostración paso a paso en entorno controlado.
- **Lectura del código vulnerable:** qué líneas fallaban y por qué.
- **Mitigación técnica:** cambios concretos para corregir la lógica insegura.
- **Mentalidad del hunter:** cómo priorizó, razonó y redactó su reporte.

## 🧠 Por qué este vídeo es especial

Los IDORs son vulnerabilidades aparentemente simples, pero su verdadero valor está en **la lógica**: entender *por qué*ocurren y *cómo* se pueden prevenir.

Aquí no solo hablamos de exploitación, sino de **responsabilidad y diseño seguro**: cómo piensan los desarrolladores y qué prácticas deben aplicar para evitar este tipo de fallos.

Este enfoque te servirá tanto si eres **hunter** como si eres **desarrollador o responsable de seguridad**.

## 🔧 Puntos clave de mitigación

✅ Validar ownership en el servidor (resource.owner == session.user).

✅ Implementar control de acceso por rol y contexto (RBAC).

✅ Usar identificadores no predecibles (UUIDs o referencias firmadas).

✅ Limitar exposición de datos sensibles en respuestas JSON.

✅ Aplicar *rate limiting* para evitar enumeraciones masivas.

## 💬 Participa

¿Quieres practicar este fallo?

Puedo subir el **laboratorio y el snippet de código** (anónimo) para que puedas probar la vulnerabilidad y aplicar la mitigación tú mismo.

Dímelo en los comentarios o en la comunidad de Discord, y lo preparo.

📺 Ver el vídeo completo: 👉 [https://youtu.be/kA4bpJX\_pFg](https://youtu.be/kA4bpJX_pFg)

💞 Mi canal de Youtube: Bug Bounty & Pentesting y Hacking Web

[https://www.youtube.com/@0xGorka](https://www.youtube.com/@0xGorka)

🧠 Aprende en nuestra comunidad de Discord:

#BugBounty #IDOR #HackerOne #Ciberseguridad #Pentesting #HackingEtico #CódigoSeguro #Mitigación #WebSecurity #InfoSec #0xGorka #GorkaElBochiMorillo
