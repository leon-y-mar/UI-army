# Componentes · Chili's DS

26 componentes publicados en Figma (v1.2.0) y su equivalente en `components.css`.
Las reglas USAR / NO USAR son textuales de la descripción del componente en Figma.

**Regla:** si necesitas algo que no está aquí, no lo inventes. Compón con lo que existe
y registra la necesidad en `solicitudes-ds.md`.

Leyenda de fidelidad: ✅ leído de Figma · ⚠️ con partes `[aprox]` en el CSS.

---

## Botones

### Button ✅
**Props:** Style `Offset | Flat | Outlined | Link` · Color `Red | Blue | Ranch | Yellow` · Size `Large (24/16) | Small (16/12)` · State `Default | Hover | Disabled` (Pressed = Hover). Íconos opcionales de 24px. Label en mayúsculas (Buttons/button-label).
**USAR:** Acción principal de cada pantalla: Offset rojo (Agregar, Checkout, Confirmar reserva, Enviar a cocina). Una sola por vista. Acción secundaria junto a una primaria: Outlined (p. ej. Cuenta junto a Enviar a cocina).
**NO USAR:** Dos botones Offset rojos en la misma vista. Outlined o Link en Ranch/Yellow: solo existen en Red y Blue.
```html
<button class="ds-button ds-button--offset ds-button--red ds-button--lg">Checkout</button>
<button class="ds-button ds-button--outlined ds-button--red ds-button--lg">Cuenta</button>
<button class="ds-button ds-button--link ds-button--blue ds-button--sm">Ver detalle</button>
```
Tokens: `button/{color}/{bg|text|stroke|shadow|bg-hover|text-hover}`, `button/outlined-*`, `button/link-*`, `button/disabled/*`. Offset = sombra sólida −4,4.

---

## Forms

### Input ⚠️
**Props:** State `Rest | Focused | Typing | Filled | Disabled` · Destructive `No | Yes` (borde 2px + helper en error). Etiqueta en mayúsculas con badge REQUIRED opcional.
**USAR:** Capturar texto corto: nombre, correo, teléfono, dirección, notas del pedido. Cuando la persona escribe un valor libre que no está en una lista cerrada.
**NO USAR:** Códigos de 6 dígitos: usa OTP Input. Elegir de una lista cerrada: usa Dropdown, Radio o Segmented.
```html
<div class="ds-field">
  <div class="ds-field__label-row"><label class="ds-field__label" for="tel">Teléfono</label><span class="ds-field__required">Required</span></div>
  <input id="tel" class="ds-field__control" placeholder="999 999 999">
  <span class="ds-field__helper">Te avisaremos cuando tu pedido salga</span>
</div>
```
Destructive: agrega `ds-field--destructive` y un mensaje en el helper (no solo color).

### Dropdown ⚠️ · Dropdown Option ⚠️
**Props:** State `Rest | Expanded | Selected | Disabled` · Destructive. Opción: `Default | Hover | Selected`.
**USAR:** Listas de 4 a ~12 opciones sin búsqueda: local, método de pago, tipo de documento. Cuando el espacio no permite mostrar todas las opciones a la vez.
**NO USAR:** 2–3 opciones que caben visibles: usa Radio o Segmented. Listas muy largas que necesitan búsqueda: usa Input con sugerencias.
```html
<div class="ds-field"><label class="ds-field__label" for="local">Local</label>
  <div class="ds-field__select"><select id="local" class="ds-field__control"><option>Chili's Larcomar</option></select></div></div>
```

### OTP Input ⚠️
**Props:** State `Rest | Focused | Filled | Disabled` · Destructive. Celda enlazada a `size/input-height`.
**USAR:** Verificar teléfono o correo con un código numérico de 6 dígitos: registro, recuperar contraseña, confirmar reserva. Con mensaje de error claro cuando el código es incorrecto.
**NO USAR:** Texto libre: usa Input. Códigos de longitud distinta a 6 sin ajustar el componente.
```html
<div class="ds-field"><label class="ds-field__label">Código de verificación</label>
  <div class="ds-otp"><input class="ds-otp__cell" maxlength="1" inputmode="numeric"> …×6</div>
  <span class="ds-field__helper">Ingresa el código de 6 dígitos</span></div>
```

