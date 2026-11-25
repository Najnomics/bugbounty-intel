# Never Trust the Client

- **Source URL:** https://medium.com/@swanawett/never-trust-the-client-como-consegui-manipular-o-ranking-de-uma-aplica%C3%A7%C3%A3o-com-sistema-antifraude-4b3a71209344
- **Fetched from:** https://medium.com/@swanawett/never-trust-the-client-como-consegui-manipular-o-ranking-de-uma-aplica%C3%A7%C3%A3o-com-sistema-antifraude-4b3a71209344?source=rss-0b98e8379885------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14888 (id 14888)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** swanawett / Sat, 29 Aug 2026 19:01:05 GMT

Recentemente, durante alguns testes em um daqueles sites de **“moggar os outros”**, onde duas pessoas aparecem na câmera e recebem uma pontuação, encontrei uma falha que acabou sendo bem mais interessante do que parecia no começo.

O funcionamento é simples: duas pessoas entram em uma partida rápida usando a webcam e, durante alguns segundos, o próprio navegador analisa informações da câmera e calcula a pontuação de cada participante.

A aplicação também possui mecanismos para tentar identificar fraudes, como detecção de imagem estática, análise de movimento e outras verificações relacionadas à câmera.

Mesmo com essas proteções, havia um problema importante na forma como o sistema havia sido construído:

**O navegador calculava a pontuação e depois dizia ao servidor qual havia sido o resultado.**

Foi a partir daí que comecei a testar até onde eu conseguiria controlar essa informação.

**Nota:** Os testes descritos neste artigo foram realizados exclusivamente com fins de pesquisa e aprendizado, sem qualquer intenção de prejudicar o serviço, seus usuários ou seus dados. Alguns detalhes foram simplificados e o código utilizado nos testes não será disponibilizado. O objetivo é compartilhar o processo de descoberta e discutir a falha do ponto de vista de segurança, não fornecer um exploit pronto contra o serviço.

Analisando o tráfego da aplicação pelo Burp Suite, encontrei a requisição enviada ao final de cada partida:

POST /api/match/finalize HTTP/2

Content-Type: application/json

Entre os dados enviados estavam campos como:

```
{
  "selfScore": 7.4,
  "opponentScore": 6.8
}
```
Além da pontuação, havia um objeto chamado selfScanValidity, contendo informações geradas pela análise da câmera:

```
{
  "selfScanValidity": {
    "microMotionScore": "...",
    "staticImageSuspicion": "...",
    "sampledFrames": "...",
    "landmarkStability": "..."
  }
}
```
O campo que mais me chamou atenção foi o selfScore.

Se aquele valor representava minha pontuação e estava sendo enviado pelo navegador, a pergunta era inevitável:

***O que aconteceria se eu simplesmente alterasse esse valor antes de ele chegar ao servidor?***

Comecei pelo caminho mais óbvio: interceptei a requisição no Burp Suite e alterei manualmente o selfScore.

O problema é que as partidas acontecem em tempo real.

Enquanto eu segurava minha requisição no Burp, alterava o JSON e liberava o envio, o outro participante já havia enviado o resultado dele.

Na prática:

Minha requisição → parada no Burp para edição

Requisição do oponente → chega primeiro ao servidor

↓

partida finalizada

Quando minha requisição finalmente chegava, já era tarde demais.

Então o problema não parecia estar na alteração em si, mas no tempo que eu levava para fazê-la.

Precisava encontrar uma forma de alterar o valor automaticamente.

A solução foi mover o teste para o console do navegador.

Em vez de esperar a requisição chegar ao Burp para modificá-la manualmente, criei um script que identificava a finalização da partida e alterava os dados antes do envio.

O processo ficou mais ou menos assim:

Aplicação termina a partida

↓

Prepara os dados

↓

Script identifica a requisição

↓

Altera a pontuação

↓

Requisição é enviada

↓

Servidor

Para isso, comecei sobrescrevendo temporariamente o comportamento do fetch().

