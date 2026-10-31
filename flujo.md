# Flujo

```
/nueva-tarea
     │
     ▼
brief.md (humano)
     │
/ejecutar ─────────────────────────────────────────────┐
     │                                                 │
     ├─ 0. Chequeo del brief ── falta algo ──► pregunta al humano
     ├─ 1. Benchmark (designer + Mobbin)
     ├─ 2. Loop, máx. 3 iteraciones
     │      designer ──► v1 v2 v3
     │      evaluator ──► lint DS + render + rúbrica ──► iter-0N.md
     │      ¿todas ≥ 3.5 y sin bloqueantes? ── no ──► designer refina o pivota
     └─ 3. Entrega: compare.html + resumen.md + review.md
     │
Review con el equipo (humano completa review.md)
     │
/cerrar
     ├─ evaluator analiza review (delta + clasificación)
     ├─ score.json + fila en log.json
     └─ learnings propuestos ──► humano aprueba ──► memory/learnings.md
     │
Merge a main
```

## Separación de roles

| Rol | Puede escribir | No puede |
|---|---|---|
| Orquestador | log, score, resumen, copiar templates | Diseñar, puntuar, editar learnings sin aprobación |
| Designer | benchmark, prototypes, respuesta a evaluación, líneas en solicitudes-ds.md | Puntuarse, tocar rúbrica, memoria o el resto del DS |
| Evaluator | evaluaciones, análisis en review.md | Tocar prototipos, rúbrica, memoria o DS |
| Figma (vía humano) | design-system/ | — |
| Humano | todo | — |

## Archivos por tarea al terminar

```
tasks/<id>/
├── brief.md
├── benchmark.md
├── prototypes/   v1.html v2.html v3.html compare.html
├── evaluations/  iter-01.md iter-01-respuesta.md … resumen.md shots/
├── review.md
└── score.json
```