### Password Strength ⚠️
**Props:** Level `None | Weak | Medium | Strong`. Barra segmentada + ícono + texto.
**USAR:** Debajo del Input de contraseña al crear o cambiar una contraseña. Con la sugerencia de requisitos visible.
**NO USAR:** Al iniciar sesión. Como único mecanismo de validación.
```html
<div class="ds-password-strength" data-level="medium">
  <div class="ds-password-strength__bar"><span></span><span></span><span></span></div>
  <span class="ds-password-strength__hint"><span class="ds-icon ds-icon--xs" data-icon="warning" aria-hidden="true"></span> Media · …</span></div>
```

### Checkbox ⚠️ · Radio ⚠️ · Toggle ⚠️
**Props:** Checkbox/Radio: Selected · Disabled. Toggle: On · Disabled.
**Checkbox USAR:** Elegir cero, una o varias opciones: extras de un plato, aceptar términos, recordarme. Cuando el cambio se confirma después con un botón. **NO USAR:** Elegir exactamente una opción: usa Radio. Ajustes que se aplican al instante: usa Toggle.
**Radio USAR:** Elegir exactamente una opción de un grupo corto (2–5) con todas visibles: tipo de pedido, método de pago. Siempre en grupo, con una opción preseleccionada cuando hay un valor razonable por defecto. **NO USAR:** Varias opciones a la vez: usa Checkbox. Listas largas: usa Dropdown.
**Toggle USAR:** Ajustes que se aplican de inmediato: notificaciones, recordar tarjeta. Etiqueta que describe el estado encendido. **NO USAR:** Cambios que requieren pulsar Guardar o Enviar: usa Checkbox. Más de dos opciones: usa Radio o Segmented.
```html
<label class="ds-check"><input type="checkbox"> Extra queso</label>
<label class="ds-check"><input type="radio" name="pago" checked> Tarjeta</label>
<label class="ds-check"><input type="checkbox" role="switch"> Recibir promociones</label>
```

### Segmented Item ⚠️
**Props:** Selected · Position `Start | Middle | End`. Seleccionado: azul noche sobre amarillo accent.
**USAR:** Alternar entre 2–4 vistas o modos excluyentes del mismo contenido: Delivery / Recojo / En local. Cuando el cambio actualiza el contenido de inmediato.
**NO USAR:** Filtros o categorías con muchas opciones: usa Chip. Selección dentro de un formulario con envío: usa Radio.
```html
<div class="ds-segmented" role="group" aria-label="Tipo de pedido">
  <button class="ds-segmented__item" aria-pressed="true">Delivery</button><button class="ds-segmented__item" aria-pressed="false">Recojo</button></div>
```

### Arrow Button ⚠️
**Props:** Direction `Left | Right` · State `Default | Hover`. 48px.
**USAR:** Navegar entre elementos secuenciales: carrusel de promociones, pasos, semana anterior/siguiente. Siempre en par.
**NO USAR:** Acción principal: usa Button. Abrir o cerrar contenido: usa los caret del Accordion.
```html
<button class="ds-arrow-button" aria-label="Semana anterior"><span class="ds-icon" data-icon="arrow-outline-l" aria-hidden="true"></span></button>
```

---

## Feedback

### Alert ⚠️
**Props:** Type `Success | Warning | Error | Loading` · Style `Inline | Boxed | Banner`.
**USAR:** Confirmar, avisar, informar un error o un proceso en curso. Inline junto a un campo, Boxed dentro del contenido, Banner para avisos globales. Mensajes que dicen qué pasó y qué hacer.
**NO USAR:** Decisiones que interrumpen el flujo: usa Modal. Mensajes decorativos o promocionales sin estado.
```html
<div class="ds-alert ds-alert--boxed ds-alert--error" role="alert">
  <span class="ds-icon" data-icon="error" aria-hidden="true"></span>No pudimos procesar el pago. Revisa los datos de tu tarjeta.</div>
```
Nota: solo existe `bg/error-subtle`; Success/Warning/Loading boxed usan `bg/surface` `[aprox]`.

