---
description: Resume las métricas del harness desde log.json
---

Lee `log.json` y `baseline/tareas-manuales.json`. Responde con:

1. Tabla por tarea: story points, horas hasta primera review, horas humano,
   horas por story point (`horas_humano / story_points`), rondas, score humano, delta,
   % comentarios repetidos (`comentarios_repetidos / comentarios_total`).
2. Comparación contra el baseline en horas por story point y rondas.
   Solo compara filas que tengan horas y story points; si el baseline no
   tiene horas, dilo: "Baseline sin horas: no se puede medir ahorro de tiempo"
   y muestra solo los story points.
3. Tendencia del delta (¿el evaluator se acerca al humano?).
4. Advertencia si hay menos de 5 tareas: "Muestra insuficiente para
   afirmar mejora; reporta como tendencia".

No calcules nada que no esté en los archivos. Valores `null` se excluyen
del promedio y se reporta cuántos se excluyeron.
