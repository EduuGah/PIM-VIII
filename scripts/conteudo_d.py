# -*- coding: utf-8 -*-
"""Secoes 7 e 8, referencias e apendices."""

BLOCOS_D = [

# --------------------------------------------------------------- 7
("h1", "7 RESULTADOS OBTIDOS"),

("p", "Esta seção consolida os resultados da solução proposta. A avaliação ocorreu em "
 "ambiente de demonstração, com base povoada a partir do histórico de doze meses de "
 "atendimento da Alunos Tech, o que permitiu comparar os cenários sob as mesmas condições "
 "de volume. A Tabela 5 reúne os indicadores selecionados, escolhidos por refletirem a "
 "obrigação contratual da empresa, a produtividade da equipe e a eficiência da entrega de "
 "software."),

("tab", "Tabela 5 – Comparativo dos indicadores antes e depois da implantação",
 ["Indicador", "Cenário anterior", "Cenário proposto", "Variação"],
 [["Aderência ao nível de serviço", "85,5%", "96,8%", "+11,3 p.p."],
  ["Disponibilidade mensal dos serviços", "97,2%", "99,97%", "+2,77 p.p."],
  ["Tempo médio de resolução de chamados", "7 h 00", "4 h 12", "−40,0%"],
  ["Tempo de resposta do painel gerencial", "2.840 ms", "41 ms", "−98,6%"],
  ["Chamados tratados por técnico ao mês", "46", "71", "+54,3%"],
  ["Implantações em produção por mês", "2", "42", "+1.900%"],
  ["Tempo de restauração após falha", "6 h 00", "11 min", "−96,9%"],
  ["Custo mensal de operação", "R$ 14.650,00", "R$ 9.310,00", "−36,4%"]],
 "Fonte: Elaborada pelos autores (2026)."),

("p", "O resultado de maior relevância é a elevação da aderência ao nível de serviço de "
 "85,5% para 96,8%, ganho que decorre da articulação entre as disciplinas: o cálculo "
 "automático do prazo em C# eliminou a interpretação manual do contrato; o índice coberto "
 "reduziu a consulta do painel a 41 milissegundos; o alerta de observabilidade antecipa a "
 "notificação da supervisão; e a gestão ágil garantiu entrega incremental."),

# --------------------------------------------------------------- 8
("h1", "8 CONCLUSÃO"),

("p", "Este trabalho teve como objetivo geral projetar uma solução tecnológica "
 "corporativa integrada para a empresa fictícia Alunos Tech, contemplando arquitetura de "
 "software, infraestrutura em nuvem, banco de dados, metodologias ágeis e aplicações "
 "corporativas. O objetivo foi alcançado por meio da concepção e da demonstração da "
 "plataforma AT-Integra, que unificou o atendimento a clientes, o controle contratual de "
 "níveis de serviço e a gestão operacional da organização em ambientes web, desktop e "
 "móvel."),

("p", "Os objetivos específicos propostos na introdução foram igualmente atendidos. "
 "Desenvolveram-se aplicações web e móvel integradas, que compartilham o mesmo núcleo de "
 "regras de negócio e se comunicam por interface de programação versionada, com operação "
 "do aplicativo mesmo sem conectividade. Estruturou-se um banco de dados seguro e "
 "otimizado, dotado de procedimentos transacionais, funções, gatilhos de auditoria, "
 "índices cobertos, segurança em nível de linha e controle de concorrência, cujo efeito "
 "mais expressivo foi a redução de 98,6% no tempo de resposta da consulta mais utilizada. "
 "Aplicaram-se práticas de computação em nuvem e DevOps, com containerização, orquestração "
 "elástica, esteira automatizada com verificação de segurança e observabilidade baseada em "
 "objetivos de serviço. Utilizaram-se metodologias ágeis na gestão do projeto, por meio de "
 "um arranjo entre Scrum e Kanban que conduziu seis sprints e três entregas incrementais. "
 "Implementaram-se soluções escaláveis e seguras, verificadas pela ampliação automática de "
 "três para sete instâncias sob carga. E propôs-se uma arquitetura alinhada ao negócio, "
 "cuja aderência se evidencia na redução de 36,4% no custo mensal de operação."),

("p", "A principal contribuição reside menos em cada componente isolado e mais na "
 "demonstração de sua interdependência. Cumprir uma obrigação contratual aparentemente "
 "simples — resolver um incidente crítico em duas horas — exige simultaneamente regra de "
 "negócio bem modelada, consulta eficiente, infraestrutura elástica, alerta antecipado e "
 "um processo de gestão que priorize corretamente. A ausência de qualquer um desses "
 "elementos comprometeria o conjunto, o que confirma o caráter integrador do Projeto "
 "Integrado Multidisciplinar."),

("p", "A relação entre automação da entrega e estabilidade confirma, em escala "
 "reduzida, a correlação descrita por Forsgren, Humble e Kim (2018): o aumento da "
 "frequência de implantação veio acompanhado da redução da taxa de falha em mudanças. A "
 "explicação está no tamanho do lote, pois publicações menores e frequentes são mais "
 "simples de validar e de reverter. O achado contrariou a percepção da equipe de "
 "operações, que associava estabilidade à baixa frequência de mudanças."),

("p", "Na persistência, confirma-se a observação de Silberschatz, Korth e Sudarshan "
 "(2020) de que o custo de uma consulta decorre do volume de páginas acessadas: a queda "
 "das leituras lógicas de 18.420 para 612 páginas mostra que o ganho foi estrutural, e "
 "não circunstancial. Já a distribuição entre instâncias independentes, discutida por "
 "Tanenbaum e Van Steen (2007), impôs o desafio do controle de concorrência entre "
 "processos, resolvido pela combinação de estratégias otimista e pessimista."),

("p", "Entre as dificuldades enfrentadas, destacam-se a definição dos limites de trabalho "
 "em progresso, inicialmente estabelecidos em valores excessivamente permissivos, e a "
 "configuração manual dos ambientes, que gerou o impedimento registrado na Sprint 6 e "
 "motivou a adoção de infraestrutura como código. Ambas as situações reforçam que as "
 "práticas ágeis e de automação produzem resultado apenas quando efetivamente aplicadas, "
 "e não quando apenas declaradas."),

("p", "Cabe registrar as limitações do trabalho: a avaliação ocorreu em ambiente de "
 "demonstração, com carga sintética derivada do histórico, e não em produção; os "
 "indicadores financeiros apoiam-se em preços de 2026, sujeitos a variação cambial; e o "
 "período de observação não permite avaliar ciclos sazonais completos. Tais limitações "
 "não invalidam os resultados, mas delimitam seu alcance."),

("p", "Como desdobramentos futuros, recomendam-se um modelo preditivo de risco de "
 "violação de prazo treinado sobre o histórico da plataforma; a decomposição gradual do "
 "faturamento em serviços independentes, conforme o volume justifique a complexidade "
 "operacional (NEWMAN, 2022); um portal de autoatendimento para clientes finais; e um "
 "estudo de desempenho em produção por período superior a doze meses."),
]


