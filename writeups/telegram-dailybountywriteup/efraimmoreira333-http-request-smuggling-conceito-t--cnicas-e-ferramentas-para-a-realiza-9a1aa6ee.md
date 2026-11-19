# http request smuggling conceito t%C3%A9cnicas e ferramentas para a realiza%C3%A7%C3%A3o do ataque de 8a99ff101a0a

- **Source URL:** https://medium.com/@efraimmoreira333/http-request-smuggling-conceito-t%C3%A9cnicas-e-ferramentas-para-a-realiza%C3%A7%C3%A3o-do-ataque-de-8a99ff101a0a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141852/https://medium.com/@efraimmoreira333/http-request-smuggling-conceito-t%C3%A9cnicas-e-ferramentas-para-a-realiza%C3%A7%C3%A3o-do-ataque-de-8a99ff101a0a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2519 (id 2519)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HTTP Request Smuggling : Conceito,técnicas e ferramentas para a realização do ataque de contrabando de requisições HTTP na prática

Você já ouviu falar do ataque “HTTP Request Smuggling”? Sabia que quando encontrado em programas de Bug Bountys a recompensa é alta? Neste artigo iremos explicar de uma vez por todas do que se trata essa falha e deixar de maneira mais clara e lógica possível para que ela seja compreendida.

## **Conceito**

Antes de explicarmos o ataque em si, vamos entender alguns termos:

**HTTP**: Protocolo responsável pela transferência de dados, com ele conseguimos fazer requisições aos servidores

**Transfer-encoding \*:** Responsável pela especificação da forma de codificação usada para transferir o corpo da mensagem. É útil quando há grande quantidade de dados que estão sendo enviados, sendo eles fragmentados, e o tamanho total da resposta é desconhecida até que seja totalmente processada pelo servidor

**Transfer-chunked (em pedaços) \* :** É uma das categorias do “Transfer-Encoding”, são dados enviados em uma série de fragmentos, na qual é necessário adicionar o tamanho do fragmento atual no formato hexadecimal, seguido por “\r\n” e o fragmento em si

**Content-Lenght:** Número de bytes do tamanho do corpo da mensagem

*O “Transfer-encondig” possui cinco categorias sendo elas (chunked,compress,deflate,gzip,identify). O segundo conceito “Transfer-chunked” foi retirado do site https://developer.mozilla.org. Importante ler mais afundo a posteriori*

## Ataque

Como o próprio nome já diz, o “HTTP Request Smuggling” (Contrabando de solicitações HTTP), é um ataque que consiste em um invasor modificar as requisições das solicitações HTTP, fazendo assim consequentemente que o mesmo obtenha acesso não autorizado aos servidores da(s) sua(s) vítima(s).

É preciso entender sobretudo, a lógica da comunicação dessas requisições. Algumas empresas utilizam em seu sistema um servidor front-end ( sendo neste caso, muitas vezes um balanceador de carga ou um proxy reverso), que somente depois de ter passado por ele, é feito em seguida a solicitação para o servidor back-end. Veja abaixo um exemplo desta arquitetura:

Caso não haja um limite de solicitações entre os servidores, isto pode ser usado por cibercriminosos para fazer requisições iguais, resultando em respostas diferentes do servidor, já que eles(front e back) irão interpretar de forma diferente essas requisições :

Observe que o servidor Back-End interpretou as requisições do Front-End de maneira diferente, dando no segundo bloco, uma resposta de redirecionamento para a área administrativa. Na prática, isso decorre através de solicitações maliciosas utilizando o Transfer-Encoding (T.E) ou Content-Lenght (C.L).

A grande maioria das falhas de HTTP Request Smuggling decorrem da especificidade que o HTTP oferece, sendo ela duas (Transfer-Encoding e Content-Lenght), de onde a solicitação deve terminar. Devido a isso, é possível utilizar em uma única requisição, os dois modos, fazendo com que o servidor entre em conflito.

## Na prática

Como vimos acima, para que o ataque aconteça, basta manipular os cabeçalhos T.E e o C.L colocando-os em uma mesma solicitação e manipula-los para que os servidores front e back processem essas requisições de maneiras diferentes.

Para executá-lo, é necessário observar os comportamentos dos servidores decorrentes de cada solicitação realizada. Estes comportamentos são anotados em formatos de siglas, exemplo:

**TE.TE:** Tanto o servidor front quanto back suportam o Transfer-Encoding em seu cabeçalho. Neste caso, é necessário fazer um solicitação com ofuscação, pois pode ocorrer de servidores não processarem.

Exemplo:

```
POST / HTTP/1.1
Host: exemplo.com 
Content-Length: 13
Transfer-Encoding: chunked
Transfer-Encoding: cow 
 
```
**CL.TE:** O servidor front usa o C.L e o servidor back utiliza T.E em seu cabeçalho. Exemplo:

```
 POST / HTTP/1.1
 Host: exemplo.com
 Content-Lenght: 13
 Transfer-Encoding: chuncked
 
 0
 PEDIDO MALICIOSO
```
**TE.CL:** O servidor front usa o Transfer-Encoding em seu cabeçalho e o back utiliza Content-Lenght. Exemplo:

```
POST / HTTP/1.1
Host: exemplo.com
Content-Length: 3
Transfer-Encoding: chunked
 
8
PEDIDO MALICIOSO
0
```
## **No Burp suite**

**TE.TE**

### CL.TE

### **TE.CL**

## Ferramentas

A ferramenta mais utilizada tanto por Pentesters quanto por Bug Hunters sem dúvidas é o “Smuggler”. Isto se deve pelo fato de que encontrar uma vulnerabilidade desta nos sistemas ( considerando que houve investimento em segurança da informação na arquitetura da empresa) pode ser um trabalho muito complexo.

Para instalação dela basta acessar : [https://github.com/defparam/smuggler](https://github.com/defparam/smuggler)

Exemplo prático da ferramenta pelo Bug Hunter “ I’m Zemo ”:

### **Soluções para evitar o ataque de Contrabando de requisições HTTP, segundo a PortSwigger:**

- Use HTTP/2 de ponta a ponta e desabilite o downgrade de HTTP, se possível. O HTTP/2 usa um mecanismo robusto para determinar o tamanho das solicitações e, quando usado de ponta a ponta, é inerentemente protegido contra contrabando de solicitações. Se você não puder evitar o downgrade do HTTP, certifique-se de validar a solicitação reescrita em relação à especificação HTTP/1.1. Por exemplo, rejeite solicitações que contenham novas linhas nos cabeçalhos, dois-pontos nos nomes dos cabeçalhos e espaços no método de solicitação.
- Faça com que o servidor front-end normalize solicitações ambíguas e faça com que o servidor back-end rejeite as que ainda forem ambíguas, fechando a conexão TCP no processo.
- Nunca assuma que as requisições não terão um corpo. Essa é a causa fundamental das vulnerabilidades de dessincronização do CL.0 e do lado do cliente.
- Padrão para descartar a conexão se exceções no nível do servidor forem acionadas ao lidar com solicitações.
- Se você rotear o tráfego por meio de um proxy de encaminhamento, verifique se o HTTP/2 upstream está ativado, se possível.

**REFERÊNCIAS**

[https://www.imperva.com/learn/application-security/http-request-smuggling/](https://www.imperva.com/learn/application-security/http-request-smuggling/)

[https://portswigger.net/web-security/request-smuggling](https://portswigger.net/web-security/request-smuggling)

[https://abraweb.com.br/index.php/artigos/http-request-smuggling-attack](https://abraweb.com.br/index.php/artigos/http-request-smuggling-attack)

[https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding)
