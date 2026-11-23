# JWT Token Manipulation

- **Source URL:** https://medium.com/@zsodex/jwt-token-manipulation-explotando-vulnerabilidades-en-la-autenticaci%C3%B3n-web-7f416c1db6b6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250405210303/https://medium.com/@zsodex/jwt-token-manipulation-explotando-vulnerabilidades-en-la-autenticaci%C3%B3n-web-7f416c1db6b6
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9261 (id 9261)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# JWT Token Manipulation: Explotando Vulnerabilidades en la Autenticación Web

# JWT Token Manipulation: Ataques en Aplicaciones Web

Los JSON Web Tokens (**JWT**) son una tecnología ampliamente adoptada para llevar a cabo tareas de autenticación y autorización en entornos web modernos. Gracias a su capacidad de encapsular datos de manera compacta, auto-contenida y verificable, estos tokens facilitan significativamente la gestión de sesiones de usuario, el control de acceso a recursos protegidos y la implementación de sistemas sin estado (stateless). Sin embargo, esta conveniencia no está exenta de riesgos. Cuando los JWT son implementados sin las debidas medidas de seguridad, pueden convertirse en un punto crítico de vulnerabilidad. Este artículo se centra en analizar en profundidad las principales técnicas de manipulación y explotación de JWTs utilizadas por profesionales del Red Team, así como en describir metodologías de detección, herramientas especializadas y ejemplos prácticos basados en escenarios reales obtenidos de plataformas como Hack The Box.

# 🔎 ¿Cómo Detectar un JWT en una Aplicación Web?

Antes de poder explotar un JWT, es fundamental confirmar su existencia y comprender su contexto dentro de la aplicación. A continuación, se describen diversas formas de detección:

# 1️⃣ Inspeccionar Cookies del Navegador

- Utilizar las herramientas de desarrollo del navegador (`DevTools`), accediendo a la pestaña `Application` → `Storage` → `Cookies`, donde es posible identificar valores que aparentan tener la estructura típica de un JWT (tres segmentos separados por puntos).
- `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvYWNvIiwicm9sZSI6ImFkbWluIn0.W5_V9IuCfl...`
- Esta estructura revela un encabezado, un payload y una firma, codificados en Base64URL.

# 2️⃣ Revisar las Cabeceras HTTP

- Muchos JWT se transmiten a través del encabezado `Authorization`, bajo el esquema Bearer:
- `curl -i https://victima.com/protected -H "Authorization: Bearer TOKEN_AQUÍ"`
- Este enfoque es común en APIs RESTful y permite una autenticación sin necesidad de cookies.

# 3️⃣ Verificar el Código JavaScript del Cliente

- JWTs también pueden almacenarse en el `localStorage` o `sessionStorage`. Ejecutar en la consola del navegador:
- `console.log(localStorage.getItem("token")); console.log(sessionStorage.getItem("jwt"));`
- Estas líneas permiten visualizar tokens utilizados por el frontend para mantener sesiones activas.

# 📘 Caso Práctico: Explotación del Campo `kid` en un JWT RS256

