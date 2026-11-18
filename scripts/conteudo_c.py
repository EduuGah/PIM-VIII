# -*- coding: utf-8 -*-
"""Secoes 5 e 6: Programacao de Banco de Dados e Cloud Computing e DevOps."""

BLOCOS_C = [

# --------------------------------------------------------------- 5
("h1", "5 PROGRAMAÇÃO DE BANCO DE DADOS"),

("p", "O sistema gerenciador escolhido foi o Microsoft SQL Server 2022, pela integração "
 "nativa com a plataforma .NET, pelos recursos de segurança em nível de linha e pela "
 "disponibilidade de serviço gerenciado equivalente na nuvem adotada."),

("h2", "5.1 Modelo de dados"),

("p", "A modelagem partiu do levantamento das entidades do negócio e observou a terceira "
 "forma normal em todo o núcleo transacional, eliminando dependências transitivas e "
 "reduzindo a redundância, conforme orientam Elmasri e Navathe (2019). A Figura 7 "
 "apresenta o modelo entidade-relacionamento resultante."),

("fig", "fig_der.png",
 "Figura 7 – Modelo entidade-relacionamento do núcleo transacional",
 "Fonte: Elaborada pelos autores (2026).", 14.0),

("p", "Quatro decisões de modelagem merecem registro: a coluna de versão do tipo "
 "rowversion, destinada ao controle de concorrência otimista; a exclusão lógica pela "
 "coluna Ativo, exigida pela política de retenção e pela legislação de proteção de dados; "
 "a tabela de histórico alimentada exclusivamente por gatilho, de modo que nenhuma "
 "aplicação registre transições fora da trilha de auditoria; e a replicação, em restrições "
 "do tipo CHECK, das regras já implementadas em C#, garantindo integridade mesmo em "
 "acessos externos à aplicação."),

("h2", "5.2 Procedimentos armazenados e transações"),

("p", "As operações que envolvem mais de uma tabela foram encapsuladas em procedimentos "
 "armazenados, o que reduz o tráfego de rede, favorece o reaproveitamento do plano de "
 "execução e permite conceder permissões sem expor as tabelas. A Figura 8 reproduz o "
 "trecho central do procedimento de abertura de chamado."),

("fig", "fig_cod_procedure.png",
 "Figura 8 – Procedimento armazenado transacional de abertura de chamado",
 "Fonte: Elaborada pelos autores (2026).", 13.0),

("p", "O procedimento ilustra o tratamento transacional completo: XACT_ABORT assegura o "
 "desfazimento automático em erro grave e o bloco TRY/CATCH captura a exceção, registra a "
 "ocorrência em log e repassa o erro à aplicação. A leitura do contrato usa a dica "
 "UPDLOCK para impedir que uma renegociação concorrente altere o nível de serviço entre a "
 "consulta e o cálculo do prazo."),

("h2", "5.3 Funções definidas pelo usuário"),

("p", "Duas funções foram criadas. A escalar fn_CalcularPrazoSla converte nível "
 "contratual e prioridade em prazo limite, centralizando a regra para que procedimentos, "
 "relatórios e rotinas de conferência produzam sempre o mesmo resultado. A função "
 "fn_ProdutividadeTecnico foi escrita como tabela em linha, e não em múltiplas "
 "instruções, porque essa variante é expandida pelo otimizador no corpo da consulta que a "
 "invoca, aproveitando os índices das tabelas de origem; a versão equivalente em "
 "múltiplas instruções apresentou tempo de resposta 7,4 vezes superior."),

("h2", "5.4 Gatilhos e trilha de auditoria"),

("p", "Os gatilhos implementam regras que precisam valer independentemente da aplicação "
 "que acessa o banco. O gatilho responsável pela trilha de "
 "auditoria das transições de estado do chamado consta do Apêndice B."),

("p", "O gatilho foi escrito em lógica de conjunto, operando sobre as tabelas virtuais "
 "inserted e deleted sem o uso de cursores, de modo a preservar o desempenho em "
 "atualizações em lote. Um segundo gatilho converte exclusões físicas em exclusões "
 "lógicas e um terceiro, ambos apresentados no Apêndice B, impede a "
 "atribuição de chamados críticos a técnicos sem certificação de nível 2, transportando "
 "para o banco uma regra contratual que anteriormente dependia da atenção do supervisor."),

("h2", "5.5 Otimização de consultas"),

("p", "A otimização partiu da análise dos planos de execução das consultas mais "
 "frequentes, identificadas pelas visões de gerenciamento dinâmico. A principal "
 "intervenção foi a criação de índices cobertos, que trazem nas próprias páginas do "
 "índice todas as colunas exigidas pela consulta, eliminando buscas na tabela base. O "
 "Apêndice B traz o índice filtrado do painel e a visão indexada de nível de serviço."),

("p", "Adotaram-se ainda a projeção explícita dos campos necessários, a paginação por "
 "OFFSET-FETCH e o uso de RECOMPILE nos procedimentos cujo desempenho variava conforme o "
 "parâmetro recebido, problema conhecido como parameter sniffing. A Figura 9 compara os "
 "tempos de resposta e as leituras lógicas antes e depois das intervenções."),

("fig", "fig_desempenho.png",
 "Figura 9 – Tempo de resposta e leituras lógicas antes e depois da otimização",
 "Fonte: Elaborada pelos autores (2026).", 13.5),

("p", "A consulta do painel caiu de 2.840 para 41 milissegundos, redução de 98,6%, e o "
 "relatório de nível de serviço, de 6.420 para 214 milissegundos. As leituras lógicas, "
 "indicador mais estável por não sofrer influência da carga concorrente, recuaram de "
 "18.420 para 612 páginas, confirmando que o ganho decorre da mudança do plano de "
 "execução."),

("h2", "5.6 Segurança e controle de concorrência"),

("p", "A segurança foi tratada em quatro níveis: papéis de banco recebem permissão de "
 "execução sobre os procedimentos, sem acesso direto às tabelas, materializando o "
 "princípio do menor privilégio; a segurança em nível de linha restringe cada sessão aos "
 "registros do cliente correspondente; o mascaramento dinâmico oculta documentos de "
 "identificação para perfis operacionais; e as credenciais são cifradas. As medidas "
 "atendem aos princípios de necessidade e segurança da Lei Geral de Proteção de Dados "
 "Pessoais (BRASIL, 2018)."),

("p", "O controle de concorrência é misto. Na edição de chamados aplica-se o modelo "
 "otimista: a coluna de versão é comparada na atualização e, se outra sessão houver "
 "alterado o registro, a aplicação recebe exceção específica e solicita a recarga. Na "
 "distribuição automática da fila, em que duas instâncias poderiam atribuir o mesmo "
 "chamado, adotou-se controle pessimista por bloqueio de aplicação. Ambos constam do "
 "Apêndice B."),

# --------------------------------------------------------------- 6
("h1", "6 CLOUD COMPUTING E DEVOPS"),

("p", "O Instituto Nacional de Padrões e Tecnologia "
 "define a computação em nuvem como o acesso ubíquo e sob demanda a um conjunto "
 "compartilhado de recursos configuráveis, provisionados com esforço mínimo de "
 "gerenciamento (MELL; GRANCE, 2011); são a elasticidade e o autoatendimento que "
 "respondem às limitações do parque local. Veras (2015) acrescenta que a nuvem desloca a "
 "decisão de tecnologia do investimento em ativos para a gestão de serviços contratados, "
 "e Kim et al. (2018) definem a cultura DevOps como o encurtamento do fluxo entre "
 "desenvolvimento e operações, com ampliação dos ciclos de retorno de informação."),

("h2", "6.1 Arquitetura em nuvem e modelo de serviço"),

("p", "Adotou-se a nuvem pública da Microsoft Azure, em modelo híbrido entre plataforma "
 "como serviço e contêineres gerenciados, conforme ilustrado na Figura 1. A região "
 "primária é a Brazil South, com réplica geográfica na Brazil Southeast, escolha que "
 "atende tanto ao requisito de latência quanto ao de manutenção dos dados em território "
 "nacional. Os serviços foram distribuídos entre três zonas de disponibilidade, de modo "
 "que a falha de um data center não interrompa a operação."),

("p", "A decisão por contêineres orquestrados, em vez de máquinas virtuais, resultou da "
 "comparação entre três alternativas: manter o parque local exigiria investimento em "
 "redundância estimado em R$ 180.000,00; migrar para máquinas virtuais reduziria o "
 "investimento inicial, mas manteria o esforço de administração do sistema operacional; "
 "adotar contêineres transfere ao provedor a manutenção da plataforma e viabiliza "
 "escalabilidade automática com custo mensal previsível."),

("h2", "6.2 Containerização"),

("p", "Cada serviço da solução é empacotado em uma imagem de contêiner, o que garante "
 "que o mesmo artefato validado em homologação seja promovido a produção sem alteração. A "
 "Apêndice C reúne o arquivo de construção da imagem da interface de programação."),

("p", "A construção em múltiplos estágios separa o ambiente de compilação do de "
 "execução: apenas o resultado publicado é copiado para a imagem final, que usa uma "
 "distribuição enxuta. O tamanho da imagem caiu de 780 para 112 megabytes, o que acelera "
 "a transferência e reduz a superfície de ataque. Incorporaram-se ainda a execução sob "
 "usuário sem privilégios administrativos e a verificação periódica de integridade, "
 "consumida pelas sondas do orquestrador."),

("h2", "6.3 Orquestração e escalabilidade"),

("p", "A orquestração emprega o serviço gerenciado de Kubernetes: os manifestos declaram "
 "o estado desejado de cada serviço e o orquestrador encarrega-se de mantê-lo, "
 "substituindo instâncias defeituosas sem intervenção humana (BURNS et al., 2022). A "
 "atualização é progressiva, com indisponibilidade máxima igual a zero."),

("p", "O dimensionamento automático horizontal foi configurado entre três e doze "
 "instâncias, com gatilhos de 65% de processador e 75% de memória e janela de "
 "estabilização de cinco minutos, que evita oscilação. Sob carga de 600 requisições por "
 "minuto, a solução ampliou de três para sete instâncias em 92 segundos, mantendo o "
 "percentil 95 abaixo de 300 milissegundos. Os manifestos constam do Apêndice C."),

("h2", "6.4 Esteira de integração e entrega contínuas"),

("p", "A integração contínua incorpora com frequência o trabalho dos desenvolvedores a "
 "um repositório comum, com verificação automatizada a cada envio, e a entrega contínua "
 "mantém o software sempre em condição de ser publicado (HUMBLE; FARLEY, 2014). A esteira "
 "reúne quatro estágios, representados na Figura 10."),

("fig", "fig_pipeline.png",
 "Figura 10 – Execução da esteira de integração e entrega contínuas",
 "Fonte: Elaborada pelos autores (2026).", 14.0),

("p", "O primeiro estágio compila e executa os testes, interrompendo a esteira se a "
 "cobertura ficar abaixo de 80%. O segundo faz análise estática e varredura de "
 "vulnerabilidades da imagem, com falha automática em severidade alta ou crítica. O "
 "terceiro publica em homologação. O quarto promove a versão a produção pela estratégia "
 "azul-verde: as novas instâncias sobem em paralelo, passam por teste de fumaça e só "
 "então recebem o tráfego, com retorno automático à versão anterior em caso de falha."),

("p", "Os indicadores de desempenho de entrega propostos por Forsgren, Humble e Kim "
 "(2018) evidenciam o efeito da automação. A frequência de implantação passou de duas "
 "para quarenta e duas por mês; o tempo entre a conclusão do código e sua disponibilização "
 "caiu de 21 dias para 1,8 dia; a taxa de falha em mudanças recuou de 27% para 4,2%; e o "
 "tempo médio de restauração do serviço passou de seis horas para onze minutos."),

("h2", "6.5 Segurança, conformidade e governança"),

("p", "A segurança seguiu o princípio da confiança zero, no qual nenhuma requisição é "
 "confiável por sua origem: o tráfego externo atravessa firewall de aplicação web; a "
 "autenticação é federada ao diretório corporativo, com segundo fator obrigatório; os "
 "segredos residem em cofre gerenciado, injetados em tempo de execução e nunca gravados "
 "em repositório; e o banco de dados é acessado por ponto de extremidade privado."),

("p", "Quanto à conformidade, a solução implementa os direitos previstos na legislação de "
 "proteção de dados: registro de consentimento, atendimento a pedidos de acesso e "
 "correção, anonimização dos dados de homologação e expurgo após sessenta meses, com "
 "trilha de auditoria que registra autor, data e conteúdo de cada alteração."),

("h2", "6.6 Monitoramento e observabilidade"),

("p", "A observabilidade apoia-se em três pilares: métricas, coletadas pelo Prometheus e "
 "apresentadas em painéis do Grafana; registros centralizados com retenção de 180 dias; e "
 "rastreamento distribuído, que correlaciona por identificador único todas as etapas "
 "percorridas por uma requisição. Os painéis consolidam disponibilidade, latência, taxa "
 "de erro e consumo de recursos em uma única visão operacional."),

("p", "Os alertas derivam de objetivos de nível de serviço, e não de limiares arbitrários "
 "de recursos. Além dos técnicos, há um alerta de negócio, que avisa a supervisão quando "
 "um chamado crítico se aproxima do prazo, e um alerta financeiro, acionado quando o "
 "custo projetado do mês supera o orçado."),

("h2", "6.7 Custos e viabilidade da operação"),

("p", "A Tabela 4 apresenta a composição do custo mensal estimado em regime permanente, "
 "dimensionado a partir da carga observada e projetado para doze meses."),

("tab", "Tabela 4 – Composição do custo mensal da infraestrutura em nuvem",
 ["Recurso", "Dimensionamento", "Custo mensal (R$)", "Participação (%)"],
 [["Cluster Kubernetes gerenciado", "3 nós D4s v5 + escala automática", "3.180,00", "34,2"],
  ["Banco de dados gerenciado", "Camada crítica, 4 vCore, réplica", "2.740,00", "29,4"],
  ["Licenças e ferramentas da esteira", "6 assentos e repositório privado", "1.420,00", "15,3"],
  ["Rede, firewall de aplicação e distribuição", "Perfil padrão com proteção", "890,00", "9,6"],
  ["Armazenamento, backup e observabilidade", "2 TB e 180 dias de registros",
   "1.080,00", "11,5"],
  ["Total mensal", "—", "9.310,00", "100,0"]],
 "Fonte: Elaborada pelos autores (2026)."),

("p", "Comparado ao custo mensal de R$ 14.650,00 do parque local, o novo arranjo "
 "representa economia de 36,4%, eleva a disponibilidade contratada e converte "
 "investimento em despesa operacional."),
]
