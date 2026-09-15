# Identidad de marca · LockIt

> Sistema de identidad propio y ownable, diseñado para que LockIt **no parezca genérico ni
> hecho con plantilla**. Todo —colores, logo, tipografía, botones, animaciones— sale de una
> misma idea: **el pulso del toque**, el instante en que acercás el celu y el locker se abre.

---

## Idea central

**"El pulso."** LockIt captura ese microsegundo mágico: tap → onda → clic → abierto. Esa onda
que se expande es el ADN visual de la marca: aparece en el logo, en el LED que respira, en el
hover de los botones, en la animación del 3D. Nada es decoración: todo repite el gesto del
producto.

---

## Paleta (ownable)

Nombres propios para que el equipo hable el mismo idioma. Sesgo de neutros hacia el verde-pulso.

| Token | Nombre | Hex | Uso |
|---|---|---|---|
| `--graf` | **Grafito** | `#0E1417` | Fondo principal / metal del locker (sesgo teal, no negro puro). |
| `--graf-2` | Grafito claro | `#161F24` | Paneles, tarjetas sobre fondo oscuro. |
| `--niebla` | **Niebla** | `#EAF0ED` | Fondo del tema claro. |
| `--pulso` | **Pulso** ⭐ | `#10E0A0` | **Color de marca.** Estado LIBRE, acentos, CTA. Verde-menta vívido y propio. |
| `--pulso-deep` | Pulso profundo | `#0C8F65` | Pulso sobre fondos claros (contraste de texto). |
| `--senal` | **Señal** | `#FF8A3D` | Estado OCUPADO / segundo acento cálido (rompe el cliché del "único pop verde"). |
| `--cristal` | Cristal | `#74D3F0` | Detalle del policarbonato / línea Clear. |
| `--ink` | Tinta | `#EAF2EC` / `#10201A` | Texto (según tema). |

**Regla de oro:** el **Pulso** es la estrella y se usa con moderación (CTA, estado, un
detalle por sección). El **Señal** (ámbar) solo para "ocupado" y micro-acentos. Nunca los dos
gritando a la vez.

### Semántica de estado (parte del producto y de la marca)
- 🟢 **Pulso** = Libre / abierto / éxito.
- 🟠 **Señal** = Ocupado / en proceso.
- 🔵 **Cristal** = Info / línea Clear.

---

## Logo

Marca gráfica: una **puerta de locker redondeada** cuyo arco de cerradura se transforma en una
**onda de pulso**, con un **punto de estado** (el LED / el tap NFC).

- Versión completa: símbolo + wordmark "LockIt" (Archivo ExtraBold, tracking ajustado).
- Isotipo (ícono/app/favicon): solo el símbolo, en un cuadrado redondeado grafito con el
  pulso en verde.
- Construcción y SVGs de referencia: [`logo.svg`](logo.svg) e [`isotipo.svg`](isotipo.svg).
- Área de protección: el alto del punto de estado alrededor del logo. No deformar, no rotar,
  no cambiar los colores fuera de las variantes definidas.

### Variantes de color del logo
- Sobre grafito: símbolo en Pulso, wordmark en Niebla.
- Sobre claro: símbolo en Pulso profundo, wordmark en Grafito.
- Monocromo (grabado en la puerta física): un solo tono, sin relleno de estado.

---

## Tipografía

| Rol | Familia | Uso |
|---|---|---|
| **Display** | **Archivo** (700–800) | Títulos. Industrial, ancha, con carácter de señalética/producto. |
| **Texto** | **IBM Plex Sans** (400–600) | Cuerpo. Técnica, cálida, legible. |
| **Dato/UI** | **IBM Plex Mono** (400–600) | IDs de locker (`GYM01·014`), labels, estados, specs. El toque "máquina". |

Pareja elegida a propósito para **no** caer en el default de IA (Inter / Space Grotesk).
Titulares con `text-wrap: balance`, labels en mayúscula con `letter-spacing` amplio.

---

## Motion (lenguaje de animación)

Todo se mueve con el **gesto del pulso**: una onda que se expande con easing suave
(`cubic-bezier(.4,0,.2,1)`), nunca rebotes exagerados.

- **LED / estado:** respira (opacidad + halo) en loop lento.
- **Botones:** al hover, una onda de pulso sale desde el centro; leve `translateY(-1px)`.
- **3D showcase:** al scrollear, los lockers se **desarman y arman** (exploded view) y el
  modelo rota; el scroll es el "dial" de la animación.
- **Reveal:** las secciones entran desde un estado ya visible (nunca parten de opacidad 0
  esperando scroll para poder leerse).
- Respetar siempre `prefers-reduced-motion`: sin ondas ni auto-rotación, versión estática.

---

## Voz y tono

- **Directo y argentino, sin ser grasa.** "Tu locker, un toque." "Sacá las llaves del medio."
- Técnico cuando toca (specs), humano cuando vende (beneficios).
- Los controles dicen exactamente qué pasa: botón "Abrir mi locker" → "¡Abierto!".

---

## Aplicaciones

- **Web:** landing con 3D en vivo ([`../landing/`](../landing/)) y webapp NFC ([`../webapp/`](../webapp/)).
- **Producto físico:** numeración y logo monocromo grabado en la puerta; LED/OLED con la
  semántica de estado.
- **Redes:** ver [`../marketing/`](../marketing/) (los copies y el guion usan esta voz y paleta).
