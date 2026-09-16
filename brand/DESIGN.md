---
# DESIGN.md · LockIt — sistema de diseño legible por agentes
# Formato inspirado en google-labs/design.md · reglas de impeccable + taste-skill
name: LockIt
style: Premium industrial cálido — oscuro, nítido, con carácter (no genérico)
colors:
  carbon:        "#100E0B"   # fondo base (dark) — casi negro CÁLIDO, nunca #000
  carbon-2:      "#15120E"
  panel:         "#1B1710"   # superficie (dark)
  panel-light:   "#FBF7F0"   # superficie (light)
  bg-light:      "#F4EFE7"   # fondo base (light) — crema cálido
  oro:           "#E7A23C"   # MARCA / acento primario
  oro-hi:        "#F2B255"   # hover
  oro-deep:      "#B07A1E"   # oro legible sobre claro (texto/borde)
  coral:         "#F0764F"   # acento secundario cálido
  cream:         "#F3EEE6"   # texto sobre carbón
  ink:           "#211A12"   # texto sobre claro
  ink-2:         "#5A4F41"
  ink-3:         "#8A7D6B"
  line:          "#2A2418"   # hairline (dark)
  line-light:    "#E1D7C6"   # hairline (light)
  # Semánticos — SOLO estado de producto, separados del acento de marca
  st-libre:      "#3BA776"
  st-ocupado:    "#F0764F"
  st-reservado:  "#74D3F0"
typography:
  display:  { family: "Archivo",        weights: [700, 800, 900], tracking: "-0.02em" }
  body:     { family: "IBM Plex Sans",  weights: [400, 500, 600] }
  mono:     { family: "IBM Plex Mono",  weights: [400, 500, 600], use: "datos, IDs, labels" }
rounded: { sm: "9px", md: "12px", lg: "14px", pill: "999px" }   # crisp, NO rounded-2xl en todo
spacing: { xs: "6px", sm: "10px", md: "16px", lg: "24px", xl: "40px", xxl: "80px" }
elevation:
  flat:   "none — la mayoría de las superficies (borde, no sombra)"
  raised: "0 10px 30px rgba(20,14,6,.28) — SOLO lo que debe elevarse (1 nivel, no en todo)"
components:
  button-primary: { bg: oro, text: carbon, rounded: sm, weight: 600, shadow: flat, hover: "translateY(-2px)+oro-hi" }
  button-ghost:   { bg: transparent, border: line, text: ink, hover: "border/text → oro" }
  card:           { bg: panel, border: line, rounded: md, shadow: flat, note: "NO anidar cards dentro de cards" }
# Dials (taste-skill) — la personalidad de LockIt
dials:
  variant: "minimalist-premium"   # Linear/Aesop lean, no brutalist ni corporate
  design_variance: 6              # 1 centrado/limpio … 10 asimétrico. 6 = tensión con orden
  motion_intensity: 4             # 1 hover … 10 scroll/magnético. Sutil, con propósito
  visual_density: 5               # 1 espacioso … 10 dashboard denso
  easing: "cubic-bezier(.4,0,.2,1)"   # NUNCA bounce/elastic (se siente viejo)
---

# Sistema de diseño · LockIt

> Leer antes de diseñar cualquier pieza (web, redes, panel, decks). El front matter de arriba
> son los **tokens** (fuente de verdad, no inventar). Abajo, el criterio.
>
> **Regla madre:** buen gusto = restricción + referencias reales + un gesto propio. Si tomaste
> una decisión "porque queda bien en general", es la mediana — y la mediana es el look de IA.

## Overview
LockIt es premium industrial cálido: base carbón (casi negro con temperatura), oro como único
protagonista, coral de apoyo. Nítido, con jerarquía fuerte, y **un** gesto memorable por pieza.
Referencia de altura: Linear (oscuro nítido), Aesop (editorial cálido), Teenage Engineering
(industrial premium).

