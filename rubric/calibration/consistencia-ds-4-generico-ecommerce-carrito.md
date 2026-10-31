# Consistencia con el DS = 4

> ⚠️ **CASO GENÉRICO.** Escrito por el agente a pedido del humano para arrancar
> el piloto. No es trabajo real ni criterio humano: reemplázalo por un caso
> real en cuanto exista (ver `README.md`).

## Tarea
Ecommerce · Cupón de descuento en el carrito · Métrica: tasa de uso de cupones en checkout

## Qué se entregó
Desktop 1440 y mobile 390. Carrito lateral con Cart Items y Quantity, un
Input "Código de cupón" con botón Outlined Red y el Cart Summary con
"Checkout" como única acción primaria. Lint sin bloqueantes. El estado de
cupón aplicado usa un Alert de éxito con ícono y texto. Faltaba una línea de
descuento dentro del Cart Summary: se compuso con texto y `.ds-price`, y se
registró en `solicitudes-ds.md`. En mobile, el cupón se movió arriba de los
Cart Items, antes del resumen, sin explicarlo en el comentario `patron-base`.

## Por qué es 4
"Componentes y variantes correctos; gaps registrados en `solicitudes-ds.md`."
Todos los componentes se usan según su USAR, hay una sola acción primaria y
el gap del descuento se declaró en lugar de inventar un estilo.

## Por qué no es 5
Un 5 exige que la composición respete el patrón del producto o justifique
romperlo. En mobile el orden del panel cambia (cupón antes de los productos)
y `patron-base` dice "sin cambios". Con una línea que justifique el cambio, o
manteniendo el orden del patrón, sería 5.

Puntuado por: Nova (agente, caso genérico) · Fecha: 2026-10-31
