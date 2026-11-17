# -*- coding: utf-8 -*-
"""Localiza em qual pagina do PDF cada titulo, figura e tabela aparece,
para preencher o sumario e as listas com a numeracao correta."""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(RAIZ, "PIM VIII - Alunos Tech.pdf")
PDFTOTEXT = next(
    (c for c in (r"C:\Users\RM-USER2\AppData\Local\Programs\Git\ucrt64\bin\pdftotext.exe",
                 r"C:\Program Files\Git\ucrt64\bin\pdftotext.exe")
     if os.path.exists(c)), "pdftotext")


def normalizar(texto):
    texto = texto.replace("­", "").replace("–", "–")
    return re.sub(r"\s+", " ", texto).strip().upper()


def paginas_do_pdf():
    """Devolve a lista de textos normalizados, uma entrada por pagina."""
    bruto = subprocess.run(
        [PDFTOTEXT, "-layout", "-enc", "UTF-8", PDF, "-"],
        capture_output=True, text=True, encoding="utf-8", errors="ignore").stdout
    return [normalizar(p) for p in bruto.split("\f")]


def localizar(paginas, alvo, a_partir_de=0):
    """Primeira pagina fisica (1-based) que contem o texto alvo."""
    chave = normalizar(alvo)
    # ignora as linhas do sumario, que contem o condutor de pontos
    for indice in range(a_partir_de, len(paginas)):
        conteudo = paginas[indice]
        # as paginas do sumario e das listas usam condutor de pontos: ignoradas
        if re.search(r"\.{6,}", conteudo):
            continue
        if chave in conteudo:
            return indice + 1
    return None


def mapear():
    import gera_documento as G

    paginas = paginas_do_pdf()
    inicio_textual = localizar(paginas, "1 INTRODUÇÃO")
    sumario, ilustracoes, tabelas = G.coletar_indices()

    mapa_sumario, mapa_fig, mapa_tab = {}, {}, {}
    base = (inicio_textual or 1) - 1

    for texto, _ in sumario:
        fisica = localizar(paginas, texto, base)
        mapa_sumario[texto] = (fisica - 1) if fisica else "—"

    for texto in ilustracoes:
        fisica = localizar(paginas, texto, base)
        mapa_fig[texto] = (fisica - 1) if fisica else "—"

    for texto in tabelas:
        fisica = localizar(paginas, texto, base)
        mapa_tab[texto] = (fisica - 1) if fisica else "—"

    return mapa_sumario, mapa_fig, mapa_tab, inicio_textual, len(paginas)


if __name__ == "__main__":
    s, f, t, inicio, total = mapear()
    print("paginas fisicas no PDF:", total)
    print("introducao na pagina fisica:", inicio, "-> numero impresso:", inicio - 1)
    print()
    for k, v in s.items():
        print("%-70s %s" % (k[:68], v))
    print()
    for k, v in list(f.items())[:3]:
        print("%-70s %s" % (k[:68], v))
