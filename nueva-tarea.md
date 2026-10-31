---
description: Crea la carpeta de una tarea nueva desde los templates
argument-hint: <id> (ej. S01-checkout-resumen)
---

Crea la tarea `$ARGUMENTS`:

1. Si `tasks/$ARGUMENTS/` ya existe, detente y avisa.
2. Crea `tasks/$ARGUMENTS/prototypes/` y `tasks/$ARGUMENTS/evaluations/shots/`.
3. Copia `templates/brief.md` a `tasks/$ARGUMENTS/brief.md`.
4. Responde solo: ruta del brief y "Completa el brief y luego corre `/ejecutar $ARGUMENTS`".
5. Commit: `ui-army($ARGUMENTS): nueva tarea`.
