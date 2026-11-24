# HTML Injection

- **Source URL:** https://medium.com/@paulo_mota/html-injection-um-gateway-para-cross-site-scripting-xss-ea813ad26948?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012215842/https://medium.com/@paulo_mota/html-injection-um-gateway-para-cross-site-scripting-xss-ea813ad26948
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3867 (id 3867)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# HTML Injection: Um gateway para o Cross-Site Scripting (XSS)

--

# Introdução

Fala pessoal! Com este artigo gostaria de abordar um tema que é crucial para entendermos o cenário de vulnerabilidades web: a injeção de HTML. Esse tipo de vulnerabilidade é frequentemente o ponto de partida para o Cross-Site Scripting (XSS), ou injeção de javascript. HTML injection e XSS são assuntos pelos quais eu tenho um grande apreço por estudar e falar sobre.

# O que é HTML Injection?

HTML Injection é um tipo de vulnerabilidade de injeção de código que se manifesta quando um usuário consegue controlar um ponto de entrada (como por exemplo um campo de nome de usuário, campo de pesquisa, entre outros) e injetar código HTML arbitrário em uma página web vulnerável. De forma mais abrangente, permite que o atacante modifique o conteúdo da página que o usuário final enxerga.

Essa vulnerabilidade ocorre quando a entrada do usuário não é corretamente sanitizada (caracteres especiais removidos) e a saída não é codificada. Uma injeção possibilita ao atacante enviar uma página HTML maliciosa ou alterada para a vítima. O navegador alvo não conseguirá distinguir (ou confiar) nas partes legítimas das partes maliciosas da página, e consequentemente, interpretará e executará toda a página no contexto da vítima.

