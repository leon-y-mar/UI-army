# Setup sin git local

UI-Army corre en **Claude Code en la nube** (claude.ai/code): clona el
repo en una máquina virtual de Anthropic, trabaja ahí y sube una rama
a GitHub. No necesitas git, terminal ni instalar nada.

Referencias oficiales:
- Claude Code en la nube: https://code.claude.com/docs/en/claude-code-on-the-web
- Primeros pasos: https://code.claude.com/docs/en/web-quickstart
- Editor github.dev: https://docs.github.com/en/codespaces/the-githubdev-web-based-editor

---

## Antes de empezar: política de la empresa

Este repo va a contener tu design system, briefs y prototipos.
Confirma que tu empresa permite alojarlos en GitHub y en Claude.
Si no, deja el DS y los briefs genéricos hasta tener el visto bueno.
El repo debe ser **privado**.

---

## 1 · Crear el repo

1. En github.com → **New repository** → nombre `UI-Army` → **Private**.
2. Descomprime `UI-Army.zip` en tu computadora.
3. En el repo vacío: **Add file → Upload files** → arrastra el contenido
   de la carpeta (no la carpeta en sí) → **Commit changes**.
4. **Verifica que subieron los archivos ocultos:** `.claude/` y `.mcp.json`.
   Algunos sistemas no arrastran archivos que empiezan con punto.
   Si faltan, créalos con **Add file → Create new file**, escribiendo la
   ruta completa en el nombre (ej. `.claude/agents/designer.md`) y
   pegando el contenido.

## 2 · Conectar Claude Code en la nube

1. Entra a https://claude.ai/code.
2. Conecta GitHub e instala la Claude GitHub App **en el repo UI-Army**
   (los repos privados necesitan la app instalada).
3. Crea el entorno. Para empezar, deja los valores por defecto
   (acceso a red "Trusted").
4. Elige el repo `UI-Army` y la rama `main`.

Requiere plan Pro, Max o Team, o asiento Enterprise con acceso a
Claude Code. Si usas una cuenta de empresa, tu admin puede tenerlo
desactivado.

## 3 · Primera ejecución (prueba de humo)

Antes de una tarea real, en una sesión nueva escribe:

```
Lee CLAUDE.md. Dime: 1) qué subagentes ves en .claude/agents,
2) si el MCP de Mobbin está disponible, 3) si puedes correr
npx playwright para screenshots. No ejecutes ninguna tarea.
```

Anota las respuestas. Si Mobbin o el render no están disponibles,
el harness tiene fallbacks, pero conviene saberlo antes.

## 4 · Ciclo de una tarea

| Paso | Dónde | Qué haces |
|---|---|---|
| 1 | claude.ai/code | `/nueva-tarea S01-<nombre>` |
| 2 | github.dev o la sesión | Completas `tasks/S01-<nombre>/brief.md` |
| 3 | claude.ai/code | `/ejecutar S01-<nombre>` |
| 4 | Tu computadora | Descargas la rama y abres `compare.html` (ver abajo) |
| 5 | Review con el equipo | Completas `review.md` |
| 6 | claude.ai/code | `/cerrar S01-<nombre>` y apruebas learnings |
| 7 | github.com | **Merge del PR a `main`** |

El paso 7 no es opcional: cada sesión nueva clona `main`. Si no haces
merge, la siguiente tarea no ve `log.json` ni los learnings nuevos.

### Ver los prototipos sin git
GitHub no renderiza HTML. En la página del repo, cambia a la rama de
la sesión → **Code → Download ZIP** → descomprime → abre
`tasks/<id>/prototypes/compare.html` en el navegador y elige el
viewport del producto.

Descarga el repo completo, no solo la carpeta de la tarea: los prototipos
enlazan `design-system/` con rutas relativas y sin él se ven sin estilos.

---

## Dónde editar

| Tipo de cambio | Herramienta |
|---|---|
| Un archivo, cambio chico | github.com → abre el archivo → ícono de lápiz → **Commit changes** |
| Varios archivos (DS, agentes, rúbrica) | github.dev: en el repo presiona la tecla `.` |
| Cambios que el agente puede hacer | Pídeselo en la sesión de claude.ai/code |

github.dev es VS Code en el navegador: editas varios archivos y
haces commit desde el panel **Source Control**, sin instalar git.

**Regla:** cada vez que cambies `CLAUDE.md`, un agente, un comando o la
rúbrica, agrega una línea en `CHANGELOG.md` y sube la versión.
