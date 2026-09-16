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

La piel de todo eso es **premium, oscura y cálida** — inspirada en el código visual de los
smart gyms de Córdoba (negro + oro, tipo Qivox): elegante, moderno y con carácter, lejos del
look "genérico de IA".

---

## Paleta (ownable)

Nombres propios para que el equipo hable el mismo idioma. Base carbón cálido + oro como
protagonista.

| Token | Nombre | Hex (oscuro / claro) | Uso |
|---|---|---|---|
| `--carbon` | **Carbón** | `#100E0B` / `#15120E` | Fondo principal / metal del locker. Casi negro **cálido** (no teal). |
| `--panel` | Panel | `#1C1811` / `#FBF7F0` | Tarjetas y superficies. |
| `--oro` | **Oro / Ámbar** ⭐ | `#E7A23C` | **Color de marca.** CTA, acentos, logo. Cálido, premium. |
| `--oro-hi` | Oro alto | `#F2B255` | Hover / brillo. |
| `--coral` | **Coral** | `#F0764F` | Segundo acento, amigable y trendy. Energía / estado "ocupado". |
| `--crema` | Crema | `#F0E6D6` | Detalle cálido / textos sobre carbón. |
| `--ink` | Tinta | `#F3EEE6` / `#211A12` | Texto (según tema). |

**Regla de oro:** el **Oro** es la estrella y se usa con intención (CTA, estado, un detalle
por sección). El **Coral** aporta calidez/energía como segundo acento. Nunca los dos gritando
a la vez; el resto es carbón y cremas.

### Semántica de estado (parte del producto y de la marca)
- 🟡 **Oro** = Libre / abierto / disponible (glow cálido que invita).
- 🟠 **Coral** = Ocupado / en proceso / energía.
- Luz general **cálida** (no fría): el producto se ve acogedor, no de laboratorio.

---

## Logo

Marca gráfica: un **candado premium** en oro con un **marco interior grabado** que evoca la
puertita del locker (el chiche que le da personalidad), y el ojo de cerradura calado.
Significado directo: **seguridad + se abre fácil**.

- Versión completa: símbolo + wordmark "LockIt" (Archivo 800, "It" en oro, tracking ajustado).
- Isotipo (ícono/app/favicon): el candado dentro de un cuadrado redondeado carbón. El calado
  del ojo de la cerradura usa el color del fondo (se lee como hueco real).
- Construcción y SVGs de referencia: [`logo.svg`](logo.svg) e [`isotipo.svg`](isotipo.svg).
- Área de protección: el alto del cuerpo del candado alrededor del logo. No deformar, no
  rotar, no cambiar los colores fuera de las variantes definidas.

### Variantes de color del logo
- Sobre carbón: símbolo en Oro, wordmark en Crema.
- Sobre claro: símbolo en Oro, wordmark en Carbón.
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
- **Producto físico:** numeración y logo monocromo grabado en la puerta; aro LED de color con la
  semántica de estado (verde libre · ámbar reservado · azul ocupado).
- **Redes:** ver [`../marketing/`](../marketing/) (los copies y el guion usan esta voz y paleta).
