# CAD — Modelo paramétrico del locker

CAD **por código** con [CadQuery](https://cadquery.readthedocs.io). Cambiás las medidas en
un archivo de parámetros y se regenera todo el modelo y los archivos para el taller.

## Requisitos

```bash
pip install cadquery        # probado con cadquery 2.8.0 / Python 3.11
```

## Uso

```bash
cd cad
python build.py             # exporta AMBAS variantes (clear + glow) a exports/
python build.py clear       # solo LockIt Clear
python build.py glow column # LockIt Glow + una columna de N módulos apilados
```

## Archivos

| Archivo | Qué es |
|---|---|
| `lockit_params.py` | **Todas las medidas** (mm). Única fuente de verdad. Editá acá. |
| `lockit_module.py` | Modelo: `build_body`, `build_door`, `build_assembly`, `build_column`, `door_profile_2d`. |
| `build.py` | Genera los archivos de fabricación en `exports/`. |
| `exports/` | Salida (STEP/STL/DXF/SVG). No se versiona el binario pesado; se regenera. |

## Qué genera (`exports/`)

Por cada variante (`clear`, `glow`):

| Salida | Para qué sirve |
|---|---|
| `..._gabinete.step` / `.stl` | Gabinete 3D. STEP = para el taller / otro CAD (Fusion, SolidWorks). STL = impresión 3D / preview. |
| `..._puerta.step` / `.stl` | Puerta 3D (ventana transparente en Clear o rebaje del aro LED en Glow). |
| `..._modulo.step` / `.stl` | **Ensamble completo** (gabinete + puerta + policarbonato en Clear), coloreado. |
| `..._puerta_corte2d.dxf` | **Plano de corte 2D** (contorno + calados) para láser/router CNC. Lo que va al taller. |
| `..._puerta_corte2d.svg` | Vista rápida del plano de corte. |
| `..._gabinete_iso.svg` | Vista previa isométrica del gabinete. |

## Medidas actuales (módulo de gimnasio)

- **Interior útil:** 300 × 400 × 450 mm (ancho × alto × prof) — entra mochila de gym, toalla, botella.
- **Exterior del módulo:** ~330 × 430 × 465 mm.
- **Columna de 4 puertas:** ~1.845 mm de alto (con base y tapa).
- **Material base:** panel de 15 mm (melamina resistente a humedad / chapa plegada equivalente).
- **Puerta:** 12 mm. Clear = policarbonato/acrílico con marco; Glow = opaca con rebaje para el aro LED.

> Ver el criterio de estas medidas y materiales en
> [`../docs/03-diseno-industrial.md`](../docs/03-diseno-industrial.md).

## Notas de diseño

- Es un modelo de **intención de diseño** para prototipo y cotización, no un plano de
  producción final. Espesores, holguras de puerta y herrajes se ajustan al material y a la
  máquina reales del taller en la Etapa 2.
- El alojamiento de cerradura + ESP32 está modelado como rebaje interno del lado opuesto a
  la bisagra (ver `_cut_lockbox`).
- La ventilación trasera evita olor/humedad (clave en gimnasios).
- Para pasar de melamina a **chapa plegada** se reusa la misma geometría: el `wall` pasa a
  representar el plegado y se generan los desarrollos de chapa (mejora futura del `build.py`).
