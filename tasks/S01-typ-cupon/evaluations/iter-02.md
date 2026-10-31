# Evaluación · S01-typ-cupon · iteración 02

MODO: con render
Rúbrica: v1.1 · Producto: ecommerce · Viewports: 1440×900, 390×844 · Tema: light

Estados renderizados por versión y viewport: por defecto (= invitado), `?estado=invitado`, `logueado`, `sin-cupon`, `cargando` y `error-cupon` (36 capturas). También se probó:
- "Copiar código" con el portapapeles real: las 3 copian `ANDREA-7KQ2`.
- La navegación con Tab para revisar el foco.
- El error de contraseña en v3.

Para cada captura se midieron:
- `scrollWidth`
- la posición del código, del vencimiento y de "Copiar código"
- los Offset rojos visibles
- los objetivos interactivos de menos de 44 px

Capturas de estados: `evaluations/shots/iter-02-<v>-<ancho>-light-<estado>.png`.

## Lint
```
## tasks/S01-typ-cupon/prototypes/v1.html · bloqueantes: 0 · otras: 2
- [ADVERTENCIA] px-sin-token: 1023px, 599px
- [REVISAR] una-primaria: 2 botones Offset rojo Large en el archivo; confirmar que no conviven en la misma vista

## tasks/S01-typ-cupon/prototypes/v2.html · bloqueantes: 0 · otras: 2
- [ADVERTENCIA] px-sin-token: 1023px, 599px
- [REVISAR] una-primaria: 2 botones Offset rojo Large en el archivo; confirmar que no conviven en la misma vista

## tasks/S01-typ-cupon/prototypes/v3.html · bloqueantes: 0 · otras: 1
- [ADVERTENCIA] px-sin-token: 1023px, 599px
```
- `px-sin-token`: son los breakpoints de `@media`. `var()` no funciona ahí. Se aceptan.
- `[REVISAR] una-primaria` (v1, v2): verificado en el render. "Copiar código" y "Reintentar" nunca conviven: dependen de `data-show` distintos. "Seguir mi pedido" se vuelve Offset solo en `sin-cupon`, y en ese estado no hay cupón. En los 6 estados y los 2 viewports hay como máximo 1 Offset rojo visible. En `cargando` de v1 y v2 no hay ninguno.

Salida de `node scripts/render.js S01-typ-cupon 2 ecommerce light`:
```
iter-02-v1-1440-light.png ok
iter-02-v1-390-light.png ok
iter-02-v2-1440-light.png ok
iter-02-v2-390-light.png ok
iter-02-v3-1440-light.png ok
iter-02-v3-390-light.png ok
```
El render por estados tampoco dio scroll horizontal (`scrollWidth` = ancho del viewport en las 36 capturas), elementos fuera del viewport ni errores de JS.

## Puntajes

| Criterio | Peso | v1 | v2 | v3 |
|---|---|---|---|---|
| Ataca la métrica | 30% | 4 | 4 | 4 |
| Criterios de aceptación | 25% | 4 | 4 | 3 |
| Consistencia DS | 20% | 4 | 4 | 4 |
| Plataforma | 15% | 3 | 3 | 4 |
| Divergencia (set) | 10% | 4 | 4 | 4 |
| **Ponderado** | | **3.85** | **3.85** | **3.75** |
| **Faltas bloqueantes** | | 0 | 0 | 0 |
| **¿Pasa umbral?** | | Sí | Sí | Sí |

Verificaciones transversales (las 3 versiones, todos los estados):
- **Una sola primaria por vista:** se cumple (ver Lint).
- **Estados solo con color:** no hay.
  - Los Alerts llevan ícono y texto.
  - El stepper de v3 dice "Listo / Ahora / Pendiente", y en 390 "En cocina ahora".
  - El error de contraseña de v3 cambia el helper ("La contraseña es muy corta o no tiene números…").
  - Password Strength lleva texto.
- **Objetivos táctiles:** dentro del diseño no hay ningún objetivo de menos de 44 px en 390.
  - Los Link envueltos en `.tap` miden 44 de alto: "Crear cuenta y guardar el cupón" 291×44, "Volver al menú" 133×44 y "Ver mis cupones".
  - El Input de v3 mide 48.
  - La única excepción es el ☰ del Header Mobile del DS (28×32), registrado en `solicitudes-ds.md`. No se penaliza.
- **Foco:** se recorrió con Tab. Botones, `.tap`, summary y ☰ muestran el contorno sólido de 2 px. El Input de v3 lleva `outline: none` y el borde de foco del componente.
- **Copiar:** las 3 escriben `ANDREA-7KQ2` en el portapapeles. El botón cambia a "Código copiado" y aparece un Alert de éxito con ícono.
- **Moneda y fechas:** `S/ 15.00`, `S/ 96.40`, `S/ 67.50`, `S/ 80.00` con el formato correcto. Fechas «Lun 30 · Nov» y «Sáb 31 · Oct». Copy en español de Perú.

