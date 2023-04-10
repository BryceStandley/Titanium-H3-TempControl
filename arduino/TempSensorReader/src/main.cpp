#include "Arduino.h"
#include "DHT.h"



#define DHTPIN 7

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.print("Temperature = ");
  Serial.println(dht.readTemperature());
  Serial.print("Humidity = ");
  Serial.println(dht.readHumidity());
  delay(1000);
}