# Hackeando GraphQL

- **Source URL:** https://medium.com/@soyelmago/hackeando-graphql-introducci%C3%B3n-1537af763d0c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240112001010/https://medium.com/@soyelmago/hackeando-graphql-introducci%C3%B3n-1537af763d0c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4807 (id 4807)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hackeando GraphQL: Introducción

--

**GraphQL** se ha convertido en una herramienta indispensable en el mundo del desarrollo Web. En esta publicación, exploraremos qué es GraphQL y por qué es importante entender su funcionamiento para la seguridad Web. de bugs.

# ¿Qué es GraphQL?

GraphQL es un lenguaje de consulta y un tiempo de ejecución para APIs. Desarrollado por Facebook (Meta) en 2012, fue lanzado al público en 2015. A diferencia del tradicional REST API (GET, POST, PUT, DELETE), GraphQL permite a los clientes definir la estructura exacta de los datos que necesitan, lo que reduce el exceso de carga y mejora la eficiencia de las aplicaciones web.

# Ejemplo de Uso

Imagina que estás desarrollando una aplicación Web para una red social. Esta aplicación necesita obtener datos de usuarios, como sus nombres, amigos, publicaciones y comentarios. Tradicionalmente, con una API REST, tendrías que hacer múltiples solicitudes a diferentes endpoints para obtener toda esta información. Por ejemplo:

- Una solicitud para obtener la información del usuario (`/user/{id}`).
- Otra para obtener sus amigos (`/user/{id}/friends`).
- Una más para sus publicaciones (`/user/{id}/posts`).
- Y otra para los comentarios en sus publicaciones (`/posts/{id}/comments`).

Cada una de estas solicitudes significa una carga extra para el servidor y más tiempo de espera para el usuario.

Ahora, con **GraphQL**, podes obtener toda esta información en una sola solicitud. En lugar de múltiples endpoints, **GraphQL** utiliza un único endpoint. Envías una consulta (query) a este endpoint, especificando exactamente lo que necesitas. Por ejemplo, tu consulta podría verse así:

*{ user(id: “123”) { name friends { name } posts { title comments { content author { name } } } } }*


Esta única consulta le dice a **GraphQL** que queres el nombre del usuario, una lista de sus amigos (y sus nombres), sus publicaciones (incluyendo el título y los comentarios en cada publicación, con el contenido del comentario y el nombre del autor del comentario).

# Cómo Empezar a Hackear GraphQL?

A continuación, te dejo un listado de recursos (videos, publicaciones, herramientas y laboratorios) que he seleccionado especialmente para facilitarte la tarea de comenzar a hackear esta tecnología.

Por supuesto te recomiendo **Mis Videos**, resolviendo los laboratorios de **PortSwigger Academy**:

[https://www.youtube.com/watch?v=3jbz2lFEdfA&list=PLplKrR\_r0x1coO4OTTb780EYOhovbumF4&index=6](https://www.youtube.com/watch?v=3jbz2lFEdfA&list=PLplKrR_r0x1coO4OTTb780EYOhovbumF4&index=6)

**Laboratorios:**

[https://portswigger.net/web-security/all-labs](https://portswigger.net/web-security/all-labs)(buscá los de

**GraphQL**en el listado)

**Libros:**Black Hat GraphQL

**Publicación:**

[https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/graphql](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/graphql)

**Herramientas:**

## Y eso es todo por ahora. Espero que esta publicación te motive a comenzar en el apasionante mundo del Hacking de GraphQL!

#HappyHacking
