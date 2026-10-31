# Rúbrica · v1.1 (Chili's DS)

Escala 1–5. La usan el evaluator y el humano, sin cambios entre ambos.
**Umbral para pasar a review humana: 3.5 ponderado y cero faltas bloqueantes.**

| Criterio | Peso |
|---|---|
| Ataca la métrica | 30% |
| Criterios de aceptación | 25% |
| Consistencia con el DS | 20% |
| Plataforma | 15% |
| Divergencia | 10% |

Ponderado = Σ (puntaje × peso). Divergencia se puntúa una vez para el
set completo y se aplica igual a las 3 versiones.

**Falta bloqueante:** cualquier `[BLOQUEANTE]` de `scripts/lint_ds.py`, o más de
una acción primaria por vista, o un estado comunicado solo con color.
Una versión con falta bloqueante no pasa, sin importar su ponderado.

---

## Ataca la métrica (30%)
¿El diseño tiene una razón creíble para mover la métrica del brief?

| | Descriptor |
|---|---|
| 1 | No hay relación visible entre el diseño y la métrica. |
| 2 | La hipótesis existe en el comentario, pero el diseño no la ejecuta. |
| 3 | La hipótesis se ejecuta, pero hay un obstáculo evidente en el flujo que la anula parcialmente. |
| 4 | Hipótesis clara y ejecutada; queda un caso relevante sin resolver (error, vacío, borde). |
| 5 | Hipótesis clara, ejecutada y cubierta en sus casos principales. Sin mejora nombrable. |

## Criterios de aceptación (25%)
| | Descriptor |
|---|---|
| 1 | Cumple menos de la mitad. |
| 2 | Cumple la mitad o más, pero falla alguno crítico. |
| 3 | Cumple todos de forma literal, con alguno resuelto débilmente. |
| 4 | Cumple todos con claridad. |
| 5 | Cumple todos y se pueden verificar sin explicación adicional. |

## Consistencia con el DS (20%)
Referencia: `design-system/guidelines.md` y `components.md`.

| | Descriptor |
|---|---|
| 1 | Valores sueltos, primitivos o detach de componentes en varios lugares. |
| 2 | Hay alguna falta bloqueante del lint, o se usan componentes contra su NO USAR. |
| 3 | Sin faltas bloqueantes, pero con usos dudosos (variante poco apropiada, componente forzado). |
| 4 | Componentes y variantes correctos; gaps registrados en `solicitudes-ds.md`. |
| 5 | Como 4, y la composición respeta las reglas del patrón del producto o justifica romperlas. |

## Plataforma (15%)
Viewports del producto: Ecommerce 1440 + 390 · Reservas 820×1180 · Toma de pedido 1180×820.

| | Descriptor |
|---|---|
| 1 | Se rompe en algún viewport del producto (scroll horizontal, solapes, texto cortado). |
| 2 | No se rompe, pero pierde la acción principal o la jerarquía en algún viewport. |
| 3 | Funciona, con fricciones: objetivos táctiles < `--size-touch-min`, CTA bajo el fold sin razón, foco no visible. |
| 4 | Funciona en todos los viewports con jerarquía clara y objetivos táctiles correctos. |
| 5 | Cada viewport está pensado para su contexto (cliente en celular, mozo en tablet), no comprimido. Si el brief pide Dark, funciona sin estilos propios por tema. |

## Divergencia (10%) · se puntúa por set
| | Descriptor |
|---|---|
| 1 | Las 3 versiones son la misma estructura. |
| 2 | Cambian solo color, copy, íconos o variantes de botón. |
| 3 | Dos versiones comparten estructura; una diverge. |
| 4 | Tres estructuras distintas; dos hipótesis son parecidas. |
| 5 | Tres estructuras y tres hipótesis distintas, cada una con su referencia. |

---

## Cambios a la rúbrica
Toda modificación sube la versión en `CHANGELOG.md`. Los puntajes de
versiones distintas de la rúbrica no se comparan directamente.

### v1.1
- "Responsive" pasa a "Plataforma", con los viewports de cada producto.
- Consistencia con el DS referida al Chili's DS y al lint.
- Faltas bloqueantes impiden pasar el umbral.
