# -*- coding: utf-8 -*-
"""Define a largura de impressao de cada figura, equilibrando legibilidade e
o limite de 20 paginas do Desenvolvimento."""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

LARGURAS = {
    "fig_arq_cloud.png": 13.0,
    "fig_kanban.png": 12.5,
    "fig_burndown.png": 11.5,
    "fig_cod_entidade.png": 12.5,
    "fig_web_painel.png": 12.5,
    "fig_mobile.png": 9.5,
    "fig_der.png": 12.5,
    "fig_cod_procedure.png": 12.5,
    "fig_desempenho.png": 12.5,
    "fig_pipeline.png": 11.5,
}

PADRAO = re.compile(
    r'\("fig", "([a-z_0-9.]+)",\s*\n\s*("[^"]+"),\s*\n\s*("[^"]+"), (\d+(?:\.\d+)?)\)')


def ajustar(arquivo):
    caminho = os.path.join(BASE, arquivo)
    s = open(caminho, encoding="utf-8").read()
    alterados = []

    def troca(m):
        nome = m.group(1)
        nova = LARGURAS.get(nome)
        if nova is None:
            return m.group(0)
        alterados.append("%s -> %.1f cm" % (nome, nova))
        return '("fig", "%s",\n %s,\n %s, %.1f)' % (nome, m.group(2), m.group(3), nova)

    novo = PADRAO.sub(troca, s)
    open(caminho, "w", encoding="utf-8").write(novo)
    print(arquivo + ":")
    for a in alterados:
        print("   ", a)


if __name__ == "__main__":
    for arquivo in ("conteudo.py", "conteudo_b.py", "conteudo_c.py"):
        ajustar(arquivo)
