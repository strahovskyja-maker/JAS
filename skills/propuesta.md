# Skill: Redactar Propuesta de Negocio en PDF

Cuando Juan Andrés invoque este comando con una transcripción, debes:

## 0. Consultar memoria
Antes de todo, lee `/Users/juanandres/Desktop/AGENTE PERSONAL/memory.md`.
- Si el cliente ya existe en la sección **Clientes**, usa los datos guardados
- Si hay preferencias relevantes en **Preferencias y reglas**, aplícalas

## 1. Preguntar valores antes de continuar
Antes de estructurar la propuesta, pregunta **siempre** a Juan Andrés:

> ¿Cuál es el valor de **Configuración y Capacitación**?
> ¿Cuál es el valor de la **suscripción mensual**?

No asumas ni uses placeholders. Sin estos dos valores no generes el PDF.

## 3. Analizar la transcripción
Lee atentamente la transcripción y extrae:
- Cliente o empresa destinataria
- Problema o necesidad planteada
- Solución o servicios propuestos (el software SaaS se llama **GESTIA**, desarrollado por **MEDCORE**)
- Precios, montos o condiciones si se mencionan
- Plazos o fechas relevantes
- Cualquier otro detalle relevante para la propuesta

## 4. Estructurar la propuesta
Construye un JSON con la siguiente estructura (adapta las secciones según lo que requiera la propuesta):

```json
{
  "titulo": "Propuesta Comercial — GESTIA",
  "cliente": "Nombre del cliente o empresa",
  "fecha": "DD de Mes de YYYY",
  "referencia": "REF-YYYY-NNN",
  "nombre_archivo": "propuesta-cliente-YYYYMMDD",
  "secciones": [
    {
      "tipo": "texto",
      "titulo": "Resumen Ejecutivo",
      "contenido": "..."
    },
    {
      "tipo": "texto",
      "titulo": "Contexto y Necesidad",
      "contenido": "..."
    },
    {
      "tipo": "texto",
      "titulo": "Solución Propuesta — GESTIA",
      "contenido": "..."
    },
    {
      "tipo": "inversion",
      "titulo": "Inversión",
      "filas": [
        {
          "descripcion": "Configuración y Capacitación",
          "detalle": "Implementación inicial y capacitación del equipo",
          "valor": "$X.XXX"
        },
        {
          "descripcion": "Suscripción Anual GESTIA",
          "detalle": "Acceso a plataforma GESTIA · Soporte técnico lunes a viernes 9:00–18:00 hrs · Almacenamiento estándar 100 GB",
          "valor": "$X.XXX/año"
        }
      ],
      "total": "$X.XXX"
    },
    {
      "tipo": "condiciones",
      "titulo": "Condiciones de Servicio"
    },
    {
      "tipo": "texto",
      "titulo": "Próximos Pasos",
      "contenido": "..."
    }
  ],
  "cierre": "Quedamos a disposición para resolver cualquier consulta. Esperamos tener la oportunidad de trabajar juntos."
}
```

### Reglas de redacción
- Tono formal y profesional en todo momento
- Mencionar siempre el producto como **GESTIA** y la empresa como **MEDCORE**
- Usar párrafos completos en las secciones de texto, no solo listas
- Las listas van con "- " al inicio de cada línea
- Si falta información clave (ej. precio), usa el placeholder "[A definir]"
- Genera referencia como REF-2026-001, REF-2026-002, etc.

### Regla fija de inversión
La sección de inversión **siempre** debe incluir estas dos líneas, sin excepción:
1. **Configuración y Capacitación** — cobro único
2. **Suscripción Anual GESTIA** — con el detalle completo:
   - Acceso a plataforma GESTIA
   - Soporte técnico lunes a viernes, 9:00 a 18:00 hrs
   - Almacenamiento estándar de datos (base 100 GB)

## 5. Guardar el JSON y generar el PDF

1. Guarda el JSON en `/Users/juanandres/Desktop/AGENTE PERSONAL/tools/temp_propuesta.json`
2. Ejecuta el script:

```bash
python3 /Users/juanandres/Desktop/AGENTE\ PERSONAL/tools/generar_propuesta.py \
  /Users/juanandres/Desktop/AGENTE\ PERSONAL/tools/temp_propuesta.json
```

3. Confirma a Juan Andrés dónde quedó guardado el PDF.
4. Elimina el archivo temporal.

## Notas
- El logo MEDCORE.png se carga automáticamente desde la raíz del proyecto
- El PDF se guarda siempre en `/Users/juanandres/Desktop/AGENTE PERSONAL/Propuestas/`
