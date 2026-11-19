# Privilege escalation mediante Race Condition.

- **Source URL:** https://medium.com/@duality084/privilege-escalation-mediante-race-condition-0254df6ffbd8?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@duality084
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5950)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Introducción

La idea de este post es contar los detalles técnicos de una vulnerabilidad que encontré recientemente en un programa de BugBounty, se trata de mi 3er vulnerabilidad encontrada, que clasificó como P1 en Bugcrowd y por la cual obtuve mi primer bounty de 4 cifras. El tipo de vulnerabilidad detallada a continuación es del tipo “Race Condition” en una funcionalidad de la aplicación donde nunca se me había ocurrido buscar este tipo de vulnerabilidades. La aplicación afectada puede ser desplegada localmente y a su vez también se puede utilizar como servicio *SaaS* alojado por la empresa desarrolladora. Aunque la vulnerabilidad se encontró en la implementación local, decidí ampliar mis pruebas en la versión SaaS debido que se encontraron diferencias en las funcionalidades entre ambas versiones, que de poder utilizarlas en la implementación *SaaS* demostraría un mayor impacto.

### Explotación

En la aplicación afectada se puede administrar los permisos de los usuarios de manera bastante granular, por ejemplo, tenemos una sección de la aplicación llamada “User Roles” donde se puede asignar los permisos dentro de la aplicación. El máximo privilegio es “System Administrator” este puede modificar la configuración de la aplicación, por debajo de ese privilegio existen otros que pueden crear usuarios, administrar los equipos, ver los logs, etc. Un usuario con permisos de editar usuarios, roles y equipos no puede asignarse a si mismo el rol de “System Administrator”. A continuación dejo una imagen de como se ve la UI de la funcionalidad “User Roles”

En otra sección podemos asignar estos roles a un equipo o “Team”.

Finalmente podemos asignar usuarios a estos equipos y los usuarios heredan los permisos asignados en el apartado “User Roles”.

Lo primero que hice fue intentar modificar el rol de mi usuario actual y ponerlo con el máximo privilegio, obviamente la modificación fallo y me dio error.

Lo siguiente fue crear usuarios, roles, equipos y acá la cosa se empezó a poner interesante. Creé un nuevo “User Role” y le asigne el privilegio “System Administrator”, le di guardar y me dejo crearlo sin problemas.

Luego creé un equipo y le asigne este nuevo “User Role”, nuevamente el cambio se pudo realizar sin problemas.

Cuando intenté agregar un usuario al nuevo equipo creado la aplicación respondió con un error de que la acción que quería realizar no era posible.

Volví sobre mis pasos, quite el “User Role” con el privilegio “System Administrator” y volví a intentar asignar el usuario al nuevo equipo creado, esta vez la aplicación me dejo realizar la acción.

Repasemos:

- La aplicación nos deja crear un rol y asignarle los máximos privilegios.
- Nos deja asignar el rol a un equipo, pero si queremos asignar un usuario al equipo con el rol de máximos privilegios nos da error.
- Si dejamos el equipo sin ningún rol asignado podemos agregar un usuario al equipo sin problemas.

En este momento surgieron algunas preguntas en mi cabeza. “Que pasa si enviamos todas estas acciones al mismo tiempo? El servidor alcanzara a hacer las validaciones correspondientes?” Si me siguieron hasta acá es probable que se hayan dado cuenta que nos encontramos ante un posible error del tipo *Time Of Use — Time Of Check.*

Para intentar explotar este fallo se enviaron 3 requests al Repeater en BurpSuite:

- La acción de agregar un usuario al nuevo equipo.
- La acción de agregar el nuevo rol al nuevo equipo.
- Por ultimo la acción de dar el privilegio “System Administrator” al nuevo rol.

Esto se agrupo en una pestaña de BurpSuite y se cambio la opción para enviar los requests en paralelo.

Al enviar en paralelo todos los requests, estos fueron exitosos y conseguí escalar a un usuario con la posibilidad de modificar la configuración de la aplicación.

Arme el reporte y envié todos los detalles y videos de la explotación, al cabo de una semana obtuve el esperado “triaged” y como respuesta que el reporte clasificaba como P2 según el triager, aun faltaba el visto bueno de quienes administraban el programa, hasta acá sabia que tenia un potencial bounty de entre 2 y 3 mil dólares.

### Bonus track

Una vez explotada y reportada la vulnerabilidad decidí como bien mencione al principio de este post extender las pruebas a la versión *SaaS* de la aplicación, una de las diferencias que encontré con la implementación *self hosted* es que en la versión *SaaS* se encontraba desactivada la funcionalidad para ejecutar comandos sobre el sistema operativo en el cual corre la aplicación, para acceder a activar esta funcionalidad necesitas los máximos privilegios, osea “System Administrator”, pero en la versión *SaaS* la cuenta que te dan para administrar la aplicación no tiene estos permisos por lo cual procedí a explotar la vulnerabilidad detallada anteriormente y obtuve los máximos privilegios en la aplicación. Al querer habilitar la funcionalidad para ejecutar comandos en la implementación *SaaS* me daba un error que mencionaba que la acción no se permitía en instancias cloud.

Esto, lejos de des motivarme me planteo un nuevo reto, si lograba saltar este control podría usarlo como justificación para que la vulnerabilidad fuera clasificada como P1, ya que un atacante que podría comprometer una instancia cloud accediendo a la funcionalidad de ejecución de comandos que se suponía que no se debía tener acceso en una implementación *SaaS*. En el detalle del programa de bugbounty se mencionaba que la aplicación *SaaS* y *self hosted* son casi idénticas ya que comparten el código, por lo cual decidí realizar reversing sobre los binarios que tenia de la aplicación *self hosted*, luego de buscar la cadena de texto que me mostraba la aplicación cuando quería activar la funcionalidad, di con el código encargado de realizar la verificación, el cual se veía mas o menos de la siguiente manera:

```
public void EnsureNotRunningOnCloud(){
if (license.IsCurrentCloudInstance())
    {
    throw new Exception("Command execution is not supported on cloud instances");
    }
}
```
Como se puede ver en el código la verificación se basa en el tipo de licencia instalada en la aplicación. Es importante destacar que entre las funciones disponibles con los máximos privilegios se encuentra el cambio de licencia. Por lo tanto, el siguiente paso fue modificar la licencia en la instancia SaaS por la que estaba asignada a mi instancia *self hosted*. Una vez completada esta acción, pude ejecutar comandos en la instancia *SaaS.* Me limite a ejecutar los comandos *whoami* y *env* el cual devolvió las variables de entorno donde se encontraron credenciales de la base de datos utilizada por la aplicación, también se observó que el servicio corría sobre un cluster de Kubernetes. Decidí dejar las pruebas y proceder a reportar que, aprovechando la vulnerabilidad para escalar privilegios y el cambio de licencia en la instancia *SaaS* un atacante podía ejecutar comandos.

Algunas semanas después del segundo reporte me subieron la clasificación a P1 y obtuve como bounty $6000.

Espero que este post los inspire y los lleve a buscar ciertos tipos de vulnerabilidades donde habitualmente no lo harían.

Happy Hacking! 🍻 💻
