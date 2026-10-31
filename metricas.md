# Métricas

El objetivo del piloto es reducir el tiempo invertido en ejecución de
diseño. Sin baseline no se puede afirmar nada.

## Baseline (antes de la primera tarea)
En `baseline/tareas-manuales.json` registra 2 o 3 tareas recientes
hechas sin agente. Usa fuentes verificables: Jira, calendario,
registro propio. Si no tienes un dato, `null`.

## Qué se mide en cada tarea (`log.json`)

| Métrica | Qué responde | Fuente |
|---|---|---|
| `horas_hasta_primera_review` | ¿Llego antes a la review? | review.md (tú) |
| `horas_humano` | ¿Cuánto tiempo mío consumió? | review.md (tú) |
| `rondas_review` | ¿La primera propuesta está más cerca? | review.md (tú) |
| `score_humano` | ¿La calidad se mantiene o sube? | review.md (tú) |
| `delta` | ¿El evaluator piensa como yo? | score.json |
| `comentarios_repetidos / comentarios_total` | ¿El sistema aprende? | análisis del evaluator |
| `harness_version` | ¿La mejora vino de un cambio al harness? | CHANGELOG.md |

## Cómo leerlas

- **Mejora real:** bajan horas y rondas, y `score_humano` no baja.
- **El evaluator se calibra:** el delta se acerca a 0 con las tareas.
- **El loop aprende:** baja el % de comentarios repetidos.
- **Señal de alerta:** horas bajan pero `score_humano` también baja.
  Vas más rápido a un resultado peor.

## Honestidad para el día 90
Con menos de 5 tareas, reporta los números crudos y la tendencia, no
"mejoras porcentuales". Muestra también lo que no funcionó.
`/estado` genera el resumen y advierte si la muestra es chica.