## Evidencia

### v1 · Cupón héroe en una columna
- **Métrica:** el cupón es el primer bloque después de "¡Gracias, Andrea!". En 1440 se ven el valor S/ 15.00 en Dirk h1, el código en y=295, el vencimiento en y=358 y "Copiar código" como única Offset en y=389–442. En 390 el código está en y=475, el vencimiento en y=538 y Copiar en y=593–646. Se resolvieron los casos que faltaban en iter-01:
  - `sin-cupon`: "Tu próximo pedido puede tener descuento" explica el umbral de S/ 80.00.
  - `cargando`: dice que el cupón también llega al correo.
  - `error-cupon`: dice qué pasó, qué no se pierde y ofrece Reintentar.

  Queda un caso relevante sin resolver:
  - En `error-cupon`, el bloque "¿Dónde encuentro mi cupón después?" sigue ofreciendo "Crear cuenta y guardar el cupón" para un cupón que todavía no existe.
  - Los estados `cargando` y `error-cupon` solo están pensados para el invitado. No hay versión con sesión ("ya está en tu cuenta"). Reintentar siempre vuelve a `invitado`.
- **Criterios:** se cumplen los 5 con claridad.
  1. El cupón se ve sin scroll en los dos viewports (coordenadas arriba).
  2. El cupón es visible después del checkout.
  3. Copiar funciona (verificado).
  4. En `sin-cupon` no hay cupón.
  5. El invitado ve correo, Seguir mi pedido (botón presente) y cuenta.

  No llega a 5 porque el criterio 4 dice "< S/ 80.00" y la regla del umbral (subtotal o total, y qué pasa con S/ 80.00 exactos) sigue abierta. La declara revisión humana y no se puede verificar sin explicación. Además, "Crear cuenta y guardar el cupón" apunta a `#` y no muestra qué pasa después del toque.
- **DS:**
  - El Alert de confirmación ya es Boxed.
  - Cart Item de solo lectura y cupón compuesto: gaps registrados.
  - Rompe el patrón con una sola columna y lo declara en `patron-base`.
  - Usos discutibles: en el valor del cupón se apilan dos clases del DS (`ds-price ds-h1`). Para que los Link midan 44 px, la instancia `ds-button` pasa a ser un `<span>` dentro de un `<a class="tap">`: el envoltorio es el elemento interactivo y el componente queda como decoración. El gap está registrado.

  Queda en 4.
- **Plataforma:** no hay scroll horizontal ni solapes en los 6 estados, y los objetivos táctiles son correctos. Fricciones:
  - **390 · `sin-cupon`:** la única primaria, "Seguir mi pedido" (Offset rojo), queda en y=1077–1130, bajo el fold de 844, después de todo el detalle del pedido. En la vista inicial solo se ven la confirmación y la explicación del umbral, sin acción. Es una CTA bajo el fold sin razón.
  - **390 · invitado:** la página mide 2296 px. "Total pagado S/ 96.40" está en y≈1770, a más de 2 pantallas. Es un trade-off declarado, pero la columna de 390 es la de 1440 apilada y no una lectura pensada para el celular.

  Queda en 3.

### v2 · Confirmación + panel lateral del cupón
- **Métrica:**
  - En 1440 el panel sticky de la derecha muestra el valor en y=190, el código en y=330, el vencimiento en y=383 y "Copiar código" en y=474–527, al lado de "Pagaste S/ 96.40 con Visa terminada en 4821".
  - En 390 el orden es confirmación → pago → cupón. Copiar queda en y=742–795, dentro del fold de 844 con unos 45 px de margen.
  - Se resolvieron `sin-cupon` (el panel explica el umbral, sin tercio vacío), `cargando` y `error-cupon` (Reintentar como única Offset).

  Sin resolver, igual que v1: en `error-cupon` "Crear cuenta y guardarlo" se ofrece para un cupón que no existe, y no hay estados de sesión para `cargando` ni `error-cupon`. Copy confuso en `sin-cupon`: "Lo verás en esta pantalla apenas pagues". Se lee como si se refiriera al pago que acaba de hacer, no a un pedido futuro de más de S/ 80.00.
- **Criterios:** se cumplen los 5 con claridad.
  1. El cupón se ve sin scroll: en 390 el vencimiento está en y=655.
  2. El cupón es visible después del checkout.
  3. Copiar funciona.
  4. En `sin-cupon` no hay cupón.
  5. "Cómo recuperarlo después" muestra correo, Seguir mi pedido y cuenta.

  Igual que en v1, la regla del umbral de S/ 80.00 no se puede verificar sin explicación. Queda en 4.
