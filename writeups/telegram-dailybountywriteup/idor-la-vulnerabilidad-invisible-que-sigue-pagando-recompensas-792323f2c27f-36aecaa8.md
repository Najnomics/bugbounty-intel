# IDOR — La vulnerabilidad invisible que sigue pagando recompensas

- **Source URL:** https://gorkaaa.medium.com/idor-la-vulnerabilidad-invisible-que-sigue-pagando-recompensas-792323f2c27f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251014075747/https://gorkaaa.medium.com/idor-la-vulnerabilidad-invisible-que-sigue-pagando-recompensas-792323f2c27f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11256 (id 11256)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔓 IDOR — La vulnerabilidad invisible que sigue pagando recompensas

💞 Mi canal de Youtube: Bug Bounty & Pentesting y Hacking Web: [https://www.youtube.com/@0xGorka](https://www.youtube.com/@0xGorka)

🧠 Aprende en nuestra comunidad de Discord:

## 🚨 ¿Qué es un IDOR?

**IDOR (Insecure Direct Object Reference)** significa que una aplicación permite acceder a recursos internos (como archivos, perfiles o facturas) **sin verificar si el usuario tiene permiso para hacerlo**.

No es un fallo técnico complicado: es un error de **lógica de autorización**. Y justamente por eso, sigue siendo uno de los más comunes y rentables en bug bounty.

## 💡 ¿Por qué ocurre?

Muchas aplicaciones confían en el ID de un objeto (por ejemplo, file\_id, user\_id, order\_id) como si fuera prueba suficiente de que el usuario puede acceder a él.

Si el servidor **no valida la propiedad o los permisos**, cambiar el ID en la URL o en una petición puede revelar información o acciones de otras cuentas.

## 🔍 Ejemplos reales

1. **Descarga de archivos sensibles:**
2. GET /download?file\_id=1234
3. → Cambiando 1234 por 1235, accedes al archivo de otro usuario.
4. **Perfiles públicos mal validados:**
5. /user/profile/5678 muestra datos personales. Cambias el ID, y ves otro perfil.
6. **Facturas o pedidos:**
7. /orders/9876/invoice entrega documentos de clientes distintos.
8. **Almacenamiento en la nube:**
9. URLs con claves secuenciales (/files/0001, /files/0002) sin control de acceso.

En cada caso, el fallo no está en la visibilidad del ID, sino en **la falta de validación de propiedad** del recurso.

## 🧠 Cómo detectar un IDOR (sin romper nada)

1. **Busca patrones en endpoints:** /id=, /file\_id=, /user/, /doc/.
2. **Cambia el ID de forma lógica (±1, IDs vistos en responses).**
3. **Revisa las respuestas:** si el status sigue siendo 200 y obtienes contenido distinto → señal fuerte.
4. **Comprueba si el recurso pertenece a tu cuenta o a otra.**
5. **Registra todo:** PoCs reproducibles, sin fuerza bruta, con contexto de impacto.

⚠️ Recuerda: esto solo se debe hacer en **entornos autorizados** o programas de bug bounty.

## 🧩 Por qué los IDORs son tan peligrosos

Un IDOR parece simple, pero combinado con otros fallos puede llevar a **Account Takeover (ATO)**, fuga de datos sensibles o escaladas de privilegios.

Por ejemplo:

- IDOR + falta de validación de sesión → acceso total a recursos de otros usuarios.
- IDOR + CSRF → un atacante puede explotar la vulnerabilidad sin interacción directa.
- IDOR + XSS o tokens predecibles → toma de control de cuentas.

## 🧰 Cómo prevenirlo (para desarrolladores)

✅ **Valida propiedad en el servidor:**

```
if resource.owner != session.user:
    return 403
```
✅ **Usa referencias no predecibles:** UUIDs o tokens firmados.

✅ **Aplica controles de acceso basados en roles (RBAC).**

✅ **Responde con 403, no 404.** No ocultes el fallo, corrígelo.

✅ **Revisa endpoints legacy o administrativos.**

## 🎯 Para bug bounty hunters

Un IDOR vale más cuando demuestras impacto.

No basta con decir “puedo ver otro perfil”; muestra **por qué eso importa**:

- ¿Exponen PII o tokens?
- ¿Puedes modificar datos ajenos?
- ¿Podría encadenarse con otro fallo lógico?

Los mejores reportes son los que explican el *por qué*, no solo el *qué*.

## 🧩 En resumen

- IDOR = acceso directo sin validación de propiedad.
- Es fácil de detectar, pero aún más fácil de subestimar.
- Los programas de bug bounty pagan bien cuando demuestras impacto real.

💞 Mi canal de Youtube: Bug Bounty & Pentesting y Hacking Web

[https://www.youtube.com/@0xGorka](https://www.youtube.com/@0xGorka)

🧠 Aprende en nuestra comunidad de Discord:

💬 ¿Quieres que prepare un artículo con ejemplos prácticos de IDOR en APIs REST y GraphQL?

Coméntalo y lo publico pronto.

#BugBounty #IDOR #Ciberseguridad #HackingEtico #Pentesting #WebSecurity #InfoSec #APIsecurity #VulnerabilityResearch #0xGorka #GorkaElBochiMorillo
