# -*- coding: utf-8 -*-
"""Montagem final do PIM VIII.

Executa duas passagens: na primeira o documento e gerado com marcadores no
sumario e nas listas; o PDF resultante e analisado para descobrir em que pagina
cada titulo, figura e tabela foi parar; na segunda, o documento e regerado com
a numeracao correta. A numeracao impressa comeca na Introducao e e contada a
partir da folha de rosto, conforme a NBR 14724.
"""

import os
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(BASE)
sys.path.insert(0, BASE)

import gera_documento as G
import mede_paginas as M

DOCX = os.path.join(RAIZ, "PIM VIII - Alunos Tech.docx")
PDF = os.path.join(RAIZ, "PIM VIII - Alunos Tech.pdf")


def encerrar_word_orfao():
    """Encerra instancias invisiveis do Word deixadas por execucoes anteriores."""
    subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "Get-Process WINWORD -ErrorAction SilentlyContinue | "
         "Where-Object { [string]::IsNullOrEmpty($_.MainWindowTitle) } | "
         "Stop-Process -Force"],
        capture_output=True, text=True, timeout=120)


def converter(tentativas=2):
    for tentativa in range(1, tentativas + 1):
        encerrar_word_orfao()
        resultado = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
             "-File", os.path.join(BASE, "para_pdf.ps1"),
             "-Entrada", DOCX, "-Saida", PDF],
            capture_output=True, text=True, timeout=900)
        if os.path.exists(PDF):
            return resultado.stdout.strip()
        print("  conversao falhou (tentativa %d):" % tentativa,
              resultado.stdout.strip(), resultado.stderr.strip())
    sys.exit("falha ao converter para PDF")


def relatorio(sumario):
    ordem = [t for t, _ in G.coletar_indices()[0]]
    marcos = {t: sumario.get(t) for t in ordem}
    desenvolvimento_inicio = marcos.get("2 A EMPRESA ALUNOS TECH E A SITUAÇÃO-PROBLEMA")
    conclusao = marcos.get("8 CONCLUSÃO")
    if isinstance(desenvolvimento_inicio, int) and isinstance(conclusao, int):
        print("Desenvolvimento: paginas %d a %d (%d paginas)"
              % (desenvolvimento_inicio, conclusao - 1,
                 conclusao - desenvolvimento_inicio))


if __name__ == "__main__":
    print("passagem 1: gerando documento com marcadores...")
    G.construir(inicio_numeracao=8)
    print(converter())

    print("passagem 1: medindo paginas...")
    sumario, figuras, tabelas, inicio_fisica, total = M.mapear()
    inicio = inicio_fisica - 1          # a capa nao e contada
    print("  introducao na pagina impressa:", inicio)

    print("passagem 2: gerando documento definitivo...")
    G.construir(paginas_sumario=sumario, paginas_fig=figuras,
                paginas_tab=tabelas, inicio_numeracao=inicio)
    print(converter())

    print("conferencia final...")
    sumario2, _, _, inicio2, total2 = M.mapear()
    divergentes = [k for k in sumario if sumario[k] != sumario2[k]]
    if divergentes:
        print("  ATENCAO: a paginacao mudou nos itens:", divergentes)
        print("  regerando com os numeros conferidos...")
        G.construir(paginas_sumario=sumario2, paginas_fig=_, paginas_tab=_,
                    inicio_numeracao=inicio2 - 1)
        print(converter())
    else:
        print("  paginacao estavel; sumario conferido.")

    relatorio(sumario2)
    print("total de paginas:", total2)
    print("arquivos:", DOCX, "|", PDF, sep="\n  ")