- **DS:**
  - Alert Boxed Success es correcto.
  - El panel reutiliza el layout del patrón Ecommerce y lo declara.
  - Mismos gaps registrados y mismo recurso `.tap` + `span.ds-button` que v1.
  - Se quitó la regla `:has()` que rompía el grid.

  Queda en 4.
- **Plataforma:** el fallo de iter-01 está resuelto. En `sin-cupon` 390 el `scrollWidth` es 390, el grid tiene una columna y no hay texto desbordado. Fricciones:
  - **390 · `sin-cupon`:** la primaria "Seguir mi pedido" (Offset rojo) queda en y=1314–1367, más de 1.5 pantallas bajo el fold. En la vista inicial no hay ninguna acción.
  - **1440 · `sin-cupon`:** el panel derecho mide unos 250 px de alto y deja la columna derecha vacía desde y≈355 hasta el final. No se rompe, pero el panel pesa poco.
  - **390 · invitado:** la página mide 2361 px y el detalle del pedido empieza en y≈1215. Para el invitado, el bloque "Cómo recuperarlo" y los 2 acordeones quedan dentro del panel, antes del pedido.

  Queda en 3.

### v3 · Cupón ganado en la tarjeta de estado + crear cuenta
- **Métrica:**
  - **390:** la primaria del invitado, "Crear cuenta y guardar cupón", ahora está en y=769–822, dentro de 844. En iter-01 estaba en y=1184.
  - **1440:** está en y=659.
  - **Detalle:** el pedido sale del Accordion y el total S/ 96.40 se ve en la columna derecha en 1440.
  - **Qué gana el invitado:** "Ya va a tu correo. Con una cuenta, además, se aplica solo al pagar y te avisamos 3 días antes de que venza."
  - **Tras copiar:** el Alert empuja a guardar el cupón.

  La hipótesis anti-olvido queda ejecutada en su caso principal. Sin resolver:
  - **(a) `error-cupon`:** la primaria sigue siendo "Crear cuenta y guardar cupón" (y=697 en 390), aunque el Alert de arriba dice que no se pudo crear el cupón. Reintentar baja a Outlined. La acción principal promete guardar algo que no existe.
  - **(b) Fold en 390:** el formulario de cuenta no tiene aceptación de términos ni de política de datos personales. Si se agrega el Checkbox que normalmente exige crear una cuenta, la primaria (borde inferior en y≈826 con la sombra) sale del fold de 844.
  - **(c) Copiar en invitado:** "Copiar código" sigue en Outlined para el invitado. Es un trade-off declarado y argumentado; no se penaliza más que en (a) y (b).
- **Criterios:**
  - 1, 2, 3 y 4 se cumplen. En 1440 el código está en y=334 y el vencimiento en y=315. En 390 el código está en y=315 y el vencimiento en y=378.
  - El 5 está resuelto de forma débil. El texto "Si no creas cuenta, lo recuperas así" remite a "En Seguir mi pedido: con tu n.º CH-284715 y tu correo", pero v3 no tiene ningún botón ni link a Seguir mi pedido:
    - no hay acciones al pie;
    - el Header solo tiene Menú, Locales, Rewards y Reservas;
    - "¿Necesitas ayuda?" también manda a "Seguir mi pedido" sin enlace.

    El cliente lee el "dónde", pero no tiene cómo llegar. v1 y v2 sí tienen el botón "Seguir mi pedido". No lo detecté en iter-01: el problema ya existía.

  Queda en 3.
- **DS:**
  - Se corrigió el Accordion: el detalle es visible y los acordeones son de apoyo, siempre 2 o más ítems.
  - Password Strength se usa según su USAR: aparece al escribir y los requisitos quedan visibles en el helper.
  - Input destructive lleva mensaje.
  - El stepper está compuesto y el gap está registrado.

  Usos discutibles:
  - "Copiar código" usa Outlined Blue sin estar junto a la primaria. El USAR de Outlined es "acción secundaria junto a una primaria", y aquí el botón está en otra sección.
  - La línea de `solicitudes-ds.md` "Resumen de pedido de solo lectura" sigue diciendo "lista dentro de un Accordion (v3)", pero ahora es una lista visible. El gap está registrado, pero describe una solución que ya no existe. El designer lo reconoce en su respuesta.

  Queda en 4.
