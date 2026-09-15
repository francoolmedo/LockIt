# Firmware · Nodo LockIt (ESP32)

Firmware del **nodo** de cada puerta. Un nodo puede correr en dos roles:
- **NODO**: controla su cerradura, lee el sensor de puerta, muestra estado, habla por ESP-NOW.
- **GATEWAY**: además, se conecta al WiFi del local y hace de puente con la nube (MQTT).

## Toolchain

Recomendado **PlatformIO** (VS Code) por manejo de librerías y multi-target. Alternativa:
Arduino IDE.

```ini
; platformio.ini (ejemplo)
[env:lockit_node]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
lib_deps =
    ; olikraus/U8g2                 ; OLED (variante Glow)
    ; fastled/FastLED               ; LED WS2812 (variante Clear con anillo)
    ; knolleary/PubSubClient        ; MQTT (solo gateway)
```

## Estructura

```
lockit_node/
├── config.h          # pines, rol, red, tiempos — TODO lo configurable
├── lockit_node.ino   # setup/loop + máquina de estados del locker
```

> Es un **esqueleto** para arrancar el prototipo: define la máquina de estados, el control de
> cerradura por pulso, la lectura del sensor Hall y los stubs de ESP-NOW/MQTT. La lógica de
> red real (emparejar peers ESP-NOW, protocolo de mensajes, MQTT topics) se completa en la
> Etapa 2 al armar el primer nodo físico.

## Máquina de estados del locker

```
LIBRE ──(reserva desde app)──> RESERVADO
RESERVADO ──(comando abrir)──> ABRIENDO ──(pulso cerradura)──> ABIERTO
ABIERTO ──(sensor: puerta cerrada)──> OCUPADO
OCUPADO ──(dueño abre de nuevo)──> ABIERTO
OCUPADO ──(liberar / fin sesión)──> LIBRE
```

## Protocolo ESP-NOW (borrador)

Mensajes cortos entre gateway y nodos:

| Tipo | Dirección | Payload |
|---|---|---|
| `OPEN` | gateway → nodo | id_locker |
| `STATE` | nodo → gateway | id_locker, estado, puerta(abierta/cerrada), rssi |
| `PING`/`PONG` | ambos | keepalive de malla |
| `ASSIGN` | gateway → nodo | id_locker ← sesión/usuario |

Se cifra con clave pre-compartida (PMK/LMK de ESP-NOW). Detalle de seguridad en
[`../../docs/02-arquitectura-tecnica.md`](../../docs/02-arquitectura-tecnica.md#8-seguridad-y-privacidad).
