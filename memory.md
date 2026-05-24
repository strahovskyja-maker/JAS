# Memoria de JAS

Este archivo es la memoria persistente del agente JAS.
Cada vez que Juan Andrés indique algo relevante, se registra aquí.

---

## Empresa
- **Empresa:** MEDCORE
- **Producto SaaS:** GESTIA
- **Email:** jstrahovsky@medcore.cl

## Clientes
<!-- Formato: - **Nombre:** datos relevantes (precio acordado, contexto, etc.) -->

## Preferencias y reglas

### Estructura fija de cotizaciones GESTIA
Toda propuesta debe incluir siempre estas dos líneas de inversión:

1. **Configuración y Capacitación** — cobro único por implementación
2. **Suscripción Anual GESTIA** — incluye:
   - Acceso a plataforma GESTIA
   - Soporte técnico en horario laboral (lunes a viernes, 9:00 a 18:00 hrs)
   - Almacenamiento estándar de datos (base de 100 GB)

### Condiciones de Servicio (incluir siempre en todas las propuestas)
| Condición | Detalle |
|---|---|
| Modalidad | Suscripción mensual |
| Vigencia mínima | 12 meses desde la fecha de activación del servicio |
| Facturación | Mensual, dentro de los primeros 5 días hábiles de cada mes |
| Plazo de pago | Mes anticipado dentro de los 5 días hábiles siguientes a la emisión de la factura |
| Implementación | Configuración inicial y capacitación a usuarios en 1 semana |
| Término anticipado | Con aviso de 30 días corridos antes del siguiente período de facturación, transcurrida la vigencia mínima |

**Antes de generar cualquier propuesta, preguntar siempre:**
- ¿Cuál es el valor de Configuración y Capacitación?
- ¿Cuál es el valor de la suscripción mensual?
Estos valores no se deben asumir ni dejar como placeholder. Sin ellos no se genera el PDF.

## Automatizaciones n8n
- **Repositorio:** `n8n-test-master/` (raíz del proyecto)
- **Workflows:** JSON en `n8n-test-master/packages/testing/playwright/workflows/`
- **Plataforma:** n8n — monorepo TypeScript con pnpm workspaces
- Cuando se pida crear o modificar una automatización, trabajar directamente sobre esos archivos JSON

## Historial de propuestas
<!-- Formato: - REF-YYYY-NNN | Cliente | Fecha | Monto -->
- REF-2026-002 | Clínica JAS | 19 de Mayo de 2026 | 45 UF/mes
