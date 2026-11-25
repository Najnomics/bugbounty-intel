# Guía Maestra de SSRF

- **Source URL:** https://medium.com/@jpablo13/gu%C3%ADa-maestra-de-ssrf-estrategias-de-explotaci%C3%B3n-y-mitigaci%C3%B3n-ae3b7a4b2ce8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260424164433/https://medium.com/@jpablo13/gu%C3%ADa-maestra-de-ssrf-estrategias-de-explotaci%C3%B3n-y-mitigaci%C3%B3n-ae3b7a4b2ce8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13368 (id 13368)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Guía Maestra de SSRF: Estrategias de Explotación y Mitigación

## Aprende a detectar y explotar vulnerabilidades SSRF en entornos Cloud-Native, desde servicios de metadata hasta evasión de filtros.

## ¿Qué es SSRF?

El SSRF (Server Side Request Forgery)hoy no es solo una petición mal formada; es la explotación de la **confianza implícita** en entornos de microservicios. En arquitecturas Cloud-Native, el SSRF permite saltar del “Public-Facing Tier” al “Management Plane”.

## Impacto

Permite la exfiltración de identidades de servicio (Identity Tokens), lo que garantiza persistencia en el Tenant de Cloud del cliente, bypass de MFA organizacional y acceso directo a bases de datos de producción (PII) sin pasar por el API Gateway.

## Metodología de Reconocimiento Específico

**Identificación de “Fetchers”:** Detectar funciones que procesan archivos externos (importar contactos, subir foto de perfil por URL, validadores de certificados SSL).

**Blind SSRF Detection:** Usa **Interactsh** o **Burp Collaborator**.

- Si el tráfico saliente está bloqueado, prueba **DNS Out-of-Band**: [http://$(your_id).interact.sh](<https://web.archive.org/web/20260424164433/http://$(your_id).interact.sh./>)
[.](<https://web.archive.org/web/20260424164433/http://$(your_id).interact.sh./>)
