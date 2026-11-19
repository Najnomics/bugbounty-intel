# Guía Completa de Broken Access Control

- **Source URL:** https://medium.com/@jpablo13/gu%C3%ADa-completa-de-broken-access-control-hacking-bug-bounty-y-prevenci%C3%B3n-en-aplicaciones-web-164103fa8cd1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250822091606/https://medium.com/@jpablo13/gu%C3%ADa-completa-de-broken-access-control-hacking-bug-bounty-y-prevenci%C3%B3n-en-aplicaciones-web-164103fa8cd1
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10151 (id 10151)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Broken Access Control (OWASP A01): Explicado para Hacking, Bug Bounty y Defensa

5 min readJul 8, 2025

En el universo de la ciberseguridad, el “Broken Access Control” se erige como una de las vulnerabilidades más críticas y recurrentes, según la clasificación de OWASP. Pero, ¿qué significa realmente? En esencia, ocurre cuando una aplicación web falla en hacer cumplir de manera adecuada sus políticas de acceso, permitiendo que usuarios realicen acciones o accedan a recursos para los que no tienen permiso. Esto puede derivar en:

- **Escalación Horizontal:** Un usuario puede acceder a los recursos o datos de otro usuario del mismo nivel de privilegio. Imagina poder ver el perfil de otro usuario sin su consentimiento, simplemente cambiando un ID en la URL.
- **Escalación Vertical:** Aquí, un usuario de bajo privilegio logra acceder a funciones o datos que deberían estar reservados para roles superiores, como administradores.
- **Bypass de Funciones Sensibles:** Esto incluye la capacidad de modificar roles de usuario, eliminar contenido ajeno o realizar otras acciones críticas sin la autorización adecuada.

# El Impacto en el Mundo del Bug Bounty: ¿Por qué son Tan Valiosas estas Fallas?

Para los Bug Bounty Hunters, las fallas de control de acceso son consideradas verdaderos tesoros…
