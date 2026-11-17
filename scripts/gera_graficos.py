# -*- coding: utf-8 -*-
"""Gera os graficos estatisticos do PIM VIII (figuras em PNG)."""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "figuras")
os.makedirs(SAIDA, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": "#c9d2de",
    "axes.labelcolor": "#2d3845",
    "text.color": "#2d3845",
    "xtick.color": "#5a6676",
    "ytick.color": "#5a6676",
    "axes.grid": True,
    "grid.color": "#e6ebf2",
    "grid.linewidth": .9,
    "figure.facecolor": "white",
})

AZUL, VERDE, LARANJA, VERMELHO = "#1b63d8", "#16a97f", "#e8853d", "#d2453c"


def salvar(fig, nome):
    caminho = os.path.join(SAIDA, nome)
    fig.savefig(caminho, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("gerado:", nome)


# --------------------------------------------------------------- burndown
def burndown():
    dias = ["D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"]
    ideal = [34, 30.6, 27.2, 23.8, 20.4, 17, 13.6, 10.2, 6.8, 3.4, 0]
    real = [34, 34, 31, 29, 24, 21, 21, 16, 11, 8, 5]

    fig, ax = plt.subplots(figsize=(7.6, 3.5))
    ax.plot(dias, ideal, "--", color="#9aacc4", lw=1.8, label="Linha ideal de queima")
    ax.plot(dias, real, "-o", color=AZUL, lw=2.3, ms=5, label="Pontos restantes (real)")
    ax.fill_between(dias, real, ideal, where=[r >= i for r, i in zip(real, ideal)],
                    color=VERMELHO, alpha=.10, label="Atraso acumulado")

    ax.set_ylabel("Pontos de história restantes")
    ax.set_xlabel("Dias úteis da Sprint 6 (19/10 a 01/11/2026)")
    ax.set_ylim(0, 37)
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    ax.annotate("Impedimento:\nindisponibilidade do\nambiente de homologação",
                xy=("D6", 21), xytext=(5.4, 30), fontsize=8.2, color="#b3443c",
                arrowprops=dict(arrowstyle="->", color="#b3443c", lw=1.1))
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    salvar(fig, "fig_burndown.png")


# ------------------------------------------------- desempenho das consultas
def desempenho():
    consultas = ["Painel\noperacional", "Fila de\ndistribuição", "Relatório\nde SLA",
                 "Produtividade\npor técnico", "Faturamento\nmensal"]
    antes = [2840, 1960, 6420, 3180, 8750]
    depois = [41, 83, 214, 156, 390]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.5),
                                   gridspec_kw={"width_ratios": [1.45, 1]})

    x = range(len(consultas))
    larg = .38
    ax1.bar([i - larg / 2 for i in x], antes, larg, color=VERMELHO, label="Antes da otimização")
    ax1.bar([i + larg / 2 for i in x], depois, larg, color=VERDE, label="Após índices e procedures")
    ax1.set_yscale("log")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(consultas, fontsize=8.4)
    ax1.set_ylabel("Tempo de resposta (ms) — escala logarítmica")
    ax1.legend(frameon=False, fontsize=8.6)
    ax1.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(v)}"))
    for i, (a, d) in enumerate(zip(antes, depois)):
        ax1.text(i + larg / 2, d * 1.25, f"-{(1 - d / a) * 100:.1f}%",
                 ha="center", fontsize=7.8, color="#0f7d60", fontweight="bold")
    for lado in ("top", "right"):
        ax1.spines[lado].set_visible(False)

    leituras_antes = [18420, 12700, 41300, 22600, 58900]
    leituras_depois = [612, 940, 2180, 1470, 3350]
    ax2.barh(consultas, leituras_antes, color=VERMELHO, height=.38,
             label="Leituras lógicas — antes")
    ax2.barh(consultas, leituras_depois, color=VERDE, height=.38,
             label="Leituras lógicas — depois")
    ax2.set_xlabel("Leituras lógicas por execução")
    ax2.tick_params(labelsize=8.2)
    ax2.legend(frameon=False, fontsize=8.2, loc="lower right")
    for lado in ("top", "right"):
        ax2.spines[lado].set_visible(False)

    fig.tight_layout()
    salvar(fig, "fig_desempenho.png")


