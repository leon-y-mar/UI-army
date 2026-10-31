# Evaluación · S01-typ-cupon · iteración 01

MODO: con render
Rúbrica: v1.1 · Producto: ecommerce · Viewports: 1440×900, 390×844 · Tema: light

Estados renderizados por versión y viewport: por defecto (= invitado), `?estado=invitado`, `logueado`, `sin-cupon` y `cargando`. Además se probó "Copiar código" (portapapeles) y "Simular error al copiar", y la navegación con Tab para revisar el foco.
Capturas de estados: `evaluations/shots/iter-01-<v>-<ancho>-light-<estado>.png`.

## Lint
```
## tasks/S01-typ-cupon/prototypes/v1.html · bloqueantes: 0 · otras: 1
- [ADVERTENCIA] px-sin-token: 1023px, 599px

## tasks/S01-typ-cupon/prototypes/v2.html · bloqueantes: 0 · otras: 1
- [ADVERTENCIA] px-sin-token: 1023px, 599px

## tasks/S01-typ-cupon/prototypes/v3.html · bloqueantes: 0 · otras: 1
- [ADVERTENCIA] px-sin-token: 1023px, 599px
```
Las advertencias son los breakpoints de `@media` (copiados de tokens.css; `var()` no funciona en media queries). Las acepto.

Salida de `node scripts/render.js S01-typ-cupon 1 ecommerce light`:
```
iter-01-v1-1440-light.png ok
iter-01-v1-390-light.png ok
iter-01-v2-1440-light.png ok
iter-01-v2-390-light.png ok
iter-01-v3-1440-light.png ok
iter-01-v3-390-light.png ok
```
El script solo renderiza el estado por defecto. El fallo de layout de v2 en 390 aparece únicamente con `estado=sin-cupon`, así que el script no lo marca (ver evidencia de v2).

## Puntajes

| Criterio | Peso | v1 | v2 | v3 |
|---|---|---|---|---|
| Ataca la métrica | 30% | 4 | 4 | 3 |
| Criterios de aceptación | 25% | 4 | 3 | 4 |
| Consistencia DS | 20% | 4 | 4 | 3 |
| Plataforma | 15% | 3 | 1 | 3 |
| Divergencia (set) | 10% | 4 | 4 | 4 |
| **Ponderado** | | **3.85** | **3.30** | **3.35** |
| **Faltas bloqueantes** | | 0 | 0 | 0 |
| **¿Pasa umbral?** | | Sí | No | No |

Verificaciones transversales (las 3 versiones, todos los estados):
- Una sola acción primaria (Offset rojo) visible por vista: sí. En `cargando` v1 y v2 no muestran ninguna; v3 mantiene "Crear cuenta y guardar cupón".
- Estados solo con color: no se encontraron. Los Alerts llevan ícono y texto, y los pasos del pedido de v3 dicen "Listo / Ahora / Pendiente".
- Foco visible: el contorno de 2px aparece en todos los botones, links y summary con Tab. En el Input de v3 el foco lo da el estilo del DS (`outline: none` con borde de foco del componente).
- Copiar: en las 3 el portapapeles recibe `ANDREA-7KQ2`. El botón cambia a "Código copiado" con ícono y un Alert de éxito. Con error, sale un Alert de error y el código queda seleccionado.
- Moneda: `S/ 15.00`, `S/ 96.40` y `S/ 50.00` con el formato correcto. Copy en español de Perú, fechas «Lun 30 · Nov».

## Evidencia

### v1 · Cupón héroe en una columna
- **Métrica:** el cupón es el primer bloque tras "¡Gracias, Andrea!": valor S/ 15.00, código, vencimiento, titular y "Copiar código" como única primaria (1440: y=389; 390: y=593). La hipótesis de copiar como siguiente paso está bien ejecutada. Sin resolver:
  - `sin-cupon` (1440 y 390): la TYP solo omite el cupón y no explica por qué no hay ni desde qué monto se gana. El benchmark ya lo marcaba como gap, y es lo que podría empujar a la recompra.
  - `cargando`: el texto es "Estamos creando tu cupón… no cierres esta página", pero no hay estado de fallo ni se dice que el cupón también llegará al correo si cierra.
