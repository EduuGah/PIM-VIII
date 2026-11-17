# -*- coding: utf-8 -*-
"""Gera paginas HTML com aparencia de editor de codigo (estilo VS Code) a partir
dos arquivos-fonte do projeto. As paginas sao depois capturadas pelo Chrome em
modo headless e viram as figuras do PIM."""

import os
import html as html_mod
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONT = os.path.join(RAIZ, "front")

TEMA = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#f0f2f5;font:13px "Segoe UI",Arial,sans-serif;padding:16px}
.win{background:#1e1e1e;border-radius:9px;overflow:hidden;
     box-shadow:0 10px 28px rgba(15,25,45,.26)}
.tb{background:#323233;display:flex;align-items:center;padding:0 12px;height:40px;gap:9px}
.dots{display:flex;gap:6px}
.dots i{width:11px;height:11px;border-radius:50%;display:block}
.tab{background:#1e1e1e;color:#ffffff;font-size:13.5px;padding:8px 14px;border-top:1.5px solid #0a84ff;
     margin-left:8px;display:flex;align-items:center;gap:6px}
.tab em{font-style:normal;color:#8a8a8a}
.path{margin-left:auto;color:#9a9a9a;font-size:12px;font-family:Consolas,monospace}
.code{display:flex;padding:11px 0 13px}
.ln{color:#6e7681;text-align:right;padding:0 11px 0 15px;font:15px/1.55 Consolas,"Cascadia Mono",monospace;
    user-select:none;border-right:1px solid #2b2b2b}
pre{margin:0;padding:0 16px;font:15px/1.55 Consolas,"Cascadia Mono",monospace;color:#d4d4d4;
    white-space:pre;overflow:visible}
.sb{background:#007acc;color:#fff;font-size:12px;padding:3px 12px;display:flex;gap:16px}
.sb span:last-child{margin-left:auto}
"""

# Paleta aproximada do tema Dark+ do Visual Studio Code
CORES = {
    "k": "#569cd6", "kd": "#569cd6", "kn": "#569cd6", "kr": "#569cd6", "kt": "#569cd6",
    "kc": "#569cd6", "kp": "#569cd6",
    "c": "#6a9955", "c1": "#6a9955", "cm": "#6a9955", "cs": "#6a9955", "cp": "#9b9b9b",
    "s": "#ce9178", "s1": "#ce9178", "s2": "#ce9178", "sb": "#ce9178", "sd": "#ce9178",
    "se": "#d7ba7d", "sh": "#ce9178", "sx": "#ce9178",
    "m": "#b5cea8", "mi": "#b5cea8", "mf": "#b5cea8", "mh": "#b5cea8",
    "n": "#d4d4d4", "na": "#9cdcfe", "nb": "#4ec9b0", "nc": "#4ec9b0", "nd": "#dcdcaa",
    "nf": "#dcdcaa", "ni": "#9cdcfe", "nl": "#c8c8c8", "nn": "#4ec9b0", "nt": "#569cd6",
    "nv": "#9cdcfe", "no": "#4fc1ff", "ne": "#4ec9b0", "nx": "#dcdcaa",
    "o": "#d4d4d4", "ow": "#569cd6", "p": "#d4d4d4", "w": "#d4d4d4",
}


def css_tokens():
    return "\n".join(".%s{color:%s}" % (cls, cor) for cls, cor in CORES.items())


def trecho(caminho, inicio, fim):
    with open(caminho, encoding="utf-8") as arq:
        linhas = arq.readlines()
    return "".join(linhas[inicio - 1:fim]), inicio


def pagina(titulo_aba, caminho_exibido, codigo, linguagem, primeira_linha,
           largura=1080, rodape=""):
    lexer = get_lexer_by_name(linguagem)
    fmt = HtmlFormatter(nowrap=True)
    corpo = highlight(codigo, lexer, fmt)
    total = codigo.count("\n") + (0 if codigo.endswith("\n") else 1)
    numeros = "<br>".join(str(primeira_linha + i) for i in range(total))

    icone = {"csharp": "#9b59d0", "sql": "#e8853d", "docker": "#2496ed",
             "yaml": "#d2453c", "xml": "#16a97f"}.get(linguagem, "#1b63d8")

    return f"""<!doctype html>
<html lang="pt-br"><head><meta charset="utf-8"><title>{html_mod.escape(titulo_aba)}</title>
<style>{TEMA}
{css_tokens()}
body{{width:{largura}px}}
</style></head><body>
<div class="win">
  <div class="tb">
    <div class="dots"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i>
      <i style="background:#28c840"></i></div>
    <div class="tab"><span style="color:{icone}">&#9679;</span>{html_mod.escape(titulo_aba)}
      <em>&#215;</em></div>
    <div class="path">{html_mod.escape(caminho_exibido)}</div>
  </div>
  <div class="code"><div class="ln">{numeros}</div><pre>{corpo}</pre></div>
  <div class="sb"><span>AlunosTech.sln</span><span>Ln {primeira_linha}</span>
    <span>UTF-8</span><span>{rodape}</span></div>
</div>
</body></html>"""


def gerar(nome, titulo_aba, caminho_rel, inicio, fim, linguagem, largura=1080, rodape=""):
    origem = os.path.join(RAIZ, caminho_rel.replace("/", os.sep))
    codigo, primeira = trecho(origem, inicio, fim)
    destino = os.path.join(FRONT, nome + ".html")
    with open(destino, "w", encoding="utf-8") as arq:
        arq.write(pagina(titulo_aba, caminho_rel, codigo, linguagem, primeira, largura, rodape))
    print("gerado:", nome, "(%d linhas)" % (fim - inicio + 1))


if __name__ == "__main__":
    gerar("cod_entidade", "Chamado.cs",
          "codigo/src/AlunosTech.Domain/Entidades/Chamado.cs", 47, 60,
          "csharp", 900, "C# 12 / .NET 8")

    gerar("cod_procedure", "02_procedures.sql",
          "codigo/banco/02_procedures.sql", 24, 42,
          "sql", 900, "SQL Server 2022")
