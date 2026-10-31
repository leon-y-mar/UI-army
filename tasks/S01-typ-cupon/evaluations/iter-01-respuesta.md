# Respuesta del designer · S01-typ-cupon · iteración 01 → 02

| Versión | Decisión | Por qué |
|---|---|---|
| v1 | refinar | 3.85, ya sobre el umbral y sin faltas bloqueantes; los problemas son de casos borde y áreas táctiles, no del patrón. |
| v2 | refinar | 3.30, a 0.20 del umbral; la caída viene de un bug de layout (Plataforma = 1), no de la hipótesis. |
| v3 | refinar | 3.35, a 0.15 del umbral; los problemas (Accordion, primaria bajo el fold en 390) se corrigen sin cambiar el patrón. |

No hay faltas bloqueantes del DS en iter-01. En esta iteración el lint marcó un detach en v2 (`.state > .ds-button`); lo corregí antes de entregar usando el modificador `ds-button--block`.

## Cambios que aplican a las 3 versiones
- **Áreas táctiles (Link Small de 25 px):** cada Button Link va dentro de un envoltorio de layout `<a class="tap">` con `min-height: var(--size-touch-min)`. La instancia `ds-button` no cambia. Con el render, ningún link, botón ni summary del diseño mide menos de 44 px en 390. Lo registré como gap en `solicitudes-ds.md`, porque Link no tiene alto mínimo y Small mide 40 px en Sizing Web.
- **`cargando`:** ahora dice "Si cierras esta página no lo pierdes: también te llega a andrea.rojas@gmail.com".
- **Nuevo estado `error-cupon`** (`?estado=error-cupon` y un chip en los controles): un Alert Boxed Error dice qué pasó (no se pudo crear), qué no se pierde (el pedido sigue confirmado y el cupón llega al correo apenas esté listo) y qué hacer (Reintentar). Reintentar pasa por `cargando` y luego muestra el cupón.
- **`sin-cupon`:** las 3 versiones explican que el pedido no generó cupón y que se gana en compras de más de S/ 80.00. Uso "más de", como dice el brief ("supera").
- **Botón ☰ del Header Mobile (28×32):** quedó registrado en `solicitudes-ds.md`, como sugirió el evaluador. No lo toqué porque es la instancia del DS.
- **Revisión humana nueva:** hay que confirmar con negocio si el umbral de S/ 80.00 se mide sobre el subtotal o sobre el total con delivery. Por eso no muestro "te faltaron S/ X": sería inventar la regla.

## v1 · Top 3
1. **Link Small < 44 px en 390.** Resuelto con el envoltorio `.tap` en "Crear cuenta y guardar el cupón", "Ver mis cupones" y "Volver al menú".
2. **`sin-cupon` no explica el umbral.** Resuelto: se agregó el bloque "Tu próximo pedido puede tener descuento", con ícono info y texto, en el lugar del cupón.
3. **`cargando` sin salida.** Resuelto con el texto del correo y el estado `error-cupon`. En ese estado "Reintentar" es la única Offset roja.

También corregí:
- El Alert de confirmación pasa de **Banner a Boxed**, porque está dentro del contenido.
- "Crear cuenta y guardar el cupón" ahora explica qué gana el cliente: queda en Mis cupones, se aplica solo al pagar y recibe un aviso antes de que venza.

No atendí el largo de página en 390 (2296 px), que salió en la evidencia y no en el Top 3. Es el trade-off declarado de la hipótesis: el cupón primero y el pedido después. El total sigue en el mismo bloque del pedido.

## v2 · Top 3
1. **Layout roto en 390 · `sin-cupon`.** Resuelto de raíz: eliminé las reglas `.layout:has(> .panel[hidden])`. El panel ya no se oculta, sino que cambia de contenido, así que el grid es el mismo en todos los estados. En 390, `scrollWidth` es 390 en los 6 estados.
2. **Tercio vacío en 1440 · `sin-cupon`.** Resuelto con el mismo cambio: en `sin-cupon` el panel derecho muestra "Gana un cupón de descuento" con el umbral de S/ 80.00.
3. **Link Small < 44 px y `sin-cupon` sin umbral.** Resuelto con `.tap` y con el contenido nuevo del panel.

Además, para separar la hipótesis de v2 de la de v1 (la divergencia está en 4 porque se parecen), la confirmación de v2 ahora incluye el total pagado ("Pagaste S/ 96.40 con Visa terminada en 4821") antes del cupón. En 390 el orden es confirmar → pagar → cupón. En v1 es gracias → cupón → pedido.

## v3 · Top 3
1. **Primaria bajo el fold en 390 (y=1184).** Resuelto: ahora está en y=769–822, dentro de 844. Para lograrlo:
   - En 390 el stepper se resume en una línea con texto ("En cocina ahora · llega 8:15 – 8:35 PM").
   - La tarjeta de estado pierde su relleno en 390.
   - El título del bloque se acorta a "Guarda tu cupón".
   - La explicación queda en una sola frase.
   - "Si no creas cuenta, lo recuperas así" pasa a ir debajo del botón.
   - Password Strength aparece cuando la persona escribe. Los requisitos siguen visibles en el helper, como pide su USAR.
2. **Detalle del pedido en un Accordion (contenido esencial).** Resuelto: el detalle sale del Accordion y queda visible con el total pagado (S/ 96.40 / S/ 67.50) en la columna derecha en 1440 y debajo del formulario en 390. El Accordion queda solo para contenido de apoyo (uso, condiciones, cómo gano un cupón, ayuda) y siempre con 2 o más ítems en cada estado, para no dejar un ítem aislado.
3. **"Copiar código" en Outlined para el invitado y fricción de la contraseña.** **Estoy de acuerdo en parte.**
   - Atendí la fricción y el "qué gana": el texto junto al campo dice que el cupón ya va al correo y que con una cuenta además se aplica solo al pagar y llega un aviso 3 días antes de que venza. El campo dice para qué correo es la contraseña, así que no hay que escribir nada más. Tras copiar, el Alert de éxito del invitado sugiere guardarlo abajo.
   - **No subo "Copiar código" a primaria para el invitado.** Si lo hago, v3 pasa a tener la misma jerarquía que v1 (copiar como siguiente paso) y se pierde la hipótesis que la distingue: que el canje cae por olvido y no por falta de copia. El Outlined Large está junto al código, mide lo mismo que una primaria y pasa a Offset en `logueado`. El costo para la métrica secundaria queda declarado en `trade-off`.

También corregí que "Llega entre…" ahora va debajo del título, alineado a la izquierda, y no a la derecha. "Ver mis cupones" usa `.tap`. Quité el teléfono de ayuda que había puesto en iter-01 porque no tenía fuente.

Una nota sobre `solicitudes-ds.md`: la línea "Resumen de pedido de solo lectura" de iter-01 todavía menciona "lista dentro de un Accordion (v3)". No edito líneas existentes; en v3 el resumen ahora es una lista visible con filas de totales.

## Verificación propia (no es un puntaje)
- Lint: 0 bloqueantes en v1, v2 y v3. Las advertencias son los breakpoints `@media` y el aviso de "dos Offset rojos en el archivo", que nunca conviven en la misma vista (uno por estado).
- Render en 1440×900 y 390×844 en 6 estados (por defecto, `invitado`, `logueado`, `sin-cupon`, `cargando`, `error-cupon`): sin scroll horizontal ni errores de JS, y como máximo una Offset roja visible por estado.
