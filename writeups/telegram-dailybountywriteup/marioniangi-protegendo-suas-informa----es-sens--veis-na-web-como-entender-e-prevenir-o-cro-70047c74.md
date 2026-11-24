# Protegendo suas informações sensíveis na web

- **Source URL:** https://medium.com/@marioniangi/protegendo-suas-informa%C3%A7%C3%B5es-sens%C3%ADveis-na-web-como-entender-e-prevenir-o-cross-site-scripting-xss-a6bafc101f18?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230202002632/https://medium.com/@marioniangi/protegendo-suas-informa%C3%A7%C3%B5es-sens%C3%ADveis-na-web-como-entender-e-prevenir-o-cross-site-scripting-xss-a6bafc101f18
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1591 (id 1591)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Protegendo suas informações sensíveis na web: Como entender e prevenir o Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) é uma das vulnerabilidades de segurança mais comuns na web. É uma técnica que permite a injeção de scripts maliciosos em páginas da web, acessadas por outros usuários. Isso pode permitir a um invasor acessar dados confidenciais, como senhas ou informações de cartão de crédito, ou mesmo controlar a sessão de um usuário.

Existem dois tipos principais de XSS: **refletido e armazenado**. O XSS refletido ocorre quando o script malicioso é enviado por meio de uma solicitação da web, como um formulário ou uma URL, e é imediatamente executado no navegador do usuário. O XSS armazenado, por outro lado, é quando o script malicioso é armazenado em um servidor e é executado sempre que uma página é carregada.

Um exemplo de XSS refletido é quando um invasor envia uma solicitação para um site com um script malicioso, como o seguinte:

`http://www.example.com/search?q=<script>alert('XSS Attack');</script>`
Se o site não valida ou filtra corretamente os dados de entrada, o script será executado no navegador do usuário e exibirá uma mensagem de alerta.

Já o XSS armazenado pode ocorrer, por exemplo, quando um invasor envia um comentário malicioso em um fórum ou em um site de mídia social. Se o site não valida corretamente os dados de entrada, o script malicioso será armazenado no servidor e será executado sempre que uma página for carregada.

Para evitar a falha de segurança XSS, é importante que os desenvolvedores web validem e filtrem corretamente os dados de entrada, especialmente quando se trata de dados sensíveis. Além disso, é importante que os desenvolvedores implementem técnicas de codificação, como a codificação HTML ou URL, para evitar a injeção de scripts maliciosos.

Em resumo, a falha de segurança XSS é uma ameaça real à segurança da web e é importante que desenvolvedores e usuários tomem medidas para proteger suas informações sensíveis. Validação e filtragem adequadas dos dados de entrada, bem como a implementação de técnicas de codificação, são importantes para evitar a falha de segurança XSS e garantir a segurança dos usuários
