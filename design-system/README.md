# Design system · Chili's DS

**Fuente de verdad:** Figma "Prueba - Chilis DS" · versión 1.2.0
https://www.figma.com/design/l78fB89GmYoqsmvvYTjLkn/Prueba---Chilis-DS
**Leído:** 2026-10-31 · Cómo actualizar: `docs/actualizar-ds.md`

Si este repo y Figma no coinciden, manda Figma.

## Archivos

| Archivo | Para qué | Quién lo lee |
|---|---|---|
| `guidelines.md` | Reglas para agentes: permitido, prohibido, accesibilidad, revisión humana | designer, evaluator |
| `tokens.json` | Todos los tokens con valores por modo (fuente para máquinas) | consulta |
| `tokens.css` | Tokens como variables CSS + text styles como clases | prototipos |
| `components.css` | Componentes publicados en HTML/CSS (equivale a instancias) | prototipos |
| `components.md` | Inventario: props, variantes, USAR / NO USAR, HTML de uso | designer, evaluator |
| `patterns.md` | Cómo se combinan los componentes en cada producto | designer, evaluator |
| `prototype.js` | Aplica `?theme=` y `?device=` en los prototipos | prototipos |
| `preview.html` | Vitrina de componentes para comparar contra Figma | humano |
| `solicitudes-ds.md` | Necesidades detectadas para llevar a QA & Changelog | designer escribe, humano decide |

## Arquitectura de tokens (igual que en Figma)

```
Primitives (ocultas)  →  Color semántico (Light / Dark)  →  Tokens de componente (button/*)
Sizing (Web / Tablet) · Layout (Desktop / Tablet / Mobile) · Typography (Desktop / Mobile)
Spacing sp-* · Radius br-* · Border bw-* · Motion · Elevation
```

Nomenclatura en CSS: el nombre de Figma con `/` → `-`.
`color/bg/canvas` → `--color-bg-canvas` · `button/red/bg` → `--button-red-bg` ·
`size/touch-min` → `--size-touch-min` · `sp-16` → `--sp-16`.

## Fidelidad
- `[figma]` en `components.css`: valor leído del componente.
- `[aprox]`: estado o detalle no leído (hover de algunos, focus, accordion, header mobile). Verifícalo con `preview.html` contra Figma.
- **Íconos y logo** son placeholders: los SVG de Assets no están exportados.
- **Dirk** no está disponible en web (licencia pendiente): se usa Montserrat 900 como respaldo.
