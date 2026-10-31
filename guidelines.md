# Guidelines para agentes · Chili's DS

Fuente: páginas **Agent Guidelines**, **Documentation** y **QA & Changelog** del archivo de Figma (v1.2.0).
Lo que está entre comillas « » es la regla original; lo demás es su traducción a HTML/CSS.

## Alcance
Tres productos, mercado Perú (es-PE, soles S/):

| Producto | Usuario | Plataforma | Viewports |
|---|---|---|---|
| Ecommerce | Clientes | Web responsive | Desktop 1440 · Mobile 390 |
| Reservas | Mozos | Tablet vertical | 820 × 1180 |
| Toma de pedido | Mozos | Tablet horizontal | 1180 × 820 |

Reservas y Toma de pedido usan `data-device="tablet"` (Sizing Tablet: touch 48, inputs 56).

## Cómo usar un componente
«Insertar siempre una instancia del componente publicado. Cambiar contenido solo con las propiedades del componente y las variantes.»
- En HTML: usa la clase de `components.css` con sus modificadores. Eso es la instancia.
- Cambia solo contenido (texto, ícono, cantidad) y variantes (`--offset`, `--red`, `aria-pressed`…).
- **No sobrescribas** estilos de una clase `ds-*` en el prototipo. Hacerlo es un detach.

## Cómo usar tokens y modos
«Enlazar fills, strokes, padding, gap y radios a variables, nunca a valores sueltos. Usar solo tokens semánticos.»
- Todo color, espaciado, radio, borde y tamaño en CSS propio usa `var(--…)`.
- Solo `--color-bg-*`, `--color-text-*`, `--color-border-*`, `--color-icon-*`, `--button-*`.
- «Para Dark aplicar el modo Dark de la colección Color al contenedor; no duplicar componentes por tema.» → `data-theme="dark"` en `<html>` o en el contenedor.
- «En tablet aplicar el modo Tablet de la colección Sizing.» → `data-device="tablet"`.

## Permitido
- «Componer pantallas con auto layout usando instancias.» → flex/grid con gaps `--sp-*`.
- «Cambiar textos y propiedades.»
- «Usar los botones con su combinación Style/Color/Size/State.»
- «Moneda en soles con el formato "S/ 39.90".» Espacio después de S/, punto decimal, dos decimales, precios con `.ds-price` (Dirk).

## Prohibido
- «Desvincular (detach) instancias.»
- «Colores o tamaños sin variable.» Ningún hex, rgb o px de color/tamaño fuera de tokens.
- «Usar tokens primitivos directamente en pantallas.» Nada de `--prim-*`.
- «Crear versiones Light/Dark duplicadas de un componente.»
- «Usar los tokens con prefijo ext/ como si fueran parte de la guía de marca.»
- «Comunicar estados solo con color.» Siempre ícono y/o texto.
- Más de una acción primaria (Button Offset rojo) por vista.
- Outlined o Link en Ranch o Yellow: no existen.

## Cuando ningún componente encaja
«No inventar variantes ni estilos. Componer con los componentes existentes y documentar la necesidad en QA & Changelog.»
→ Registra la necesidad en `design-system/solicitudes-ds.md`. El humano la lleva a Figma.

## Decisiones que requieren revisión humana
«Modo oscuro completo, contraste del borde por defecto, uso de Dirk (licencia), reemplazo de imágenes placeholder, íconos faltantes de la guía y cualquier desviación de la guía de marca.»
→ Si una propuesta toca alguna, decláralo en el comentario `revision-humana:` del prototipo.

## Accesibilidad
«Objetivo WCAG 2.1 AA: texto 4.5:1 (3:1 para texto grande), componentes de interfaz 3:1, objetivos táctiles de tablet de al menos 48 px (size/touch-min), foco visible con borde de 2px.»
- Objetivo táctil: `--size-touch-min` (44 Web / 48 Tablet).
- El borde Warning (ámbar) es decorativo (1.94:1): el estado lo comunican ícono y texto.

## Voz y copy
- Español de Perú. Montos en soles. Fechas como en los patrones: «Vie 15 · Nov», «7:30 PM».
- Labels, botones y títulos Dirk en mayúsculas los aplica el estilo; escribe el texto en tipo oración.
- Errores: qué pasó y qué hacer.
- Los patrones de Ecommerce tienen copy en inglés («Add», «Menu», «Locations»). No lo copies: usa español salvo que el brief diga lo contrario.

## Desviaciones documentadas de la guía de marca (no corregir)
1. Botón rojo usa rojo AA.
2. Placeholder usa gris 6.
3. Segmented seleccionado: azul noche sobre amarillo accent.
4. En Light, borde por defecto en ext/gray-6 y texto de marca en alert/error, por contraste.
5. Seleccionados de Chip, Date Cell, Time Slot y Table Card · Bill usan bg/inverse.

## Limitaciones conocidas
- Íconos: 49 de ~90 de la guía. Imágenes de producto y modales son placeholders.
- No existe la variante mobile de las pantallas de Ecommerce (solo Header Mobile).
- Elevación y motion son extensiones.