## Colors
Neutros **siempre tintados** (carbón cálido, cremas), nunca `#000`/`#fff`/gris puro. Oro con
intención (CTA, un acento por sección). Coral escaso. Estados (libre/ocupado/reservado) son
semánticos y viven aparte del acento de marca. Nunca texto gris sobre fondo de color.

## Typography
Archivo para títulos (peso alto, tracking negativo), IBM Plex Sans para cuerpo, IBM Plex Mono
para datos. Jerarquía con **contraste real** de tamaño (no todo 16–20px). Un elemento manda.

## Layout
Grid/flex con `gap`. Varianza 6: buscar asimetría/tensión, no todo centrado. Aire generoso O
densidad elegida a propósito. Gutter lateral ≥16px. Mobile-first: mirar a ~400px y arreglar.

## Elevation & Shapes
Una sola sombra, sutil, **solo** donde algo se eleva — no en cada tarjeta (aplana la jerarquía).
Radios crisp (9–14px). Bordes/hairlines antes que sombras para separar.

## Do's & Don'ts (lista negra de AI-tells)
**Hacer:** tokens de arriba · referencia real antes que descripción · un gesto distintivo por
pieza · jerarquía fuerte · pasada final de reducción (sacar el 20% que sobra).

**Nunca (tells):**
- ❌ Fuentes genéricas: Inter, Roboto, Poppins, Montserrat, Space Grotesk, system defaults.
- ❌ `#000`/gris puro; texto gris sobre fondo de color (Impeccable). Tintar siempre.
- ❌ Gradiente violeta→azul en hero; glassmorphism.
- ❌ **Anidar cards dentro de cards**; envolver todo en tarjetas (Impeccable).
- ❌ Misma sombra + mismo radio en TODOS los bloques.
- ❌ Easing **bounce/elastic** (Impeccable) — usar el `easing` del front matter.
- ❌ Barrita/rail de color al costado de tarjetas.
- ❌ Todo centrado; sin asimetría.
- ❌ Grilla de 3 "features" ícono+título+parrafito ×3.
- ❌ Emojis como íconos/bullets → íconos = SVG de línea, un solo estilo.
- ❌ Negro puro + un único pop de color; combo crema+serif+terracota.
- ⚠️ **Nuestro propio riesgo:** abusar de eyebrows mono (`§01`) + grilla de puntos + marcas de
  esquina en TODO. Dosificar; si se repite en cada bloque, vuelve a ser plantilla.

## Vocabulario de trabajo (impeccable)
Al pedir cambios, usar verbos claros: `polish` (alinear al sistema), `critique` (jerarquía/
claridad), `quieter`/`bolder` (subir/bajar intensidad), `distill` (reducir), `animate`.

## Referencias (⚠️ COMPLETAR — Franco)
Pegá 3–5 marcas/webs que ames; diseñamos sacando el lenguaje de ESTAS. Fuente de más ejemplos:
`github.com/VoltAgent/awesome-design-md` (DESIGN.md reales de Stripe, Apple, Shopify, Tesla…).
- [ ] `[Marca 1]` — qué te gusta: `[...]`
- [ ] `[Marca 2]` — `[...]`
- [ ] `[Marca 3]` — `[...]`

## Checklist antes de publicar
- [ ] Tokens del front matter (nada inventado).
- [ ] Cero ítems de la lista negra.
- [ ] Salió de una referencia real, no del genérico.
- [ ] Un gesto distintivo; el resto quieto.
- [ ] Funciona a ancho de teléfono.
- [ ] Copy pasado por [`VOICE.md`](VOICE.md).
- [ ] Pregunta final: **"¿esto lo vi mil veces?"** → si sí, cambialo.

## Herramientas vivas (opcional, para instalar)
- `npx impeccable install` — detectores de anti-patterns en tiempo real (github.com/pbakaus/impeccable).
- taste-skill (github.com/leonxlnx/taste-skill) — skills por variante (soft/minimal/brutalist).
- google-labs/design.md — CLI para validar/exportar este archivo a Tailwind / W3C tokens.
