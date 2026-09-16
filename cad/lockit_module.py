"""
LockIt · Modelo CAD paramétrico del módulo de locker
====================================================

CAD por código con CadQuery. Genera:
  - build_body(p)     -> cuerpo/gabinete (5 caras, frente abierto) con ventilación
                         y alojamiento de cerradura/ESP32.
  - build_door(p)     -> puerta según variante (Clear = ventana transparente,
                         Glow = panel opaco con rebaje para el aro LED), con agarre.
  - build_assembly(p) -> gabinete + puerta (cerrada), coloreado para preview.
  - build_column(p)   -> columna de N módulos apilados con base y tapa.

Uso rápido:
    python cad/build.py          # exporta STEP/STL de ambas variantes a cad/exports/

Nota: es un modelo de INTENCIÓN de diseño para prototipo y cotización, no un
plano de producción final. Espesores y holguras se ajustan al material real
(melamina 15mm, chapa plegada, policarbonato) en la Etapa 2.
"""

import cadquery as cq
from lockit_params import LockerParams


# ---------------------------------------------------------------------------
# Cuerpo / gabinete
# ---------------------------------------------------------------------------
def build_body(p: LockerParams) -> cq.Workplane:
    """Gabinete de 5 caras (fondo, techo, piso, 2 laterales), frente abierto."""
    w, h, d, t = p.ext_width, p.ext_height, p.ext_depth, p.wall

    # Bloque exterior con aristas verticales redondeadas (carácter de producto)
    outer = (
        cq.Workplane("XY")
        .box(w, d, h, centered=(True, True, False))
    )
    # Redondeo de las 4 aristas verticales exteriores
    try:
        outer = outer.edges("|Z").fillet(p.corner_fillet)
    except Exception:
        pass  # si el fillet falla por geometría, seguimos sin él

    # Vaciado interior: hueco abierto hacia el frente (+Y)
    cavity = (
        cq.Workplane("XY")
        .box(p.inner_width, p.inner_depth + t, p.inner_height,
             centered=(True, True, False))
        .translate((0, t, t))  # deja fondo cerrado atrás, abre al frente
    )
    body = outer.cut(cavity)

    # Ventilación en la cara trasera (ranuras horizontales)
    body = _cut_vents(body, p)

    # Alojamiento de cerradura + ESP32 en el lateral del lado opuesto a la bisagra
    body = _cut_lockbox(body, p)

    return body


def _cut_vents(body: cq.Workplane, p: LockerParams) -> cq.Workplane:
    """Ranuras de ventilación en la pared trasera (higiene en gimnasios)."""
    d = p.ext_depth
    z0 = p.wall + p.inner_height * 0.25
    dz = p.inner_height * 0.5 / max(1, (p.vent_rows - 1)) if p.vent_rows > 1 else 0
    for i in range(p.vent_rows):
        z = z0 + i * dz
        slot = (
            cq.Workplane("XZ")
            .workplane(offset=-(d - p.wall / 2))  # sobre la pared trasera
            .center(0, z)
            .slot2D(p.vent_slot_w, p.vent_slot_h, 0)
            .extrude(p.wall * 2, both=True)
        )
        try:
            body = body.cut(slot)
        except Exception:
            pass
    return body


def _cut_lockbox(body: cq.Workplane, p: LockerParams) -> cq.Workplane:
    """Rebaje interno para caja de cerradura + ESP32, del lado del cierre."""
    sign = -1 if p.hinge_side == "left" else 1   # cerradura opuesta a bisagra
    x = sign * (p.inner_width / 2 - p.lock_box_w / 2 + p.wall / 2)
    z = p.wall + p.inner_height / 2
    box = (
        cq.Workplane("XY")
        .box(p.lock_box_w, p.lock_box_d, p.lock_box_h, centered=(True, True, False))
        .translate((x, p.ext_depth - p.wall - p.lock_box_d / 2, z - p.lock_box_h / 2))
    )
    try:
        return body.cut(box)
    except Exception:
        return body


