# XSS e SSTI. É por isso que o desenvolvedor deve se preocupar em aprender segurança.

- **Source URL:** https://medium.com/@Diegoeducacao404.../xss-e-ssti-%C3%A9-por-isso-que-o-desenvolvedor-deve-se-preocupar-em-aprender-seguran%C3%A7a-aaa51356b2b?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@Diegoeducacao404...
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 2364)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
XSS e SSTI. É por isso que o desenvolvedor deve se preocupar em aprender segurança.

A intenção desse texto é única e exclusivamente para alertar desenvolvedores e mostrar oque pode ocorrer quando você ou sua empresa não se preocupa com a segurança.

*Nenhuma parte do exemplo abaixo foi danificada ou destruída.*

Era o mês de Março e eu estava navegando na internet para ver alguns presentes e ter boas ideias para presentear uma pessoa.

Foi então que apareceu na pesquisa um site em que você poderia se cadastrar e fazer uma espécie de convite online para seu aniversário. Dentro desse site você também poderia comprar um presente online para a pessoa e a presente-la pelo próprio site, além de outras funcionalidades.

Então decidi entrar para explorar o site, e ver suas funcionalidades para tentar ter boas ideias.

De início fiz meu cadastro normalmente e havia uma parte que você poderia colocar o texto de convite, instintivamente tentei colocar um Payload de XSS, mas ele estava sendo filtrado e não era disparado.

Depois de olhar tudo, antes de excluir minha conta eu tentei colocar uma carga de XSS no lugar do meu nome e foi injetado com sucesso. Um Payload que gosto muito de usar é esse: ( **\<img src=xx onerror=alert(7\*7)>.jpg** ) Pois, se ele for disparado com um alerta ( 7\*7 ) há um xss, e se o alerta sair como ( 49 ) pode ser que exista SSTI(*isso não é uma regra*). E foi esse o resultado:

Então eu pensei: Ok, vamos então ver se tem SSTI, com uma carga simples:

E o resultado foi esse:

Como não tinha autorização, não queria continuar cavando, mas eu poderia ver se isso realmente era explorável e tentar escalar para um RCE. Após isso, vi que na parte de baixo do site havia o link do site da equipe de TI que fez esse serviço. Entrei para ver, e no site deles eles colocaram todos os outros sites que eles fizeram para outras empresas e adivinhe! metade deles continham a mesma Vulnerabilidades, provavelmente porque foi feito pela mesma equipe. Imediatamente me senti na obrigação de avisar os responsáveis de uma forma educada o quão isso era grave.

Se você é desenvolvedor, preocupe-se de entender o básico de segurança. Obrigado por ler.
