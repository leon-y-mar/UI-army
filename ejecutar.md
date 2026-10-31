---
description: Ejecuta benchmark y loop designer/evaluator para una tarea
argument-hint: <id>
---

Ejecuta la tarea `$ARGUMENTS` siguiendo `CLAUDE.md`, pasos 0 a 3, en orden:

0. Chequeo del brief (bloqueante).
1. Benchmark con el subagente `designer`.
2. Loop `designer` ⇄ `evaluator`, máximo 3 iteraciones.
3. Entrega para review.

En tu primer mensaje informa:
- Versión del harness (`CHANGELOG.md`)
- Si Mobbin MCP está disponible
- Si el render para screenshots funciona

Al terminar, muestra solo:
- Tabla de scores finales por versión
- Versión recomendada por el evaluator
- Iteraciones usadas y tiempo del loop
- Qué debe hacer el humano ahora
