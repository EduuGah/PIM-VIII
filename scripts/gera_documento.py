# -*- coding: utf-8 -*-
"""Monta o documento do PIM VIII em formato .docx seguindo as normas da ABNT.

Formatacao aplicada:
  - papel A4; margens superior e esquerda 3 cm, inferior e direita 2 cm;
  - fonte Arial 12, entrelinhas 1,5, alinhamento justificado;
  - recuo de primeira linha de 1,5 cm;
  - citacoes longas com recuo de 4 cm, fonte 10 e espacamento simples;
  - paginacao contada a partir da folha de rosto e exibida a partir da
    Introducao, no canto superior direito;
  - secoes primarias iniciando em nova pagina.
"""

import os
import sys

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import conteudo as C
from conteudo_b import BLOCOS_B
from conteudo_c import BLOCOS_C
from conteudo_d import BLOCOS_D, REFERENCIAS, APENDICES

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURAS = os.path.join(RAIZ, "figuras")
SAIDA = os.path.join(RAIZ, "PIM VIII - Alunos Tech.docx")

BLOCOS = C.BLOCOS + BLOCOS_B + BLOCOS_C + BLOCOS_D

FONTE = "Arial"
LARGURA_UTIL = Cm(16)


# =====================================================================
# Utilitarios de formatacao
# =====================================================================
def aplicar_fonte(run, tamanho=12, negrito=False, italico=False, fonte=FONTE):
    run.font.name = fonte
    run.font.size = Pt(tamanho)
    run.bold = negrito
    run.italic = italico
    run.font.color.rgb = RGBColor(0, 0, 0)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for atributo in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(atributo), fonte)


def paragrafo(doc, texto="", alinhamento=WD_ALIGN_PARAGRAPH.JUSTIFY, tamanho=12,
              negrito=False, italico=False, recuo_primeira=None, entrelinhas=1.5,
              espaco_antes=0, espaco_depois=0, recuo_esquerda=None, fonte=FONTE):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    p.alignment = alinhamento
    pf.line_spacing = entrelinhas
    pf.space_before = Pt(espaco_antes)
    pf.space_after = Pt(espaco_depois)
    if recuo_primeira is not None:
        pf.first_line_indent = recuo_primeira
    if recuo_esquerda is not None:
        pf.left_indent = recuo_esquerda
    if texto:
        escrever_formatado(p, texto, tamanho, negrito, italico, fonte)
    return p


def escrever_formatado(p, texto, tamanho=12, negrito=False, italico=False, fonte=FONTE):
    """Interpreta **negrito** dentro do texto."""
    for i, parte in enumerate(texto.split("**")):
        if not parte:
            continue
        run = p.add_run(parte)
        aplicar_fonte(run, tamanho, negrito or (i % 2 == 1), italico, fonte)


def quebra_pagina(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.add_run().add_break(WD_BREAK.PAGE)


def bordas_tabela(tabela, estilo="abnt"):
    """estilo 'abnt': apenas linhas horizontais; 'quadro': grade completa."""
    tbl = tabela._tbl
    tbl_pr = tbl.tblPr
    antigas = tbl_pr.find(qn("w:tblBorders"))
    if antigas is not None:
        tbl_pr.remove(antigas)

    bordas = OxmlElement("w:tblBorders")
    if estilo == "abnt":
        visiveis = {"top": 8, "bottom": 8, "insideH": 6,
                    "left": 0, "right": 0, "insideV": 0}
    else:
        visiveis = {"top": 6, "bottom": 6, "insideH": 4,
                    "left": 6, "right": 6, "insideV": 4}

    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        elemento = OxmlElement("w:" + lado)
        largura = visiveis[lado]
        elemento.set(qn("w:val"), "single" if largura else "none")
        elemento.set(qn("w:sz"), str(largura if largura else 0))
        elemento.set(qn("w:space"), "0")
        elemento.set(qn("w:color"), "000000")
        bordas.append(elemento)
    tbl_pr.append(bordas)


def sombrear(celula, cor="E8ECF2"):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), cor)
    celula._tc.get_or_add_tcPr().append(shd)


