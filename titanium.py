# GPIO functions related to the Libre Computers Titanium H3

# Sensors connected to GPIO 21

try:
    from RPi.GPIO import GPIO
    import board
    import busio
except:
    import VPi.GPIO as GPIO
    import VPi.board as board
    import VPi.busio as busio

channel = 21 #GPIO for sensor 1
output = 16 # GPIO output to switch
outputState = False # State tracker of output GPIO
thresholdTemp = 30 # threshold temperature before output is turned on in c

def SetupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.input)
    GPIO.setup(output, GPIO.output, GPIO.LOW)
    GPIO.add_event_detect(channel, GPIO.BOTH, SensorCallback, bouncetime=300)
    GPIO.add_event_callback(channel, SensorCallback)
    return True

def SensorCallback(channel):
    input = GPIO.input(channel)
        #convert to c
    if input >= thresholdTemp and not(outputState):
        GPIO.output(output, GPIO.HIGH)
        outputState = True
    elif input < thresholdTemp and outputState:
        GPIO.output(output, GPIO.LOW)
        outputState = False
        