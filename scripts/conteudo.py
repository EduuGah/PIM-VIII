# -*- coding: utf-8 -*-
"""Conteudo textual do PIM VIII. Estruturado em blocos para que o gerador
monte o documento com a formatacao exigida pela ABNT."""

AUTORES = [
    ("Allison Miguel de Oliveira", "2527226"),
    ("Carlos Eduardo da Silva de Oliveira", "2525997"),
    ("Cauã de Almeida Paiva", "2508932"),
    ("Guilherme Almeida da Silva", "2510058"),
    ("Marco Antonio Figueredo Silva", "2524300"),
    ("Vitor Alexandre Fulgoni Cambuhy Lara", "2528970"),
]

TITULO = "SOLUÇÃO TECNOLÓGICA CORPORATIVA INTEGRADA PARA A EMPRESA ALUNOS TECH"
SUBTITULO = ("arquitetura em nuvem, gestão ágil, aplicações .NET e banco de dados "
             "otimizado para a modernização dos serviços digitais")
CURSO = "Análise e Desenvolvimento de Sistemas"
CIDADE = "São Paulo – SP"
ANO = "2026"
ORIENTADOR = "Prof. Paulo Lourenção"

RESUMO = (
    "Este trabalho apresenta o projeto de uma solução tecnológica corporativa integrada "
    "para a empresa fictícia Alunos Tech, organização do segmento de serviços corporativos "
    "digitais que enfrenta dificuldades de integração de sistemas, de controle da operação "
    "de atendimento e de escalabilidade da sua infraestrutura. O objetivo geral foi projetar "
    "e demonstrar, por meio de protótipos funcionais, uma plataforma denominada AT-Integra, "
    "capaz de unificar o atendimento a clientes, o controle contratual de níveis de serviço "
    "e a gestão operacional da empresa em ambiente web, desktop e móvel. A metodologia "
    "adotada foi a pesquisa aplicada, de natureza exploratória e descritiva, conduzida em "
    "quatro etapas: levantamento do cenário e dos requisitos da organização; definição da "
    "arquitetura da solução; construção dos artefatos de projeto e dos componentes de "
    "software; e avaliação dos resultados por meio de indicadores operacionais. O "
    "desenvolvimento integrou quatro disciplinas do semestre. Em Gerenciamento de Projetos "
    "Ágil, estruturaram-se o backlog do produto, o planejamento de seis sprints, o quadro "
    "Kanban com limites de trabalho em progresso e o orçamento do projeto. Em Programação "
    "Aplicada em .NET, implementou-se uma arquitetura modular em camadas com C# e .NET 8, "
    "aplicando orientação a objetos e os padrões de projeto Strategy, Factory Method, "
    "Repository e Unit of Work. Em Programação de Banco de Dados, construíram-se o modelo "
    "relacional, procedimentos armazenados transacionais, funções, gatilhos de auditoria, "
    "índices cobertos e mecanismos de controle de concorrência e de segurança. Em Cloud "
    "Computing e DevOps, definiu-se uma arquitetura em nuvem com contêineres, orquestração "
    "por Kubernetes, esteira de integração e entrega contínuas e monitoramento. Os "
    "resultados obtidos no ambiente de demonstração indicam redução de até 98,6% no tempo "
    "de resposta das consultas críticas, elevação da aderência ao nível de serviço de 85,5% "
    "para 96,8% e aumento da frequência de implantações de duas para quarenta e duas por "
    "mês, com redução de 36,4% no custo mensal de operação. Conclui-se que a integração "
    "entre as quatro disciplinas foi determinante para que a solução atendesse "
    "simultaneamente aos requisitos técnicos, gerenciais e econômicos da organização."
)

PALAVRAS_CHAVE = ("Computação em nuvem. DevOps. Metodologias ágeis. "
                  "Banco de dados. Desenvolvimento de software.")

