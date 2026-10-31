# UI-Army

Harness de diseño para ejecutar tareas de sprint con agentes:
benchmark, 3 propuestas de interfaz con el design system de Chili's,
evaluación independiente y aprendizaje curado por un humano.

**Versión del harness:** v0.2.1 (ver `CHANGELOG.md`) · **DS:** Chili's DS v1.2.0

## Qué hace

```
brief ──► chequeo ──► benchmark ──► designer ⇄ evaluator ──► review humana ──► cierre
                        (Mobbin)    (lint DS + render + rúbrica)   (rúbrica)    (log + learnings)
```

| Pieza | Archivo | Rol |
|---|---|---|
| Orquestador | `CLAUDE.md` | Sesión principal. Valida, delega, registra. |
| Designer | `.claude/agents/designer.md` | Benchmark y 3 propuestas con el DS. |
| Evaluator | `.claude/agents/evaluator.md` | Lint, render y puntaje. Nunca diseña. |
| Design system | `design-system/` | Copia en código del Figma de Chili's. |
| Humano | `tasks/<id>/review.md` | Review real, puntaje, learnings y solicitudes al DS. |

## Productos que cubre

| Producto | Viewports | Patrón base |
|---|---|---|
| Ecommerce | Desktop 1440 · Mobile 390 | Menú con carrito lateral |
| Reservas | Tablet vertical 820×1180 | Fecha → Hora → Personas → Resumen |
| Toma de pedido | Tablet horizontal 1180×820 | Plano de mesas + pedido + Action Bar |

## Comandos

| Comando | Cuándo |
|---|---|
| `/nueva-tarea <id>` | Crear la carpeta de una tarea desde el template |
| `/ejecutar <id>` | Correr benchmark + loop designer/evaluator |
| `/cerrar <id>` | Después de tu review: score, delta, log y learnings propuestos |
| `/estado` | Resumen de métricas de `log.json` |

## Empezar

1. `docs/setup.md`: GitHub + Claude Code en la nube, sin git local.
2. Abre `design-system/preview.html` y compáralo con Figma.
3. `rubric/calibration/` y `baseline/` (ver `docs/personalizar.md`).
4. `/nueva-tarea S01-<nombre>` → completa el brief → `/ejecutar S01-<nombre>`.

## Estructura

```
UI-Army/
├── CLAUDE.md               # orquestador
├── .mcp.json               # Mobbin MCP
├── .claude/agents/         # designer, evaluator
├── .claude/commands/       # nueva-tarea, ejecutar, cerrar, estado
├── design-system/          # Chili's DS: tokens, componentes, patrones, reglas
├── scripts/lint_ds.py      # reglas mecánicas del DS
├── scripts/render.js       # screenshots por viewport/tema + scroll horizontal
├── docs/                   # setup, flujo, métricas, personalizar, actualizar-ds
├── rubric/                 # rúbrica v1.1 + calibración (tuya)
├── memory/learnings.md     # reglas aprobadas por el humano
├── templates/              # brief, benchmark, prototipo, evaluación, review, comparador
├── baseline/               # tiempos sin agente
├── tasks/                  # una carpeta por tarea
├── log.json                # una fila por tarea cerrada
└── CHANGELOG.md            # versiones del harness
```
