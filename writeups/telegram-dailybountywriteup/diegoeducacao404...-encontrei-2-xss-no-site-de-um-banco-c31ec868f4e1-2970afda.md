# Encontrei 2 XSS no site de um Banco.

- **Source URL:** https://medium.com/@Diegoeducacao404.../encontrei-2-xss-no-site-de-um-banco-c31ec868f4e1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230111225116/https://medium.com/@Diegoeducacao404.../encontrei-2-xss-no-site-de-um-banco-c31ec868f4e1
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1216 (id 1216)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Encontrei 2 XSS no site de um Banco.

Olá, como vocês estão, espero que estejam bem.

Vamos direto ao assunto.

Eu estava em casa a noite fazendo alguns testes no meu kali, quando de repente chega um e-mail de um Banco, não estou autorizado a divulgar seu nome, mas esse Banco está entre um dos maiores do Brasil, tendo uma fortuna milionária com mais de 1 milhão de clientes.

Depois de receber esse e-mail, mesmo sem abrir, eu fui olhar o nome do Banco, como eu não me lembrava de ter feito nada nesse Banco, decidi dar uma olhada nele pelo meu navegador no site oficial. Depois de passar um bom tempo olhando o site e verificando a tecnologia, decidi dar uma olhada mais a fundo em outros recursos do Banco. Usei a ferramenta **subfinder** para enumeração de subdomínios, depois de passar um tempo olhando, vi que tinha uma url, era algo como: **compre.bancoexemplo.com.br** era uma parte em que você poderia comprar algumas coisas pelo site do Banco e ter alguns recursos e vantagens, mas para isso, o usuário deveria estar autenticado. Então eu clico na parte de cadastro e sou redirecionado para a tela de fazer cadastro e a url muda para algo como: **compre.bancoexemplo.com.br/cadastro?go=/**

Então pensei que poderia haver um XSS ali, coloquei esse payload na url**:**

**“>\<svg onload=confirm(10)> Após inserir o payload, para a minha surpresa, ele foi carregado e disparado.**

Curiosamente também cliquei na tela de login para quem já tem conta e ela também deixava a url parecida: **compre.bancoexemplo.com.br/login?go=/**

Coloquei o mesmo payload e novamente XSS:

O Banco não tinha programa de Bug bounty, mas enviei um relatório por uma plataforma especializada no assunto para que o Banco fosse notificado da vulnerabilidade e ela fosse corrigida.

Obrigado por ler. Eu estou no instagram como: diego\_o.santossl