De forma simplificada:

const originalFetch = window.fetch;

```
window.fetch = function (...args) {
    // identifica a requisição de finalização
    // e altera os dados antes do envio
```
return originalFetch.apply(this, args);

};

Agora não existia mais o atraso causado pela edição manual no Burp.

A requisição modificada finalmente chegou ao servidor no momento certo.

Só que o resultado não foi o que eu esperava.

Coloquei uma pontuação próxima de 10.

Minha nota final virou:

1.0

No começo achei que o servidor simplesmente estivesse ignorando minha alteração.

Mas percebi um detalhe importante.

Enquanto estava focado no script e nas requisições, em alguns testes minha webcam estava coberta ou praticamente sem movimento.

Isso afetava diretamente os dados de selfScanValidity.

Dois campos, em especial, chamaram minha atenção:

staticImageSuspicion → muito alto

microMotionScore → praticamente zero

Ou seja, eu estava enviando algo parecido com:

Pontuação: 9.8

Movimento na câmera: praticamente nenhum

Suspeita de imagem estática: muito alta

Para o sistema, aquilo claramente não parecia uma partida normal.

A pontuação 1.0, então, provavelmente não era um erro.

Era o antifraude reagindo ao resultado suspeito.

Refiz o teste aparecendo normalmente diante da webcam e deixei os dados da câmera completamente intactos.

Agora havia movimento, piscadas, pequenas mudanças de iluminação e todas as variações normais de uma pessoa diante da câmera.

Mas havia outro problema.

Mesmo com a câmera funcionando normalmente, forçar valores muito altos ainda fazia a pontuação cair para 1.0.

Ainda faltava alguma coisa.

Durante os testes também percebi que algumas finalizações não estavam sendo capturadas pelo meu script.

O motivo era o navigator.sendBeacon().

A Beacon API permite que o navegador envie dados em segundo plano, inclusive quando o usuário está saindo da página ou fechando uma aba.

Em algumas situações, a aplicação utilizava esse caminho para finalizar a partida.

Isso significava que observar apenas o fetch() não era suficiente.

Depois de adaptar o teste para identificar também essas finalizações, consegui acompanhar de forma consistente o que estava sendo enviado ao servidor.

Mas ainda restava descobrir por que uma pontuação muito alta era rejeitada mesmo quando os dados da câmera eram normais.

Foi então que comecei a suspeitar que o backend também comparava as informações enviadas pelos dois participantes.

Fazia sentido.

Se uma pessoa informa:

Minha pontuação: 9.9

Pontuação do oponente: 5.2

Mas os dados enviados pelo outro participante não combinam com uma diferença tão grande, existe um bom motivo para desconfiar daquele resultado.

Isso explicava por que simplesmente colocar 9.8, 9.9 ou 10 não funcionava.

Quanto mais eu aumentava a pontuação, mais fácil provavelmente ficava perceber que havia algo errado.

E foi aí que mudei a estratégia.

O próprio JSON já continha o opponentScore.

Em vez de escolher uma pontuação fixa, eu poderia usar a pontuação que a aplicação havia calculado para o oponente como referência.

A lógica deixou de ser:

Minha pontuação = 9.9

e passou a ser:

Minha pontuação = pontuação do oponente + pequena diferença

Por exemplo, em vez de transformar uma partida:

Oponente: 5.4

Eu: 10

Em algo obviamente fora do normal, a alteração poderia continuar próxima dos valores daquela partida:

Oponente: 6.x

Eu: 7.x

Os valores são apenas exemplos.

O importante foi perceber que **eu não precisava forçar uma pontuação absurda. Bastava usar o próprio resultado da partida como referência e alterar minha pontuação o suficiente para ficar acima do oponente.**

Mantendo os dados reais da câmera e fazendo apenas essa alteração, o resultado passou a ser aceito.

A parte mais interessante é que eu não precisei quebrar o sistema de análise da câmera.

Também não precisei descobrir exatamente como cada regra do antifraude funcionava.

