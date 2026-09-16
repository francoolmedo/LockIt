# 04 · Fabricación en Córdoba

> Cómo pasar del CAD ([`../cad/`](../cad/)) a un locker físico, con proveedores y procesos
> reales de Córdoba, Argentina. Incluye una **plantilla de cotización** lista para mandar a
> talleres.

---

## Qué se manda a fabricar

Un módulo LockIt tiene tres "paquetes" de fabricación:

| Paquete | Piezas | Proceso | Archivo que se manda |
|---|---|---|---|
| **A. Estructura** | Gabinete (5 paneles), puerta, dividers, base | Corte CNC/láser + plegado o armado | `*.dxf` de corte + `*.step` de referencia |
| **B. Electrónica** | Nodo ESP32, cerradura, sensor, indicador | Compra + ensamble en placa | [`../hardware/BOM.md`](../hardware/BOM.md) |
| **C. Terminación** | Pintura/laminado, herrajes, numeración, aro LED | Pintura + montaje | Especificación de color y acabado |

---

## Procesos según material

### Opción melamina (recomendada para prototipo y piloto)
- **Corte:** router CNC sobre placa de melamina hidrófuga 15 mm.
- **Armado:** tornillería + tarugos / minifix; cantos con ABS.
- **Puerta Clear:** marco de melamina + **policarbonato** cortado a medida (láser o sierra).
- **Ventaja:** rápido, barato, muchos talleres en Córdoba lo hacen (mueblerías/carpinterías CNC).

### Opción chapa plegada (para versión robusta/premium)
- **Corte:** láser sobre chapa (acero 0.9–1.2 mm).
- **Plegado:** plegadora CNC.
- **Terminación:** pintura en polvo (termolacado) — muy resistente en vestuarios.
- **Ventaja:** antivandálico, durabilidad; **Contra:** más caro, menos talleres.

---

## Dónde cotizar en Córdoba (tipos de proveedor)

| Necesidad | Tipo de proveedor | Cómo buscar |
|---|---|---|
| Corte CNC melamina | Carpintería CNC / mueblería a medida | "corte CNC melamina Córdoba", parques industriales |
| Corte láser chapa + plegado | Taller metalúrgico / corte láser | "corte láser chapa Córdoba", polo metalúrgico |
| Policarbonato/acrílico a medida | Corte láser acrílico / cartelería | "corte acrílico Córdoba", "policarbonato Córdoba" |
| Pintura en polvo | Termolacado / pintura industrial | "termolacado Córdoba" |
| Electrónica y ensamble | Casas de electrónica + freelance | MercadoLibre + electrónicos locales |
| Impresión 3D (prototipo de piezas) | Servicios de impresión 3D FDM/resina | "impresión 3D Córdoba" |

> Estrategia recomendada: **melamina para el prototipo** (rápido y barato para validar), y
> cotizar **chapa en paralelo** para tener la versión "producto final" lista cuando escale.

---

## Plantilla de cotización (copiar y enviar)

> Copiá este texto, adjuntá los archivos `cad/exports/*.dxf` y `*.step` y las medidas.
> Reemplazá lo que está entre corchetes.

```
Asunto: Cotización — prototipo de casillero (mueble/metal) con corte CNC

Hola [nombre del taller], ¿cómo estás?

Estoy desarrollando un producto de casilleros inteligentes (marca LockIt, Córdoba) y
necesito cotizar la fabricación de un PROTOTIPO de 1 columna de 4 puertas.

DETALLE:
- Material: [melamina hidrófuga 15 mm / chapa 1 mm plegada] color [grafito/blanco].
- Módulo (x4 apilados): interior 300 x 400 x 450 mm; exterior aprox. 330 x 430 x 465 mm.
- Puerta por módulo: [policarbonato con marco (línea Clear) / opaca con ventana (línea Glow)].
- Incluye: paneles laterales, fondo con ranuras de ventilación, 3 divisiones horizontales,
  base/zócalo y tapa. Alojamiento interno para caja de electrónica (60 x 80 x 40 mm) por puerta.
- Herrajes: bisagras [ocultas/piano] y previsión de cerradura eléctrica embutida (la
  electrónica la proveo yo).

ADJUNTO:
- Planos de corte 2D (DXF) de la puerta y referencia 3D (STEP).
- (Puedo pasar el resto de los planos de corte al confirmar el material.)

NECESITO:
1) Precio del PROTOTIPO (1 columna de 4 puertas), armado.
2) Precio estimado por unidad para una PRIMERA SERIE de [10 / 25 / 50] columnas.
3) Plazo de entrega del prototipo.
4) Qué necesitás de mi lado para arrancar.

¡Gracias! Quedo atento.
[Tu nombre] — LockIt — [tu teléfono/mail]
```

---

## Costeo objetivo (orden de magnitud)

> A **validar** con las cotizaciones reales. Sirve para saber si el negocio cierra.

| Concepto (por columna de 4 puertas) | Estimado ARS | Nota |
|---|---|---|
| Estructura melamina (corte + armado) | 180.000 – 320.000 | Muy variable por taller |
| Puertas (policarbonato x4 con marco) | 90.000 – 160.000 | Clear; Glow: melamina + rebaje para aro LED |
| Herrajes + tornillería | 30.000 – 60.000 | |
| Electrónica (4 nodos + prorrateo gateway) | ≈ 104.000 | Ver [BOM](../hardware/BOM.md) |
| Ensamble + pruebas | 60.000 – 120.000 | Mano de obra |
| **Total prototipo por columna** | **≈ 460.000 – 760.000 ARS** | ≈ USD 330 – 540 |

> Al escalar (series de 25–50), la estructura y la electrónica bajan fuerte por volumen.
> El objetivo es un **costo por puerta** que deje margen sano según el
> [modelo de negocio](05-modelo-negocio.md).

---

## Normativa y seguridad (a tener en cuenta)

- **Eléctrica:** instalación de 12 V con fuente certificada, fusibles, cableado en canaleta.
  Para venta comercial, revisar requisitos de seguridad eléctrica y garantía.
- **Materiales:** en vestuarios húmedos, priorizar materiales que no se hinchen (hidrófugo/HPL).
- **Accesibilidad:** prever al menos una fila a altura accesible por instalación.
- **Facturación/IVA:** definir con contador la estructura para vender a empresas.

---

## Siguiente paso concreto

1. Elegir material del prototipo (recomendado: **melamina**).
2. Generar los DXF definitivos (`python cad/build.py`) y mandar la **plantilla de cotización**
   a 3–5 talleres.
3. Comprar la electrónica del [BOM](../hardware/BOM.md) para 1 columna.
4. Armar y probar el primer nodo (ver [roadmap](06-roadmap.md)).