### Modal ✅
**Props:** Layout `Image Left | Image Right | Image Top | No Image`. Imagen placeholder.
**USAR:** Una decisión o mensaje que interrumpe y requiere respuesta: invitación a Rewards, confirmación, aviso importante. Una acción primaria y una secundaria opcional.
**NO USAR:** Mensajes que no requieren respuesta: usa Alert. Formularios largos: usa una página.
```html
<div class="ds-scrim"><div class="ds-modal" role="dialog" aria-labelledby="mt">
  <div class="ds-modal__image"></div>
  <div class="ds-modal__content"><h2 id="mt" class="ds-modal__title">Únete a Rewards</h2><p class="ds-modal__body">…</p>
    <div class="ds-modal__actions"><button class="ds-button ds-button--offset ds-button--red ds-button--sm">Unirme</button><button class="ds-button ds-button--link ds-button--blue ds-button--sm">Ahora no</button></div></div>
  <button class="ds-modal__close" aria-label="Cerrar">×</button></div></div>
```

---

## Navigation

### Accordion Item ⚠️
**Props:** Theme `Navy | Ranch` · Open.
**USAR:** Preguntas frecuentes y contenido de apoyo que no todos necesitan leer: políticas, alérgenos, términos. Apilado; cada ítem abre y cierra de forma independiente.
**NO USAR:** Contenido esencial para completar una tarea. Un solo ítem aislado.
```html
<div class="ds-accordion"><details class="ds-accordion__item ds-accordion__item--ranch"><summary>¿Tienen opciones sin gluten?</summary><div class="ds-accordion__body">…</div></details></div>
```

---

## Ecommerce

### Header ⚠️ (Mobile)
**Props:** Breakpoint `Desktop (1440) | Mobile (390)`.
**USAR:** Una vez en la parte superior de cada página del ecommerce. Desktop con navegación visible; Mobile con menú.
**NO USAR:** Pantallas de tablet del mozo: Reservas solo muestra el logo y Toma de pedido no lleva encabezado. Más de un Header por página.
```html
<header class="ds-header"><span class="ds-logo">Chili's</span>
  <nav class="ds-header__nav"><a href="#">Menú</a><a href="#">Locales</a><a href="#">Rewards</a><a href="#">Reservas</a></nav>
  <span class="ds-header__spacer"></span>
  <div class="ds-header__actions"><button class="ds-header__menu" aria-label="Menú">☰</button><span class="ds-icon ds-icon--md" data-icon="account" aria-label="Cuenta"></span><span class="ds-icon ds-icon--md" data-icon="cart" aria-label="Carrito"></span></div></header>
```

### Chip ✅
**Props:** Selected (fondo inverse).
**USAR:** Filtrar o cambiar de categoría en una lista: categorías del menú, filtros de zona (Todas, Salón, Terraza, Barra). Una fila de 3–8 chips con selección única.
**NO USAR:** Alternar 2–4 modos de un mismo control: usa Segmented. Elegir dentro de un formulario: usa Radio o Dropdown.
```html
<div class="ds-chip-row" role="tablist"><button class="ds-chip" aria-pressed="true">Hamburguesas</button><button class="ds-chip" aria-pressed="false">Fajitas</button></div>
```

### Quantity ✅
**USAR:** Cambiar la cantidad de un producto dentro de Cart Item y Order Item. Con min definido según el contexto (0 elimina la línea).
**NO USAR:** Número de comensales: usa Party Size. Cantidades grandes que requieren teclear: usa Input.
```html
<div class="ds-quantity"><button class="ds-quantity__btn" data-glyph="−" aria-label="Quitar uno"></button><span class="ds-quantity__value">1</span><button class="ds-quantity__btn ds-quantity__btn--increase" data-glyph="+" aria-label="Agregar uno"></button></div>
```
Nota: en Figma los botones miden 32px; en CSS el área táctil se amplía a `--size-touch-min`.

