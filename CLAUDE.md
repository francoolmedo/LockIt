# CLAUDE.md — LockIt

Guía para cualquier sesión de Claude que trabaje en este repo. Leer antes de empezar.

## Qué es
**LockIt**: casilleros inteligentes que se abren con un **tag NFC** (sin llaves ni candados),
para gimnasios (mercado ancla) y luego coworkings, clubes, aeropuertos. Córdoba, Argentina.
Monorepo: `docs/` (visión, arquitectura, negocio) · `hardware/` (BOM, firmware ESP32) ·
`cad/` (modelo paramétrico CadQuery → STEP/STL/DXF) · `webapp/` · `panel/` · `landing/` ·
`marketing/` · `brand/`. Índice completo en [`README.md`](README.md).

## Reglas de diseño y voz (IMPORTANTE)
- **Diseño:** todo lo visual sigue **[`brand/DESIGN.md`](brand/DESIGN.md)** (formato tipo
  google-labs/design.md: tokens en YAML + reglas + dials + lista negra de AI-tells). Leerlo
  antes de diseñar. **Dirección activa: "Warm"** (Aesop) — ground **crema cálido** (no oscuro),
  títulos **serif Newsreader**, cuerpo IBM Plex Sans, oro muteado, mucho aire (varianza 7,
  densidad 3), easing `cubic-bezier(.4,0,.2,1)` (nunca bounce). El locker 3D queda sobre banda
  oscura (foto de producto). Variantes oscuras (Dark Room/Editorial) en `landing/variants/`.
- **Texto/copy:** todo el texto sigue **[`brand/VOICE.md`](brand/VOICE.md)** (Humanizer +
  Stop-Slop en español). Sin muletillas de IA, voz activa, no inventar datos → `[placeholder]`.

Lo no negociable de diseño:
- **Usar los tokens de marca** (carbón + oro + coral; Archivo / IBM Plex Sans / IBM Plex Mono).
  Definidos en `brand/DESIGN.md` §1 y `brand/identidad.md`. No inventar colores/tipografías.
- **Referencias antes que descripciones.** Diseñar mirando las referencias de `DESIGN.md` §4,
  no la "mediana". Un **gesto distintivo por pieza**; el resto quieto.
- **Prohibidos (AI-tells)**, ver `DESIGN.md` §2: fuentes genéricas (Inter/Roboto/Space Grotesk),
  gradientes violeta/glass, rail de color al costado de tarjetas, misma sombra en todo, emojis
  como íconos (usar SVG de línea), grilla de 3-features, negro puro + un solo pop, copy tipo
  "elevá tu…". Correr el **checklist §5** antes de publicar ("¿esto lo vi mil veces?").
- El logo es un **candado en oro con marco interior grabado** (`brand/logo.svg`, `isotipo.svg`).

## Convenciones del repo
- **Branch de trabajo:** `claude/smart-nfc-locker-wkg8da`. Commitear y pushear ahí.
- Todo el contenido de cara a cliente/taller va **en español (Córdoba)**.
- CAD: `pip install cadquery` y `python cad/build.py` (exporta a `cad/exports/`).
- **Datos sensibles:** no publicar testimonios ni precios inventados como reales — usar
  plantillas con placeholders hasta tener datos del piloto.
- **Acciones externas:** no publicar en redes ni mandar mails a empresas sin lista + OK
  explícito del usuario.

## Artifacts publicados (links vivos)
- Landing 3D: `claude.ai/artifact/CepHEsEPv8VyLDjGzw8v8m`
- Kit de redes: `claude.ai/artifact/UGQmJ89ahwhAuYNbVSaG1e` · Reel: `.../QuDMYe3GqAKa4rGzLq8dL2`
- Panel del local: `claude.ai/artifact/5emg6niyPqGjkHo7iQ9rs5`
