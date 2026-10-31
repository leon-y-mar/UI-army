# Calibración

Estos archivos enseñan al evaluator **tu** criterio. Sin ellos, puntúa
con criterio genérico y el delta con tu puntaje será alto.

## Qué escribir
Mínimo 3 ejemplos antes de la primera tarea. Idealmente:
- 1 caso con puntaje bajo (1–2)
- 1 caso medio (3)
- 1 caso alto (4–5)

Usa trabajo real: tareas pasadas tuyas o del equipo, o benchmarks
que ya evaluaste. No inventes casos.

## Cómo nombrarlos
`<criterio>-<puntaje>-<tarea>.md`
Ejemplo: `responsive-2-checkout-v2.md`

## Formato (copia esta plantilla)

```md
# <Criterio> = <puntaje>

## Tarea
<nombre> · Métrica: <métrica>

## Qué se entregó
<descripción concreta de la pantalla o flujo, 3–5 líneas.
 Si puedes, enlaza la imagen o el Figma.>

## Por qué es <puntaje>
<qué descriptor de la rúbrica cumple>

## Por qué no es <puntaje + 1>
<lo que le falta para subir. Esta es la parte más útil.>

Puntuado por: <nombre> · Fecha: <AAAA-MM-DD>
```

## Cuándo agregar más
Después de cada `/cerrar`, si el delta en un criterio es ≥ 1.5,
convierte ese caso en un ejemplo de calibración.
