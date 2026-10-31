# Actualizar el design system desde Figma

`design-system/` es una copia en código del archivo de Figma. Cuando el DS
cambie de versión (ver la página QA & Changelog), hay que regenerarla.

## Opción recomendada: Claude en claude.ai con el conector de Figma
1. Abre un chat en claude.ai con el conector de Figma activo.
2. Pega este pedido con el link del archivo:

```
Lee el archivo de Figma <link>. Primero la página Agent Guidelines,
luego las colecciones de variables, text styles, effect styles y los
componentes de las páginas "Components · …" (props, variantes, descripción
y specs de la variante default). Luego las páginas Patterns.
Regenera en UI-Army: design-system/tokens.json, tokens.css,
components.css, components.md, patterns.md y guidelines.md, conservando
la nomenclatura actual (ver design-system/README.md). Marca [figma] lo leído
y [aprox] lo inferido. Dame la lista de cambios contra la versión anterior.
```

3. Sube los archivos regenerados al repo con github.dev.
4. Actualiza la versión del DS en `design-system/README.md` y agrega una
   entrada en `CHANGELOG.md` del harness (un cambio de DS cambia los resultados).
5. Abre `design-system/preview.html` en Light y Dark y compara contra Figma.

## Por qué no lo hace el agente en la nube
Las sesiones de Claude Code en la nube no garantizan acceso al conector de Figma
(ver `docs/setup.md`). Mantener el DS en el repo hace que el agente funcione
igual con o sin conectores.

## Qué revisar después de regenerar
- Que no aparezcan nuevos `[aprox]` donde antes había `[figma]`.
- Que los nombres de clase `ds-*` no cambien: si cambian, los prototipos
  viejos se rompen. Si un componente se renombra en Figma, documenta el alias.
