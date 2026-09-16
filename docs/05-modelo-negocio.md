# 05 · Modelo de Negocio

> Cómo gana plata LockIt. Números **estimados** para ordenar la conversación y validar que el
> negocio cierra. Ajustar con cotizaciones reales ([fabricación](04-fabricacion-cordoba.md)) y
> el mercado.

---

## Modelos de ingreso (se pueden combinar)

| Modelo | Cómo | Pro | Contra |
|---|---|---|---|
| **A. Venta directa** | El local compra las columnas (CAPEX) | Ingreso grande de una; simple | Ciclo de venta más lento; el local pone la plata |
| **B. Hardware + suscripción (SaaS)** | Vende el hardware + fee mensual por el panel/soporte/nube | Ingreso recurrente (MRR); pegajoso | Requiere sostener la plataforma |
| **C. Locker-as-a-Service** | LockIt instala gratis/subsidiado y cobra por uso o revenue share | Bajísima barrera para el local | Necesita capital para financiar el hardware |
| **D. Pago por uso (público)** | En aeropuertos/públicos, el usuario paga por usar | Ingreso directo del usuario final | Requiere pasarela de pago y alto tránsito |

**Recomendado para arrancar (gimnasios):** **B — Hardware + suscripción.** Vendés/instalás
las columnas y cobrás una **mensualidad por local** (panel, actualizaciones, soporte, garantía).
Da recurrencia y te diferencia de un simple mueble.

---

## Estructura de precios (propuesta inicial, ARS/USD — validar)

### Hardware (una vez)
- **Columna de 4 puertas (Clear):** precio de venta objetivo **USD 700 – 1.000** por columna
  (según costo real ~USD 330–540 → margen bruto ~45–55%).
- **Columna Glow (aro LED):** +USD 60–120 por la puerta opaca y el aro LED direccionable.
- **Instalación y setup:** por proyecto (según cantidad de columnas).

### Suscripción (recurrente, por local)
- **Plan base:** **USD 20 – 40 / mes por local** (panel, soporte, updates).
- Escala por cantidad de puertas / features (asignación avanzada, reportes, cobro por uso).

### Ejemplo de un gimnasio tipo
- Compra 5 columnas Clear (20 puertas): 5 × USD 850 = **USD 4.250** (hardware).
- Suscripción: **USD 30 / mes** → **USD 360 / año** recurrente.

---

## Unit economics (por puerta, estimado)

| Concepto | USD |
|---|---|
| Costo hardware por puerta (estructura + electrónica, a escala) | 90 – 135 |
| Precio de venta por puerta (columna/4) | 175 – 250 |
| **Margen bruto por puerta** | **~45 – 55%** |
| + Suscripción anual prorrateada por puerta | ~4 – 8 / año recurrente |

> A escala (series de 25–50 columnas), el costo por puerta baja y el margen mejora. La
> **suscripción** es lo que convierte a LockIt de "vender muebles" a "negocio recurrente".

---

## Costos del negocio (además del hardware)

- **Desarrollo** (firmware, webapp, panel, nube) — mayor al principio, luego mantenimiento.
- **Hosting/nube** (API, MQTT, base de datos) — bajo por local, escala con el uso.
- **Soporte y garantía** — clave para retención; cubierto por la suscripción.
- **Ventas y marketing** — ver [marketing](../marketing/).
- **Stock/producción** — capital de trabajo para fabricar series.

---

## Estrategia de entrada (go-to-market)

1. **1 gimnasio piloto en Córdoba** (idealmente con relación previa): instalar 1–2 columnas,
   medir uso, juntar testimonio y video real.
2. **Caso de éxito** → usarlo para vender a otros gimnasios de Córdoba (boca a boca + outreach).
3. **Estandarizar** el producto y la instalación para bajar costos y tiempos.
4. **Escalar por segmento**: gimnasios → cadenas de gym → coworkings → clubes → aeropuertos.

---

## Métricas del negocio a seguir

- **CAC** (costo de adquirir un local) vs **LTV** (hardware + suscripción en el tiempo).
- **MRR** (ingreso recurrente mensual) y churn de locales.
- **Margen bruto por columna** real (post-cotizaciones).
- **Uso por puerta/día** (prueba de valor y base para pago por uso).

---

## Riesgos y mitigación

| Riesgo | Mitigación |
|---|---|
| Costo de hardware alto (Argentina/importación) | Compra por volumen, componentes locales, diseño frugal |
| Ciclo de venta lento a locales | Modelo as-a-service / financiación; empezar por conocidos |
| Competencia (lockers electrónicos importados) | Diferenciación: NFC sin app + malla + soporte local + estética |
| Dependencia del WiFi del local | Malla ESP-NOW + modo degradado ([arquitectura](02-arquitectura-tecnica.md#6-modo-degradado-sin-internet)) |
| Soporte técnico a distancia | Panel con diagnóstico remoto; red de instaladores |
