# CÓMO DESCUBRÍ UNA VULNERABILIDAD XSS EN UN PROGRAMA VDP

- **Source URL:** https://medium.com/@anripo2006/c%C3%B3mo-descubr%C3%AD-una-vulnerabilidad-xss-en-un-programa-vdp-c9133241cc5b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501125816/https://medium.com/@anripo2006/c%C3%B3mo-descubr%C3%AD-una-vulnerabilidad-xss-en-un-programa-vdp-c9133241cc5b
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8885 (id 8885)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CÓMO DESCUBRÍ UNA VULNERABILIDAD XSS EN UN PROGRAMA VDP

Mientras navegaba por la aplicación objetivo, me encontré con un formulario de ingreso de usuario que pedía un “User ID”. Hasta aquí, todo parecía normal, pero decidí inspeccionar el código fuente para entender mejor su funcionamiento.

almacenaba el input en value así que se me ocurrió bypassearlo con “\< y puse código HTML para ver como respondía

El primer intento consistió en inyectar código HTML en el campo. La respuesta del sistema confirmó que el input era reflejado sin filtros, lo que indicaba una posible vulnerabilidad XSS. A continuación, decidí probar la ejecución de código JavaScript.

Inicialmente, al inyectar un payload con código JavaScript, el sistema devolvía un error relacionado con *class=* `"required"`, lo que impedía la ejecución del script. Este comportamiento sugería que había ciertos mecanismos de validación en juego que bloqueaban la inyección directa de código.

# *Bypass y Payload Final*

Para eludir esta restricción, opté por definir previamente el atributo `value` y, de manera inmediata, adjuntar un payload basado en un evento. El código utilizado fue el siguiente:

 `value="prueba" onfocus="alert('Antonio Rivera')"`
# Conclusión

El hallazgo de esta vulnerabilidad XSS resalta la importancia de implementar una correcta sanitización y validación de todos los datos ingresados por el usuario. La capacidad de manipular atributos HTML, como `value`, y adjuntar eventos sin las debidas restricciones, puede abrir la puerta a ataques que comprometan la seguridad de la aplicación y la información de los usuarios.

Este descubrimiento me recordó la relevancia de la seguridad en el desarrollo web y la necesidad de revisar y reforzar las medidas de protección en todas las capas de la aplicación.