def campo_pagina(paragrafo_destino):
    run = paragrafo_destino.add_run()
    aplicar_fonte(run, 10)
    inicio = OxmlElement("w:fldChar")
    inicio.set(qn("w:fldCharType"), "begin")
    instrucao = OxmlElement("w:instrText")
    instrucao.set(qn("xml:space"), "preserve")
    instrucao.text = "PAGE"
    fim = OxmlElement("w:fldChar")
    fim.set(qn("w:fldCharType"), "end")
    run._r.append(inicio)
    run._r.append(instrucao)
    run._r.append(fim)


def iniciar_numeracao(secao, inicio):
    sect_pr = secao._sectPr
    antigo = sect_pr.find(qn("w:pgNumType"))
    if antigo is not None:
        sect_pr.remove(antigo)
    pg = OxmlElement("w:pgNumType")
    pg.set(qn("w:start"), str(inicio))
    sect_pr.append(pg)


def configurar_pagina(secao):
    secao.page_width = Cm(21)
    secao.page_height = Cm(29.7)
    secao.top_margin = Cm(3)
    secao.left_margin = Cm(3)
    secao.bottom_margin = Cm(2)
    secao.right_margin = Cm(2)
    secao.header_distance = Cm(1.5)
    secao.footer_distance = Cm(1.2)


# =====================================================================
# Elementos do trabalho
# =====================================================================
def montar_capa(doc):
    paragrafo(doc, "UNIVERSIDADE PAULISTA – UNIP EaD", WD_ALIGN_PARAGRAPH.CENTER,
              12, True, entrelinhas=1.5)
    paragrafo(doc, "Projeto Integrado Multidisciplinar", WD_ALIGN_PARAGRAPH.CENTER, 12)
    paragrafo(doc, "Curso Superior de Tecnologia em " + C.CURSO,
              WD_ALIGN_PARAGRAPH.CENTER, 12)

    for _ in range(4):
        paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER)

    for nome, ra in C.AUTORES:
        paragrafo(doc, nome + " – RA: " + ra, WD_ALIGN_PARAGRAPH.CENTER, 12,
                  entrelinhas=1.5)

    for _ in range(3):
        paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER)

    paragrafo(doc, C.TITULO, WD_ALIGN_PARAGRAPH.CENTER, 14, True)
    paragrafo(doc, C.SUBTITULO, WD_ALIGN_PARAGRAPH.CENTER, 12)

    for _ in range(6):
        paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER)

    paragrafo(doc, C.CIDADE, WD_ALIGN_PARAGRAPH.CENTER, 12)
    paragrafo(doc, C.ANO, WD_ALIGN_PARAGRAPH.CENTER, 12)
    quebra_pagina(doc)


def montar_folha_rosto(doc):
    for nome, ra in C.AUTORES:
        paragrafo(doc, nome + " – RA: " + ra, WD_ALIGN_PARAGRAPH.CENTER, 12)

    for _ in range(4):
        paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER)

    paragrafo(doc, C.TITULO, WD_ALIGN_PARAGRAPH.CENTER, 14, True)
    paragrafo(doc, C.SUBTITULO, WD_ALIGN_PARAGRAPH.CENTER, 12)

    for _ in range(3):
        paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER)

    natureza = ("Projeto Integrado Multidisciplinar apresentado à Universidade Paulista – "
                "UNIP EaD como requisito parcial para a obtenção do título de tecnólogo em "
                + C.CURSO + ".")
    paragrafo(doc, natureza, WD_ALIGN_PARAGRAPH.JUSTIFY, 12, entrelinhas=1.0,
              recuo_esquerda=Cm(8), recuo_primeira=Cm(0))
    paragrafo(doc, "", recuo_esquerda=Cm(8))
    paragrafo(doc, "Orientador: " + C.ORIENTADOR, WD_ALIGN_PARAGRAPH.LEFT, 12,
              entrelinhas=1.0, recuo_esquerda=Cm(8), recuo_primeira=Cm(0))

    for _ in range(5):
        paragrafo(doc, "", WD_ALIGN_PARAGRAPH.CENTER)

    paragrafo(doc, C.CIDADE, WD_ALIGN_PARAGRAPH.CENTER, 12)
    paragrafo(doc, C.ANO, WD_ALIGN_PARAGRAPH.CENTER, 12)
    quebra_pagina(doc)


