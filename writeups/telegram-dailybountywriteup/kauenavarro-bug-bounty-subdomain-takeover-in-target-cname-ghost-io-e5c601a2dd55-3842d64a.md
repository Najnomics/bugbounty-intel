# [BUG BOUNTY] SUBDOMAIN TAKEOVER IN TARGET CNAME GHOST.IO

- **Source URL:** https://medium.com/@kauenavarro/bug-bounty-subdomain-takeover-in-target-cname-ghost-io-e5c601a2dd55?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142220/https://medium.com/@kauenavarro/bug-bounty-subdomain-takeover-in-target-cname-ghost-io-e5c601a2dd55
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1691 (id 1691)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# \[Bugbounty\] Subdomain Takeover in Target Cname Ghost.io

*Um controle de subdomínio ocorre quando um invasor obtém controle sobre um subdomínio de um domínio de destino. Normalmente, isso acontece quando o subdomínio tem um nome canônico (CNAME) no Domain Name System (DNS), mas nenhum host está fornecendo conteúdo para ele. Isso pode acontecer porque um host virtual ainda não foi publicado ou um host virtual foi removido. Um invasor pode assumir esse subdomínio fornecendo seu próprio host virtual e, em seguida, hospedando seu próprio conteúdo para ele, segundo developer.mozilla.org.*


**Processo de reconhecimento**

Realizo meu reconhecimento usando varias ferramentas, como, por exemplo, subfinder e findomain.

Após o levantamento dos subdomínios obtive os CNAMES usando o DNSX, filtrando as saídas por “ghost.io.”.

Abri todos os domínios filtrados no navegador usando uma extensão do Mozilla ([https://github.com/htrinter/Open-Multiple-URLs/](https://github.com/htrinter/Open-Multiple-URLs/)), que abre diversas URLS de forma rápida, para poder verificar a resposta de cada uma.

Encontrei um subdomínio que ao ser aberto redirecionava para essa imagem.

O CNAME desse domínio apontava para \*.ghost.io.

Nesse momento procurei no repositorio [https://github.com/EdOverflow/can-i-take-over-xyz/](https://github.com/EdOverflow/can-i-take-over-xyz/) para verificar se tinha informação se era vulneravel ou não a aquisição de subdominio, então encontrei [https://github.com/EdOverflow/can-i-take-over-xyz/issues/89](https://github.com/EdOverflow/can-i-take-over-xyz/issues/89) e dai em diante realizei o cadastro na plataforma e assumi o subdomínio.

O processo é simples, você cria uma conta e depois um site. Nesse site você tem opção de usar um template ou subir um projeto seu, eu criei um projeto e editei algumas informações do mesmo.

Quando fazemos isso obtemos um subdomínio aleatório com o domínio raiz ghost.io.

No meu caso eu precisei fazer 2 processos.

1- Usar um cartão de credito valido para obter o trial pois somente com essa opção é possível editar o domain do serviço e colocar o cname que encontrei no campo Ghost.io .

2-Alterar o nome do domínio customizado para o nome do subdomínio do que eu encontrei, blog.example.com.

Feito isso assumi totalmente o subdomínio da empresa.

Ela era apenas uma pagina com informações inofensivas para quem acessasse a página, porém isso poderia ter um formulário para capturar credenciais.

Poderia ter um javascript com a intenção de obter cookies do navegador entre outras possibilidades como o impacto na imagem da empresa.

**Impacto**

O controle básico do subdomínio pode levar ao roubo de dados e perda financeira indireta por meio da capacidade do invasor de interagir com usuários legítimos. Essas ações maliciosas também podem resultar em danos à reputação da empresa, por exemplo, a confiança dos clientes.

**Referência**

[https://github.com/EdOverflow/can-i-take-over-xyz/issues/89](https://github.com/EdOverflow/can-i-take-over-xyz/issues/89)

## Linha do tempo:

Envio do relatório: 11/02/2023

Triagem: Aguardando

**My social medial accounts**

Linkedin — [https://www.linkedin.com/in/surendra-pander-4066761b7/](https://www.linkedin.com/in/kau%C3%AA-navarro/)
