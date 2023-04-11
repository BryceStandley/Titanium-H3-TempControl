import time
import board
import adafruit_dht
import psutil
import RPi.GPIO as GPIO

sensor = adafruit_dht.DHT11(board.D16)

def sensorSetup():
	GPIO.setup(20, GPIO.OUT)
	

def sensorRead():
	temp = sensor.temperature
	return temp

def setOutput(value):
	if value is True :
		GPIO.output(board.D20, 1)
	else:
		GPIO.output(board.D20, 0)
