# PIM VIII – Alunos Tech

Trabalho montado a partir do **Manual do PIM VIII** e do cruzamento dos pareceres
dos tutores nos PIMs I a VI.

## Entregáveis

| Arquivo | O que é |
|---|---|
| `PIM VIII - Alunos Tech.docx` | Documento editável (é este que você revisa e ajusta) |
| `PIM VIII - Alunos Tech.pdf` | Mesmo documento em PDF, para conferência e postagem |
| `figuras/` | As 10 figuras do trabalho, em PNG de alta resolução |
| `front/` | Páginas HTML que geraram os prints (telas, diagramas, editor de código) |
| `codigo/` | Código-fonte real do protótipo (C#, SQL, Docker, Kubernetes, CI/CD) |
| `scripts/` | Geradores do documento, das figuras e da paginação |
| `revisao/` | Páginas do PDF renderizadas em imagem, para conferência rápida |

## Como o trabalho está estruturado

Capa · Folha de rosto · Resumo · Abstract · Sumário · Lista de ilustrações ·
Lista de tabelas e quadros · 1 Introdução · **2 a 7 Desenvolvimento (20 páginas)** ·
8 Conclusão · Referências · Apêndices A, B e C.

As quatro disciplinas exigidas pelo manual ocupam uma seção cada:

- **3 Gerenciamento de Projetos Ágil** — Scrumban, backlog, 6 sprints, quadro Kanban,
  burndown, métricas de fluxo, retrospectivas, riscos e orçamento de R$ 289.575,00.
- **4 Programação Aplicada em .NET** — arquitetura em camadas, orientação a objetos,
  padrões Strategy, Factory, Repository, Unit of Work, DI e MVVM, aplicação web,
  módulo desktop, app .NET MAUI, testes e desempenho.
- **5 Programação de Banco de Dados** — modelo entidade-relacionamento, stored
  procedures transacionais, funções, gatilhos, índices cobertos, visão indexada,
  segurança em nível de linha e controle de concorrência.
- **6 Cloud Computing e DevOps** — arquitetura Azure, Docker, Kubernetes com
  escalabilidade automática, esteira CI/CD, DevSecOps, LGPD, observabilidade e custos.

## Conferência contra o manual e contra os pareceres anteriores

- [x] ABNT: A4, margens 3/3/2/2 cm, Arial 12, entrelinhas 1,5, texto justificado,
      recuo de primeira linha de 1,5 cm
- [x] Paginação contada a partir da folha de rosto e exibida a partir da Introdução,
      no canto superior direito
- [x] Resumo de 150 a 500 palavras com palavras-chave; Abstract com keywords (NBR 6028)
- [x] Sumário e listas com a numeração real das páginas
- [x] Títulos de seção numerados conforme a NBR 6024 (sem ponto após o indicativo)
- [x] Desenvolvimento com 20 páginas — dentro do intervalo de 15 a 20 do manual
- [x] Elementos obrigatórios iniciando em página própria
- [x] Citação longa com recuo de 4 cm, fonte 10 e espaçamento simples
- [x] 27 referências pela NBR 6023, todas citadas no texto — nenhuma da Wikipédia
- [x] Artefatos práticos que o tutor cobrou: orçamento, inventário de equipamentos,
      requisitos funcionais e não funcionais, backlog, planejamento de sprints,
      diagramas e planilhas de custo
- [x] Código extenso nos Apêndices A, B e C, como o tutor autorizou

## Antes de postar

1. **Revise e adapte o texto.** O trabalho precisa ser autoral e a UNIP roda detector
   de similaridade. Reescreva trechos com as palavras de vocês.
2. **Confirme o nome do orientador** na folha de rosto (está como Prof. Paulo Lourenção,
   que assinou os pareceres do PIM V e do PIM VI).
3. **Confira os RAs** da capa e da folha de rosto.
4. Se precisar regerar o documento depois de editar o conteúdo em `scripts/conteudo*.py`,
   rode `python scripts/build.py` — ele reconstrói o .docx, converte para PDF e recalcula
   o sumário e as listas.
