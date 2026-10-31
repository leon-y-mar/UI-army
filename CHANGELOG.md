# Changelog del harness

Cada cambio a CLAUDE.md, agentes, rúbrica, comandos o design system sube versión.
`log.json` registra con qué versión se ejecutó cada tarea, para saber si una
mejora vino del harness o de la tarea.

## v0.2.1 · Estructura, render y Mobbin
- Estructura de carpetas restaurada (la subida por web la había aplanado).
- `scripts/render.js`: render con el Playwright del entorno, todas las
  versiones × viewports × temas en una llamada; reporta scroll horizontal y
  errores JS. Reemplaza `npx playwright install` en el evaluator.
- Designer: herramientas `mcp__Mobbin__search_*` (antes `mcp__mobbin`, que no
  coincidía con el conector), búsqueda en modo `deep` y revisión de cada imagen.
- `docs/setup.md`: Mobbin entra como conector de claude.ai; `.mcp.json` no
  funciona detrás del proxy de la nube.

## v0.2.0 · Chili's DS
- `design-system/` generado desde Figma "Prueba - Chilis DS" v1.2.0:
  tokens.json, tokens.css (Light/Dark, Web/Tablet), components.css (26 componentes),
  components.md, patterns.md, guidelines.md, preview.html, solicitudes-ds.md.
- Brief pide producto (ecommerce, reservas, toma de pedido) y tema.
- Viewports por producto: 1440+390, 820×1180, 1180×820.
- Prototipos enlazan el DS en lugar de copiar estilos (`templates/prototype.html`).
- `scripts/lint_ds.py`: reglas mecánicas del DS; sus bloqueantes impiden pasar el umbral.
- Rúbrica v1.1: "Responsive" pasa a "Plataforma"; faltas bloqueantes.
- Comparador con 4 viewports y Light/Dark.

## v0.1.0
- Orquestador con chequeo de brief.
- Designer y evaluator como subagentes separados.
- Loop de hasta 3 iteraciones con umbral 3.5.
- Cierre con delta evaluador vs humano y learnings propuestos.