**Dica maneira:** Uma forma interessante de testar injeção de HTML/javascript, payloads de XSS, payloads de CSRF e outras vulnerabilidades é utilizando o site: [https://www.lncc.br/\~borges/php/testar.html](https://www.lncc.br/~borges/php/testar.html) . A sacada aqui é colar o código HTML da página que você está testando e tentar escapar para conseguir um XSS ou validar seus inputs de HTML

# Escalando de HTML Injection para JavaScript Injection e Cross-Site Scripting (XSS)

HTML Injection e Cross-Site Scripting (XSS) são dois lados da mesma moeda quando falamos de vulnerabilidades web. Ambos exploram a dinâmica de como os sites interagem com os navegadores, mas enquanto o HTML Injection foca na inserção de código HTML malicioso, o XSS vai além, permitindo a execução de código JavaScript. Vamos entender como essa escalada ocorre.

A relação entre HTML e JavaScript é intrínseca ao funcionamento das páginas web modernas. Enquanto o HTML serve como a espinha dorsal que estrutura o conteúdo, o JavaScript adiciona a camada de interatividade que os usuários esperam. O JavaScript pode ser incorporado diretamente em uma página usando as tags `<script>` ou pode ser "puxado" de uma fonte externa através do atributo "src" (comumente visto pelo script src). Isso permite que o navegador execute uma variedade de ações, desde simples alterações na página até operações mais complexas, como o envio de dados para um servidor.

Agora, imagine um cenário onde um atacante consegue injetar tags `<script>` em uma página web através de uma vulnerabilidade de HTML Injection. Nesse contexto, o navegador não tem como distinguir o código JavaScript legítimo do malicioso, executando os dois. Além disso, o JavaScript tem a capacidade de interagir com diversos elementos HTML através de manipuladores de eventos, como "onload" e "onmouseover", ampliando ainda mais as possibilidades de ataque. Portanto, o que começou como uma simples injeção de HTML pode rapidamente escalar para um ataque XSS, dando ao atacante controle total sobre o navegador da vítima.

O exemplo de código abaixo foi extraído do site da própria OWASP para ilustrar um código vulnerável a injeção. Neste caso, a aplicação não realiza nenhum tipo de sanitização do input do usuário e simplesmente recebe a variável **+user** e utiliza a mesma variável do jeito que está:

```
var userposition=location.href.indexOf("user=");
var user=location.href.substring(userposition+5);
document.getElementById("Welcome").innerHTML=" Hello, "+user;
```
# Explicando os tipos de XSS

## 1. Reflected XSS (XSS Refletido)

No Reflected XSS, o ataque ocorre quando a aplicação web reflete de volta um conteúdo que foi manipulado maliciosamente pelo usuário, geralmente por meio da URL. Isso significa que o ataque é efetivo quando a vítima clica em um link malicioso que contém o código de ataque. Por exemplo, se um site tem um código PHP que extrai o nome do usuário da URL e o exibe na página, um atacante pode manipular essa URL para incluir um script JavaScript malicioso. Quando a vítima clica no link, o script é executado no navegador dela.

## 2. Stored XSS (XSS Armazenado)

O Stored XSS é mais perigoso que o Reflected porque o código malicioso é armazenado permanentemente no servidor, geralmente por meio de campos como comentários, campos de perfil, cadastro de itens, clientes, dentre outros. Isso significa que qualquer usuário que acesse a página onde o código malicioso está armazenado se torna uma vítima em potencial. O ataque é “persistente” porque o código fica armazenado e é executado sempre que a página é acessada.

## 3. DOM-based XSS (XSS Baseado em DOM)

O DOM-based XSS é um tipo mais complexo de ataque XSS que explora vulnerabilidades no Modelo de Objeto de Documento (DOM) da página web. Nesse caso, o código malicioso manipula os DOM sinks (pontos DOM de uma página web onde os dados podem ser inseridos ou manipulados) para executar o script, em vez de ser refletido ou armazenado no servidor. Esse tipo de ataque pode ser tanto refletido quanto armazenado, dependendo de como o código malicioso é inserido na página. Abaixo alguns exemplos de Sinks que **podem** ser vulneráveis:

```
Vulnerabilidade                   Sink exemplo
DOM XSS                           document.write()
Open redirection LABS             window.location
Cookie manipulation               document.cookie
JavaScript injection              eval()
Document-domain manipulation      document.domain
WebSocket-URL poisoning           WebSocket()
Link manipulation                 element.src
Web message manipulation          postMessage()
Ajax request-header manipulation  setRequestHeader()
Local file-path manipulation      FileReader.readAsText()
Client-side SQL injection         ExecuteSql()
HTML5-storage manipulation        sessionStorage.setItem()
Client-side XPath injection       document.evaluate()
Client-side JSON injection        JSON.parse()
DOM-data manipulation             element.setAttribute()
Denial of service                 RegExp()
```
# Como testar e buscar pontos de injeção de HTML/Javascript

Há diversas maneiras de testar para encontrar vulnerabilidades de injeção de código HTML ou javascript, de forma automatizada ou manual. Eu particularmente encontro mais vulnerabilidades e de forma mais profunda utilizando testes manuais.

1. Inserindo tags simples de HTML como \<b>Negrito\</b> ou \<h1>Test\</h1> em campos de input do usuário. Dificilmente um WAF ou mecanismo de defesa vai entender uma tag de negrito como maliciosa, a não ser que o input seja devidamente sanitizado, impedindo a injeção. Caso o teste da tag HTML "simples" passe, é interessante tentar escalar para tags HTML que possam desfigurar a página e até injetar javascript.
2. Busca por parâmetros em URL utilizando o crawler do BurpSuite, ou ferramentas como paramspider, GetAllUrls, WayBackUrls, realizando um filtro http pelos URLs que retornam status 200 OK e fazendo um grep por "=". Em seguida, substituir os parâmetros encontrados por input HTML como mencionado no exemplo anterior ou até substituir por caracteres como >\<"= e checar se estão sendo corretamente refletidos. Lembrando que, no contexto de bug bounty, esta técnica pode trazer muitos reports duplicados;
3. E não acidentalmente por último, o uso de ferramentas automatizadas como o Nuclei, ou o próprio scanner do BurpSuite.
