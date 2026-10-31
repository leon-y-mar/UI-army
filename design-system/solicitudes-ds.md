# Solicitudes al design system

Equivale a la página **QA & Changelog** de Figma. Aquí el designer registra
lo que el DS no cubre. El humano decide y, si procede, lo lleva a Figma.

Formato:
`- [ ] <fecha> · <tarea> · <componente o patrón> · <qué falta> · <cómo se resolvió en el prototipo>`

Estados: `[ ]` pendiente · `[x]` llevado a Figma · `[-]` descartado (con motivo)

## Pendientes
- [ ] 2026-10-31 · S01-typ-cupon · Cupón / Ticket (nuevo componente) · No existe un bloque de cupón con valor del descuento, código, vencimiento, titular y acción "Copiar código" · Compuesto con layout propio (bg/surface-warm + bloque bg/canvas para el código) + estilos de texto ds-label-sm/ds-h4/ds-p-* + ds-price + ds-button (v1, v2, v3)
- [ ] 2026-10-31 · S01-typ-cupon · Feedback "copiado" (toast / snackbar) · No hay feedback efímero tras copiar al portapapeles · Alert Inline Success ("Código copiado…") y Alert Inline Error si falla, debajo del botón; el botón cambia a "Código copiado" con ícono checkmark (v1, v2, v3)
- [ ] 2026-10-31 · S01-typ-cupon · Resumen de pedido de solo lectura (Order Summary sin Checkout) · Cart Summary incluye Checkout y Cart Item incluye Quantity; la TYP necesita ambos de solo lectura · Cart Item sin Quantity con "Cant. 1" en los modificadores + filas de subtotal/delivery/total compuestas con layout propio y ds-price (v1, v2); lista dentro de un Accordion (v3)
- [ ] 2026-10-31 · S01-typ-cupon · Campo de código copiable (Input read-only) · Input es para capturar texto; no hay variante de solo lectura para mostrar un código seleccionable · Texto ds-h4/ds-p-xl-800 en un bloque bg/canvas con user-select: all (v1, v2, v3)
- [ ] 2026-10-31 · S01-typ-cupon · Stepper de estado del pedido · No hay componente para los pasos Confirmado → En cocina → En camino → Entregado · Lista compuesta con ds-icon + estilos ds-p-xs-700/500 y texto de estado ("Listo", "Ahora", "Pendiente") para no depender del color (v3)
- [ ] 2026-10-31 · S01-typ-cupon · Patrón TYP (confirmación de pedido) Desktop 1440 + Mobile 390 · No existe pantalla de confirmación en Patterns · Ecommerce ni versión Mobile 390 del ecommerce (revisión humana) · Tres propuestas compuestas con Header Desktop/Mobile y componentes existentes (v1, v2, v3)
- [ ] 2026-10-31 · S01-typ-cupon · Íconos copiar, correo y cupón · No están entre los íconos exportados (revisión humana: íconos faltantes de la guía) · Se omiten y la acción se comunica con texto ("Copiar código", "en tu correo"); pasos del pedido usan placeholders clock/delivery/location (v1, v2, v3)

## Resueltas
