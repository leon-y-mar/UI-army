---
description: Cierra una tarea después de la review humana
argument-hint: <id>
---

Cierra la tarea `$ARGUMENTS`:

1. Lee `tasks/$ARGUMENTS/review.md`. Si la tabla "Puntaje humano" o
   "Horas" está vacía, detente y pide que la complete.
2. Delega en `evaluator`, modo "análisis de review".
3. Escribe `tasks/$ARGUMENTS/score.json`:
   ```json
   {
     "version_elegida": "",
     "score_evaluator": 0,
     "score_humano": 0,
     "delta": 0,
     "delta_por_criterio": {},
     "iteraciones": 0
   }
   ```
4. Agrega una fila a `log.json` con este esquema exacto:
   ```json
   {
     "tarea": "",
     "fecha_cierre": "",
     "harness_version": "",
     "story_points": 0,
     "horas_hasta_primera_review": 0,
     "horas_humano": 0,
     "iteraciones_loop": 0,
     "minutos_loop": 0,
     "score_evaluator": 0,
     "score_humano": 0,
     "delta": 0,
     "rondas_review": 0,
     "comentarios_total": 0,
     "comentarios_anticipados": 0,
     "comentarios_repetidos": 0,
     "mobbin_disponible": true,
     "render_disponible": true
   }
   ```
   Los valores salen de `brief.md` (story_points), `review.md`, `score.json`
   y `evaluations/`.
   Si un dato no existe, usa `null`, nunca un estimado.
5. Muestra los learnings propuestos y pregunta cuáles aprobar.
   Solo agrega a `memory/learnings.md` los que el humano apruebe
   explícitamente. Si un learning aprobado ya existía, sube su contador.
6. Commit: `ui-army($ARGUMENTS): cierre`.
