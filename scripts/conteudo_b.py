# -*- coding: utf-8 -*-
"""Secoes 3 e 4: Gerenciamento de Projetos Agil e Programacao Aplicada em .NET."""

BLOCOS_B = [

# --------------------------------------------------------------- 3
("h1", "3 GERENCIAMENTO DE PROJETOS ÁGIL"),

("p", "A condução do projeto adotou abordagem ágil, com entrega incremental de valor e "
 "adaptação contínua ao aprendizado de cada ciclo. A escolha decorre do cenário da Alunos "
 "Tech: os requisitos de controle de nível de serviço só foram plenamente compreendidos "
 "após a primeira versão operacional do painel, situação em que um planejamento preditivo "
 "detalhado produziria retrabalho."),

("h2", "3.1 Fundamentos e escolha do método"),

("p", "O Manifesto para o Desenvolvimento Ágil de Software estabelece a preferência por "
 "indivíduos e interações, software em funcionamento, colaboração com o cliente e "
 "resposta a mudanças (BECK et al., 2001). O Scrum operacionaliza esses valores por meio "
 "de um arcabouço leve, descrito por seus autores nos seguintes termos:"),

("cit", "O Scrum é um framework leve que ajuda pessoas, times e organizações a gerar "
 "valor por meio de soluções adaptativas para problemas complexos. [...] O Scrum emprega "
 "uma abordagem iterativa e incremental para otimizar a previsibilidade e controlar os "
 "riscos (SCHWABER; SUTHERLAND, 2020, p. 3)."),

("p", "Optou-se pelo modelo híbrido conhecido como Scrumban. Do Scrum preservaram-se as "
 "sprints de duas semanas, o backlog do produto e as cerimônias de planejamento, revisão "
 "e retrospectiva; do Kanban incorporaram-se a visualização explícita do fluxo e os "
 "limites de trabalho em progresso, descritos por Anderson (2011) como mecanismos de "
 "redução do tempo de atravessamento. A combinação justifica-se porque a equipe também "
 "atende demandas emergenciais da operação, exigindo um fluxo capaz de absorver "
 "interrupções sem comprometer o compromisso da sprint."),

("h2", "3.2 Estrutura do time e cerimônias"),

("p", "O time foi composto por seis integrantes. O papel de Product Owner coube ao "
 "gerente de operações da Alunos Tech, responsável por ordenar o backlog conforme o valor "
 "de negócio; o de Scrum Master foi assumido em rodízio a cada duas sprints, de modo a "
 "desenvolver a competência de facilitação em todo o grupo. As cerimônias foram fixadas "
 "em planejamento de duas horas, reunião diária de quinze minutos, revisão com "
 "demonstração ao Product Owner e retrospectiva de uma hora."),

("h2", "3.3 Backlog do produto"),

("p", "O backlog foi construído a partir dos requisitos do Quadro 1 e organizado em "
 "épicos, decompostos em histórias de usuário. A estimativa empregou pontos de história "
 "com a sequência de Fibonacci, atribuídos por consenso em sessões de planning poker, e a "
 "priorização utilizou o método MoSCoW, como mostra o Quadro 2."),

("quadro", "Quadro 2 – Backlog do produto da plataforma AT-Integra",
 ["Épico", "Principais histórias de usuário", "Pontos", "MoSCoW"],
 [["Atendimento", "Registrar chamado com protocolo; calcular o prazo de nível de serviço; "
   "distribuir a fila automaticamente; acompanhar o painel em tempo real", "26", "Must"],
  ["Mobilidade", "Consultar atendimentos no aplicativo; apontar horas e concluir sem "
   "conexão; anexar evidências fotográficas", "16", "Must / Should"],
  ["Governança", "Registrar trilha de auditoria; controlar acesso por perfil e por cliente; "
   "exportar relatório de conformidade com a LGPD", "11", "Must / Could"],
  ["Financeiro", "Gerar prévia de faturamento por contrato; consolidar horas excedentes "
   "por competência", "10", "Should"],
  ["Plataforma", "Publicar por esteira automatizada; escalar conforme a demanda; monitorar "
   "indicadores de saúde e de custo", "18", "Must / Should"],
  ["Total estimado", "15 histórias de usuário distribuídas em cinco épicos", "81", "—"]],
 "Fonte: Elaborado pelos autores (2026)."),

("p", "O total estimado somou 81 pontos. A velocidade média foi de 14 pontos por ciclo "
 "nas duas primeiras sprints e de 15,5 a partir da terceira, quando a esteira de "
 "automação reduziu o esforço manual de publicação."),

("h2", "3.4 Planejamento de releases e sprints"),

("p", "O escopo foi distribuído em seis sprints de duas semanas, agrupadas em três "
 "entregas incrementais, cada uma capaz de ser colocada em produção e de gerar valor "
 "mensurável (HUMBLE; FARLEY, 2014). A Tabela 2 apresenta o planejamento executado."),

("tab", "Tabela 2 – Planejamento de releases e sprints do projeto AT-Integra",
 ["Sprint", "Período", "Objetivo principal", "Pontos", "Release"],
 [["1", "24/08 a 06/09", "Fundação da arquitetura e do modelo de dados", "13", "R1"],
  ["2", "07/09 a 20/09", "Registro de chamados e cálculo de nível de serviço", "15", "R1"],
  ["3", "21/09 a 04/10", "Painel de operações e autenticação por perfil", "16", "R2"],
  ["4", "05/10 a 18/10", "Aplicativo móvel e apontamento de horas", "16", "R2"],
  ["5", "19/10 a 01/11", "Distribuição automática e esteira de implantação", "13", "R3"],
  ["6", "02/11 a 15/11", "Observabilidade, faturamento e ajustes finais", "8", "R3"]],
 "Fonte: Elaborada pelos autores (2026)."),

("h2", "3.5 Acompanhamento do fluxo e métricas"),

("p", "O quadro Kanban tornou visível o estado de cada item e explicitou os limites de "
 "trabalho em progresso definidos por coluna. A Figura 2 reproduz o quadro ao final da "
 "quinta sprint, momento em que a coluna de desenvolvimento atingiu seu limite, sinal que "
 "orientou a equipe a concentrar esforço na conclusão dos itens em revisão antes de "
 "iniciar novas tarefas."),

("fig", "fig_kanban.png",
 "Figura 2 – Quadro Kanban do projeto ao final da Sprint 5",
 "Fonte: Elaborada pelos autores (2026).", 12.5),

("p", "As métricas de fluxo acompanhadas foram o tempo de atravessamento (3,4 dias em "
 "média), a vazão (nove itens por sprint) e o trabalho em progresso médio (6,8 itens), "
 "relação coerente com a Lei de Little. O gráfico de queima da Figura 3 evidencia o "
 "impacto de um impedimento ocorrido no sexto dia útil."),

("fig", "fig_burndown.png",
 "Figura 3 – Gráfico de queima (burndown) da Sprint 6",
 "Fonte: Elaborada pelos autores (2026).", 11.5),

("p", "A indisponibilidade do ambiente de homologação entre o quinto e o sétimo dia "
 "paralisou a validação de duas histórias, o que produziu o patamar observado na curva "
 "real. Dos 34 pontos comprometidos, 29 foram concluídos, resultando em aderência de "
 "85,3% ao compromisso da sprint. Os cinco pontos restantes retornaram ao topo do backlog."),

("h2", "3.6 Melhoria contínua e gestão de riscos"),

("p", "As retrospectivas produziram ações objetivas, com responsável e prazo. A da "
 "Sprint 5 identificou que a indisponibilidade do ambiente decorria de sua configuração "
 "manual e resultou na adoção de infraestrutura como código, que passou a recriar o "
 "ambiente em onze minutos. A da Sprint 3 estabeleceu a Definição de Pronto: código "
 "revisado por outro integrante, testes aprovados, cobertura mínima de 80% e documentação "
 "atualizada."),

("p", "Os riscos do projeto foram registrados e reavaliados a cada planejamento, prática "
 "que o Guia PMBOK associa ao domínio de desempenho da incerteza (PROJECT MANAGEMENT "
 "INSTITUTE, 2021). Os de maior "
 "exposição foram a dependência de um único integrante com domínio de Kubernetes, "
 "mitigada por programação em pares; a indisponibilidade de ambientes, mitigada pela "
 "automação citada; e a instabilidade de requisitos do faturamento, mitigada pela "
 "antecipação de uma demonstração ao setor financeiro."),

("h2", "3.7 Orçamento do projeto"),

("p", "O orçamento foi elaborado com base no esforço estimado e nos preços praticados no "
 "mercado em 2026, considerando o regime de contratação dos profissionais e a aquisição "
 "dos recursos necessários à implantação. A Tabela 3 apresenta a composição."),

("tab", "Tabela 3 – Orçamento de implantação da solução AT-Integra",
 ["Item", "Quantidade", "Valor unitário (R$)", "Valor total (R$)"],
 [["Desenvolvedor pleno (12 semanas)", "3", "9.800,00/mês", "88.200,00"],
  ["Desenvolvedor sênior (12 semanas)", "1", "14.500,00/mês", "43.500,00"],
  ["Especialista em dados (6 semanas)", "1", "13.200,00/mês", "19.800,00"],
  ["Especialista em nuvem (8 semanas)", "1", "15.100,00/mês", "30.200,00"],
  ["Estação de trabalho para desenvolvimento", "6", "7.400,00", "44.400,00"],
  ["Consumo de nuvem no período do projeto", "3 meses", "6.350,00/mês", "19.050,00"],
  ["Licenças, capacitação e contingência", "—", "—", "44.425,00"],
  ["Total do investimento", "—", "—", "289.575,00"]],
 "Fonte: Elaborada pelos autores (2026)."),

("p", "Confrontando o investimento com a economia mensal projetada de R$ 5.340,00 em "
 "infraestrutura e com a redução estimada de R$ 18.700,00 por trimestre em multas "
 "contratuais, obtém-se prazo de retorno aproximado de 23 meses, valor considerado "
 "aceitável pela diretoria diante da natureza estruturante da solução."),

# --------------------------------------------------------------- 4
("h1", "4 PROGRAMAÇÃO APLICADA EM .NET"),

("p", "Esta seção descreve a construção dos módulos corporativos da plataforma sobre a "
 "plataforma .NET 8 e a linguagem C#. São apresentados a organização arquitetural da "
 "solução, a aplicação dos conceitos de orientação a objetos, os padrões de projeto "
 "adotados e as estratégias de desempenho, teste e manutenção."),

("h2", "4.1 Arquitetura modular da solução"),

("p", "A solução foi estruturada em quatro camadas, segundo os princípios da arquitetura "
 "limpa descritos por Martin (2019). A regra fundamental é a da dependência: o código das "
 "camadas externas pode referenciar o das camadas internas, nunca o contrário. Na "
 "prática, isso significa que o projeto que concentra as regras de negócio não referencia "
 "nem o mapeador objeto-relacional nem o arcabouço web, permanecendo independente de "
 "tecnologia. A organização adotada distribui os projetos da solução entre as camadas de apresentação, aplicação, domínio e infraestrutura."),

("p", "A separação trouxe dois ganhos verificáveis: testar as regras de negócio sem "
 "banco de dados reduziu a bateria de testes de 4 min 10 s para 38 s, viabilizando sua "
 "execução a cada envio de código; e o núcleo de domínio é reaproveitado integralmente "
 "pelos canais web, desktop e móvel, eliminando a duplicação de regras do cenário "
 "anterior."),

("h2", "4.2 Orientação a objetos aplicada ao domínio"),

("p", "O modelo de domínio reúne entidades que encapsulam estado e comportamento, e não "
 "apenas dados. A classe abstrata EntidadeBase concentra os atributos de identificação, "
 "auditoria e versão, aplicando herança e definindo um método abstrato de validação que "
 "cada entidade concreta implementa — caso típico de polimorfismo. A classe Chamado, na "
 "Figura 4, é a raiz de agregação do módulo de atendimento."),

("fig", "fig_cod_entidade.png",
 "Figura 4 – Classe Chamado: encapsulamento e invariantes do domínio",
 "Fonte: Elaborada pelos autores (2026).", 12.5),

("p", "Três decisões de projeto merecem destaque. Os atributos têm escrita privada, de "
 "modo que o estado só é alterado pelos métodos de negócio, o que impede que uma camada "
 "externa coloque o objeto em situação inválida. A coleção de apontamentos é exposta "
 "como somente leitura, obrigando qualquer inclusão a passar pelo método que verifica as "
 "regras aplicáveis. Por fim, a validação é invocada no próprio construtor, garantindo "
 "que não exista instância inválida em memória."),

("h2", "4.3 Padrões de projeto adotados"),

("p", "Os padrões de projeto constituem soluções reutilizáveis para problemas recorrentes "
 "de projeto de software (GAMMA et al., 2000). Os padrões voltados à persistência, como "
 "Repository e Unit of Work, foram sistematizados por Fowler (2006) no contexto de "
 "aplicações corporativas. O Quadro 3 relaciona os padrões empregados e a justificativa "
 "técnica de cada escolha."),

("quadro", "Quadro 3 – Padrões de projeto aplicados na solução AT-Integra",
 ["Padrão", "Aplicação na solução", "Justificativa técnica"],
 [["Strategy", "Cálculo do prazo de nível de serviço por tipo de contrato",
   "Permite acrescentar novos níveis sem alterar a entidade Chamado"],
  ["Factory Method", "Criação da estratégia a partir do nível registrado no contrato",
   "Isola a decisão de instanciação em um único ponto do código"],
  ["Repository", "Abstração do acesso aos dados de cada agregado",
   "Desacopla o domínio do mapeador objeto-relacional"],
  ["Unit of Work", "Confirmação atômica das operações de uma requisição",
   "Garante que falhas parciais não deixem dados inconsistentes"],
  ["Dependency Injection", "Fornecimento das dependências pelo contêiner nativo",
   "Viabiliza substituição por simulações nos testes de unidade"],
  ["MVVM", "Separação entre interface e lógica nos módulos desktop e móvel",
   "Permite testar o comportamento da tela sem executá-la"]],
 "Fonte: Elaborado pelos autores (2026)."),

("p", "O Apêndice A reúne a implementação do padrão Strategy: cada nível contratual tem "
 "classe própria de cálculo de prazo, sendo que a Silver considera apenas horas úteis e a "
 "Gold opera em regime ininterrupto. Um futuro nível Platinum exigiria apenas uma nova "
 "classe e uma linha na fábrica, sem alterar regras já testadas — aplicação direta do "
 "princípio aberto-fechado."),

("h2", "4.4 Aplicação web e módulo desktop"),

("p", "A camada web foi implementada com ASP.NET Core, expondo uma interface de "
 "programação no estilo REST, versionada e documentada, e um portal de operações "
 "construído sobre ela. O controle de acesso usa token JWT assinado, com autorização por "
 "papéis, de modo que o perfil de atendente não alcança as operações da supervisão. A "
 "Figura 5 apresenta o painel de operações da central."),

("fig", "fig_web_painel.png",
 "Figura 5 – Painel de operações da aplicação web AT-Integra",
 "Fonte: Elaborada pelos autores (2026).", 12.5),

("p", "O painel responde à pergunta operacional mais frequente da central: qual chamado "
 "deve ser tratado agora. Por isso a fila é ordenada por criticidade e por proximidade do "
 "prazo contratado, e não por data de abertura. O bloco lateral mostra a aderência por "
 "contrato, informação que antes exigia consolidação manual de planilhas. O módulo "
 "desktop, desenvolvido em WPF com o padrão MVVM, reaproveita os mesmos serviços de "
 "aplicação e atende às estações internas em rede corporativa restrita."),

("h2", "4.5 Aplicativo móvel integrado"),

("p", "O aplicativo dos técnicos em campo foi construído com .NET MAUI, compartilhando a "
 "lógica de apresentação entre Android e iOS a partir de uma única base de código. O "
 "requisito determinante é a operação sem conexão, pois parte dos atendimentos ocorre em "
 "data centers e áreas industriais sem cobertura móvel. A Figura 6 apresenta as duas "
 "telas principais."),

("fig", "fig_mobile.png",
 "Figura 6 – Aplicativo móvel: fila de atendimentos e execução em campo",
 "Fonte: Elaborada pelos autores (2026).", 9.5),

("p", "Adotou-se a prioridade ao funcionamento local: toda alteração é gravada em banco "
 "SQLite no dispositivo e enfileirada para sincronização; restabelecida a conectividade, "
 "um serviço em segundo plano reenvia os pendentes e trata conflitos pela comparação do "
 "token de versão. A decisão eliminou a principal causa de atraso no faturamento, pois o "
 "apontamento passou a ocorrer no momento da execução do serviço."),

("h2", "4.6 Desempenho, testes e manutenção"),

("p", "A estratégia de testes seguiu a pirâmide clássica: maior volume em testes de "
 "unidade sobre o domínio e a aplicação, complementados por testes de integração e por um "
 "conjunto reduzido de testes de ponta a ponta. A suíte reúne 142 casos, com cobertura "
 "global de 86,4% e de 94,2% no domínio, e bloqueia a entrega quando a cobertura fica "
 "abaixo do limite."),

("p", "No tocante ao desempenho, três medidas produziram efeito mensurável: a desativação "
 "do rastreamento de mudanças nas consultas somente de leitura, a compressão das respostas "
 "e o uso de cache distribuído para o painel de operações, todas documentadas como boas "
 "práticas da plataforma (MICROSOFT, 2026). Em conjunto, reduziram o tempo "
 "de resposta do percentil 95 de 341 para 212 milissegundos. A manutenção apoia-se na "
 "organização em projetos independentes e na análise estática executada a cada "
 "integração. O código completo consta do Apêndice A."),
]
