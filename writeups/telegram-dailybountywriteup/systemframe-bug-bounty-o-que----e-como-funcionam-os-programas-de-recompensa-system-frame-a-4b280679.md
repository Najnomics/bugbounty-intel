# Bug bounty

- **Source URL:** https://medium.com/@systemframe/bug-bounty-o-que-%C3%A9-e-como-funcionam-os-programas-de-recompensa-system-frame-a17c95792f69
- **Fetched from:** https://medium.com/feed/@systemframe
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/15000 (id 15000)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Bug bounty é um programa em que uma empresa paga recompensas a pesquisadores de segurança que encontram e relatam vulnerabilidades em seus sistemas, seguindo regras definidas com antecedência. Em vez de esperar que a falha seja descoberta por um criminoso, a empresa convida especialistas a procurá-la de forma autorizada. O pesquisador relata o problema em sigilo, a empresa corrige e, depois, paga um valor proporcional à gravidade. É uma forma de ampliar os testes de segurança com gente de fora, que pensa diferente da equipe interna.

O tema voltou ao noticiário no fim de outubro. Segundo o TecMundo, o pesquisador Orange Tsai, da DEVCORE, ganhou 175 mil dólares no Pwn2Own ao encadear quatro falhas lógicas no Microsoft Edge, todas já corrigidas. Poucos dias depois, em 3 de novembro, a OpenAI elevou a recompensa máxima do seu programa de bug bounty para 172 mil dólares, com efeito retroativo para relatórios que ainda estavam pendentes. Os dois casos mostram o mesmo movimento: grandes empresas preferem pagar caro por uma falha descoberta do lado certo do que arcar com o custo de um ataque.

O que é bug bounty, na prática

Um programa de bug bounty tem três elementos básicos: um escopo, regras de participação e uma tabela de recompensas.

\- Escopo: quais sistemas podem ser testados (um site, um aplicativo, uma API) e quais estão fora, como sistemas de terceiros ou ambientes de produção sensíveis. — Regras: o que é permitido fazer durante o teste. Em geral, é proibido acessar dados reais de clientes além do mínimo necessário para provar a falha, derrubar serviços ou usar engenharia social contra funcionários. — Recompensas: valores definidos por nível de gravidade, normalmente baixa, média, alta e crítica.

Quando um pesquisador encontra algo, ele envia um relatório com a descrição da falha, os passos para reproduzi-la e o impacto possível. A equipe da empresa faz a triagem, confirma o problema, corrige e paga. Se o relatório for duplicado (outra pessoa já relatou a mesma falha) ou estiver fora do escopo, normalmente não há pagamento.

Bug bounty, Pwn2Own e pentest: qual a diferença

São três formas de encontrar vulnerabilidades, com lógicas diferentes.

O pentest (teste de intrusão) é um serviço contratado: uma equipe é paga para testar um ambiente durante um período definido, com relatório no final. O pagamento é pelo trabalho, não pelo resultado.

O bug bounty paga pelo resultado. Muitas pessoas podem testar ao mesmo tempo, por tempo indeterminado, e só recebe quem encontra algo válido.

O Pwn2Own é uma competição. Pesquisadores se inscrevem para explorar produtos conhecidos, como navegadores, sistemas operacionais e equipamentos, diante de juízes, em um evento com data marcada. As falhas exploradas são repassadas aos fabricantes para correção antes de qualquer divulgação pública. Foi nesse formato que a cadeia de falhas do Edge foi demonstrada.

Na prática, as três abordagens se complementam. Pentest dá profundidade em um momento específico, bug bounty dá cobertura contínua e competições ajudam a encontrar falhas em produtos de uso massivo.

Divulgação responsável: a regra que sustenta tudo

O conceito central por trás do bug bounty é a divulgação responsável, também chamada de divulgação coordenada. A ideia é simples: quem encontra a falha avisa primeiro o responsável e dá um prazo razoável para a correção antes de tornar o assunto público.

Esse acordo protege todos os lados:

\- O usuário final, porque a falha é corrigida antes de ser amplamente conhecida. — A empresa, porque tem tempo para corrigir sem pressão de um ataque em andamento. — O pesquisador, porque atua com autorização e regras claras, em vez de ficar numa zona cinzenta.

Por isso, programas de bug bounty costumam incluir uma cláusula de porto seguro: a empresa se compromete a não tomar medidas contra quem testou de boa-fé, dentro das regras. Sem essa garantia, muitos pesquisadores simplesmente não relatam o que encontram.

Como funcionam as plataformas de bug bounty

A maior parte dos programas roda em plataformas especializadas, como HackerOne, Bugcrowd e Intigriti. Elas fazem a ponte entre empresas e pesquisadores e cuidam de parte do trabalho operacional:

\- Publicação do escopo e das regras. — Recebimento padronizado dos relatórios. — Triagem inicial, para filtrar duplicados e relatórios sem fundamento. — Pagamento aos pesquisadores em vários países. — Histórico e reputação de cada participante.