### Product Card ✅
**USAR:** Grilla del menú del ecommerce: una tarjeta = un producto con acción rápida de agregar. Precio en soles con formato S/ 39.90 en Dirk.
**NO USAR:** Más de un botón primario por tarjeta. Productos que requieren personalizar sin pasar al detalle.
```html
<article class="ds-product-card"><div class="ds-product-card__image" role="img" aria-label="…"></div>
  <div class="ds-product-card__body"><h3 class="ds-product-card__name">Original Big Mouth Burgers</h3><p class="ds-product-card__desc">…</p>
    <div class="ds-product-card__footer"><span class="ds-price ds-price--sm">S/ 39.90</span><button class="ds-button ds-button--offset ds-button--red ds-button--sm">Agregar</button></div></div></article>
```
Nota: la tarjeta tiene botón Offset rojo Small. En la grilla del menú hay varias, pero la acción primaria de la vista sigue siendo Checkout (Large).

### Cart Item ✅
**USAR:** Panel Tu pedido del ecommerce, apiladas antes del Cart Summary. Con imagen, nombre, modificadores, cantidad y precio.
**NO USAR:** Pedido del mozo en tablet: usa Order Item. Listados del menú: usa Product Card.

### Cart Summary ✅
**USAR:** Al final del panel Tu pedido, debajo de los Cart Items. Contiene la única acción primaria (Checkout).
**NO USAR:** Más de una acción primaria. Resúmenes de reserva: usa Reservation Summary.

---

## Reservas

### Date Cell ✅
**Props:** State `Default | Selected | Disabled`.
**USAR:** Paso Fecha de una reserva: fila de 5–7 días con selección única. Días sin disponibilidad deshabilitados, no ocultos.
**NO USAR:** Calendarios completos de mes: requieren otro componente. Selección múltiple.
```html
<button class="ds-date-cell" aria-pressed="true"><span class="ds-date-cell__day">Vie</span><span class="ds-date-cell__num">15</span></button>
```

### Time Slot ✅
**Props:** State `Default | Selected | Disabled`.
**USAR:** Paso Hora de una reserva, bajo las Date Cells; selección única. Horas completas deshabilitadas.
**NO USAR:** Elegir fechas: usa Date Cell. Rangos de horas libres: usa Input o Dropdown.

### Party Size ✅
**USAR:** Paso Personas de una reserva, después de Fecha y Hora. Con min y max según el aforo. Objetivos táctiles de 48px.
**NO USAR:** Cantidad de producto: usa Quantity. Grupos grandes sin canal de contacto alterno.

### Reservation Summary ✅
**USAR:** Al final del flujo de Reservas (tablet) con Fecha, Hora, Personas y Local. Contiene la única acción primaria: Confirmar reserva.
**NO USAR:** Resumen de pedido o carrito: usa Cart Summary. Más de una acción primaria.

---

## Toma de pedido

### Table Card ✅
**Props:** Status `Free | Occupied | Reserved | Bill` → etiquetas Libre, Ocupada, Reservada, Cuenta.
**USAR:** Plano de mesas de la Toma de pedido (tablet horizontal), con filtros en Chips. Estado siempre con color y etiqueta.
**NO USAR:** Comunicar el estado solo con color. Uso en el ecommerce.
```html
<button class="ds-table-card ds-table-card--occupied"><span class="ds-table-card__caption">Mesa</span><span class="ds-table-card__number">2</span><span class="ds-table-card__meta">4</span><span class="ds-table-card__status">Ocupada</span></button>
```

### Order Item ✅
**USAR:** Panel Pedido · Mesa N en la Toma de pedido (tablet). Modificadores con prefijo + (añadido) o − (quitado).
**NO USAR:** Carrito del cliente con imagen: usa Cart Item. Comunicar añadidos o quitados solo con color.

### Action Bar ✅
**USAR:** Pie de la Toma de pedido (tablet horizontal), siempre visible. Total + acción secundaria (Cuenta) + acción primaria (Enviar a cocina).
**NO USAR:** Más de una acción primaria. Ecommerce: usa Cart Summary.

---

## Assets
- **Logo/Chilis** → placeholder `.ds-logo`.
- **Icon/*** (121 assets en Figma: íconos, Payment/*, Illustration/*, Animation/*, FAQ/*, Badge/Cart count) → placeholder `.ds-icon data-icon="<nombre>"`. Usa el nombre real del ícono de Figma, por ejemplo `cart`, `calendar`, `clock`, `users`, `location`, `delivery`, `pickup`, `dine-in`, `send`, `table`.
