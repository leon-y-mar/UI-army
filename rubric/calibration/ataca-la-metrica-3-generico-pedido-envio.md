# Ataca la métrica = 3

> ⚠️ **CASO GENÉRICO.** Escrito por el agente a pedido del humano para arrancar
> el piloto. No es trabajo real ni criterio humano: reemplázalo por un caso
> real en cuanto exista (ver `README.md`).

## Tarea
Toma de pedido · Revisar el pedido antes de enviarlo a cocina · Métrica: pedidos corregidos después de enviados a cocina

## Qué se entregó
Tablet horizontal 1180 × 820. Hipótesis: si el mozo relee el pedido antes de
enviarlo, bajan las correcciones. "Enviar a cocina" de la Action Bar abre un
Modal con la lista de Order Items y los modificadores + / −, y un botón
"Confirmar envío". Hasta ahí, ejecutado. El obstáculo: en el Modal, los
modificadores se muestran en una línea truncada ("+ Extra queso, − Sin ceb…")
y no se puede editar una cantidad sin cerrar el Modal y volver al panel.

## Por qué es 3
"La hipótesis se ejecuta, pero hay un obstáculo evidente en el flujo que la
anula parcialmente." El paso de revisión existe, pero lo que más se corrige
(los modificadores) es justo lo que el Modal trunca, y corregir obliga a
salir del paso de revisión.

## Por qué no es 4
Un 4 exige que la hipótesis funcione en el caso principal y que solo quede
un borde sin resolver. Aquí el caso principal (detectar un modificador
equivocado) falla. Para subir: modificadores completos sin truncar y una
forma de corregir desde la revisión, o que la revisión ocurra en el mismo
panel de Pedido sin Modal.

Puntuado por: Nova (agente, caso genérico) · Fecha: 2026-10-31
