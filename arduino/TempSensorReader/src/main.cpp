#include "Arduino.h"
#include <math.h>
#include "DHT.h"

int dhtPin = 2;
DHT dht(dhtPin, DHT11);

void setup()
{
  dht.begin();
  Serial.begin(9600);
}

void loop()
{

  Serial.println(dht.readTemperature());

  delay(2000);
}