# --------------------------------------------------------- custos da nuvem
def custos():
    itens = ["AKS\n(computação)", "Azure SQL\nBusiness Critical", "Armazenamento\ne backup",
             "Rede, WAF e\nFront Door", "Observabilidade", "Licenças e\nferramentas"]
    valores = [3180.00, 2740.00, 610.00, 890.00, 470.00, 1420.00]
    cores = [AZUL, "#2f7df6", VERDE, LARANJA, "#7d5bd6", "#8b95a3"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.4),
                                   gridspec_kw={"width_ratios": [1, 1.25]})

    ax1.pie(valores, colors=cores, startangle=90, counterclock=False,
            wedgeprops=dict(width=.46, edgecolor="white", linewidth=2),
            autopct=lambda p: f"{p:.1f}%", pctdistance=.77,
            textprops=dict(fontsize=8, color="white", fontweight="bold"))
    ax1.text(0, .08, "R$ 9.310", ha="center", fontsize=14, fontweight="bold")
    ax1.text(0, -.16, "custo mensal", ha="center", fontsize=8.5, color="#7b8794")
    ax1.legend(itens, frameon=False, fontsize=7.6, loc="center left",
               bbox_to_anchor=(-.42, -.14), ncol=2)
    ax1.set_title("Composição do custo mensal de operação", fontsize=9.5, pad=10)
    ax1.grid(False)

    meses = ["Jun", "Jul", "Ago", "Set", "Out", "Nov"]
    legado = [14200, 14200, 14650, 14650, 14650, 14650]
    nuvem = [0, 4100, 7300, 8620, 9050, 9310]
    ax2.plot(meses, legado, "-s", color=VERMELHO, lw=2, ms=4.5,
             label="Custo do parque legado (on-premise)")
    ax2.plot(meses, nuvem, "-o", color=VERDE, lw=2, ms=4.5,
             label="Custo da solução em nuvem")
    ax2.fill_between(meses, nuvem, legado, color=VERDE, alpha=.09)
    ax2.set_ylabel("R$ por mês")
    ax2.set_title("Evolução do custo durante a migração", fontsize=9.5, pad=10)
    ax2.legend(frameon=False, fontsize=8.2, loc="center right")
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v/1000:.0f} mil"))
    ax2.annotate("economia de 36,4%\nao final da migração", xy=("Nov", 11980),
                 fontsize=8, color="#0f7d60", ha="center")
    for lado in ("top", "right"):
        ax2.spines[lado].set_visible(False)

    fig.tight_layout()
    salvar(fig, "fig_custos.png")


# ------------------------------------------------- indicadores antes/depois
def indicadores():
    rotulos = ["Aderência\nao SLA (%)", "Disponibilidade\n(%)", "Chamados tratados\npor técnico/mês",
               "Implantações\npor mês", "Satisfação do\ncliente (0-10)"]
    antes = [85.5, 97.2, 46, 2, 6.4]
    depois = [96.8, 99.97, 71, 42, 8.7]
    maximos = [100, 100, 90, 50, 10]

    fig, ax = plt.subplots(figsize=(8.6, 3.2))
    y = range(len(rotulos))
    for i, (a, d, m) in enumerate(zip(antes, depois, maximos)):
        ax.plot([a / m * 100, d / m * 100], [i, i], color="#c9d2de", lw=5, solid_capstyle="round")
        ax.scatter(a / m * 100, i, s=110, color=VERMELHO, zorder=3, label="Antes" if i == 0 else "")
        ax.scatter(d / m * 100, i, s=110, color=VERDE, zorder=3, label="Depois" if i == 0 else "")
        ax.text(a / m * 100, i + .3, f"{a:g}", ha="center", fontsize=8, color="#b3443c")
        ax.text(d / m * 100, i + .3, f"{d:g}", ha="center", fontsize=8,
                color="#0f7d60", fontweight="bold")

    ax.set_yticks(list(y))
    ax.set_yticklabels(rotulos, fontsize=8.6)
    ax.set_xlabel("Percentual do valor máximo de referência de cada indicador")
    ax.set_xlim(0, 112)
    ax.invert_yaxis()
    ax.legend(frameon=False, fontsize=9, loc="lower right", ncol=2)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    salvar(fig, "fig_indicadores.png")


if __name__ == "__main__":
    burndown()
    desempenho()
    custos()
    indicadores()
