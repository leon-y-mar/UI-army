# Brief · S01-typ-cupon

## Story points
2

## Producto
Marca uno. Define viewports y sizing (ver design-system/guidelines.md).
- [x] Ecommerce · Desktop 1440 + Mobile 390 · Sizing Web
- [ ] Reservas · Tablet vertical 820 × 1180 · Sizing Tablet
- [ ] Toma de pedido · Tablet horizontal 1180 × 820 · Sizing Tablet

## Tema
- [x] Solo Light (default)
- [ ] Light + Dark (el modo oscuro completo requiere revisión de marca)

## Contexto
Actualmente no tenemos una forma de brindarle cupones de descuento en su
próximo pedido a los usuarios que compran a través de la web y generar recompra.

## Tarea
Flujo de asignación y visualización de cupones personalizados post-compra:

1. **Visualización del cupón post compra:** en la pantalla de confirmación del
   pedido (TYP) se muestra un cupón cuando el monto de la compra supera un
   umbral de S/ 80.00.
2. **Códigos personalizados:** códigos únicos asociados al cliente, no genéricos.
3. **Clientes logueados y no logueados:** el cupón queda asociado al cliente o
   pedido para consulta posterior.
   Pregunta abierta del humano: ¿es factible mapear el código a un cliente no
   logueado (p. ej. por cookies)? → **PENDIENTE de decisión de producto/tecnología**
4. **Sección de Avisos:** el mismo cupón se muestra también en Avisos. Avisos
   también lista otros tipos de cupón: delivery gratis, primera compra (si aplica).
   Pregunta abierta del humano: ¿aplica para logueados y no logueados?
   → **PENDIENTE**

## Usuario
Cliente del ecommerce, justo después de completar una compra (TYP) y en una
visita posterior (Avisos).

## Objetivo
Incentivar la recompra mediante cupones personalizados después de una compra
que cumpla el monto mínimo, disponibles en la confirmación del pedido y en Avisos.

## Métrica
- **Principal:** % de usuarios que canjea cupones al mes · valor actual: **PENDIENTE** · fuente: **PENDIENTE**
- **Secundaria:** # de usuarios que copia el código de descuento
- Otras métricas mencionadas: # de transacciones con cupón de descuento ·
  prom. de códigos canjeados por usuario al mes

## Criterios de aceptación
Cada uno debe poder responderse con sí/no mirando el diseño.
- [ ] El usuario tendrá visibilidad clara del cupón. ⚠️ no verificable tal cual
- [ ] El cupón es visible después del checkout.
- [ ] El usuario podrá copiar el código desde la TYP.
- [ ] En una compra < S/ 20, la TYP no muestra cupón. ⚠️ contradice el umbral S/ 80.00
- [ ] El cliente no logueado ve en la TYP dónde y cómo recuperar su cupón después.

## Restricciones
- No existe pantalla de confirmación (TYP) ni de Avisos en el DS: se componen
  con componentes existentes y se registran en `solicitudes-ds.md`.
- No existe versión Mobile 390 del ecommerce en Figma (revisión humana).

## Material de apoyo (opcional)
<links a TYP y Avisos actuales, data, Figma>