Durante un escenario de laboratorio con una app vulnerable tipo CTF, identificamos un token JWT firmado con el algoritmo RS256. Al inspeccionar los campos del JWT en [jwt.io](https://jwt.io), observamos dos elementos clave: un campo `admin_cap` con valor `0`, y un `kid` con una ruta local.

💡 Nuestra hipótesis fue que el servidor cargaba la clave pública desde una ruta determinada por el `kid`, sin validación estricta. Esto nos permitió ejecutar una inyección de `kid` para que apuntara a una clave maliciosa generada por nosotros.

# 🔨 Pasos del ataque:

1. **Generamos una clave privada RSA:**

`openssl genrsa -out privKey.key 2048`
1. **Modificamos el token JWT:**

- Cambiamos el campo `admin_cap` de false a true.
- Reemplazamos `kid` por una URL controlada por nosotros: `http://<IP>:7070/privKey.key`
- Firmamos el nuevo token en jwt.io usando nuestra clave privada.

1. **Levantamos un servidor local para servir la clave pública:**

`python3 -m http.server 7070`
1. **Insertamos el JWT modificado con Cookie Editor** y recargamos la página.

# 🔥 Mas técnicas de Manipulación y Ataque de JWT (Red Team)

Una vez identificado y extraído un JWT, el atacante puede utilizar diversas técnicas ofensivas para analizar, modificar o falsificar el token con el fin de escalar privilegios o acceder a información sensible:

# 1️⃣ Decodificación y Análisis de Claims

Al estar codificados en Base64URL, los JWT permiten una lectura directa de sus campos sin necesidad de la clave secreta, lo que posibilita el análisis inicial de los claims (declaraciones). Entre los campos más interesantes para un atacante se encuentran: `username`, `admin`, `role`, `scope`, `exp`, entre otros.

- Puede utilizarse el sitio [jwt.io](https://jwt.io/), comandos con `base64`, o código en Python como:
- `import jwt print(jwt.decode(token, options={"verify_signature": False}))`
- Herramientas útiles incluyen: `jwt_tool.py`, `JWTInspector`, plugins de Burp Suite como JWT Decoder.

Este paso permite determinar si los claims pueden ser manipulados directamente, si existen valores codificados con roles elevados, o si hay una sobreexposición de datos sensibles.

# 2️⃣ Fuerza Bruta de Claves (HS256)

Cuando el algoritmo de firma utilizado es HS256 (HMAC con SHA-256, clave simétrica), una clave débil o predecible puede ser recuperada mediante ataques de diccionario o fuerza bruta, lo cual habilita al atacante a generar tokens firmados válidos.

- Usar diccionarios comunes como `rockyou.txt` o `jwt-secrets.txt`:
- `python3 jwt-cracker.py -t TOKEN_AQUÍ -w rockyou.txt john --wordlist=rockyou.txt --format=HMAC-SHA256 jwt_hash.txt`
- También se pueden emplear scripts personalizados utilizando la librería `hmac` de Python, o herramientas web como `CrackStation`.

Una vez obtenida la clave secreta, se puede modificar el contenido del token y firmarlo de nuevo, obteniendo acceso no autorizado con privilegios personalizados.

# 3️⃣ Confusión de Algoritmo (RS256 → HS256)

Este ataque aprovecha la flexibilidad del campo `alg` en el encabezado del JWT. El atacante modifica el algoritmo de firma de RS256 (asimétrico) a HS256 (simétrico), y engaña al servidor haciendo que acepte la clave pública como si fuera una clave secreta.

- Modificar el header:

`{ "alg": "HS256", "typ": "JWT" }`

- Generar el nuevo token:
- `new_token = jwt.encode({"admin": True}, open("public.pem").read(), algorithm="HS256")`

Si el backend no valida adecuadamente el tipo de algoritmo, el nuevo token puede ser aceptado como válido, permitiendo la escalada de privilegios.

# 4️⃣ Inyección en el Campo `kid`

El campo `kid` (Key ID) se utiliza para indicar qué clave debe usarse para verificar la firma del JWT. Si el backend utiliza este valor de forma dinámica, accediendo a archivos o URLs externas, se puede explotar para apuntar a claves controladas por el atacante

- Modificar el header para apuntar a una ruta relativa:
- `{ "alg": "RS256", "kid": "../../../../tmp/key" }`
- Generar claves propias con `ssh-keygen`:
- `ssh-keygen -t rsa -b 4096 -m PEM -f privKey.key`
- Subir la clave pública a una ruta accesible y firmar el token con la privada.

En entornos vulnerables con LFI o SSRF, se pueden apuntar rutas del sistema como `/proc/self/environ` o incluso recursos internos.

# 5️⃣ Ataques con `None Algorithm`

Algunas implementaciones defectuosas aceptan tokens cuyo algoritmo es `none`, lo que desactiva la verificación de firma.

- Modificar el header:
- `{ "alg": "none", "typ": "JWT" }`
- Eliminar la firma del token y modificar libremente los claims.

Este ataque es trivial pero extremadamente crítico. Herramientas como `jwt_tool -X alg_none` pueden automatizar el proceso para verificar esta debilidad.

# 6️⃣ Timing Attack y Oracle Side-Channel

Si el servidor realiza la validación de firmas carácter por carácter, se puede usar un ataque de canal lateral basado en tiempo para deducir la firma correcta.

- Medir diferencias en tiempos de respuesta para cada intento de firma.
- Automatizar con herramientas como `jwt-pwn`, que ajustan dinámicamente los valores basándose en la latencia.

Este ataque requiere un entorno controlado y muchas peticiones, pero puede ser efectivo en APIs mal protegidas.

# 7️⃣ Replay y Session Fixation

Los JWT robados pueden ser reutilizados si no existen mecanismos adecuados de invalidación.

- Usar un token capturado (por ejemplo, mediante XSS o tráfico sin HTTPS) para autenticarse en múltiples sesiones.
- En ataques de fijación de sesión, un atacante puede forzar el uso de un JWT controlado por él mismo en la víctima, y luego modificar los permisos en el servidor sin necesidad de cambiar el token del cliente.

# 8️⃣ JWTs en Subdominios

Cuando múltiples subdominios (como `api.victima.com` y `admin.victima.com`) comparten el mismo dominio padre, y los JWT son válidos entre ellos, se puede explotar esa relación para escalar privilegios lateralmente.

- Si los tokens se almacenan como cookies en `.victima.com`, pueden enviarse a cualquier subdominio.
- Esto permite explorar servicios que acepten el mismo JWT y obtener accesos no previstos.

# 🛠️ Herramientas Clave para JWT Attacks

- [jwt_tool.py](https://github.com/ticarpi/jwt_tool)
- [jwt-cracker](https://github.com/brendan-rius/jwt-cracker)
- \[`Burp Suite` con plugins de JWT\] – análisis dinámico en entornos web.
- `Postman` con extensiones JWT para testeo de APIs.
- `HackTricks JWT Cheatsheet` – excelente referencia de vulnerabilidades comunes.
- `CyberChef` – para decodificación, codificación y análisis visual.

# 📌 Conclusión

Aunque los JSON Web Tokens son una solución práctica y escalable para la gestión de sesiones y control de acceso, su seguridad depende en gran medida de una implementación rigurosa y cuidadosa. Este artículo ha explorado una serie de vectores de ataque que van desde la fuerza bruta de claves débiles y confusión de algoritmos, hasta técnicas avanzadas como explotación de campos `kid`, algoritmos `none`, o ataques por canal lateral. Comprender estos ataques es esencial para ofensores que buscan evaluar aplicaciones web modernas y también para defensores que deben diseñar sistemas más robustos.