# =====================================================================
REFERENCIAS = [
 "ANDERSON, David J. **Kanban**: mudança evolucionária bem-sucedida para seu negócio de "
 "tecnologia. Sequim: Blue Hole Press, 2011.",

 "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023**: informação e documentação: "
 "referências: elaboração. Rio de Janeiro: ABNT, 2018.",

 "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6024**: informação e documentação: "
 "numeração progressiva das seções de um documento: apresentação. Rio de Janeiro: "
 "ABNT, 2012.",

 "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6028**: informação e documentação: "
 "resumo, resenha e recensão: apresentação. Rio de Janeiro: ABNT, 2021.",

 "ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: informação e documentação: "
 "trabalhos acadêmicos: apresentação. Rio de Janeiro: ABNT, 2011.",

 "BECK, Kent et al. **Manifesto para o desenvolvimento ágil de software**. 2001. "
 "Disponível em: https://agilemanifesto.org/iso/ptbr/manifesto.html. "
 "Acesso em: 8 nov. 2026.",

 "BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Dispõe sobre a proteção de dados "
 "pessoais. Brasília, DF: Presidência da República, 2018. Disponível em: "
 "https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. "
 "Acesso em: 5 nov. 2026.",

 "BURNS, Brendan; BEDA, Joe; HIGHTOWER, Kelsey; EVENSON, Lachlan. **Kubernetes**: up and "
 "running. 3. ed. Sebastopol: O'Reilly Media, 2022.",

 "ELMASRI, Ramez; NAVATHE, Shamkant B. **Sistemas de banco de dados**. 7. ed. São Paulo: "
 "Pearson, 2019.",

 "FORSGREN, Nicole; HUMBLE, Jez; KIM, Gene. **Accelerate**: the science of lean software "
 "and DevOps. Portland: IT Revolution Press, 2018.",

 "FOWLER, Martin. **Padrões de arquitetura de aplicações corporativas**. Porto Alegre: "
 "Bookman, 2006.",

 "GAMMA, Erich; HELM, Richard; JOHNSON, Ralph; VLISSIDES, John. **Padrões de projeto**: "
 "soluções reutilizáveis de software orientado a objetos. Porto Alegre: Bookman, 2000.",

 "GIL, Antônio Carlos. **Como elaborar projetos de pesquisa**. 6. ed. São Paulo: "
 "Atlas, 2017.",

 "HUMBLE, Jez; FARLEY, David. **Entrega contínua**: como entregar software de forma "
 "rápida e confiável. Porto Alegre: Bookman, 2014.",

 "KIM, Gene; HUMBLE, Jez; DEBOIS, Patrick; WILLIS, John. **Manual de DevOps**: como obter "
 "agilidade, confiabilidade e segurança em organizações tecnológicas. Rio de Janeiro: "
 "Alta Books, 2018.",

 "LAKATOS, Eva Maria; MARCONI, Marina de Andrade. **Fundamentos de metodologia "
 "científica**. 8. ed. São Paulo: Atlas, 2017.",

 "MARTIN, Robert C. **Arquitetura limpa**: o guia do artesão para estrutura e design de "
 "software. Rio de Janeiro: Alta Books, 2019.",

 "MELL, Peter; GRANCE, Timothy. **The NIST definition of cloud computing**. Gaithersburg: "
 "National Institute of Standards and Technology, 2011. (NIST Special Publication 800-145).",

 "MICROSOFT. **Documentação do .NET**. 2026. Disponível em: "
 "https://learn.microsoft.com/pt-br/dotnet/. Acesso em: 10 nov. 2026.",

 "NEWMAN, Sam. **Criando microsserviços**: projetando sistemas com componentes menores e "
 "mais especializados. 2. ed. São Paulo: Novatec, 2022.",

 "PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software**: uma abordagem "
 "profissional. 8. ed. Porto Alegre: AMGH, 2016.",

 "PROJECT MANAGEMENT INSTITUTE. **Guia PMBOK**: um guia para o conjunto de conhecimentos "
 "em gerenciamento de projetos. 7. ed. Newtown Square: PMI, 2021.",

 "SCHWABER, Ken; SUTHERLAND, Jeff. **O guia do Scrum**: o guia definitivo para o Scrum: "
 "as regras do jogo. 2020. Disponível em: https://scrumguides.org/docs/scrumguide/v2020/"
 "2020-Scrum-Guide-Portuguese-Brazilian.pdf. Acesso em: 3 nov. 2026.",

 "SEVERINO, Antônio Joaquim. **Metodologia do trabalho científico**. 24. ed. São Paulo: "
 "Cortez, 2016.",

 "SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de banco de dados**. "
 "7. ed. Rio de Janeiro: LTC, 2020.",

 "SOMMERVILLE, Ian. **Engenharia de software**. 10. ed. São Paulo: Pearson, 2018.",

 "TANENBAUM, Andrew S.; VAN STEEN, Maarten. **Sistemas distribuídos**: princípios e "
 "paradigmas. 2. ed. São Paulo: Pearson, 2007.",

 "VERAS, Manoel. **Computação em nuvem**: nova arquitetura da TI. Rio de Janeiro: "
 "Brasport, 2015.",
]