def titulo_pre_textual(doc, texto):
    paragrafo(doc, texto, WD_ALIGN_PARAGRAPH.CENTER, 12, True,
              recuo_primeira=Cm(0), espaco_depois=12)


def montar_resumo(doc):
    titulo_pre_textual(doc, "RESUMO")
    paragrafo(doc, C.RESUMO, recuo_primeira=Cm(0), entrelinhas=1.0)
    paragrafo(doc, "", recuo_primeira=Cm(0))
    p = paragrafo(doc, "", WD_ALIGN_PARAGRAPH.JUSTIFY, recuo_primeira=Cm(0),
                  entrelinhas=1.0)
    escrever_formatado(p, "**Palavras-chave:** " + C.PALAVRAS_CHAVE)
    quebra_pagina(doc)

    titulo_pre_textual(doc, "ABSTRACT")
    paragrafo(doc, C.ABSTRACT, recuo_primeira=Cm(0), entrelinhas=1.0)
    paragrafo(doc, "", recuo_primeira=Cm(0))
    p = paragrafo(doc, "", WD_ALIGN_PARAGRAPH.JUSTIFY, recuo_primeira=Cm(0),
                  entrelinhas=1.0)
    escrever_formatado(p, "**Keywords:** " + C.KEYWORDS)
    quebra_pagina(doc)