- **Criterios:** se cumplen los 5.
  1. El código, el descuento y el vencimiento se ven sin scroll en 1440 (vencimiento en y≈367) y en 390 (vencimiento en y≈547).
  2. El cupón es visible después del checkout.
  3. Se puede copiar (verificado en el portapapeles).
  4. En `sin-cupon` no hay cupón.
  5. El invitado ve "¿Dónde encuentro mi cupón después?" con correo y Seguir mi pedido (n.º + correo).
  Débil: "Crear cuenta y guardar el cupón" es un Link sin destino ni explicación de qué pasa. Queda en 4.
- **DS:** sin overrides de `ds-*` y sin bloqueantes. Usos discutibles:
  - El Alert **Banner** se usa para la confirmación del pedido dentro de la columna. Banner es "para avisos globales"; Boxed encaja mejor dentro del contenido.
  - Cart Item se usa sin Quantity como resumen de solo lectura. El gap está registrado en solicitudes-ds.md.
  Rompe el patrón del panel lateral y lo declara en `patron-base`. Queda en 4.
- **Plataforma:** no hay scroll horizontal ni solapes en ninguno de los 5 estados. Fricciones:
  - En 390, los Link Blue Small "Crear cuenta y guardar el cupón" (291×25) y "Volver al menú" (133×25) miden menos de `--size-touch-min` (44).
  - En 390, la página del invitado mide 2123 px. El detalle del pedido y el total pagado quedan a más de 2 pantallas de distancia.
  Queda en 3.

### v2 · Confirmación + panel lateral del cupón
- **Métrica:** en 1440 el panel derecho muestra el cupón completo, "Copiar código" (y=474) y "Cómo recuperarlo después", al lado del detalle del pedido. Toda la TYP cabe casi en un viewport. En 390 el panel se apila después de la confirmación y "Copiar código" queda en y=716, dentro del fold. Hipótesis ejecutada. Sin resolver, igual que v1: `sin-cupon` no dice por qué no hay cupón y `cargando` no tiene caso de fallo.
- **Criterios:**
  - 1, 2, 3 y 5 se cumplen (vencimiento en 390 en y≈638).
  - El 4 se cumple de forma literal, pero en 390 el estado `sin-cupon` está roto (ver Plataforma). La pantalla que verifica el criterio no se lee bien. Queda en 3.
- **DS:** es igual que v1 en la composición del cupón y en Cart Item de solo lectura (gaps registrados). Alert Boxed Success para la confirmación es correcto. El panel reutiliza el layout del patrón Ecommerce y lo declara. Queda en 4.
- **Plataforma:**
  - **390 · `estado=sin-cupon`:** el grid mantiene 2 columnas (`228px 114px`) aunque el `aside.panel` está oculto. Las causas:
    - La regla `.layout:has(> .panel[hidden])` (línea 42) tiene más especificidad que la media query `max-width: 1023px` (línea 69) y la pisa.
    - El contenido queda en 239 px de ancho dentro de 358 disponibles.
    Efectos:
    - El texto del Alert "Pedido confirmado y pagado… andrea.rojas@gmail.com" se sale del borde del Alert.
    - Los nombres de producto se parten en 3 líneas ("Oldtimer / con / queso").
    - `scrollWidth` 262 > 239 en `.confirm` y 267 > 239 en `.details`.
    Es texto que desborda su contenedor en un viewport del producto, así que queda en 1.
  - **1440 · `sin-cupon`:** la columna principal no se expande. Queda a la izquierda con un tercio vacío a la derecha. No se rompe, pero se ve desbalanceado.
  - Los Link Small de 25 px de alto ("Crear cuenta y guardarlo", "Volver al menú", "Ver mis cupones") miden menos de 44 en 390.

