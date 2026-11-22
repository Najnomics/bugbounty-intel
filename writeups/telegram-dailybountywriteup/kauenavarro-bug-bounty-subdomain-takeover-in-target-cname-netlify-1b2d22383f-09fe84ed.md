# [BUG BOUNTY] SUBDOMAIN TAKEOVER IN TARGET CNAME NETLIFY

- **Source URL:** https://medium.com/@kauenavarro/bug-bounty-subdomain-takeover-in-target-cname-netlify-1b2d22383f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221207094823/https://medium.com/@kauenavarro/bug-bounty-subdomain-takeover-in-target-cname-netlify-1b2d22383f
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/926 (id 926)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# \[BUG BOUNTY\] SUBDOMAIN TAKEOVER IN TARGET CNAME NETLIFY

Um controle de subdomínio ocorre quando um invasor obtém controle sobre um subdomínio de um domínio de destino. Normalmente, isso acontece quando o subdomínio tem um nome canônico ([CNAME](https://en.wikipedia.org/wiki/CNAME_record)) no Domain Name System ([DNS](https://developer.mozilla.org/en-US/docs/Glossary/DNS)), mas nenhum host está fornecendo conteúdo para ele. Isso pode acontecer porque um host virtual ainda não foi publicado ou um host virtual foi removido. Um invasor pode assumir esse subdomínio fornecendo seu próprio host virtual e, em seguida, hospedando seu próprio conteúdo para ele, segundo developer.mozilla.org.


**Processo de reconhecimento**

Realizo meu reconhecimento usando varias ferramentas, como, por exemplo, subfinder e findomain.

Após o levantamento dos subdomínios obtive os CNAMES usando o DNSX, filtrando as saídas por “NETLIFY”.

Abri todos os domínios filtrados no navegador usando uma extensão do Mozilla ([https://github.com/htrinter/Open-Multiple-URLs/](https://github.com/htrinter/Open-Multiple-URLs/)), que abre diversas urls de forma rápida, para poder verificar a resposta de cada uma.

Encontrei um subdomínio que retornava o erro.

Confirmei com o template (/nuclei-templates/takeovers/netlify-takeover.yaml), do nuclei.

O CNAME desse domínio apontava para \*.netlifyglobalcdn.com.

Nesse momento já tinha cadastro nessa plataforma, foi então que comecei a configuração para assumir o subdomínio.

O processo é simples, você cria uma conta e depois um site. Nesse site você tem opção de usar um template ou subir um projeto seu, eu criei um projeto e hospedei um único arquivo index.html.

Quando fazemos isso obtemos um subdomínio aleatório com o domínio raiz netlify.app.

No meu caso eu precisei fazer 3 processos.

1- Alterar o nome do domínio padrão para o nome do subdomínio do CNAME que eu encontrei, exemplo: xyzw.netlifyglobalcdn.com ficando xyzw.netlify.app.

2- Adicionar o domínio raiz da empresa empresa.com no add custom domain.

3- Criar um alias com o subdomínio completo.

Feito isso assumi totalmente o subdomínio da empresa.

Ela era apenas um (\<h1>takeover kaue\</h1>) inofensivo para quem acessasse a página, porém isso poderia ter um formulário para capturar credenciais.

**Impacto**

O controle básico do subdomínio pode levar ao roubo de dados e perda financeira indireta por meio da capacidade do invasor de interagir com usuários legítimos. Essas ações maliciosas também podem resultar em danos à reputação da empresa, por exemplo, a confiança dos clientes.

**Resolução**

A empresa resolveu o problema removendo o apontamento do CNAME, sendo assim, automaticamente a aquisição que criei parou de funcionar.

**Referência**

# Linha do tempo:

Envio do relatório: 27/11/2022

Triagem: 28/11/2022

Aceito : 28/11/2022

Resolvido: 28/11/2022

**My social medial accounts**

Linkedin — [https://www.linkedin.com/in/surendra-pander-4066761b7/](https://www.linkedin.com/in/kau%C3%AA-navarro/)
