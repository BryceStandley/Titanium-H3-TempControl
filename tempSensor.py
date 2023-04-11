import time
import board
import adafruit_dht
import psutil
import RPi.GPIO as GPIO

def sensorSetup():
	# We first check if a libgpiod process is running. If yes, we kill it!
	for proc in psutil.process_iter():
		if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
			proc.kill()
	sensor = adafruit_dht.DHT11(board.D16)

def sensorRead():
	temp = sensor.temperature
	humidity = sensor.humidity
	return temp

def setOutput(value):
	if value is True :
		GPIO.output(board.D20, GPIO.HIGH)
	else:
		GPIO.output(board.D20, GPIO.LOW)
