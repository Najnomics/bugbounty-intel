# XSS em uma IA.

- **Source URL:** https://medium.com/@Diegoeducacao404.../xss-em-uma-ia-199fe41bf3f9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142700/https://medium.com/@Diegoeducacao404.../xss-em-uma-ia-199fe41bf3f9
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2365 (id 2365)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS em uma IA.

Essa vulnerabilidade ocorreu em uma IA bem conheçida que tem recursos para texto.

Eu e um colega(Ruben) estávamos conversando pelo messenger ( *Sim eu uso messenger, me julgue*) e ele me pediu alguns payloads de XSS para dar Bypass em WAF. Mandei então uma lista para ele. Cerca de 10 minutos depois ele me mandou uma mensagem dizendo que algum script tinha dado Bypass na IA e falou para eu dar uma olhada.

Mais tarde fui olhar e entender oque ocorria, e funcionava assim: o input de texto tinha um limite, por exemplo: 200 palavras, se você colocasse alguns payloads de XSS estando dentro do limite de palavras, nada acontecia, mas se você atingisse o limite de palavras e dentre essas palavras tivesse alguns payloads de XSS, ele era disparado, ou seja: a carga maliciosa só era disparada se você colocasse uma quantidade de palavra tal que atingisse o limite de palavras.

Depois de dar uma olhada, achei a falha em outro prompt da IA

Se você olhar no canto superior esquerdo a aplicação diz que existe uma extensão do Chrome.

Com a curiosidade aguçada baixei a extensão no meu navegador e após seguir o mesmo método de atingir o limite de caracteres com payloads de XSS ocorreu a mesma coisa, XSS na extensão:

Em vermelho está o inicio de uma parte da grande lista contendo varios payloads de xss para atingir o limite de caracteres, o payload disparado foi: **>/option>/select>img src=’x’ onerror=’alert(1)’>** que está mais a baixo na lista.

Após isso, entrei em contato com os responsáveis que, rapidamente me pediram para detalhar a vulnerabilidade.

Fiz um relatório e enviei, e essa foi a resposta:

Obrigado por ler.
