# 03 · Diseño Industrial

> Cómo se ve, se siente y se arma el locker. El objetivo: que **no parezca una caja de
> metal industrial**, sino un producto de diseño con carácter, y que a la vez sea
> **fabricable en Córdoba** y aguante el uso real de un gimnasio.

El modelo CAD paramétrico que materializa todo esto está en [`../cad/`](../cad/).

---

## Concepto de diseño

**"Confianza a la vista."** El locker comunica su estado sin que tengas que tocarlo: o ves
adentro (Clear) o te lo dice con luz (Glow). Líneas limpias, aristas suavemente redondeadas,
un punto de color (verde LockIt) como firma. Nada de bisagras a la vista ni candados
colgando.

- **Carácter, no ruido:** superficies mate, un solo acento de color, tipografía/numeración
  clara en cada puerta.
- **Modular y apilable:** se venden **columnas** de N puertas; el local arma su pared.
- **Antivandálico y anti-humedad:** pensado para vestuario de gym (sudor, agua, golpes).

---

## Dimensiones (módulo de gimnasio)

| Medida | Valor | Por qué |
|---|---|---|
| Interior útil | **300 × 400 × 450 mm** (an × al × prof) | Entra mochila de gym, toalla, botella, zapatillas. |
| Exterior módulo | ~330 × 430 × 465 mm | Con paredes de 15 mm. |
| Puertas por columna | 4 (config.) | Altura de columna cómoda (~1.85 m). |
| Altura de columna | ~1.845 mm | Todo alcanzable sin escalera. |
| Puerta | 12 mm | Rígida sin ser pesada. |

> Variante **Large** (mochilas grandes / cascos / aeropuerto): 350 × 550 × 500 mm, 3 puertas
> por columna. Definida en `cad/lockit_params.py` como `GYM_LARGE_CLEAR`.

---

## Materiales

### Estructura (gabinete)
| Opción | Pro | Contra | Uso |
|---|---|---|---|
| **Melamina 15 mm hidrófuga** | Barata, se corta/arma local, muchos colores | Menos resistente al agua extrema | ✅ Prototipo y gimnasios estándar |
| **Chapa plegada (acero pintado)** | Muy robusta, antivandálica | Más cara, requiere plegado/pintura | Ambientes duros / premium |
| **Compact/HPL fenólico** | Impermeable, ideal vestuario húmedo | El más caro | Spa, natatorios, premium |

### Puerta
- **Clear:** **policarbonato** (resistente a impacto, no astilla) o **acrílico** (más barato,
  se raya más). Recomendado policarbonato para uso intenso.
- **Glow:** melamina/MDF laminado o chapa, con **ventana** para el OLED.

### Herrajes
- Bisagras ocultas o de piano (según variante y presupuesto).
- Cerradura solenoide 12 V embutida (ver [hardware](../hardware/)).
- Patas/zócalo niveladores en la base de la columna.

---

## "Chiches" y detalles (lo que da carácter)

1. **LED perimetral / anillo de estado** (Clear): verde = libre, ámbar = ocupado, blanco
   parpadeo = abriendo. Se lee de lejos en todo el vestuario.
2. **OLED embutido** (Glow): muestra número de locker, ícono "acercá el celu", microanimación
   de apertura. Es el "wow".
3. **Numeración grande y legible** grabada/impresa en cada puerta.
4. **Rebaje de agarre** (sin manija que enganche ni se rompa) — modelado en el CAD.
5. **Ventilación trasera** discreta (ranuras) para que no junte olor/humedad.
6. **Zona NFC señalizada**: un círculo/ícono impreso donde apoyar el celu (UX física).
7. **Base con luz indirecta** opcional (línea LED al piso) para look premium.

---

## Ergonomía y accesibilidad

- Puertas y tags a altura alcanzable (evitar la fila más alta > 1.7 m para NFC).
- Al menos una columna con módulos a **altura accesible** (silla de ruedas) por instalación.
- Apertura que no invada el pasillo (puerta ~90°, o corredera en espacios chicos — variante futura).

---

## Acabados y color

- **Cuerpo:** grafito mate (firma LockIt) o blanco/gris para ambientes claros.
- **Acento:** verde LockIt en LED, detalles y numeración.
- **Personalización por cliente:** color de cuerpo y branding del gym en la puerta (upsell).

---

## De diseño a fabricación

El CAD paramétrico ([`../cad/`](../cad/)) exporta:
- **STEP/STL** del gabinete, puerta y ensamble → para el taller y para visualizar/renderizar.
- **DXF de corte 2D** de la puerta (contorno + calados) → directo a láser/router CNC.

El detalle de cómo mandarlo a fabricar en Córdoba y la plantilla de cotización están en
[`04-fabricacion-cordoba.md`](04-fabricacion-cordoba.md).
