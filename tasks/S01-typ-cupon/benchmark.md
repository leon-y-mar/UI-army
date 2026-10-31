# Benchmark · S01-typ-cupon

**Pregunta guía:** ¿Cómo muestran otros productos, en la confirmación del pedido, una recompensa para la próxima compra de modo que el cliente la vea, copie el código y sepa cómo recuperarla después (incluso sin cuenta), para subir el % de usuarios que canjea cupones al mes?
**Búsquedas realizadas** (todas en `mode: deep`):
1. `web` · screens · "order confirmation page with discount coupon code for next order"
2. `ios` · screens · "food delivery app order confirmed screen with reward or coupon for next order"
3. `web` · screens · "thank you page after purchase with promo code and copy button"
4. `ios` · screens · "voucher card with discount code, copy code button and expiry date"
5. `web` · screens · "guest checkout order confirmation page prompting to create account to save order"

**Fuente:** Mobbin MCP

## Referencias

| # | App | Patrón observado | Link | Alimenta |
|---|---|---|---|---|
| 1 | adidas (iOS) | Voucher como tarjeta grande: valor (15%) y código único en la tarjeta. Debajo, una fila con Tipo, Vencimiento y Valor. Acción "Copiar código" a todo el ancho y aviso "copiado" con el código. | https://mobbin.com/screens/bc3534ff-50e7-4945-a684-7eca87f52f97 | v1 |
| 2 | SHEIN (iOS) | Cupón con forma de ticket: el monto del descuento en grande a la izquierda y las condiciones y el vencimiento a la derecha. Abajo, una franja "Ingresa el código en el checkout" con botón Copy y un toast "Copied coupon code…". | https://mobbin.com/screens/9456204e-10bb-4c64-aa0b-b102ff5f9f4e | v1 |
| 3 | Squarespace (web) | TYP de una columna centrada. Bajo "Thank you for your purchase", la oferta para la próxima acción va antes del resumen de pago y el resumen queda debajo. | https://mobbin.com/screens/5ba32e11-9c1a-490b-bb62-2e4fbf93b2c1 | v1 |
| 4 | Shop (web) | TYP de checkout en dos columnas: a la izquierda la confirmación con un bloque "obtén S/ off en tu próximo pedido" (enlace en un campo de solo lectura y acciones para compartir) y a la derecha el resumen del pedido persistente. | https://mobbin.com/screens/557a8608-5950-4147-98fe-2d8ff68ee2fa | v2 |
| 5 | Typeform (web) | Confirmación a la izquierda (titular, "tu recibo va a tu correo", desglose) y una tarjeta lateral a la derecha con su propia acción. Es la jerarquía principal más lateral. | https://mobbin.com/screens/79f7d7bd-72d2-44fa-a407-d89f1db4176b | v2 |
| 6 | Adobe (web) | Banner de éxito a todo el ancho, una tarjeta principal con la siguiente acción ("Create my password") y una columna lateral con el correo de confirmación, el n.º de pedido y el método de pago, que sirven de datos de consulta. | https://mobbin.com/screens/9b8bc8b0-e5da-4daf-bf22-0e00f943e140 | v2 |
| 7 | talabat (iOS) | Confirmación con seguimiento del pedido arriba. Debajo, una tarjeta "You've earned 39 points! Redeem them… on your next order" con enlace "View my rewards", integrada en el estado del pedido. | https://mobbin.com/screens/81773dd9-acfd-4b8c-a5d8-2b19beff92f4 | v3 |
| 8 | Keeta (iOS) | Detalle del pedido entregado con un banner de descuento grande ("40 off, redeemable across next 2 orders") entre el resumen del pedido y la ayuda. | https://mobbin.com/screens/1465658f-007d-4f75-a2f7-d47981b27c4e | v3 |
| 9 | MasterClass (web) | "Your order is complete" con "Your receipt has been emailed to you" y, en la misma tarjeta, la creación de la cuenta del cliente que compró sin sesión (nombre + contraseña). | https://mobbin.com/screens/b3454660-3f22-43c2-acfa-c707d20fdaca | v3 |

## Patrones elegidos
- **v1 · Cupón héroe (ticket primero, pedido después):** adidas, SHEIN y Squarespace ponen la recompensa como primer bloque después del "gracias", con valor, código, vencimiento y "Copiar" juntos. La confirmación del pedido pasa a segundo plano. Hipótesis: si el cupón es lo primero que se ve y copiar es la acción dominante, sube el # de copias (secundaria) y, por arrastre, el canje. Riesgo: le quita protagonismo a la confirmación del pedido.
  - DS: `Header` (Desktop/Mobile), `Button` (Offset Red Large para "Copiar código", única primaria; Link Blue para "Ver mi pedido"), `Alert` Inline Success con ícono y texto para "Código copiado", `Accordion` para condiciones de uso.
  - **Gap:** no existe un componente Cupón/Ticket (valor + código + vencimiento + copiar). Tampoco existe el feedback de "copiado" tipo toast: se resuelve con `Alert` Inline.

