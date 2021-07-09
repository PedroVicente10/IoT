#include <ESP8266WiFi.h>
#include <PubSubClient.h>

   double alpha=0.75;
   int period=20;
   double refresh=0.0;


// WiFi
const char *ssid = "MEO-F93290"; // Enter your WiFi name
const char *password = "c87fb69396";  // Enter WiFi password

// MQTT Broker
const char *mqtt_broker = "192.168.1.79";
const char *topic = "Teste";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(A0,INPUT);
 // Set software serial baud to 115200;
 Serial.begin(115200);
 // connecting to a WiFi network
 WiFi.begin(ssid, password);
 while (WiFi.status() != WL_CONNECTED) {
     delay(500);
     Serial.println("Connecting to WiFi..");
 }
 Serial.println("Connected to the WiFi network");
 //connecting to a mqtt broker
 client.setServer(mqtt_broker, mqtt_port);
 while (!client.connected()) {
     String client_id = "esp8266-client-";
     client_id += String(WiFi.macAddress());
     Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
     if (client.connect(client_id.c_str())) {
         Serial.println("Public emqx mqtt broker connected");
     } 
     else {
         Serial.print("failed with state ");
         Serial.print(client.state());
         Serial.print("\n");
         delay(2000);
     }
 }
}


void loop() {
   client.loop();
   static double oldValue=0;
   static double oldrefresh=0;
   char msg[100]; 
   
   int beat=analogRead(A0);
   int heart_m = beat/10;

   double value=alpha*oldValue+(0-alpha)*beat;
   refresh=value-oldValue;

   Serial.print(" Heart Monitor "); 
   Serial.print("          ");
   Serial.println(heart_m);
   snprintf(msg, 100, "%ld" ,heart_m);
   client.publish(topic,msg);
   
   oldValue=value;
   oldrefresh=refresh;
   delay(period*10);

}
