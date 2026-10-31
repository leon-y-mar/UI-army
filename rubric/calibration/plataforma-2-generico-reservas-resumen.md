# Plataforma = 2

> ⚠️ **CASO GENÉRICO.** Escrito por el agente a pedido del humano para arrancar
> el piloto. No es trabajo real ni criterio humano: reemplázalo por un caso
> real en cuanto exista (ver `README.md`).

## Tarea
Reservas · Nuevo flujo de reserva en tablet · Métrica: reservas confirmadas por mozo / turno

## Qué se entregó
Tablet vertical 820 × 1180. La propuesta cambia el patrón: muestra un
calendario de 3 semanas armado con Date Cells en 3 filas de 7, luego
16 Time Slots en 4 filas y Party Size. El Reservation Summary con
"Confirmar reserva" queda debajo, en y ≈ 1400 px. No hay scroll horizontal
ni solapes, pero en 820 × 1180 el mozo no ve la acción primaria ni el resumen
sin hacer scroll, y nada indica que hay más contenido abajo.

## Por qué es 2
"No se rompe, pero pierde la acción principal o la jerarquía en algún
viewport." El layout aguanta (no es 1), pero en el único viewport del
producto la acción primaria queda fuera de la vista inicial y el resumen,
que es lo que el mozo confirma con el cliente, no se lee junto a la selección.

## Por qué no es 3
Para ser 3 la acción principal tiene que estar presente; solo se aceptan
fricciones menores (un objetivo táctil chico, foco poco visible). Aquí el
problema es estructural: el calendario de 3 semanas desplaza el resumen. El
patrón de Reservas usa una fila de 5–7 Date Cells justamente para que el flujo
quepa en 1180 px de alto.

Puntuado por: Nova (agente, caso genérico) · Fecha: 2026-10-31
