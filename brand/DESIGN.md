# Playbook de diseño · LockIt

> Guía para diseñar cualquier pieza de LockIt (web, redes, panel, decks) **con criterio y sin
> "look de IA"**. Toda sesión de Claude (y cualquier diseñador) debe leer esto antes de diseñar.
> Complementa [`identidad.md`](identidad.md) (la marca) con **reglas de ejecución**.

**Regla madre:** el buen gusto sale de **restricción + referencias + un gesto propio**, no de
"hacelo lindo y moderno". Si una decisión la tomaste "porque queda bien en general", pará: es
la mediana, y la mediana es el look de IA.

---

## 1. Tokens (única fuente de verdad)

Usar SIEMPRE estos valores (no inventar colores ni tamaños nuevos sin sumarlos acá primero).

**Color**
| Token | Hex | Uso |
|---|---|---|
| Carbón | `#100E0B` / `#15120E` | Fondo base (casi negro cálido). |
| Panel | `#1B1710` (oscuro) / `#FBF7F0` (claro) | Tarjetas/superficies. |
| Oro | `#E7A23C` (hi `#F2B255`) | Color de marca. CTA, acentos, logo. Con intención. |
| Coral | `#F0764F` | Segundo acento cálido / energía. |
| Tinta | `#F3EEE6` (osc.) / `#211A12` (claro) | Texto. |
| Líneas | `#2A2418` / `#E1D7C6` | Bordes/hairlines. |
| Semánticos (solo estado) | libre `#3BA776` · ocupado `#F0764F` · reservado `#74D3F0` | Estados del producto; **separados del acento de marca**. |

**Tipografía:** Archivo (display, 700–900) · IBM Plex Sans (texto) · IBM Plex Mono (dato/UI).
**Radios:** 9–14px (crisp, no `rounded-2xl` en todo). **Sombra:** una sola, sutil, y **solo
donde algo tiene que elevarse** — no en cada tarjeta.

---

## 2. AI-tells PROHIBIDOS (lista negra)

Si aparece algo de esto, está mal:

**Tipografía**
- ❌ Inter, Roboto, Poppins, Montserrat, Space Grotesk, Lato (las "seguras"/genéricas).
- ❌ Todo en un solo peso; sin jerarquía real de tamaños.

**Color / fondo**
- ❌ Gradiente violeta→azul (o teal→lila) en el hero. Glassmorphism (vidrio esmerilado).
- ❌ Negro puro `#000` con **un único pop** de verde ácido/violeta.
- ❌ Combo crema `#F4F1EA` + serif + terracota (otro cliché de IA).
- ❌ Saturación alta en "blancos"/"negros" (mantener neutros cálidos, casi sin croma).

**Layout / componentes**
- ❌ **Barrita/rail de color al costado** de una tarjeta. (ya la sacamos: no vuelve)
- ❌ La **misma sombra + mismo radio** estampados en TODOS los bloques.
- ❌ Todo centrado, sin asimetría ni tensión.
- ❌ Grilla de 3 "features": ícono + título + parrafito, ×3.
- ❌ **Emojis como íconos** o bullets de sección. Íconos = SVG de línea dibujado, un estilo.
- ❌ Círculos/blobs de color difusos decorativos "de relleno".

**Uso excesivo (nuestro propio riesgo)**
- ⚠️ Eyebrows en monospace (`§01`, `SEG·01`) en **cada** bloque → se vuelve plantilla. Usar
  con moderación, no en todo.
- ⚠️ Grilla de puntos de fondo + marcas de esquina en TODAS las tarjetas → dosificar.

**Copy**
- ❌ "Elevá tu…", "En el mundo de hoy…", "No es solo X, es Y", "seamless", "revolucioná".
- ❌ Exceso de guiones largos (—). Datos/stats de relleno que no aportan.
- ❌ Aclaraciones tipo instrucción o meta ("el detalle wow", "acá iría…").

---

## 3. Reglas de ejecución (lo que SÍ hacemos)

1. **Referencias antes que descripciones.** Antes de diseñar, mirar 2–3 referencias reales
   (ver §4) y sacar de ahí paleta, tipografía y ritmo. Imitar una referencia > inventar.
2. **Un gesto distintivo por pieza.** Cada pieza tiene UNA cosa memorable (un detalle, una
   composición, una animación). El resto, quieto y prolijo. No diez efectos.
3. **Jerarquía real.** Tamaños con contraste fuerte (no todo 16–20px). Un elemento manda.
4. **Espaciado con intención.** Aire generoso O densidad controlada, elegido a propósito.
5. **Restringir la paleta.** Carbón + oro + (a veces) coral. El oro se gana su lugar.
6. **Mirar el resultado a ancho de teléfono** y arreglar lo que rompe, antes de entregar.
7. **Pasada de reducción.** Al final, sacar el 20% que sobra. Menos es más.

---

## 4. Referencias (⚠️ COMPLETAR — Franco)

Pegá acá **3–5 marcas/webs cuyo estilo te vuele la cabeza**. Cuando diseñemos, sacamos el
lenguaje de ESTAS, no del genérico. (Las de abajo son sugerencias de arranque — reemplazalas
por las tuyas.)

- [ ] `[Marca/web 1]` — qué te gusta (paleta / tipografía / composición): `[...]`
- [ ] `[Marca/web 2]` — `[...]`
- [ ] `[Marca/web 3]` — `[...]`

_Sugerencias iniciales para reemplazar/curar:_ Teenage Engineering (industrial premium),
Aesop (editorial cálido), Linear (oscuro nítido), Oura/Whoop (hardware+app), y los gyms que
te gustan (Qivox, etc.). **Elegí y pegá links/capturas.**

---

## 5. Checklist antes de publicar

- [ ] ¿Usé los tokens de §1 (nada inventado)?
- [ ] ¿Hay algo de la lista negra §2? Sacarlo.
- [ ] ¿Tomé algo de una referencia real (§4), no del genérico?
- [ ] ¿Hay UN gesto distintivo y el resto está quieto?
- [ ] ¿Se lee y funciona a ancho de teléfono?
- [ ] Pregunta final honesta: **"¿esto lo vi mil veces?"** Si sí, cambialo.

---

## 6. Herramientas que ayudan
- Skills de Claude: `artifact-design`, `design`, `dataviz` (traen reglas anti-slop).
- Figma MCP (a futuro): conectar un sistema de diseño real y que Claude ejecute con esos tokens.
- Fuentes con carácter: Google Fonts (las menos usadas) o Fontshare.
- Galerías para referencias: godly.website, land-book, minimal.gallery; libro *Refactoring UI*.