Os programas podem ser públicos, abertos a qualquer pesquisador cadastrado, ou privados, em que só pessoas convidadas participam. Empresas que estão começando costumam optar pelo modelo privado, com poucos pesquisadores, para não serem inundadas de relatórios antes de terem processo para tratá-los.

Empresa pequena precisa de bug bounty?

Nem toda empresa precisa de um programa pago com recompensas. Para muitas pequenas e médias empresas, abrir um bug bounty sem estrutura para responder pode gerar mais trabalho do que proteção. Mas toda empresa que tem site, sistema ou aplicativo exposto na internet deveria ter, no mínimo, um canal para receber avisos de vulnerabilidade.

Esse canal é chamado de política de divulgação de vulnerabilidades (VDP, na sigla em inglês). A diferença para o bug bounty é que não há recompensa obrigatória: a empresa apenas informa como quer ser avisada, se compromete a responder e garante que não vai processar quem relatar de boa-fé.

Um jeito simples de começar é o arquivo security.txt. Ele é um arquivo de texto publicado no endereço /.well-known/security.txt do site, padronizado pela RFC 9116, que informa:

\- Um contato para relatos de segurança (um e-mail dedicado, por exemplo). — A data de validade das informações. — Opcionalmente, um link para a política de divulgação e idiomas aceitos.

Com isso, quem encontrar uma falha no seu site sabe a quem avisar, em vez de mandar a informação para o SAC, para uma rede social ou, pior, não mandar para ninguém.

Como estruturar um canal de vulnerabilidades

Antes de publicar qualquer canal, vale organizar o processo interno. Um roteiro básico:

1\. Defina quem recebe os relatos. Um e-mail dedicado, como seguranca@ ou security@, monitorado por mais de uma pessoa. 2. Estabeleça um prazo de primeira resposta. Confirmar o recebimento em poucos dias já passa confiança. 3. Tenha critério de gravidade. Usar uma escala conhecida, como o CVSS, ajuda a priorizar. 4. Combine o fluxo de correção com quem desenvolve ou mantém o sistema, inclusive fornecedores. 5. Registre tudo: data do relato, avaliação, correção e retorno ao pesquisador. 6. Agradeça. Mesmo sem recompensa em dinheiro, um agradecimento público (com autorização) é valorizado.

Quando esse processo estiver funcionando bem, a empresa pode avaliar se faz sentido evoluir para um programa com recompensas, começando pelo modelo privado e com escopo pequeno.

O que define o valor de uma recompensa

Os valores recentes chamam atenção, mas a maioria das recompensas é bem menor. O que pesa na conta:

\- Gravidade: uma falha que permite executar código remotamente vale muito mais do que um erro de configuração de baixo impacto. — Alcance: falhas em produtos usados por milhões de pessoas, como navegadores, valem mais. — Qualidade do relatório: descrições claras e passos de reprodução precisos aceleram a correção e costumam ser mais bem pagos. — Encadeamento: como no caso do Edge, combinar várias falhas aparentemente pequenas em um ataque completo mostra um impacto real e eleva o valor.

Esse último ponto é uma lição importante para quem cuida de TI: falhas lógicas, que não são erros de programação clássicos, mas falhas de raciocínio no fluxo do sistema, podem ser tão perigosas quanto as mais técnicas.

Bug bounty como carreira

Para quem está começando na área de segurança, o bug bounty é uma porta de entrada conhecida. Ele permite praticar em sistemas reais, com autorização, e construir reputação. Alguns caminhos comuns:

\- Estudar fundamentos de redes, sistemas operacionais e desenvolvimento web. — Conhecer as categorias de falhas mais frequentes em aplicações web, como as listadas pelo OWASP. — Praticar em laboratórios e ambientes de treinamento antes de participar de programas reais.

Vale um cuidado: testar sistemas sem autorização, fora de um programa ou de um contrato, pode configurar crime. A autorização é o que separa pesquisa de segurança de invasão.

Perguntas frequentes

O que é bug bounty? É um programa em que uma empresa paga recompensas a pesquisadores que encontram e relatam vulnerabilidades em seus sistemas, seguindo regras e escopo definidos previamente.

Qual a diferença entre bug bounty e pentest? No pentest, a empresa contrata uma equipe e paga pelo trabalho realizado em um período. No bug bounty, várias pessoas podem testar, e só recebe quem encontra uma falha válida.

Testar um site em busca de falhas é crime? Testar sem autorização pode ser. Dentro de um programa de bug bounty ou de um contrato de pentest, o teste é autorizado, desde que siga o escopo e as regras definidas.

O que é o arquivo security.txt? É um arquivo publicado no site, no caminho /.well-known/security.txt, que informa como e para quem relatar problemas de segurança. É uma forma simples de qualquer empresa abrir um canal de vulnerabilidades.

Empresa pequena deve ter bug bounty? Nem sempre. O primeiro passo recomendado é ter um canal de divulgação de vulnerabilidades e um processo para responder. O programa com recompensas pode vir depois, se fizer sentido.

Na sua empresa, alguém de fora saberia a quem avisar se encontrasse uma falha no seu site?
