"""
LockIt · Parámetros del módulo de locker (mercado ancla: GIMNASIO)
==================================================================

Todas las dimensiones en MILÍMETROS. Este archivo es la única fuente de verdad
de las medidas: lo importan `lockit_module.py` y `build.py`. Cambiá acá y todo
el CAD y los planos se regeneran coherentes.

Variantes:
  - "clear": puerta transparente (policarbonato/acrílico) + LED de estado.
  - "glow" : puerta opaca (melamina/chapa) + ventana para indicador OLED.
"""

from dataclasses import dataclass, field


@dataclass
class LockerParams:
    # --- Dimensiones internas útiles (lo que entra: mochila de gym, toalla, botella) ---
    inner_width: float = 300.0     # ancho interior
    inner_height: float = 400.0    # alto interior
    inner_depth: float = 450.0     # profundidad interior

    # --- Estructura ---
    wall: float = 15.0             # espesor de panel (melamina 15mm / chapa plegada equiv.)
    door_gap: float = 2.0          # luz perimetral de la puerta respecto al marco
    door_thickness: float = 12.0   # espesor de la puerta

    # --- Puerta / bisagra ---
    hinge_side: str = "left"       # "left" | "right"
    handle_recess_d: float = 40.0  # diámetro del rebaje/agarre para tirar

    # --- Electrónica y cerradura (alojamientos) ---
    lock_box_w: float = 60.0       # caja de cerradura+ESP32 (ancho)
    lock_box_h: float = 80.0       # (alto)
    lock_box_d: float = 40.0       # (profundidad, sobresale hacia adentro)

    # --- Ventilación (que no junte olor/humedad en el gym) ---
    vent_slot_w: float = 40.0
    vent_slot_h: float = 6.0
    vent_rows: int = 3

    # --- Variante e indicador ---
    variant: str = "clear"         # "clear" | "glow"
    # Clear: agujero para LED puntual. Glow: ventana rectangular para OLED.
    led_hole_d: float = 8.0
    oled_win_w: float = 30.0
    oled_win_h: float = 15.0

    # --- Columna (apilado vertical de módulos) ---
    doors_per_column: int = 4      # cuántas puertas apiladas por columna
    base_height: float = 100.0     # zócalo/base de la columna
    top_cap: float = 20.0          # tapa superior

    # --- Redondeos estéticos (carácter de producto, no caja industrial) ---
    corner_fillet: float = 6.0     # radio de aristas exteriores visibles

    # --- Colores para preview (no afecta fabricación) ---
    color_body: tuple = (0.14, 0.15, 0.18)     # gris grafito
    color_door_clear: tuple = (0.55, 0.75, 0.85)  # policarbonato tintado
    color_door_glow: tuple = (0.11, 0.12, 0.14)   # opaca oscura
    color_accent: tuple = (0.10, 0.85, 0.55)      # verde LockIt

    # --- Dimensiones derivadas ---
    @property
    def ext_width(self) -> float:
        return self.inner_width + 2 * self.wall

    @property
    def ext_height(self) -> float:
        return self.inner_height + 2 * self.wall

    @property
    def ext_depth(self) -> float:
        return self.inner_depth + self.wall  # fondo cerrado, frente abierto

    @property
    def door_width(self) -> float:
        return self.ext_width - 2 * self.door_gap

    @property
    def door_height(self) -> float:
        return self.ext_height - 2 * self.door_gap

    @property
    def column_height(self) -> float:
        return self.base_height + self.doors_per_column * self.ext_height + self.top_cap


# Presets listos para usar
GYM_CLEAR = LockerParams(variant="clear")
GYM_GLOW = LockerParams(variant="glow")

# Un módulo "grande" opcional (para mochilas grandes / cascos / aeropuerto)
GYM_LARGE_CLEAR = LockerParams(
    variant="clear", inner_width=350, inner_height=550, inner_depth=500,
    doors_per_column=3,
)


if __name__ == "__main__":
    for name, p in [("GYM_CLEAR", GYM_CLEAR), ("GYM_GLOW", GYM_GLOW)]:
        print(f"{name}: ext {p.ext_width:.0f} x {p.ext_height:.0f} x {p.ext_depth:.0f} mm "
              f"| columna de {p.doors_per_column} = {p.column_height:.0f} mm de alto")