A partida continuava acontecendo normalmente:

Pessoa real diante da câmera

↓

Aplicação analisa a partida

↓

Dados reais da câmera são mantidos

↓

Pontuações são calculadas

↓

Minha pontuação é alterada antes do envio

↓

Servidor recebe o resultado

Foi aí que o problema ficou claro.

**O sistema tinha várias proteções para descobrir se a pontuação enviada parecia verdadeira, mas a pontuação ainda vinha de um lugar controlado pelo próprio usuário.**

Esse é o ponto central da vulnerabilidade.

No navegador, praticamente tudo pode ser alterado pelo usuário.

O JavaScript pode ser modificado, funções podem ser sobrescritas e as requisições podem ser alteradas antes de chegarem ao servidor.

Por isso existe uma regra muito conhecida em segurança:

***Never trust the client.***

Nesse caso, o navegador podia fazer todo o trabalho de analisar a câmera e calcular informações da partida.

O problema era permitir que ele também tivesse influência direta sobre uma informação tão importante quanto a pontuação que seria usada pelo servidor.

O sistema tentava compensar isso com várias verificações antifraude.

E elas realmente funcionavam.

Pontuações muito altas eram rejeitadas.

Dados estranhos da câmera eram identificados.

Resultados incompatíveis aparentemente também eram tratados como suspeitos.

Mas todas essas proteções estavam tentando responder à pergunta:

***“Essa pontuação que o navegador me enviou parece verdadeira?”***

Quando o ideal seria não depender apenas da resposta enviada pelo navegador para decidir o resultado.

A correção não é simplesmente esconder melhor o JavaScript ou dificultar a alteração da requisição.

Também não adianta depender apenas de bloquear o DevTools, ofuscar o código ou esconder o endpoint.

Tudo isso acontece no dispositivo do usuário.

Uma abordagem mais segura seria deixar o navegador responsável principalmente por coletar os dados necessários da partida e deixar a decisão final para o servidor.

De forma simples:

Navegador

↓

Envia os dados necessários da partida

↓

Servidor

↓

Valida as informações

↓

Calcula ou confirma o resultado

↓

Atualiza o ranking

Quanto mais importante for uma informação para o funcionamento da aplicação, menos sentido faz confiar que o próprio cliente entregue seu valor final sem uma validação independente no servidor.

O que mais gostei nesse teste foi que a vulnerabilidade não apareceu imediatamente.

Primeiro, alterar a requisição pelo Burp não funcionou.

Depois consegui fazer a alteração chegar ao servidor, mas recebi 1.0.

Corrigi o problema da câmera e continuei recebendo 1.0.

Descobri o sendBeacon().

Depois percebi que valores muito altos também pareciam ser identificados.

Cada tentativa que dava errado mostrava um pouco mais sobre como a aplicação funcionava.

No final, o problema não estava em quebrar cada uma dessas proteções.

Estava em perceber que, apesar de todas elas, **o navegador ainda conseguia alterar uma informação que influenciava diretamente o resultado da partida.**

É fácil associar uma vulnerabilidade a algo muito explícito: SQL Injection, XSS, SSRF, RCE e por aí vai.

Mas algumas das falhas mais interessantes aparecem simplesmente na forma como uma aplicação foi projetada.

Nesse caso, havia análise da câmera, detecção de comportamento suspeito e aparentemente até comparação entre os participantes.

As proteções não eram inúteis. Pelo contrário: várias delas conseguiram identificar minhas primeiras tentativas.

O problema estava na base.

A aplicação permitia que uma informação importante fosse calculada no navegador, enviada pelo próprio usuário e utilizada pelo servidor para determinar o resultado.

No fim, todo o teste pode ser resumido em uma pergunta bastante simples:

***Se o navegador está me dizendo qual é o resultado, o que impede o usuário de mudar esse resultado antes de enviá-lo?***

Essa é uma pergunta que vale fazer sempre que uma informação importante é calculada no frontend.
