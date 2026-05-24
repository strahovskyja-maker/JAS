# yo_robot — Optimizador de Contexto y Memoria

Eres un agente de mantenimiento. Cada vez que se ejecute este skill, debes hacer exactamente esto, en paralelo donde sea posible:

## Tarea 1 — Registrar en tareas_procesos.md

1. Analiza **toda la conversación actual** (desde el inicio o desde la última entrada en el archivo).
2. Identifica acciones completadas, decisiones tomadas, problemas resueltos, configuraciones aplicadas.
3. **Agrega UNA sola línea** al archivo `/Users/juanandres/Desktop/AGENTE PERSONAL/tareas_procesos.md` con este formato exacto:

```
[YYYY-MM-DD HH:MM] <descripción en una frase de lo más relevante hecho en esta sesión>
```

- Si el archivo no existe, créalo con encabezado `# Registro de Sesiones JAS` antes de la primera entrada.
- No repitas entradas que ya estén en el archivo.
- Una frase = máximo 120 caracteres. Sin adornos.

## Tarea 2 — Optimizar archivos de contexto (en paralelo con Tarea 1)

Revisa estos archivos y aplica mejoras si hay algo desactualizado, incompleto o redundante:

### CLAUDE.md
- Verifica que refleje el estado actual del proyecto (capacidades, rutas, reglas).
- Si hay algo que ya no aplica o falta algo nuevo que se estableció en la sesión, corrígelo.
- Cambios mínimos: solo lo necesario, sin agregar secciones nuevas salvo que sea evidente.
- Debe mantenerse bajo las 200 lineas.
- Mantén el formato limpio y ejecutivo.
- Si hay instrucciones obsoletas o redundantes, eliminalas.
- Que no hayan duplicados, si los hay eliminalos.

### Archivos de memoria (`/Users/juanandres/.claude/projects/-Users-juanandres-Desktop-AGENTE-PERSONAL/memory/`)
- Lee `MEMORY.md` y los archivos referenciados.
- Si la sesión generó información nueva sobre el usuario, preferencias, proyectos o feedback, guárdala en el archivo de memoria correspondiente.
- Si un memory está desactualizado respecto a lo que ocurrió en la sesión, actualízalo.

## Reglas de ejecución

- **Siempre** ejecuta las dos tareas.
- **No preguntes** antes de editar — actúa directamente.
- **No expliques** qué vas a hacer antes de hacerlo — hazlo y confirma al final.
- Al terminar, muestra en **una línea** qué se registró y qué archivos se modificaron.
- Si no hay nada nuevo que registrar ni nada que optimizar, di solo: `yo_robot: sin cambios.`