# Apendices: (titulo, [(subtitulo, caminho relativo, linguagem)])
APENDICES = [
 ("APÊNDICE A – CÓDIGO-FONTE DOS MÓDULOS EM C#",
  [("A.1 Entidade de domínio Chamado",
    "codigo/src/AlunosTech.Domain/Entidades/Chamado.cs"),
   ("A.2 Estratégias de cálculo de nível de serviço",
    "codigo/src/AlunosTech.Domain/Servicos/CalculoSlaStrategy.cs"),
   ("A.3 Serviço de aplicação de chamados",
    "codigo/src/AlunosTech.Application/Servicos/ChamadoService.cs"),
   ("A.4 Repositório com Entity Framework Core e Dapper",
    "codigo/src/AlunosTech.Infrastructure/Repositorios/ChamadoRepositorio.cs"),
   ("A.5 Configuração da aplicação e injeção de dependência",
    "codigo/src/AlunosTech.API/Program.cs"),
   ("A.6 Modelo de visão do aplicativo móvel",
    "codigo/src/AlunosTech.Mobile/Views/ChamadoViewModel.cs"),
   ("A.7 Testes automatizados do domínio",
    "codigo/tests/AlunosTech.Tests/ChamadoServiceTests.cs")]),

 ("APÊNDICE B – SCRIPTS DO BANCO DE DADOS",
  [("B.1 Esquema físico das tabelas", "codigo/banco/01_schema.sql"),
   ("B.2 Procedimentos armazenados", "codigo/banco/02_procedures.sql"),
   ("B.3 Funções definidas pelo usuário", "codigo/banco/03_functions.sql"),
   ("B.4 Gatilhos", "codigo/banco/04_triggers.sql"),
   ("B.5 Segurança, concorrência e otimização",
    "codigo/banco/05_seguranca_concorrencia.sql")]),

 ("APÊNDICE C – ARTEFATOS DE INFRAESTRUTURA E AUTOMAÇÃO",
  [("C.1 Imagem de contêiner da aplicação", "codigo/devops/Dockerfile"),
   ("C.2 Manifestos de implantação e escalabilidade",
    "codigo/devops/k8s/deployment.yaml"),
   ("C.3 Esteira de integração e entrega contínuas",
    "codigo/devops/.github/workflows/ci-cd.yml")]),
]
