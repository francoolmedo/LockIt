"""
LockIt · Render de los STL a PNG (capturas del 3D)
=================================================
Sin dependencias extra: parsea STL binario y rendea con matplotlib (Agg).
Genera vistas 3/4 y frontal de cada variante en cad/exports/renders/.

Uso:  python cad/render.py
"""
import os, struct
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.join(HERE, "exports")
OUT = os.path.join(EXP, "renders")
os.makedirs(OUT, exist_ok=True)


def load_stl_binary(path):
    with open(path, "rb") as f:
        f.read(80)                                   # header
        n = struct.unpack("<I", f.read(4))[0]        # nº de triángulos
        data = f.read(n * 50)
    tris = np.zeros((n, 3, 3), dtype=np.float32)
    normals = np.zeros((n, 3), dtype=np.float32)
    for i in range(n):
        base = i * 50
        vals = struct.unpack("<12f", data[base:base + 48])
        normals[i] = vals[0:3]
        tris[i, 0] = vals[3:6]
        tris[i, 1] = vals[6:9]
        tris[i, 2] = vals[9:12]
    return tris, normals


def shade(normals, base_rgb, light=(0.35, 0.8, 0.5)):
    """Sombreado Lambert simple por triángulo."""
    l = np.array(light, dtype=float); l /= np.linalg.norm(l)
    nn = normals.copy()
    mag = np.linalg.norm(nn, axis=1, keepdims=True); mag[mag == 0] = 1
    nn = nn / mag
    lam = np.clip(nn @ l, 0, 1) * 0.75 + 0.25       # 0.25..1.0
    base = np.array(base_rgb)
    return np.clip(base[None, :] * lam[:, None], 0, 1)


def render(stl_path, out_png, base_rgb, title, elev=15, azim=35):
    tris, normals = load_stl_binary(stl_path)
    fc = shade(normals, base_rgb)

    fig = plt.figure(figsize=(7, 8), dpi=130)
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("none"); fig.patch.set_facecolor("#0d1512")

    coll = Poly3DCollection(tris, facecolors=fc, edgecolors=(0, 0, 0, 0.06), linewidths=0.1)
    ax.add_collection3d(coll)

    # Encuadre / límites iguales
    pts = tris.reshape(-1, 3)
    mins, maxs = pts.min(0), pts.max(0)
    ctr = (mins + maxs) / 2; span = (maxs - mins).max() / 2
    ax.set_xlim(ctr[0]-span, ctr[0]+span)
    ax.set_ylim(ctr[1]-span, ctr[1]+span)
    ax.set_zlim(ctr[2]-span, ctr[2]+span)
    try: ax.set_box_aspect((1, 1, 1))
    except Exception: pass

    ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off()
    ax.set_title(title, color="#eaf2ec", fontsize=15, fontweight="bold", pad=2, family="monospace")
    fig.text(0.5, 0.045, "LockIt · casilleros inteligentes NFC", ha="center",
             color="#2bd48a", fontsize=10, family="monospace")
    fig.savefig(out_png, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  ✓", os.path.relpath(out_png, HERE))


def main():
    jobs = [
        ("lockit_clear_modulo.stl", (0.60, 0.79, 0.88), "LockIt CLEAR — puerta transparente", 35, 15),
        ("lockit_clear_modulo.stl", (0.60, 0.79, 0.88), "LockIt CLEAR — 3/4 frontal", 62, 10),
        ("lockit_glow_modulo.stl",  (0.20, 0.24, 0.27), "LockIt GLOW — puerta opaca + OLED", 35, 15),
        ("lockit_clear_gabinete.stl",(0.34, 0.40, 0.44), "LockIt — gabinete abierto (interior)", 30, 22),
    ]
    print("▶ Renderizando 3D...")
    for i, (stl, rgb, title, azim, elev) in enumerate(jobs, 1):
        p = os.path.join(EXP, stl)
        if not os.path.exists(p):
            print("   (falta", stl, "- corré build.py primero)"); continue
        out = os.path.join(OUT, f"lockit_render_{i:02d}.png")
        render(p, out, rgb, title, elev=elev, azim=azim)
    print("✅ Renders en:", OUT)


if __name__ == "__main__":
    main()
