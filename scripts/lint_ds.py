#!/usr/bin/env python3
"""UI-Army · lint del DS para prototipos.

Revisa reglas verificables de design-system/guidelines.md sin interpretar diseño.
Uso:  python3 scripts/lint_ds.py tasks/<id>/prototypes/v1.html [v2.html ...]
Salida: tabla por archivo. Código de salida 1 si hay faltas BLOQUEANTES.
"""
import re, sys, pathlib

REQUIRED_FIELDS = ["version", "producto", "hipotesis", "referencia", "patron-base",
                   "trade-off", "componentes-ds", "gaps-ds", "revision-humana"]

def own_css(html):
    """CSS escrito por el designer: bloques <style> y atributos style=."""
    blocks = re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I)
    inline = re.findall(r'style="([^"]*)"', html, re.I)
    return "\n".join(blocks), "\n".join(inline)

def check(path):
    html = pathlib.Path(path).read_text(encoding="utf-8")
    css, inline = own_css(html)
    allcss = css + "\n" + inline
    issues = []  # (nivel, regla, detalle)

    def add(level, rule, detail):
        issues.append((level, rule, detail))

    # 1. Enlaces al DS
    for f in ["tokens.css", "components.css", "prototype.js"]:
        if f not in html:
            add("BLOQUEANTE", "enlace-ds", f"no enlaza design-system/{f}")

    # 2. Colores sin variable
    for m in re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)", allcss):
        add("BLOQUEANTE", "color-sin-token", m)

    # 3. Primitivos y ext/
    for m in set(re.findall(r"--prim-[a-z0-9-]+", allcss)):
        add("BLOQUEANTE", "token-primitivo", m)
    for m in set(re.findall(r"--[a-z-]*ext-[a-z0-9-]+", allcss)):
        add("BLOQUEANTE", "token-ext", m)

    # 4. Detach: reestilar clases del DS en el CSS propio
    for sel in re.findall(r"([^{}]*\.ds-[a-z0-9_-]+[^{}]*)\{", css):
        add("BLOQUEANTE", "detach", sel.strip()[:80])

    # 5. Tamaños sueltos en px (fuera de var) en CSS propio: advertencia
    px = [m for m in re.findall(r"(?<![\w-])(\d+(?:\.\d+)?px)", allcss) if m not in ("0px", "1px")]
    if px:
        add("ADVERTENCIA", "px-sin-token", ", ".join(sorted(set(px))[:10]))

    # 6. Una sola acción primaria (Offset rojo) visible por vista: aproximación por archivo
    primaries = len(re.findall(r'class="[^"]*ds-button--offset[^"]*ds-button--red[^"]*ds-button--lg|class="[^"]*ds-button--offset[^"]*ds-button--lg[^"]*ds-button--red', html))
    if primaries > 1:
        add("REVISAR", "una-primaria", f"{primaries} botones Offset rojo Large en el archivo; confirmar que no conviven en la misma vista")

    # 7. Outlined/Link solo en red y blue
    for cls in re.findall(r'class="([^"]*ds-button[^"]*)"', html):
        if re.search(r"ds-button--(outlined|link)", cls) and re.search(r"ds-button--(ranch|yellow)", cls):
            add("BLOQUEANTE", "variante-inexistente", cls)

    # 8. Comentario UI-ARMY completo
    head = re.search(r"<!--\s*UI-ARMY(.*?)-->", html, re.S)
    if not head:
        add("BLOQUEANTE", "comentario", "falta el bloque <!-- UI-ARMY -->")
    else:
        for f in REQUIRED_FIELDS:
            mm = re.search(rf"^\s*{re.escape(f)}:\s*(.+)$", head.group(1), re.M)
            if not mm or "<" in mm.group(1):
                add("BLOQUEANTE", "comentario", f"campo '{f}' vacío o sin completar")

    # 9. Producto y tablet
    prod = re.search(r"producto:\s*([^\n]+)", html)
    if prod and prod.group(1).strip() not in ("ecommerce", "reservas", "toma-de-pedido"):
        add("BLOQUEANTE", "comentario", "producto debe ser ecommerce, reservas o toma-de-pedido")
    prod = re.search(r"producto:\s*([a-z-]+)\s*$", html, re.M)
    if prod and prod.group(1) in ("reservas", "toma-de-pedido") and 'data-device="tablet"' not in html:
        add("BLOQUEANTE", "sizing-tablet", "producto de mozos sin data-device=\"tablet\"")

    # 10. Moneda
    for m in re.findall(r"S/\.?\s?\d+(?:[.,]\d+)?", html):
        if not re.fullmatch(r"S/ \d+\.\d{2}", m):
            add("ADVERTENCIA", "formato-moneda", f"'{m}' (esperado 'S/ 39.90')")

    # 11. Lorem ipsum
    if re.search(r"lorem ipsum", html, re.I):
        add("BLOQUEANTE", "contenido", "contiene Lorem ipsum")

    return issues

def main(paths):
    blocking = 0
    for p in paths:
        issues = check(p)
        b = sum(1 for i in issues if i[0] == "BLOQUEANTE")
        blocking += b
        print(f"\n## {p} · bloqueantes: {b} · otras: {len(issues) - b}")
        if not issues:
            print("Sin observaciones.")
        for level, rule, detail in issues:
            print(f"- [{level}] {rule}: {detail}")
    sys.exit(1 if blocking else 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    main(sys.argv[1:])
