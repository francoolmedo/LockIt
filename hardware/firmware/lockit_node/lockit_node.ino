// =============================================================================
// LockIt · lockit_node.ino — Firmware del nodo (ESP32)
// Esqueleto funcional: máquina de estados + control de cerradura + sensor de
// puerta + stubs de red (ESP-NOW / MQTT). / Functional skeleton.
//
// NOTA: la capa de red real (peers ESP-NOW, protocolo de mensajes, MQTT) se
// completa en la Etapa 2 al armar el primer nodo físico. Los TODO marcan dónde.
// =============================================================================
#include <Arduino.h>
#include "config.h"

// ---- Estados del locker / Locker states ------------------------------------
enum LockerState { LIBRE, RESERVADO, ABRIENDO, ABIERTO, OCUPADO };
LockerState state = LIBRE;
unsigned long sessionStart = 0;

// ---------------------------------------------------------------------------
// Helpers de hardware / Hardware helpers
// ---------------------------------------------------------------------------
bool doorIsClosed() {
  int v = digitalRead(PIN_DOOR);
  bool closed = DOOR_CLOSED_IS_LOW ? (v == LOW) : (v == HIGH);
  return closed;
}

void pulseLock() {
  // Pulso corto para liberar la cerradura. NUNCA energizar de forma continua.
  digitalWrite(PIN_LOCK, HIGH);
  delay(LOCK_PULSE_MS);
  digitalWrite(PIN_LOCK, LOW);
}

void showState(LockerState s) {
  // Aro LED WS2812 en ambas variantes (Clear y Glow): color por estado.
  // TODO: implementar con FastLED/Adafruit_NeoPixel sobre PIN_LEDRING (LEDRING_COUNT).
  switch (s) {
    case LIBRE:      /* verde  */ break;
    case RESERVADO:  /* ámbar  */ break;
    case ABRIENDO:   /* animación suave */ break;
    case ABIERTO:    /* azul   */ break;
    case OCUPADO:    /* azul fijo */ break;
  }
}

void setState(LockerState s) {
  state = s;
  showState(s);
  reportState();   // avisar al gateway/nube
}

// ---------------------------------------------------------------------------
// Red / Network (stubs)
// ---------------------------------------------------------------------------
void netSetup() {
#if DEVICE_ROLE == ROLE_GATEWAY
  // TODO: WiFi.begin(WIFI_SSID, WIFI_PASS); conectar MQTT (PubSubClient/TLS).
#endif
  // TODO: esp_now_init(); registrar PMK/LMK; agregar peers de la malla.
}

void reportState() {
  // TODO: enviar STATE por ESP-NOW al gateway (id, estado, puerta, rssi).
  //       El gateway lo publica por MQTT a la nube.
}

// Se llama cuando llega un comando OPEN (por ESP-NOW / MQTT). / On OPEN command.
void onOpenCommand() {
  if (state == RESERVADO || state == OCUPADO) {
    setState(ABRIENDO);
    pulseLock();
    setState(ABIERTO);
    sessionStart = millis();
  }
}

// Se llama cuando la app reserva este locker. / On reservation.
void onReserve() {
  if (state == LIBRE) {
    setState(RESERVADO);
    sessionStart = millis();
  }
}

// ---------------------------------------------------------------------------
// setup / loop
// ---------------------------------------------------------------------------
void setup() {
  Serial.begin(115200);
  pinMode(PIN_LOCK, OUTPUT);
  digitalWrite(PIN_LOCK, LOW);
  pinMode(PIN_DOOR, INPUT);
  pinMode(PIN_LEDRING, OUTPUT);   // aro WS2812 (la lib toma este pin de data)

  netSetup();
  setState(LIBRE);
  Serial.printf("LockIt nodo %s-%s listo. Rol=%d Variante=%d\n",
                LOCKER_SITE, LOCKER_ID, DEVICE_ROLE, VARIANT);
}

void loop() {
  // 1) Transiciones por sensor de puerta / door sensor transitions
  static bool lastClosed = true;
  bool closed = doorIsClosed();
  if (closed != lastClosed) {
    delay(DOOR_DEBOUNCE_MS);
    closed = doorIsClosed();
    if (closed != lastClosed) {
      lastClosed = closed;
      if (state == ABIERTO && closed) setState(OCUPADO);   // cerró con cosas
      // (si estaba OCUPADO y abre, el comando OPEN maneja la transición)
    }
  }

  // 2) Timeout de sesión / session timeout -> volver a LIBRE si nunca se usó
  if (state == RESERVADO && millis() - sessionStart > SESSION_TIMEOUT_MS) {
    setState(LIBRE);
  }

  // 3) TODO: procesar mensajes de red entrantes (OPEN/ASSIGN/PING).
  delay(10);
}
