<div align="center">

# 🔐 LockIt

**Lockers inteligentes que se abren con un toque.**
Sin llaves, sin candados, sin fichas. Acercás tu celu al tag NFC y tu locker se abre.

*Córdoba, Argentina* · Producto físico + IoT + Web

</div>

---

## ¿Qué es LockIt?

LockIt es un sistema de **casilleros inteligentes** pensado para gimnasios, coworkings,
clubes, escuelas de danza/música, oficinas y aeropuertos. Cada locker se desbloquea
acercando el celular a un **tag NFC** pegado en la puerta, que abre una **webapp rápida**
y linda; la cerradura se libera sola. Un **sensor magnético** confirma si la puerta quedó
bien cerrada, y todos los lockers se comunican **en malla** por el WiFi del local para
mostrar, en conjunto, cuáles están libres y cuáles ocupados.

### El problema que resuelve
- **Llaves y fichas que se pierden**, se roban o hay que reponer.
- **No saber qué locker está libre** sin ir probando puerta por puerta.
- **Candados propios** que el local no controla ni puede liberar.
- Una experiencia **anticuada** en lugares que quieren verse modernos.

### La propuesta
- 📱 **Apertura con NFC**: acercás el celu, se abre. Cero fricción, cero app para instalar.
- 👀 **Estado visible**: dos líneas de producto —
  - **LockIt Clear** → puerta transparente (ves si hay algo adentro) + LED de estado.
  - **LockIt Glow** → puerta opaca + indicador OLED/LED "fachero".
- 🕸️ **Red en malla**: los lockers se hablan entre sí y con un panel central.
- 🔒 **Confirmación real de cierre**: sensor de efecto Hall + imán detecta puerta cerrada.
- 🧰 **Control del local**: panel para asignar, liberar, ver ocupación y cobrar por uso.

---

## Estructura del repositorio

Este repo es un **monorepo** que contiene todo el proyecto: producto físico, electrónica,
firmware, software y go-to-market.

| Carpeta | Qué hay |
|---|---|
| [`docs/`](docs/) | Visión, **arquitectura técnica**, diseño industrial, fabricación en Córdoba, modelo de negocio y roadmap. |
| [`hardware/`](hardware/) | **BOM** (lista de materiales con costos), esquemático de conexiones y **firmware** del ESP32. |
| [`cad/`](cad/) | Modelo **CAD paramétrico** del locker (por código, exporta STEP/STL/DXF) y planos. |
| [`webapp/`](webapp/) | La **webapp** que se abre al escanear el NFC (prototipo funcional). |
| [`landing/`](landing/) | **Landing page** animada para vender el producto. |
| [`marketing/`](marketing/) | Estrategia, copies de redes, guion de animación y outreach a empresas. |
| [`brand/`](brand/) | Identidad de marca (nombre, tono, paleta, dirección de logo). |

### Por dónde empezar a leer
1. [`docs/01-vision-y-producto.md`](docs/01-vision-y-producto.md) — qué construimos y para quién.
2. [`docs/02-arquitectura-tecnica.md`](docs/02-arquitectura-tecnica.md) — **cómo funciona todo el sistema**.
3. [`docs/06-roadmap.md`](docs/06-roadmap.md) — el camino de prototipo → piloto → producción.

---

## Estado del proyecto

🌱 **Etapa 1 — Fundación** (actual). Se define el producto, la arquitectura, el CAD, la
landing y el go-to-market. Todavía **no hay prototipo físico armado**.

Ver el detalle de etapas en [`docs/06-roadmap.md`](docs/06-roadmap.md).

---

## Líneas de producto

| | **LockIt Clear** | **LockIt Glow** |
|---|---|---|
| Puerta | Transparente (policarbonato/acrílico) | Opaca (melamina/chapa) |
| Estado | Se ve el interior + LED | Indicador OLED/LED en la puerta |
| Ideal para | Gimnasios, clubes, escuelas | Oficinas, coworkings, uso premium |
| Costo relativo | Menor | Mayor (más electrónica) |

---

## Licencia

Ver [`LICENSE`](LICENSE).

> ⚠️ Este README y los documentos del repo son material de trabajo interno del proyecto.
> Precios, proveedores y especificaciones son estimaciones a validar en Córdoba.
