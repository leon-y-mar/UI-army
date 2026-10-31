# Personalizar UI-Army

El design system ya está cargado desde Figma. Lo que queda es enseñarle
al harness **tu** criterio y medir contra tu realidad.

## Obligatorio antes de la primera tarea

| # | Qué | Qué hacer | Si no lo haces |
|---|---|---|---|
| 1 | `design-system/preview.html` | Ábrelo en Light, Dark y Tablet y compáralo con Figma. Revisa sobre todo lo marcado `[aprox]` en `components.css` | El agente replica errores del CSS en cada prototipo |
| 2 | `rubric/calibration/` | 3 ejemplos reales (bajo, medio, alto) | El evaluator puntúa con criterio genérico |
| 3 | `baseline/tareas-manuales.json` | 2–3 tareas con datos reales | No hay contra qué comparar |

## Decisiones pendientes del DS (heredadas de Figma)
Estas las debes resolver tú o el equipo de marca; el agente solo las señala.
- Copy del patrón de Ecommerce en inglés.
- Separación vertical entre Product Cards en la grilla.
- Versión mobile del Ecommerce (no existe en Figma).
- Quantity con botones de 32px frente al mínimo táctil de 44px.
- Íconos, logo y fuente Dirk: hoy son placeholders.

## Mejoras de fidelidad con más impacto
1. **Exportar íconos y logo.** Pon los SVG de la página Assets en
   `design-system/icons/` y reemplaza `.ds-icon` por `<img>` o SVG inline.
2. **Cerrar los `[aprox]`.** Lee en Figma los estados Focused, Hover y
   Disabled que faltan y ajusta `components.css`.
3. **Fuente Dirk.** Si la licencia lo permite, agrégala con `@font-face`
   en `tokens.css`.

## Ajustes recomendados después de 2–3 tareas

| Archivo | Qué ajustar | Señal para hacerlo |
|---|---|---|
| `rubric/rubric.md` | Pesos y umbral | El delta en un criterio es ≥ 1.5 de forma sostenida |
| `rubric/rubric.md` | Agregar un criterio | Muchos comentarios "fuera de rúbrica" |
| `scripts/lint_ds.py` | Nuevas reglas mecánicas | El evaluator detecta a mano el mismo error del DS varias veces |
| `.claude/agents/evaluator.md` | Reglas de puntuación | El evaluator es sistemáticamente blando o duro |
| `.claude/agents/designer.md` | Reglas de divergencia | Divergencia ≤ 3 en varias tareas |
| `CLAUDE.md` | Máximo de iteraciones | El loop casi siempre usa 3 sin llegar al umbral |

## Lo que puedes cambiar con libertad
- Redacción y tono de los agentes.
- El diseño de `templates/compare.html`.
- Las búsquedas sugeridas para Mobbin en el designer.
- Agregar comandos en `.claude/commands/`.

## Lo que conviene no romper
- **La separación designer / evaluator.**
- **La aprobación humana de learnings y de solicitudes al DS.**
- **`design-system/` como copia de Figma:** no lo edites a mano salvo para cerrar
  `[aprox]`; para todo lo demás, regenera (`docs/actualizar-ds.md`).
- **Los nombres de clase `ds-*`:** si cambian, los prototipos viejos se rompen.
- **El esquema de `log.json`** y el campo `harness_version`.

## Cómo probar un cambio
1. Sube la versión en `CHANGELOG.md` y describe el cambio.
2. Corre la siguiente tarea normalmente.
3. Compara con `/estado` las tareas de la versión anterior contra la nueva.
Cambia una cosa por vez; si cambias tres, no sabrás cuál funcionó.

## Roadmap después del piloto
- **Planner como agente:** cuando otras personas escriban briefs.
- **Salida a Figma:** con el MCP de Figma, usando las instancias reales.
- **Agente de handoff:** casuísticas y escenarios para QA y dev.