def linha_sumario(doc, texto, pagina, nivel=1):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = 1.5
    pf.space_after = Pt(0)
    pf.first_line_indent = Cm(0)
    pf.left_indent = Cm(0.8) if nivel == 2 else Cm(0)
    pf.tab_stops.add_tab_stop(LARGURA_UTIL, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    run = p.add_run(texto + "\t" + str(pagina))
    aplicar_fonte(run, 12, negrito=(nivel == 1))
    return p


def montar_sumario(doc, entradas):
    titulo_pre_textual(doc, "SUMÁRIO")
    for texto, nivel, pagina in entradas:
        linha_sumario(doc, texto, pagina, nivel)
    quebra_pagina(doc)


def montar_listas(doc, ilustracoes, tabelas):
    titulo_pre_textual(doc, "LISTA DE ILUSTRAÇÕES")
    for texto, pagina in ilustracoes:
        linha_sumario(doc, texto, pagina, nivel=2)
    quebra_pagina(doc)

    titulo_pre_textual(doc, "LISTA DE TABELAS E QUADROS")
    for texto, pagina in tabelas:
        linha_sumario(doc, texto, pagina, nivel=2)
    quebra_pagina(doc)


# =====================================================================
# Blocos do desenvolvimento
# =====================================================================
def inserir_figura(doc, arquivo, legenda, fonte_texto, largura_cm):
    # a legenda, a ilustracao e a fonte permanecem sempre na mesma pagina
    cab = paragrafo(doc, legenda, WD_ALIGN_PARAGRAPH.CENTER, 10, recuo_primeira=Cm(0),
                    entrelinhas=1.0, espaco_antes=4, espaco_depois=2)
    cab.paragraph_format.keep_with_next = True

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(os.path.join(FIGURAS, arquivo), width=Cm(largura_cm))

    paragrafo(doc, fonte_texto, WD_ALIGN_PARAGRAPH.CENTER, 10, recuo_primeira=Cm(0),
              entrelinhas=1.0, espaco_depois=8)


def larguras_colunas(cabecalhos, linhas, total=16.0, minimo=1.4):
    """Distribui a largura das colunas conforme o volume de texto de cada uma.

    O minimo de cada coluna considera a maior palavra que ela contem, de modo
    que nenhuma palavra seja partida ao meio pela quebra de linha.
    """
    # a 9 pt, cada caractere ocupa cerca de 0,19 cm; 0,45 cm cobre as margens
    LARGURA_CARACTERE, MARGEM_CELULA = 0.19, 0.45

    pesos, minimos = [], []
    for i in range(len(cabecalhos)):
        textos = [cabecalhos[i]] + [linha[i] for linha in linhas]
        pesos.append(max(max(len(t) for t in textos), 6))
        maior_palavra = max((len(palavra) for t in textos for palavra in t.split()),
                            default=4)
        minimos.append(min(5.0, max(minimo,
                                    maior_palavra * LARGURA_CARACTERE + MARGEM_CELULA)))

    # se os minimos nao couberem, reduz todos proporcionalmente
    if sum(minimos) > total * 0.95:
        fator = total * 0.95 / sum(minimos)
        minimos = [m * fator for m in minimos]

    soma = float(sum(pesos))
    larguras = [total * peso / soma for peso in pesos]

    # eleva as colunas estreitas ao seu minimo, descontando das mais folgadas
    for _ in range(6):
        deficit = sum(max(0.0, minimos[i] - w) for i, w in enumerate(larguras))
        if deficit < 0.01:
            break
        folgadas = [i for i, w in enumerate(larguras) if w > minimos[i]]
        if not folgadas:
            break
        disponivel = sum(larguras[i] for i in folgadas)
        larguras = [minimos[i] if w < minimos[i]
                    else w - deficit * w / disponivel
                    for i, w in enumerate(larguras)]

    fator = total / sum(larguras)
    return [w * fator for w in larguras]


def fixar_largura_tabela(tabela, larguras):
    """Aplica layout fixo: sem o ajuste automatico, o Word respeita as larguras."""
    tbl_pr = tabela._tbl.tblPr

    for marca in ("w:tblLayout", "w:tblW"):
        antigo = tbl_pr.find(qn(marca))
        if antigo is not None:
            tbl_pr.remove(antigo)

    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tbl_pr.append(layout)

    largura_total = OxmlElement("w:tblW")
    largura_total.set(qn("w:w"), str(int(sum(larguras) * 567)))
    largura_total.set(qn("w:type"), "dxa")
    tbl_pr.append(largura_total)

    tabela.autofit = False
    for linha in tabela.rows:
        for celula, largura in zip(linha.cells, larguras):
            celula.width = Cm(largura)


def manter_linha_inteira(linha, com_a_proxima):
    """Impede que a linha se parta ao meio e, opcionalmente, que se separe
    do que vem depois — e o que mantem a tabela inteira na mesma pagina."""
    tr_pr = linha._tr.get_or_add_trPr()
    tr_pr.append(OxmlElement("w:cantSplit"))
    if com_a_proxima:
        for celula in linha.cells:
            for p in celula.paragraphs:
                p.paragraph_format.keep_with_next = True


def repetir_cabecalho(linha):
    tr_pr = linha._tr.get_or_add_trPr()
    tr_pr.append(OxmlElement("w:tblHeader"))


def inserir_tabela(doc, titulo, cabecalhos, linhas, fonte_texto, estilo="abnt"):
    cab = paragrafo(doc, titulo, WD_ALIGN_PARAGRAPH.CENTER, 10, recuo_primeira=Cm(0),
                    entrelinhas=1.0, espaco_antes=4, espaco_depois=2)
    cab.paragraph_format.keep_with_next = True

    larguras = larguras_colunas(cabecalhos, linhas)
    # colunas com texto corrido ficam alinhadas a esquerda; as curtas, centradas
    extensao = [max([len(cabecalhos[i])] + [len(l[i]) for l in linhas])
                for i in range(len(cabecalhos))]
    alinhamentos = [WD_ALIGN_PARAGRAPH.LEFT if (i == 0 or extensao[i] > 24)
                    else WD_ALIGN_PARAGRAPH.CENTER
                    for i in range(len(cabecalhos))]

    tabela = doc.add_table(rows=1, cols=len(cabecalhos))
    tabela.alignment = WD_TABLE_ALIGNMENT.CENTER

    for i, texto in enumerate(cabecalhos):
        celula = tabela.rows[0].cells[i]
        celula.text = ""
        p = celula.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.line_spacing = 1.0
        aplicar_fonte(p.add_run(texto), 9, negrito=True)
        sombrear(celula)

    for linha in linhas:
        celulas = tabela.add_row().cells
        for i, valor in enumerate(linha):
            p = celulas[i].paragraphs[0]
            p.alignment = alinhamentos[i]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.line_spacing = 1.0
            negrito = valor.lower().startswith("total")
            aplicar_fonte(p.add_run(valor), 9, negrito=negrito)

    fixar_largura_tabela(tabela, larguras)
    bordas_tabela(tabela, estilo)
    repetir_cabecalho(tabela.rows[0])
    for linha in tabela.rows:
        manter_linha_inteira(linha, com_a_proxima=True)

    paragrafo(doc, fonte_texto, WD_ALIGN_PARAGRAPH.LEFT, 10, recuo_primeira=Cm(0),
              entrelinhas=1.0, espaco_antes=2, espaco_depois=8)


def inserir_codigo(doc, caminho_rel):
    caminho = os.path.join(RAIZ, caminho_rel.replace("/", os.sep))
    with open(caminho, encoding="utf-8") as arq:
        linhas = arq.read().splitlines()

    for linha in linhas:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = 1.0
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.first_line_indent = Cm(0)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(linha if linha.strip() else "")
        aplicar_fonte(run, 8, fonte="Consolas")


# Elementos obrigatorios da estrutura que iniciam em nova pagina: a
# Introducao, o inicio do Desenvolvimento e a Conclusao. As demais secoes
# primarias do Desenvolvimento seguem na mesma pagina, de modo a respeitar
# o limite de 20 paginas estabelecido pelo manual do PIM.
SECOES_EM_NOVA_PAGINA = ("1 ", "2 ", "8 ")


def montar_desenvolvimento(doc):
    primeiro = True
    for bloco in BLOCOS:
        tipo = bloco[0]

        if tipo == "h1":
            nova_pagina = not primeiro and bloco[1].startswith(SECOES_EM_NOVA_PAGINA)
            primeiro = False
            titulo = paragrafo(doc, bloco[1], WD_ALIGN_PARAGRAPH.LEFT, 12, True,
                               recuo_primeira=Cm(0), espaco_antes=(0 if nova_pagina else 10),
                               espaco_depois=8)
            titulo.paragraph_format.keep_with_next = True
            # a quebra vai no proprio titulo: um paragrafo de quebra avulso
            # pode sobrar no fim da pagina anterior e gerar uma folha em branco
            titulo.paragraph_format.page_break_before = nova_pagina

        elif tipo == "h2":
            titulo = paragrafo(doc, bloco[1], WD_ALIGN_PARAGRAPH.LEFT, 12, True,
                               recuo_primeira=Cm(0), espaco_antes=8, espaco_depois=4)
            titulo.paragraph_format.keep_with_next = True

        elif tipo == "p":
            paragrafo(doc, bloco[1], recuo_primeira=Cm(1.5))

        elif tipo == "cit":
            paragrafo(doc, bloco[1], WD_ALIGN_PARAGRAPH.JUSTIFY, 10,
                      recuo_primeira=Cm(0), recuo_esquerda=Cm(4), entrelinhas=1.0,
                      espaco_antes=8, espaco_depois=8)

        elif tipo == "fig":
            inserir_figura(doc, bloco[1], bloco[2], bloco[3], bloco[4])

        elif tipo == "tab":
            inserir_tabela(doc, bloco[1], bloco[2], bloco[3], bloco[4], "abnt")

        elif tipo == "quadro":
            inserir_tabela(doc, bloco[1], bloco[2], bloco[3], bloco[4], "quadro")


def montar_referencias(doc):
    titulo = paragrafo(doc, "REFERÊNCIAS", WD_ALIGN_PARAGRAPH.CENTER, 12, True,
                       recuo_primeira=Cm(0), espaco_depois=12)
    titulo.paragraph_format.page_break_before = True
    titulo.paragraph_format.keep_with_next = True
    for referencia in sorted(REFERENCIAS):
        p = paragrafo(doc, "", WD_ALIGN_PARAGRAPH.LEFT, recuo_primeira=Cm(0),
                      entrelinhas=1.0, espaco_depois=12)
        escrever_formatado(p, referencia)


def montar_apendices(doc):
    for titulo, arquivos in APENDICES:
        cabecalho = paragrafo(doc, titulo, WD_ALIGN_PARAGRAPH.CENTER, 12, True,
                              recuo_primeira=Cm(0), espaco_depois=12)
        cabecalho.paragraph_format.page_break_before = True
        cabecalho.paragraph_format.keep_with_next = True
        for subtitulo, caminho in arquivos:
            paragrafo(doc, subtitulo, WD_ALIGN_PARAGRAPH.LEFT, 11, True,
                      recuo_primeira=Cm(0), espaco_antes=10, espaco_depois=6,
                      entrelinhas=1.0)
            inserir_codigo(doc, caminho)


# =====================================================================
# Indices do sumario e das listas
# =====================================================================
def coletar_indices():
    sumario, ilustracoes, tabelas = [], [], []
    for bloco in BLOCOS:
        if bloco[0] == "h1":
            sumario.append((bloco[1], 1))
        elif bloco[0] == "h2":
            sumario.append((bloco[1], 2))
        elif bloco[0] == "fig":
            ilustracoes.append(bloco[2])
        elif bloco[0] in ("tab", "quadro"):
            tabelas.append(bloco[1])
    sumario.append(("REFERÊNCIAS", 1))
    for titulo, _ in APENDICES:
        sumario.append((titulo, 1))
    return sumario, ilustracoes, tabelas


def construir(paginas_sumario=None, paginas_fig=None, paginas_tab=None,
              inicio_numeracao=7):
    sumario, ilustracoes, tabelas = coletar_indices()

    doc = Document()
    estilo = doc.styles["Normal"]
    estilo.font.name = FONTE
    estilo.font.size = Pt(12)
    estilo.paragraph_format.line_spacing = 1.5
    estilo.paragraph_format.space_after = Pt(0)

    configurar_pagina(doc.sections[0])

    montar_capa(doc)
    montar_folha_rosto(doc)
    montar_resumo(doc)

    entradas = [(t, n, (paginas_sumario or {}).get(t, "—")) for t, n in sumario]
    montar_sumario(doc, entradas)
    montar_listas(
        doc,
        [(t, (paginas_fig or {}).get(t, "—")) for t in ilustracoes],
        [(t, (paginas_tab or {}).get(t, "—")) for t in tabelas],
    )

    # ---- nova secao: parte textual, com numeracao visivel ----
    secao = doc.add_section(WD_SECTION.NEW_PAGE)
    configurar_pagina(secao)
    secao.different_first_page_header_footer = False
    secao.header.is_linked_to_previous = False
    iniciar_numeracao(secao, inicio_numeracao)

    cabecalho = secao.header.paragraphs[0]
    cabecalho.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    cabecalho.paragraph_format.space_after = Pt(0)
    campo_pagina(cabecalho)

    montar_desenvolvimento(doc)
    montar_referencias(doc)
    montar_apendices(doc)

    doc.save(SAIDA)
    return SAIDA


if __name__ == "__main__":
    caminho = construir()
    print("documento gerado:", caminho)