- **v2 · Confirmación + panel lateral del cupón (split persistente):** Shop, Typeform y Adobe mantienen la confirmación y los datos del pedido como contenido principal, y la oferta para la próxima compra vive en un panel lateral con su propia acción. Reutiliza el layout del patrón Ecommerce (panel "Tu pedido" a la derecha). Hipótesis: el cliente confirma primero que su compra salió bien (reduce ansiedad) y el cupón ocupa el lugar que ya asocia con su pedido. Así gana credibilidad y se ve sin scroll en 1440. En 390 el panel se apila arriba de los detalles.
  - DS: `Header`, `Alert` Boxed Success ("Pedido confirmado", con ícono y texto), `Cart Item` (solo lectura, sin `Quantity`), `Button` (una Offset Red en el panel y Outlined Blue o Link para las secundarias), `Alert` Inline Success para "copiado".
  - **Gap:** `Cart Summary` incluye la acción Checkout y no hay un resumen de pedido de solo lectura para la TYP. Tampoco existen el bloque Cupón ni un campo de código copiable: `Input` deshabilitado sería un uso forzado (su USAR es capturar texto).

- **v3 · Recompensa ganada dentro del estado del pedido + "guárdalo" para no logueados:** talabat y Keeta integran la recompensa en el estado o resumen del pedido como algo "ganado", con condiciones de la próxima compra. MasterClass usa la misma confirmación para vincular la compra a una cuenta. Hipótesis: el canje cae porque el cliente olvida o pierde el cupón. Si el cupón se presenta como ganado con este pedido y se muestra explícitamente dónde queda guardado (correo, n.º de pedido, crear cuenta en un paso), sube el canje del mes, sobre todo en no logueados. Cubre el criterio "el no logueado ve dónde y cómo recuperar su cupón".
  - DS: `Header`, `Alert` Boxed Success, `Input` + `Password Strength` + `Button` Offset Red para "Crear cuenta y guardar cupón" (única primaria, solo para no logueados; en logueados la primaria cambia), `Button` Outlined Blue "Copiar código", `Accordion` para "¿Cómo uso mi cupón?".
  - **Gap:** no hay stepper ni seguimiento del estado del pedido (talabat lo usa como ancla). Tampoco existe el bloque Cupón. La variante logueado/no logueado del mismo bloque no está documentada en el DS.

## Descartados
- Campo "Ingresa tu código promocional" en el checkout (Tripadvisor, DoorDash, Uber Eats, Givingli, HelloFresh, Upwork) · motivo: es el canje, no la entrega del cupón. No responde la pregunta de la TYP.
- Recompensa en puntos sin código (sweetgreen, Chipotle, CHOPT, Everyday Rewards, 7-Eleven) · motivo: no hay código para copiar (criterio de aceptación) y supone un programa de lealtad con cuenta, lo que excluye a los no logueados.
- Cupón u oferta en modal sobre la TYP (Surfshark, Zara, Polywork) · motivo: según `Modal` NO USAR, un mensaje que no requiere respuesta va en `Alert`. Además, tapa la confirmación del pedido.
- Billetera o listado de cupones (Keeta Vouchers, foodpanda, Gojek, Agoda) · motivo: corresponde a una página "Mis cupones", no a la TYP. Fuera de alcance.
- Referidos "invita y gana" (Yami, Instacart, Skip) · motivo: es otro tipo de cupón, fuera de alcance de S01 (ver S02).

## Gaps
Lo que ninguna referencia resuelve y queda como oportunidad:
- **Estado sin cupón (< S/ 80.00):** ninguna referencia muestra la TYP cuando el pedido no califica. Falta decidir si se muestra el monto que faltó ("te faltaron S/ 12.50") o nada. El criterio de aceptación exige que no aparezca el cupón.
- **Recuperación para no logueados sin crear cuenta:** las referencias (MasterClass, Adobe) piden crear cuenta. Ninguna muestra recuperar el cupón solo con correo + n.º de pedido, que es lo que permite el brief.
- **Cupón personalizado con nombre del cliente:** ninguna referencia muestra el código explícitamente asociado a la persona ("Válido solo para Andrea · andrea@…"). Es una oportunidad para dar credibilidad y evitar que el código se comparta.
- **Gaps del DS (a registrar en `solicitudes-ds.md` en la fase de diseño):** componente Cupón/Ticket con acción de copiar; feedback de "copiado" (toast); resumen de pedido de solo lectura para la TYP; stepper de estado del pedido; layout Mobile 390 de la TYP (no existe en Figma, revisión humana).