# ---------------------------------------------------------------------------
# Puerta
# ---------------------------------------------------------------------------
def build_door(p: LockerParams) -> cq.Workplane:
    """Puerta según variante. Se modela en su propio origen (centrada en XY)."""
    dw, dh, dt = p.door_width, p.door_height, p.door_thickness

    door = (
        cq.Workplane("XY")
        .box(dw, dt, dh, centered=(True, True, True))
    )
    try:
        door = door.edges("|Y").fillet(p.corner_fillet * 0.6)
    except Exception:
        pass

    if p.variant == "clear":
        # Marco perimetral: se vacía el centro (ahí va el policarbonato transparente).
        frame = 45.0  # ancho del marco
        window = (
            cq.Workplane("XY")
            .box(dw - 2 * frame, dt * 2, dh - 2 * frame, centered=(True, True, True))
        )
        door = door.cut(window)
        # Nota: el "vidrio" transparente se agrega en el assembly como pieza aparte.
    else:  # glow
        # Rebaje circular para el aro LED WS2812 (embutido a ras), arriba y centrado,
        # más un paso de cable pasante.
        ring_cz = dh / 2 - p.led_ring_dia
        recess = (
            cq.Workplane("XZ")
            .cylinder(p.led_ring_recess * 2, p.led_ring_dia / 2)
            .translate((0, dt / 2, ring_cz))
        )
        cable = (
            cq.Workplane("XZ")
            .cylinder(dt * 3, p.led_hole_d / 2)
            .translate((0, 0, ring_cz))
        )
        door = door.cut(recess).cut(cable)

    # Rebaje de agarre (semiesfera) del lado del cierre para tirar sin manija.
    sign = 1 if p.hinge_side == "left" else -1
    grip = (
        cq.Workplane("XY")
        .sphere(p.handle_recess_d / 2)
        .translate((sign * (dw / 2 - p.handle_recess_d / 2 - 15), dt / 2, 0))
    )
    try:
        door = door.cut(grip)
    except Exception:
        pass

    return door


def door_profile_2d(p: LockerParams) -> cq.Workplane:
    """Perfil 2D plano de la puerta para corte láser/CNC (contorno + calados).

    Devuelve wires 2D en el plano XY -> se exporta limpio a DXF y SVG.
    Es lo que realmente se manda a cortar (melamina, acrílico, chapa o
    policarbonato según variante).
    """
    dw, dh = p.door_width, p.door_height
    sign = 1 if p.hinge_side == "left" else -1

    # Cada loop se construye como un wire independiente y se combinan con .add()
    # -> DXF/SVG con contorno exterior + calados separados (listos para cortar).
    loops = [cq.Workplane("XY").rect(dw, dh)]  # contorno exterior

    if p.variant == "clear":
        frame = 45.0
        loops.append(cq.Workplane("XY").rect(dw - 2 * frame, dh - 2 * frame))  # ventana
    else:  # glow
        loops.append(
            cq.Workplane("XY").center(0, dh / 2 - p.led_ring_dia)
              .circle(p.led_hole_d / 2)  # paso de cable del aro LED (el rebaje se fresa aparte)
        )

    # Agujero de agarre del lado del cierre
    gx = sign * (dw / 2 - p.handle_recess_d / 2 - 15)
    loops.append(cq.Workplane("XY").center(gx, 0).circle(p.handle_recess_d / 2))

    prof = loops[0]
    for extra in loops[1:]:
        prof = prof.add(extra)
    return prof


def _clear_window_glass(p: LockerParams) -> cq.Workplane:
    """Panel transparente para la variante Clear (pieza separada, para preview)."""
    dw, dh = p.door_width, p.door_height
    frame = 45.0
    return (
        cq.Workplane("XY")
        .box(dw - 2 * frame + 10, 3, dh - 2 * frame + 10, centered=(True, True, True))
    )


# ---------------------------------------------------------------------------
# Ensamble (gabinete + puerta cerrada), coloreado
# ---------------------------------------------------------------------------
def build_assembly(p: LockerParams) -> cq.Assembly:
    body = build_body(p)
    door = build_door(p)

    # Posición de la puerta: pegada al frente (+Y). El cuerpo está centrado en Y,
    # así que su cara frontal está en +ext_depth/2.
    door_y = p.ext_depth / 2 + p.door_thickness / 2 + p.door_gap
    door_z = p.ext_height / 2  # centrada respecto al hueco (cuerpo en Z:[0,ext_height])

    door_color = p.color_door_clear if p.variant == "clear" else p.color_door_glow

    asm = cq.Assembly(name=f"LockIt_{p.variant}")
    asm.add(body, name="gabinete", color=cq.Color(*p.color_body))
    asm.add(door, name="puerta",
            loc=cq.Location(cq.Vector(0, door_y, door_z)),
            color=cq.Color(*door_color))

    if p.variant == "clear":
        glass = _clear_window_glass(p)
        asm.add(glass, name="policarbonato",
                loc=cq.Location(cq.Vector(0, door_y, door_z)),
                color=cq.Color(0.6, 0.8, 0.9, 0.35))
    return asm


def build_column(p: LockerParams) -> cq.Assembly:
    """Columna de N módulos apilados (una 'pared' de lockers)."""
    asm = cq.Assembly(name=f"LockIt_columna_{p.variant}")

    # Base / zócalo
    base = (
        cq.Workplane("XY")
        .box(p.ext_width, p.ext_depth, p.base_height, centered=(True, True, False))
    )
    asm.add(base, name="base", color=cq.Color(*p.color_body))

    for i in range(p.doors_per_column):
        z = p.base_height + i * p.ext_height
        mod = build_assembly(p)
        asm.add(mod, name=f"modulo_{i+1}", loc=cq.Location(cq.Vector(0, 0, z)))

    return asm