### v3 · Cupón ganado en la tarjeta de estado + crear cuenta
- **Métrica:** el cupón está en la franja de la tarjeta de estado y el invitado tiene como primaria "Crear cuenta y guardar cupón", con una contraseña. Obstáculos que anulan en parte la hipótesis anti-olvido:
  - (a) En 390 la primaria que ejecuta la hipótesis queda en y=1184 en un viewport de 844. El invitado ve el cupón y el Outlined "Copiar código", pero no el paso de guardar ni el campo de contraseña.
  - (b) "Copiar código" baja a Outlined para el invitado. La métrica secundaria (# que copia) pierde peso justo en el segmento con más riesgo de perder el código.
  - (c) Para guardar hay que crear una contraseña en la TYP. Es fricción en el momento de menor intención, y nada muestra cuánto gana el cliente frente a lo que ya recibe por correo.
  `sin-cupon` sí explica "En pedidos desde S/ 80.00 te regalamos un descuento…", y es la única versión que lo hace.
- **Criterios:** se cumplen los 5.
  1. El código, el descuento y el vencimiento se ven sin scroll en 1440 (franja en y≈280–340) y en 390 (vencimiento en y≈587).
  2. El cupón es visible después del checkout.
  3. Se puede copiar.
  4. En `sin-cupon` no hay cupón.
  5. "Que no se te pierda tu cupón" muestra correo, Seguir mi pedido y cuenta.
  Queda en 4.
- **DS:**
  - El **Detalle del pedido va dentro de un Accordion**. Accordion NO USAR: "Contenido esencial para completar una tarea". En una TYP, ver qué se compró y el total pagado es contenido esencial: el total S/ 96.40 no se ve en ningún viewport sin expandir.
  - El stepper de estado está compuesto, con el gap registrado. Password Strength se usa según su USAR.
  - El badge del Input dice "Obligatorio" con `ds-field__required` (traducción válida).
  Queda en 3 por el Accordion.
- **Plataforma:** no hay scroll horizontal ni solapes en ningún estado. Fricciones:
  - En 390 la primaria del invitado está bajo el fold (y=1184) sin indicio de que haya más contenido.
  - En `logueado`, el Link Small "Ver mis cupones" mide 139×25.
  - En 1440, "Llega entre 8:15 y 8:35 PM" queda alineado a la derecha y desconectado del título.
  Queda en 3.

### Divergencia (set) = 4
Hay 3 estructuras distintas (columna única con cupón héroe, split con panel lateral, tarjeta de estado con formulario y acordeones) y 3 hipótesis con referencias propias. Pero las hipótesis de v1 y v2 son parecidas: en ambas el cupón se ve primero y la primaria es copiar. En 390 casi convergen en el mismo orden: confirmación → gracias → cupón → recuperar → detalle → acciones.

## Top 3 problemas por versión
**v1**
1. En 390, "Crear cuenta y guardar el cupón" y "Volver al menú" son Link Small de 25 px de alto, menos que `--size-touch-min` (44).
2. En `sin-cupon` (1440 y 390) la TYP no explica por qué no hay cupón ni desde qué monto se gana. Pierde el incentivo de recompra en el caso que no califica.
3. El estado `cargando` no tiene salida si el cupón no se genera, y no dice que también llegará al correo. El usuario que cierra la página no sabe si lo perdió.

**v2**
1. En 390 con `estado=sin-cupon` el layout se rompe: el grid queda en 2 columnas (228/114 px) con el panel oculto, el texto del Alert de confirmación se sale de su borde y los nombres de producto se parten en 3 líneas. Causa: `.layout:has(> .panel[hidden])` le gana a la media query.
2. En 1440 con `sin-cupon` la columna principal no ocupa el espacio del panel ausente y deja un tercio vacío a la derecha.
3. Los Link Small ("Crear cuenta y guardarlo", "Volver al menú", "Ver mis cupones") miden 25 px de alto en 390, menos de 44. Además, `sin-cupon` no explica el umbral de S/ 80.00.

**v3**
1. En 390 la acción primaria del invitado ("Crear cuenta y guardar cupón", y=1184) queda bajo el fold de 844, y el mecanismo de la hipótesis no se ve en la vista inicial.
2. El detalle del pedido y el total pagado están dentro de un Accordion cerrado, contra su NO USAR (contenido esencial). En ningún viewport se ve el total S/ 96.40 sin expandir.
3. Para el invitado, "Copiar código" pasa a Outlined y guardar exige crear una contraseña en la TYP. Baja el peso de la métrica secundaria y suma fricción sin mostrar qué gana el cliente frente al correo.

## Learnings violados
- Ninguno (`memory/learnings.md` no tiene reglas activas).

## Revisión humana
- Layout Mobile 390 del ecommerce: no existe en Figma (v1, v2, v3).
- Uso de Dirk en el valor del cupón: `ds-price` + `ds-h1` en v1, `ds-h2` en v2 y `ds-h4` en v3.
- Imágenes placeholder en Cart Item (v1, v2; en v3 dentro del Accordion).
- Íconos faltantes (copiar, correo, pasos del pedido) resueltos con texto y placeholders (v1, v2, v3).
- Fuera del alcance del designer: el botón ☰ del Header Mobile del DS mide 28×32, menos de 44, en las 3 versiones. No se penaliza; es candidato a `solicitudes-ds.md`.
