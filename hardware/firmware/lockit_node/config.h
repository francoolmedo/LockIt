// =============================================================================
// LockIt · config.h  — Configuración del nodo (pines, rol, red, tiempos)
// Toda la configuración editable del firmware vive acá. / All tunables live here.
// =============================================================================
#pragma once

// ---- Rol del dispositivo / Device role -------------------------------------
#define ROLE_NODE     0
#define ROLE_GATEWAY  1
#define DEVICE_ROLE   ROLE_NODE      // cambiar a ROLE_GATEWAY en el nodo puente

// ---- Identidad del locker / Locker identity --------------------------------
#define LOCKER_SITE   "GYM01"        // id del local / site id
#define LOCKER_ID     "014"          // id de esta puerta / this door id

// ---- Variante / Variant ----------------------------------------------------
#define VARIANT_CLEAR 0              // LED de estado
#define VARIANT_GLOW  1              // OLED de estado
#define VARIANT       VARIANT_CLEAR

// ---- Pines / Pins (ESP32 WROOM-32) -----------------------------------------
#define PIN_LOCK      25             // gate del MOSFET -> cerradura / lock MOSFET gate
#define PIN_DOOR      34             // sensor Hall (input only) / door sensor
#define PIN_LED       26             // LED o data WS2812 (Clear)
#define PIN_OLED_SDA  21             // I2C SDA (Glow)
#define PIN_OLED_SCL  22             // I2C SCL (Glow)

// ---- Tiempos / Timings -----------------------------------------------------
#define LOCK_PULSE_MS       200      // pulso para abrir la cerradura / open pulse
#define DOOR_DEBOUNCE_MS    50       // antirrebote del sensor / sensor debounce
#define SESSION_TIMEOUT_MS  90000    // ventana de sesión (90 s) / session window

// ---- Sensor de puerta / Door sensor logic ----------------------------------
// true = el sensor lee LOW cuando la puerta está CERRADA (imán presente)
#define DOOR_CLOSED_IS_LOW  true

// ---- Red del local (solo GATEWAY) / Site WiFi (gateway only) ---------------
#define WIFI_SSID     "WIFI_DEL_GYM"     // completar en instalación
#define WIFI_PASS     "********"
#define MQTT_HOST     "mqtt.lockit.ar"   // broker de la nube / cloud broker
#define MQTT_PORT     8883               // TLS

// ---- ESP-NOW ----------------------------------------------------------------
// Clave pre-compartida de la malla (16 bytes). Cambiar por local en producción.
#define ESPNOW_PMK    "LockIt_PMK_16by"