ABSTRACT = (
    "This paper presents the design of an integrated corporate technological solution for "
    "the fictitious company Alunos Tech, an organization in the digital corporate services "
    "segment that faces difficulties regarding systems integration, control of its service "
    "operation and infrastructure scalability. The general objective was to design and "
    "demonstrate, through functional prototypes, a platform named AT-Integra, able to unify "
    "customer support, the contractual control of service levels and the company's "
    "operational management in web, desktop and mobile environments. The adopted "
    "methodology was applied research, of exploratory and descriptive nature, carried out "
    "in four stages: survey of the organization's scenario and requirements; definition of "
    "the solution architecture; construction of the design artifacts and software "
    "components; and evaluation of results through operational indicators. The development "
    "integrated four subjects of the semester. In Agile Project Management, the product "
    "backlog, the planning of six sprints, the Kanban board with work-in-progress limits "
    "and the project budget were structured. In Applied .NET Programming, a modular layered "
    "architecture was implemented with C# and .NET 8, applying object orientation and the "
    "Strategy, Factory Method, Repository and Unit of Work design patterns. In Database "
    "Programming, the relational model, transactional stored procedures, functions, audit "
    "triggers, covering indexes and concurrency control and security mechanisms were built. "
    "In Cloud Computing and DevOps, a cloud architecture was defined with containers, "
    "Kubernetes orchestration, a continuous integration and delivery pipeline and "
    "monitoring. The results obtained in the demonstration environment indicate a reduction "
    "of up to 98.6% in the response time of critical queries, an increase in service level "
    "adherence from 85.5% to 96.8% and an increase in deployment frequency from two to "
    "forty-two per month, with a 36.4% reduction in the monthly operating cost. It is "
    "concluded that the integration between the four subjects was decisive for the solution "
    "to simultaneously meet the technical, managerial and economic requirements of the "
    "organization."
)

KEYWORDS = ("Cloud computing. DevOps. Agile methodologies. "
            "Database. Software development.")


