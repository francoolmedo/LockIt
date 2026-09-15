# 01 · Visión y Producto

## La visión

Convertir el casillero —un objeto tonto que no cambió en 50 años— en un **punto de
contacto inteligente** entre un local y sus clientes. LockIt vende dos cosas al mismo
tiempo:

1. A la **persona que lo usa**: una experiencia mágica y sin fricción (acercás el celu, se abre).
2. Al **local que lo compra**: control, datos de uso, una nueva fuente de ingresos y una
   imagen moderna, sin tener que manejar llaves ni reponer candados.

> **Frase ancla:** *"Tu locker, un toque."*

---

## Para quién (segmentos)

Mercado **ancla: gimnasios** (donde arrancamos). Después escalamos:

| Segmento | Dolor principal | Qué valora | Modelo de cobro típico |
|---|---|---|---|
| **Gimnasios** 🏋️ (ancla) | Candados propios, robos, "¿cuál está libre?" | Higiene, rapidez, imagen premium | Incluido en cuota / venta al gym |
| Coworkings / oficinas | Asignación de casillero fijo, seguridad | Estética sobria, control de accesos | Venta o alquiler mensual |
| Clubes / danza / música | Uso por clase/evento, rotación alta | Robustez, asignación rápida | Venta al club |
| Aeropuertos / público | Anonimato, seguridad, cobro por uso | Normativa, pago integrado | Pago por uso (self-service) |

La **decisión de foco** (gimnasios) fija: tamaño de módulo mediano, materiales que aguantan
humedad y uso intenso, y un pitch centrado en higiene + imagen + cero-llaves.

---

## Propuesta de valor

### Para el usuario final
- **Cero llaves, cero fichas, cero candado propio.** Nada que perder ni cargar.
- **Apertura en 2 segundos** acercando el celular al tag NFC (no hace falta instalar app).
- **Saber al toque qué locker está libre** (puerta transparente o indicador luminoso).
- **Seguridad**: solo vos (tu sesión) abrís tu locker durante tu uso.

### Para el local (quien compra)
- **Sin gestión de llaves** ni reposición de candados perdidos.
- **Panel de control**: ver ocupación en vivo, asignar, liberar remotamente, historial.
- **Higiene e imagen**: producto lindo, moderno, que se muestra.
- **Nuevo ingreso**: cobro por uso, alquiler premium de lockers grandes, o valor agregado a la cuota.
- **Instalación simple**: se conecta al WiFi que ya tienen; los módulos se hablan en malla.

---

## Las dos líneas de producto

Decidido con el equipo: lanzamos **dos variantes** que comparten el 90% de la estructura y
la electrónica, cambiando puerta e indicador.

### 🪟 LockIt Clear
- **Puerta transparente** de policarbonato (resistente a golpes) o acrílico (más económico).
- El estado "libre/ocupado" se ve **directo** (hay o no hay cosas) y se **refuerza con un
  LED** perimetral o un punto de luz (verde = libre, azul/rojo = ocupado).
- **Ventaja**: resuelve de una el problema de "¿está usado?" y es la variante **más barata**
  (menos electrónica por puerta).
- **Ideal**: gimnasios, clubes, escuelas — donde ver el interior es un plus de confianza.

### 🌗 LockIt Glow
- **Puerta opaca** (melamina, MDF laminado o chapa plegada) para **privacidad**.
- Indicador **OLED chico** (o anillo/tira LED direccionable) embutido en la puerta que
  muestra estado, número de locker, ícono de "acercá el celu", animaciones.
- **Ventaja**: más "tech", más premium, más privacidad.
- **Ideal**: oficinas, coworkings, uso premium.

> Ambas variantes usan el **mismo nodo electrónico** (ESP32 + NFC + cerradura + sensor de
> puerta). La diferencia de costo está en la puerta y en el indicador (LED simple vs OLED).

---

## Principios de diseño de producto

1. **Cero fricción para el usuario**: no instalar app, no crear cuenta obligatoria, no esperar.
2. **A prueba de local real**: humedad, golpes, uso intenso, gente apurada, poco WiFi.
3. **Falla en seguro**: si se corta internet o luz, hay un modo de apertura garantizado
   (ver [arquitectura](02-arquitectura-tecnica.md#modo-degradado-sin-internet)).
4. **Modular y apilable**: se venden columnas de N puertas; el local arma su pared.
5. **Estético con carácter**: no parece una caja de metal industrial; parece un producto
   de diseño (ver [diseño industrial](03-diseno-industrial.md)).
6. **Fabricable en Córdoba**: materiales y procesos que consigue un taller local.

---

## Qué NO es LockIt (alcance)

- No es una cerradura para puertas de casa (es para casilleros de local comercial).
- No reemplaza la seguridad de una caja fuerte (es conveniencia + control, no alta seguridad
  bancaria).
- En la Etapa 1 **no** procesa pagos reales todavía (se diseña el flujo, se implementa después).

---

## Métricas de éxito (cómo sabremos que funciona)

- ⏱️ **Tiempo de apertura** < 3 s desde que acerca el celu.
- ✅ **Tasa de apertura exitosa** > 99% (que "se abra siempre").
- 🔁 **Confiabilidad del sensor de cierre** (falsos "abierto/cerrado" < 1%).
- 😍 **NPS del usuario** en el piloto del gimnasio.
- 💵 **Costo por puerta** por debajo del objetivo del [modelo de negocio](05-modelo-negocio.md).