- **Plataforma:** no hay scroll horizontal ni solapes en los 6 estados. Los objetivos táctiles son correctos (Input 48, botones 53). En 390 el stepper se resume en una línea con texto, la tarjeta de estado pierde el relleno y la primaria queda sobre el fold en `invitado` (y=769), `cargando` (y=632), `error-cupon` (y=697) y `sin-cupon` (y=556). Es el único set de 390 recompuesto para el celular y no solo apilado. Fricciones:
  - **1440 · `logueado`:** la columna izquierda termina en "Ver mis cupones" (y≈610). Queda un hueco de unos 280 px frente a la columna del detalle.
  - **1440:** el valor "S/ 15.00" en `ds-h4` (119×25) es más chico que el código (`ds-h4` en bloque blanco). El descuento compite con el código en la franja.
  - **390:** el margen de la primaria contra el fold es de unos 20 px (ver Métrica b).

  Queda en 4.

### Divergencia (set) = 4
Hay 3 estructuras distintas: columna única con cupón héroe, split con panel lateral sticky, y tarjeta de estado con formulario de cuenta. Las 3 tienen referencias propias. v2 se separó de v1 al confirmar primero ("Pagaste S/ 96.40…") y no cambió la primaria. Aun así, las hipótesis de v1 y v2 siguen siendo parecidas:
- La primaria es "Copiar código" (Offset).
- El cupón está sobre el fold.
- El bloque de recuperación es el mismo.

En 390 las dos se leen casi igual: alert → gracias → cupón con Copiar → recuperar → acordeones → pedido.

## Top 3 problemas por versión
**v1**
1. **390 · `sin-cupon`:** la única primaria, "Seguir mi pedido" (Offset rojo), queda en y=1077, bajo el fold de 844, detrás de todo el detalle del pedido. La vista inicial no tiene ninguna acción.
2. **`error-cupon`:** el bloque de recuperación ofrece "Crear cuenta y guardar el cupón" para un cupón que no se creó. Los estados `cargando` y `error-cupon` solo existen para el invitado, y Reintentar siempre vuelve a `invitado`.
3. **390 · invitado:** la página mide 2296 px y "Total pagado S/ 96.40" está en y≈1770. Es la columna de 1440 apilada, sin decisiones propias para el celular. "Crear cuenta y guardar el cupón" apunta a `#` y no muestra el paso siguiente.

**v2**
1. **390 · `sin-cupon`:** la primaria "Seguir mi pedido" (Offset rojo) queda en y=1314. Son más de 1.5 pantallas bajo el fold, y la vista inicial no tiene ninguna acción.
2. **`error-cupon`:** se ofrece "Crear cuenta y guardarlo" para un cupón que no existe, y no hay estados de sesión para `cargando` ni `error-cupon`. En `sin-cupon`, "Lo verás en esta pantalla apenas pagues" se puede leer como si hablara del pago que el cliente acaba de hacer.
3. **1440 · `sin-cupon`:** el panel derecho mide unos 250 px y deja vacía la columna derecha desde y≈355. En 390 el detalle del pedido empieza en y≈1215, después del panel con recuperación y acordeones.

**v3**
1. **Criterio 5 resuelto débilmente:** "Si no creas cuenta, lo recuperas así" y "¿Necesitas ayuda?" mandan a "Seguir mi pedido", pero en v3 no hay botón ni link a Seguir mi pedido. El invitado lee dónde recuperar el cupón, pero no puede llegar.
2. **`error-cupon`:** la primaria sigue siendo "Crear cuenta y guardar cupón" (y=697 en 390), justo debajo de un Alert que dice que el cupón no se pudo crear. Reintentar queda en Outlined. La acción principal promete algo que no existe en ese estado.
3. **Formulario de cuenta:** no tiene aceptación de términos ni de política de datos personales. Si se agrega el Checkbox que exige crear una cuenta, la primaria en 390 (borde inferior en y≈826 con la sombra) sale del fold de 844 y vuelve el problema de iter-01.

## Learnings violados
- Ninguno (`memory/learnings.md` no tiene reglas activas).

## Revisión humana
- Umbral "más de S/ 80.00": no está definido si es sobre el subtotal o sobre el total con delivery, ni qué pasa con S/ 80.00 exactos. Lo declaran v1, v2 y v3. Afecta la verificación del criterio 4.
- Aviso "3 días antes de que venza" (v3): hay que confirmarlo con negocio.
- Layout Mobile 390 del ecommerce: no existe en Figma (v1, v2, v3).
- Uso de Dirk en el valor del cupón: `ds-price` + `ds-h1` en v1, `ds-h2` en v2 y `ds-h4` en v3.
- Imágenes placeholder en Cart Item (v1, v2).
- Íconos faltantes (copiar, correo, pasos del pedido) resueltos con texto y placeholders (v1, v2, v3).
- Fuera de lo que el designer puede corregir: el botón ☰ del Header Mobile (28×32) ya está registrado en `solicitudes-ds.md`.
- Consentimiento de datos al crear cuenta (v3): no lo cubren ni el brief ni el DS. Lo debe decidir el humano o legal, porque afecta el fold de 390.
