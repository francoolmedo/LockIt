# Hardware · Bill of Materials (BOM)

> Lista de materiales de **un nodo (una puerta)** y del **gateway**. Precios **estimados** a
> septiembre 2025, en USD (referencia internacional) y ARS (a validar en Córdoba/MercadoLibre).
> Tomar como orden de magnitud para cotizar, no como precio cerrado. TC de referencia usado:
> **~1 USD = 1.400 ARS** (ajustar al cambio del día).

## Nodo por puerta — variante base (tag NFC pasivo)

| # | Componente | Detalle | Cant. | USD c/u | USD total |
|---|---|---|---|---|---|
| 1 | **ESP32** | WROOM-32 devkit (o C3 más barato) | 1 | 4.5 | 4.5 |
| 2 | **Cerradura eléctrica 12 V** | Solenoide tipo "cabinet lock" (consume solo al abrir) | 1 | 5.0 | 5.0 |
| 3 | **MOSFET driver** | IRLZ44N + resistencias + diodo flyback | 1 | 0.8 | 0.8 |
| 4 | **Sensor Hall + imán** | A3144 (o reed switch ~0.3) + imán de neodimio | 1 | 0.6 | 0.6 |
| 5 | **Tag NFC pasivo** | NTAG213/215 sticker (grabado con URL NDEF) | 1 | 0.3 | 0.3 |
| 6 | **Aro LED de estado** | Anillo WS2812 direccionable (12–16 px), Clear y Glow | 1 | 1.5 – 3.0 | 1.5 – 3.0 |
| 7 | **Buck converter** | 12 V → 3.3/5 V (MP1584 o similar) | 1 | 0.7 | 0.7 |
| 8 | **PCB / protoboard + conectores** | placa del nodo, borneras, cableado | 1 | 2.0 | 2.0 |
| 9 | **Gabinete electrónico** | caja plástica del nodo (o impreso 3D) | 1 | 1.0 | 1.0 |
| | | | | **Subtotal nodo** | **≈ USD 16.4 – 18.9** |

- **Variante Clear:** mismo aro LED sobre puerta transparente (~USD 16.4 / **≈ ARS 23.000**).
- **Variante Glow:** mismo aro LED sobre puerta opaca; el costo extra está en la puerta, no en el indicador.
- **Nodo "Pro" (con lector NFC PN532):** +USD 4–8 → apertura offline y credencial física.

> ⚠️ La **cerradura** y la **puerta** son los ítems que más mueven el costo. Comprar por
> volumen (50–100 u.) baja el nodo a **~USD 11–13** por puerta.

## Gateway (uno por local / por zona)

| # | Componente | Detalle | Cant. | USD |
|---|---|---|---|---|
| 1 | ESP32 | Igual que nodo, con WiFi al router del local | 1 | 4.5 |
| 2 | Fuente 12 V | Alimenta la columna de cerraduras (ej. 12 V 5 A) | 1 | 8.0 |
| 3 | Caja + antena | Gabinete con mejor antena WiFi | 1 | 5.0 |
| | | | **Total gateway** | **≈ USD 17.5** |

> El gateway puede ser **uno de los nodos** con el firmware en rol gateway (ahorra hardware),
> o un dispositivo dedicado si el local es grande.

## Costeo de una columna de 4 puertas (variante Clear)

| Concepto | USD | ARS aprox. |
|---|---|---|
| 4 nodos Clear × ~16.4 | 65.6 | 92.000 |
| Prorrateo gateway (1 cada ~8 puertas) | 8.8 | 12.300 |
| Fuente 12 V compartida | (incluida en gateway) | — |
| **Electrónica por columna de 4** | **≈ 74** | **≈ 104.000** |

> A esto se le suma la **estructura física** (melamina/chapa, herrajes, puertas, corte y
> armado) que cotiza el taller — ver
> [`../docs/04-fabricacion-cordoba.md`](../docs/04-fabricacion-cordoba.md).

## Dónde comprar (Argentina / Córdoba)

- **ESP32, sensores, MOSFET, buck, aro LED WS2812:** MercadoLibre, Nubbeo, Vistronica, Electrocomponentes.
- **Cerraduras solenoide 12 V "cabinet lock":** MercadoLibre / AliExpress (importar por volumen).
- **Tags NFC NTAG213:** MercadoLibre / importación (baratísimos por cantidad).
- **Fuentes 12 V:** proveedores de electrónica locales de Córdoba.

## Notas de ingeniería

- **Diodo flyback obligatorio** en paralelo a la cerradura (protege el MOSFET del pico inductivo).
- Cerradura **activada por pulso corto** (150–250 ms), nunca energizada de forma continua
  (calienta y consume).
- Un imán de neodimio chico en la puerta + Hall en el marco da lectura confiable de cierre.
- Todo el detalle de conexiones en [`esquematico.md`](esquematico.md).
