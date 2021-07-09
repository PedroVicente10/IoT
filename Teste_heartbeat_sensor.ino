#include "Adafruit_MQTT.h"
#include "Adafruit_MQTT_Client.h"
#include "Adafruit_MQTT_FONA.h"

#include <ESP8266WiFi.h>

#define WLAN_SSID      "MEO-F93290"
#define WLAN_PASS      "c87fb69396"

#define AIO_SERVER      "192.168.1.79"
#define AIO_SERVERPORT  5001

WiFiClient client;
Adafruit_MQTT_Client mqtt(&client, AIO_SERVER, AIO_SERVERPORT);

Adafruit_MQTT_Publish Inf = Adafruit_MQTT_Publish(&mqtt,"Teste");

double alpha = 0.75;
int period=20;
double refresh=0.0;

void setup(void)
{
Serial.begin(115200);
 delay(10);
pinMode(A0,INPUT);
unsigned long lastMillis = 0;

Serial.println(F("Adafruit MQTT demo"));

  // Connect to WiFi access point.
  Serial.println(); Serial.println();
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);

  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.println("WiFi connected");
  Serial.println("IP address: "); Serial.println(WiFi.localIP());
}

uint32_t x=0;

void loop(void)
{
    MQTT_connect();
    static double oldValue=0;
    static double oldrefresh=0;
   
    int beat=analogRead(A0)* 5 / 3.3;
    double value=alpha*oldValue+(0-alpha)*beat;

    refresh=value-oldValue;

    Serial.print(" Heart Monitor "); 
    Serial.print("          ");
    Serial.println(beat/10);
    Inf.publish(beat/10);
  
    oldValue=value;
    oldrefresh=refresh;

    delay(period*10);
}

void MQTT_connect() {
  int8_t ret;

  // Stop if already connected.
  if (mqtt.connected()) {
    return;
  }

  Serial.print("Connecting to MQTT... ");

  uint8_t retries = 3;
  while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected
       Serial.println(mqtt.connectErrorString(ret));
       Serial.println("Retrying MQTT connection in 5 seconds...");
       mqtt.disconnect();
       delay(5000);  // wait 5 seconds
       retries--;
       if (retries == 0) {
         // basically die and wait for WDT to reset me
         while (1);
       }
  }
  Serial.println("MQTT Connected!");
}
