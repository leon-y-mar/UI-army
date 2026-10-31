# Resumen · S01-typ-cupon

**Harness:** v0.2.3 · **DS:** Chili's DS v1.2.0 · **Producto:** Ecommerce (1440×900 + 390×844) · **Tema:** Light
**Loop:** 2026-10-31T16:38:20+00:00 → 2026-10-31T17:03:52+00:00 (25 min) · **Iteraciones usadas:** 2 de 3
**Mobbin:** disponible (conector) · **Render:** disponible

## Score final (iteración 2)

| Criterio | Peso | v1 · Cupón primero | v2 · Confirmación + panel | v3 · Cupón ganado + guárdalo |
|---|---|---|---|---|
| Ataca la métrica | 30% | 4 | 4 | 4 |
| Criterios de aceptación | 25% | 4 | 4 | 3 |
| Consistencia DS | 20% | 4 | 4 | 4 |
| Plataforma | 15% | 3 | 3 | 4 |
| Divergencia (set) | 10% | 4 | 4 | 4 |
| **Ponderado** | | **3.85** | **3.85** | **3.75** |
| Faltas bloqueantes | | 0 | 0 | 0 |

Todas sobre el umbral (3.5). Evolución: iter-01 3.85 / 3.30 / 3.35 → iter-02 3.85 / 3.85 / 3.75.

## Versión recomendada por el evaluator
**v2** · Desempata con v1 (3.85): cumple los mismos criterios sin el trade-off de v1; en 1440 se ven a la vez el total pagado y el cupón completo con "Copiar código" sin scroll.

## Problemas abiertos (de `iter-02.md`)
- v1 y v2 · 390 · `sin-cupon`: "Seguir mi pedido", la única primaria, queda bajo el fold (v1 y=1077, v2 y=1314).
- v1 y v2 · `error-cupon`: se sigue ofreciendo "Crear cuenta y guardar el cupón" para un cupón que no se creó.
- v3 · criterio 5: manda al invitado a "Seguir mi pedido" pero no hay enlace hacia allí.
- v3 · `error-cupon`: la primaria sigue siendo "Crear cuenta"; "Reintentar" queda secundaria.
- Designer en desacuerdo con el evaluator (iter-01, v3): no sube "Copiar código" a primaria para el invitado, para no perder la hipótesis de v3. Ver `iter-01-respuesta.md`.

## Solicitudes al DS registradas en `design-system/solicitudes-ds.md`
9 líneas de S01-typ-cupon: Cupón/Ticket · feedback "copiado" · resumen de pedido de solo lectura · campo de código copiable · stepper de estado del pedido · patrón TYP desktop + mobile 390 · íconos copiar/correo/cupón · área táctil de Button Link/Small · botón ☰ del Header Mobile (28×32).
Nota: la línea "Resumen de pedido de solo lectura" menciona un Accordion en v3 que ya no existe en iter-02 (pendiente de corregir por el humano).

## Decisiones de revisión humana
- **Layout Mobile 390** del ecommerce: no existe en Figma; las 3 versiones lo proponen.
- **Dirk** en el valor del cupón (`ds-price` + estilos de título).
- **Imágenes placeholder** en Cart Item (v1, v2) e **íconos faltantes** (copiar, correo, cupón) resueltos con texto.
- **Umbral S/ 80.00:** ¿sobre subtotal o total con delivery? ¿Qué pasa con exactamente S/ 80.00? Sin esto el criterio 4 no es verificable del todo.
- **Contenido del cupón inventado por el designer:** valor (S/ 15.00), pedido mínimo de canje (S/ 50.00) y vencimiento. No están en el brief.
- **v3:** consentimiento de datos/términos al crear cuenta (no cubierto por brief ni DS) y aviso 3 días antes del vencimiento.
