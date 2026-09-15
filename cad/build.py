"""
LockIt · Generador de archivos de fabricación
=============================================

Corre el modelo paramétrico y exporta a cad/exports/:
  - STEP  (.step)  -> intercambio universal para el taller / otro CAD (SolidWorks, Fusion...)
  - STL   (.stl)   -> impresión 3D del prototipo / visualización
  - DXF   (.dxf)   -> corte 2D de piezas planas (láser/router CNC de melamina o chapa)
  - SVG   (.svg)   -> vista previa de los planos 2D (para revisar de un vistazo)

Uso:
    python cad/build.py                # exporta todo
    python cad/build.py clear          # solo variante clear
    python cad/build.py glow column    # variante glow + columna
"""

import os
import sys

import cadquery as cq
from cadquery import exporters

import lockit_module as lm
from lockit_params import GYM_CLEAR, GYM_GLOW

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "exports")
os.makedirs(OUT, exist_ok=True)


def _path(name: str) -> str:
    return os.path.join(OUT, name)


def export_solid(wp: cq.Workplane, base: str):
    """Exporta un sólido a STEP y STL."""
    exporters.export(wp, _path(f"{base}.step"))
    exporters.export(wp, _path(f"{base}.stl"))
    print(f"  ✓ {base}.step / {base}.stl")


def export_assembly(asm: cq.Assembly, base: str):
    """Exporta un ensamble a STEP (con colores) y STL (mallado)."""
    asm.save(_path(f"{base}.step"))
    # STL del ensamble: lo compilamos a un shape combinado
    try:
        exporters.export(asm.toCompound(), _path(f"{base}.stl"))
    except Exception as e:
        print(f"    (STL del ensamble omitido: {e})")
    print(f"  ✓ {base}.step (+STL)")


def export_flat_2d(profile: cq.Workplane, base: str):
    """Exporta un perfil 2D (wires) a DXF (corte CNC/láser) y SVG (preview)."""
    try:
        exporters.export(profile, _path(f"{base}.dxf"),
                         exportType=exporters.ExportTypes.DXF)
        print(f"  ✓ {base}.dxf")
    except Exception as e:
        print(f"    (DXF de {base} omitido: {e})")
    try:
        exporters.export(profile, _path(f"{base}.svg"),
                         exportType=exporters.ExportTypes.SVG,
                         opt={"width": 500, "height": 650, "showAxes": False,
                              "projectionDir": (0, 0, 1)})
        print(f"  ✓ {base}.svg")
    except Exception as e:
        print(f"    (SVG de {base} omitido: {e})")


def export_preview_svg(wp: cq.Workplane, base: str):
    """SVG isométrico de un sólido, como vista previa rápida del plano."""
    try:
        exporters.export(wp, _path(f"{base}.svg"),
                         exportType=exporters.ExportTypes.SVG,
                         opt={"width": 700, "height": 700, "showAxes": False,
                              "projectionDir": (1, -1, 0.6), "strokeWidth": 0.6})
        print(f"  ✓ {base}.svg (preview iso)")
    except Exception as e:
        print(f"    (preview SVG de {base} omitido: {e})")


def build_variant(variant: str):
    p = GYM_CLEAR if variant == "clear" else GYM_GLOW
    print(f"\n▶ Variante '{variant}'  "
          f"(ext {p.ext_width:.0f}×{p.ext_height:.0f}×{p.ext_depth:.0f} mm)")

    body = lm.build_body(p)
    door = lm.build_door(p)
    asm = lm.build_assembly(p)

    export_solid(body, f"lockit_{variant}_gabinete")
    export_solid(door, f"lockit_{variant}_puerta")
    export_assembly(asm, f"lockit_{variant}_modulo")

    # Puerta como PERFIL 2D plano para corte láser/CNC (contorno + calados)
    profile = lm.door_profile_2d(p)
    export_flat_2d(profile, f"lockit_{variant}_puerta_corte2d")

    # Vista previa isométrica del gabinete
    export_preview_svg(body, f"lockit_{variant}_gabinete_iso")


def build_column(variant: str = "clear"):
    p = GYM_CLEAR if variant == "clear" else GYM_GLOW
    print(f"\n▶ Columna '{variant}' de {p.doors_per_column} módulos "
          f"({p.column_height:.0f} mm de alto)")
    asm = lm.build_column(p)
    export_assembly(asm, f"lockit_{variant}_columna")


def main(argv):
    args = [a.lower() for a in argv[1:]]
    variants = [a for a in args if a in ("clear", "glow")]
    want_column = "column" in args or "columna" in args

    if not variants and not want_column:
        variants = ["clear", "glow"]  # default: ambas

    for v in variants:
        build_variant(v)
    if want_column:
        build_column(variants[0] if variants else "clear")

    print(f"\n✅ Listo. Archivos en: {OUT}")
    for f in sorted(os.listdir(OUT)):
        size = os.path.getsize(os.path.join(OUT, f))
        print(f"   - {f}  ({size/1024:.1f} KB)")


if __name__ == "__main__":
    main(sys.argv)
