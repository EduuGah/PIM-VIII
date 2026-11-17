# -*- coding: utf-8 -*-
"""Captura as paginas HTML do projeto em PNG usando o Chrome em modo headless.
As imagens resultantes sao as figuras inseridas no documento do PIM VIII."""

import os
import subprocess
import sys
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT = os.path.join(RAIZ, "front")
SAIDA = os.path.join(RAIZ, "figuras")
os.makedirs(SAIDA, exist_ok=True)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME):
    CHROME = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# (arquivo html, png de saida, largura, altura, recortar fundo)
PAGINAS = [
    ("arq-cloud.html",   "fig_arq_cloud.png",   1180,  730, False),
    ("kanban.html",      "fig_kanban.png",      1340,  700, False),
    ("web-painel.html",  "fig_web_painel.png",  1280,  900, False),
    ("mobile.html",      "fig_mobile.png",       880,  800, False),
    ("der.html",         "fig_der.png",         1240,  700, False),
    ("pipeline.html",    "fig_pipeline.png",    1300,  640, False),
    ("cod_entidade.html",  "fig_cod_entidade.png",  900,  700, True),
    ("cod_procedure.html", "fig_cod_procedure.png", 900,  720, True),
]


def capturar(html, png, largura, altura):
    origem = os.path.join(FRONT, html)
    destino = os.path.join(SAIDA, png)
    url = "file:///" + origem.replace("\\", "/").replace(" ", "%20")

    comando = [
        CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
        "--no-sandbox", "--force-device-scale-factor=2",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=2500",
        f"--window-size={largura},{altura}",
        f"--screenshot={destino}",
        url,
    ]
    subprocess.run(comando, capture_output=True, timeout=120)
    return destino


def recortar(caminho, margem=18):
    """Remove o excesso de fundo uniforme ao redor da janela de codigo."""
    img = Image.open(caminho).convert("RGB")
    fundo = img.getpixel((2, 2))
    larg, alt = img.size

    def linha_vazia(y):
        return all(img.getpixel((x, y)) == fundo for x in range(0, larg, 6))

    base = alt - 1
    while base > 0 and linha_vazia(base):
        base -= 1

    direita = larg - 1
    while direita > 0 and all(img.getpixel((direita, y)) == fundo
                              for y in range(0, alt, 6)):
        direita -= 1

    img.crop((0, 0, min(larg, direita + margem), min(alt, base + margem))).save(caminho)


if __name__ == "__main__":
    if not os.path.exists(CHROME):
        sys.exit("Navegador nao localizado para a captura.")

    for html, png, larg, alt, cortar in PAGINAS:
        caminho = capturar(html, png, larg, alt)
        if not os.path.exists(caminho):
            print("FALHOU:", png)
            continue
        if cortar:
            recortar(caminho)
        tam = Image.open(caminho).size
        print("capturado: %-26s %sx%s" % (png, tam[0], tam[1]))