# =====================================================================
# Blocos do texto. Tipos aceitos pelo gerador:
#   h1, h2, h3, p, fig, tab, quadro, cit
# =====================================================================
BLOCOS = [

# --------------------------------------------------------------- 1
("h1", "1 INTRODUÇÃO"),

("p", "A transformação digital deixou de ser um diferencial competitivo e passou a "
 "constituir condição de permanência das organizações no mercado. Empresas prestadoras "
 "de serviços corporativos digitais enfrentam, simultaneamente, a pressão por "
 "disponibilidade contínua, por previsibilidade de prazos contratados e por redução de "
 "custos operacionais. Nesse contexto, soluções construídas de forma fragmentada — com "
 "planilhas, sistemas isolados e processos manuais — tornam-se o principal obstáculo ao "
 "crescimento, pois impedem a visão unificada da operação e multiplicam o esforço de "
 "manutenção."),

("p", "O presente Projeto Integrado Multidisciplinar tem como objetivo geral projetar uma "
 "solução tecnológica corporativa integrada para a empresa fictícia Alunos Tech, "
 "contemplando arquitetura de software, infraestrutura em nuvem, banco de dados, "
 "metodologias ágeis e aplicações corporativas. Como objetivos específicos, pretende-se: "
 "desenvolver aplicações web e móvel integradas; estruturar um banco de dados seguro e "
 "otimizado; aplicar práticas de computação em nuvem e DevOps; utilizar metodologias "
 "ágeis na gestão do projeto; implementar soluções escaláveis e seguras; e propor uma "
 "arquitetura tecnológica alinhada ao negócio."),

("p", "Quanto à metodologia, trata-se de pesquisa aplicada, de natureza exploratória e "
 "descritiva, com abordagem predominantemente qualitativa complementada por indicadores "
 "quantitativos. Conforme Gil (2017), a pesquisa exploratória tem como propósito "
 "proporcionar maior familiaridade com o problema, com vistas a torná-lo mais explícito, "
 "o que se mostrou adequado ao diagnóstico inicial da organização. O trabalho foi "
 "conduzido em quatro etapas. Na primeira, realizou-se o levantamento do cenário da "
 "empresa, de seus processos de atendimento e das limitações do parque tecnológico "
 "existente. Na segunda, definiu-se a arquitetura da solução e elaboraram-se os artefatos "
 "de projeto, como requisitos, backlog, modelo de dados e topologia de infraestrutura. Na "
 "terceira, construíram-se os componentes de software em ambiente de demonstração, "
 "abrangendo a interface web, o módulo desktop, o aplicativo móvel, a camada de "
 "persistência e a esteira de automação. Na quarta, avaliaram-se os resultados por meio "
 "de indicadores operacionais, financeiros e de qualidade, comparando-se o cenário "
 "anterior ao cenário proposto. A fundamentação teórica apoiou-se no material oficial das "
 "disciplinas do curso e em obras de referência das áreas envolvidas. Quanto à "
 "normalização, observaram-se as orientações de Severino (2016) e de Lakatos e Marconi "
 "(2017) e as normas NBR 14724 (ABNT, 2011), NBR 6024 (ABNT, 2012), NBR 6023 (ABNT, 2018) "
 "e NBR 6028 (ABNT, 2021)."),

("p", "A empresa selecionada para a investigação, a Alunos Tech, é uma organização "
 "fictícia que atua no segmento de serviços corporativos digitais, prestando suporte "
 "técnico, sustentação de sistemas e serviços gerenciados de infraestrutura a clientes de "
 "médio porte. Com o crescimento acelerado da carteira, a empresa passou a enfrentar "
 "dificuldades relacionadas à integração de sistemas, ao gerenciamento de informações, à "
 "segurança dos dados, à comunicação entre equipes e à escalabilidade de seus serviços, o "
 "que motivou a contratação de uma equipe de desenvolvimento para elaborar a proposta "
 "descrita neste trabalho."),

# --------------------------------------------------------------- 2
("h1", "2 A EMPRESA ALUNOS TECH E A SITUAÇÃO-PROBLEMA"),

("h2", "2.1 Caracterização da organização"),

("p", "A Alunos Tech é uma empresa de serviços corporativos digitais sediada em São "
 "Paulo, com 86 colaboradores, dos quais 34 na equipe técnica, e carteira de 27 clientes "
 "atendidos por contratos de prestação continuada em dois níveis de serviço. O contrato "
 "Gold prevê cobertura ininterrupta, com prazo de duas horas para incidentes críticos; o "
 "Silver, atendimento em horário comercial, com quatro horas úteis. O cumprimento desses "
 "prazos é a principal obrigação contratual da empresa e está associado a multas."),

("p", "A receita provém da mensalidade fixa dos contratos (62% do faturamento), das horas "
 "técnicas excedentes apontadas em campo (27%) e de projetos pontuais de implantação "
 "(11%). Essa composição evidencia que o controle de prazos e o registro confiável das "
 "horas trabalhadas impactam diretamente o resultado financeiro da empresa."),

("h2", "2.2 Diagnóstico do parque tecnológico e dos processos"),

("p", "O levantamento revelou um ambiente heterogêneo, formado por sistemas adquiridos em "
 "momentos distintos e sem integração: os chamados chegam a uma caixa de correio "
 "compartilhada e são transcritos para uma planilha; os contratos residem em um sistema "
 "legado cliente-servidor; e o apontamento de horas é preenchido em papel e digitado ao "
 "final da semana. A Tabela 1 sintetiza o inventário."),

("tab", "Tabela 1 – Inventário do parque tecnológico e dos processos da Alunos Tech",
 ["Recurso ou processo", "Situação identificada", "Limitação principal"],
 [["Registro de chamados", "Caixa de correio compartilhada e planilha",
   "Ausência de protocolo e de rastreabilidade"],
  ["Controle de contratos", "Sistema legado cliente-servidor (2011)",
   "Não calcula prazos de nível de serviço"],
  ["Apontamento de horas", "Formulário impresso digitado semanalmente",
   "Atraso de até sete dias no faturamento"],
  ["Servidores", "2 servidores físicos locais, sem redundância",
   "Indisponibilidade média de 14 h por trimestre"],
  ["Banco de dados", "Instância única, sem índices revisados",
   "Consultas gerenciais acima de 8 segundos"],
  ["Publicação de versões", "Cópia manual de arquivos, fora do expediente",
   "Duas implantações por mês, com falhas frequentes"],
  ["Acesso remoto da equipe", "Área de trabalho remota sem segundo fator",
   "Exposição de credenciais e risco de acesso indevido"]],
 "Fonte: Elaborada pelos autores (2026)."),

("p", "A consequência é a perda de controle sobre a obrigação contratual mais relevante "
 "da empresa: no trimestre analisado, a aderência aos prazos foi de 85,5%, o que gerou "
 "multas e três pedidos de revisão de contrato. A ausência de registro único impede ainda "
 "identificar qual cliente, incidente ou técnico concentra as violações, inviabilizando "
 "ação corretiva fundamentada em dados."),

("h2", "2.3 Requisitos da solução"),

("p", "A partir do diagnóstico, elaborou-se a especificação de requisitos da plataforma, "
 "denominada AT-Integra. Os requisitos funcionais descrevem o que o sistema deve fazer, "
 "enquanto os não funcionais estabelecem restrições de qualidade, desempenho e segurança "
 "(SOMMERVILLE, 2018; PRESSMAN; MAXIM, 2016). O Quadro 1 apresenta o conjunto "
 "consolidado."),

("quadro", "Quadro 1 – Requisitos funcionais e não funcionais da plataforma AT-Integra",
 ["Código", "Descrição do requisito", "Prioridade"],
 [["RF01", "Registrar chamados com protocolo único, vinculados a cliente e a contrato", "Essencial"],
  ["RF02", "Calcular o prazo de atendimento conforme o nível de serviço do contrato", "Essencial"],
  ["RF03", "Distribuir chamados por prioridade, especialidade e disponibilidade do técnico", "Essencial"],
  ["RF04", "Apontar horas e concluir atendimentos em campo, inclusive sem conexão", "Essencial"],
  ["RF05", "Manter trilha de auditoria e painel gerencial de nível de serviço", "Essencial"],
  ["RF06", "Gerar prévia de faturamento e notificar o responsável do cliente", "Importante"],
  ["RNF01", "Responder a 95% das requisições em até 500 ms, com 99,9% de disponibilidade", "Essencial"],
  ["RNF02", "Cifrar dados em trânsito e em repouso, com acesso por perfil e aderência à LGPD", "Essencial"],
  ["RNF03", "Escalar até doze instâncias e operar em navegadores corporativos, Android e iOS", "Importante"]],
 "Fonte: Elaborado pelos autores (2026)."),

("h2", "2.4 Visão geral da arquitetura proposta"),

("p", "A arquitetura adotada é distribuída e orientada a serviços, hospedada em nuvem "
 "pública sob o modelo de plataforma como serviço combinado a contêineres gerenciados. A "
 "escolha considerou três critérios: a necessidade de elasticidade para absorver os picos "
 "de abertura de chamados no início do expediente; a exigência de disponibilidade superior "
 "à oferecida pelo parque local; e a redução do esforço de administração de infraestrutura "
 "por uma equipe técnica reduzida. A Figura 1 apresenta a topologia lógica da solução, que "
 "será detalhada nas seções subsequentes sob a perspectiva de cada disciplina."),

("fig", "fig_arq_cloud.png",
 "Figura 1 – Topologia lógica da solução AT-Integra em nuvem",
 "Fonte: Elaborada pelos autores (2026).", 15.5),

("p", "O fluxo parte do canal de acesso — portal web, aplicativo móvel, módulo desktop "
 "ou integração de parceiros — e atravessa as camadas de proteção de borda, autenticação "
 "e limitação de requisições antes de alcançar o cluster. O processamento assíncrono foi "
 "separado do síncrono para que tarefas demoradas não comprometam o tempo de resposta, e "
 "a persistência é segregada por natureza do dado: banco relacional para o núcleo "
 "transacional, cache em memória para o painel e armazenamento de objetos para as "
 "evidências."),
]
