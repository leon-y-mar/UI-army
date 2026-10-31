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
Diseñar la pantalla de confirmación del pedido (TYP) del ecommerce con un cupón
personalizado de descuento para el próximo pedido, cuando la compra supera
S/ 80.00, para clientes logueados y no logueados.

- **Códigos personalizados:** códigos únicos asociados al cliente, no genéricos.
- **Clientes no logueados:** el checkout sin sesión captura datos del cliente
  (confirmado por el humano); el cupón queda asociado a esos datos y al pedido
  para consulta posterior. El mecanismo técnico (cookies u otro) no es parte
  de esta tarea.
- **Fuera de alcance:** sección de Avisos y otros tipos de cupón (delivery
  gratis, primera compra) → tarea S02.

## Usuario
Cliente del ecommerce (logueado o no), justo después de completar una compra.

## Objetivo
Incentivar la recompra mediante cupones personalizados después de una compra
que cumpla el monto mínimo, mostrados en la confirmación del pedido.

## Métrica
- **Principal:** % de usuarios que canjea cupones al mes · valor actual: sin dato · fuente: sin fuente
- **Secundaria:** # de usuarios que copia el código de descuento
- Otras métricas mencionadas: # de transacciones con cupón de descuento ·
  prom. de códigos canjeados por usuario al mes

## Criterios de aceptación
Cada uno debe poder responderse con sí/no mirando el diseño.
- [ ] El cupón (código, descuento y vencimiento) se ve sin hacer scroll en desktop 1440×900 y en mobile 390×844.
- [ ] El cupón es visible después del checkout.
- [ ] El usuario podrá copiar el código desde la TYP.
- [ ] En una compra < S/ 80.00, la TYP no muestra cupón.
- [ ] El cliente no logueado ve en la TYP dónde y cómo recuperar su cupón después.

## Restricciones
- No existe pantalla de confirmación (TYP) en el DS: se componen
  con componentes existentes y se registran en `solicitudes-ds.md`.
- No existe versión Mobile 390 del ecommerce en Figma (revisión humana).

## Material de apoyo (opcional)
sin material
