---
description: Resume las métricas del harness desde log.json
---

Lee `log.json` y `baseline/tareas-manuales.json`. Responde con:

1. Tabla por tarea: horas hasta primera review, rondas, score humano, delta,
   % comentarios repetidos (`comentarios_repetidos / comentarios_total`).
2. Comparación contra el promedio del baseline en horas y rondas.
3. Tendencia del delta (¿el evaluator se acerca al humano?).
4. Advertencia si hay menos de 5 tareas: "Muestra insuficiente para
   afirmar mejora; reporta como tendencia".

No calcules nada que no esté en los archivos. Valores `null` se excluyen
del promedio y se reporta cuántos se excluyeron.
