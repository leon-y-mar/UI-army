# Patterns · Cómo se combinan los componentes

Fuente: páginas **Patterns · Ecommerce / Reservas / Toma de pedido** de Figma.
Cada producto tiene una pantalla Light y una Dark idénticas en estructura:
el modo Dark solo cambia el modo de la colección Color en el contenedor.

Usa estos patrones como **línea base** del producto. Las 3 versiones de una tarea
pueden romper el patrón si la hipótesis lo justifica, pero deben declararlo.

---

## Ecommerce · Menú (Desktop 1440)
Frame `Ecommerce / Menú / Light` · Modo Color Light/Dark · Sizing Web.

```
┌───────────────────────────────── Header (Desktop) ──────────────────────────────────┐
│ Logo  Menu  Locations  Rewards  Reservations                       Account  Cart(●) │
├──────────────────────────────────────────────┬──────────────────────────────────────┤
│ NUESTRO MENÚ (h1)                            │ TU PEDIDO (h6)                       │
│ [Chip●][Chip][Chip][Chip][Chip]              │ Cart Item (img · nombre · mods ·     │
│ ┌Product┐ ┌Product┐                          │            Quantity · precio)        │
│ │ Card  │ │ Card  │   × 3 filas              │ Cart Item                            │
│ └───────┘ └───────┘                          │ Cart Summary (subtotal, delivery,    │
│                                              │   total, CHECKOUT offset rojo lg)    │
└──────────────────────────────────────────────┴──────────────────────────────────────┘
```

| Componente | Variante | Cantidad |
|---|---|---|
| Header | Breakpoint=Desktop | 1 |
| Chip | Selected=True / False | 1 / 4 |
| Product Card | — (botón Offset Red Small) | 6 |
| Cart Item (+ Quantity) | — | 2 |
| Cart Summary (+ Button Offset Red Large) | — | 1 |
| Badge/Cart count | — | 1 |

**Reglas que muestra el patrón**
- Una sola acción primaria grande en la vista: Checkout. Los "Add" de las tarjetas son Small.
- Categorías con Chip, selección única.
- El carrito vive en un panel lateral persistente en desktop.

**Observaciones del patrón (a validar con el humano, no copiar)**
- Copy mixto: navegación y tarjetas en inglés ("Menu", "Add", descripción), títulos en español.
- La grilla de Product Cards no tiene separación vertical entre filas (las tarjetas se tocan).
- **No existe la versión Mobile 390** del menú. Si la tarea es ecommerce, la versión mobile
  es una propuesta nueva compuesta con componentes existentes y Header Mobile.

---

## Reservas · Tablet vertical (820 × 1180)
Frame `Reservas / Tablet vertical / Light` · Modo Color Light/Dark · **Sizing Tablet**.

```
┌──────────────────────────────┐
│ Logo                         │   ← sin Header: solo el logo
│ NUEVA RESERVA (h2)           │
│ FECHA (label)                │
│ [LUN 12][MAR 13]…[DOM 17 ✕]  │   Date Cell × 6 (1 selected, 1 disabled)
│ HORA                         │
│ [6:00][6:30][7:00][7:30●]…   │   Time Slot × 8 (1 selected, 1 disabled), wrap
│ PERSONAS                     │
│ ( −  👥 4  + )               │   Party Size
│ ┌ TU RESERVA ──────────────┐ │
│ │ Fecha · Hora · Personas ·│ │   Reservation Summary
│ │ Local                    │ │
│ │ [CONFIRMAR RESERVA]      │ │   única acción primaria
│ └──────────────────────────┘ │
└──────────────────────────────┘
```

**Reglas que muestra el patrón**
- Flujo de una sola columna en orden fijo: Fecha → Hora → Personas → Resumen.
- Días y horas no disponibles se muestran deshabilitados, no se ocultan.
- Una sola acción primaria al final, dentro del resumen.
- Títulos de sección con label en mayúsculas.

---

## Toma de pedido · Tablet horizontal (1180 × 820)
Frame `Toma de pedido / Tablet horizontal / Light` · Modo Color Light/Dark · **Sizing Tablet**.

```
┌───────────────────────────────────────────┬──────────────────────────────┐
│ MESAS (h3)                                │ PEDIDO · MESA 12             │
│ [Todas●][Salón][Terraza][Barra]           │ Order Item (nombre, Quantity,│
│ [Mesa 1 ][Mesa 2 ][Mesa 3 ]               │   precio, + Extra queso,     │
│ [Libre  ][Ocupada][Reserv.]               │   − Sin cebolla)             │
│ [Mesa 4 ][Mesa 5 ][Mesa 6 ]   Table Card  │ Order Item                   │
│ [Mesa 7 ][Mesa 8 ]                        │ Order Item                   │
├───────────────────────────────────────────┴──────────────────────────────┤
│ TOTAL S/ 87.80                         [CUENTA]  [ENVIAR A COCINA]       │  Action Bar fija
└──────────────────────────────────────────────────────────────────────────┘
```

| Componente | Variante | Cantidad |
|---|---|---|
| Chip | Selected=True / False | 1 / 3 |
| Table Card | Free 3 · Occupied 2 · Reserved 2 · Bill 1 | 8 |
| Order Item (+ Quantity) | — | 3 |
| Action Bar | Button Outlined Red Large + Offset Red Large | 1 |

**Reglas que muestra el patrón**
- Sin Header. Dos paneles: plano de mesas y pedido de la mesa activa.
- Estado de mesa siempre con color **y** etiqueta.
- Modificadores con prefijo + / −.
- Acción secundaria Outlined junto a la primaria Offset, ambas en la Action Bar.

---

## Lo que esto significa para el designer
1. Empieza cada versión desde el patrón del producto y cambia solo lo que tu hipótesis necesita.
2. Si tu versión saca el carrito del panel lateral o reordena el flujo de Reservas, dilo en `hipotesis:`.
3. Respeta: una acción primaria por vista, estados con texto, Sizing Tablet en productos de mozos.
