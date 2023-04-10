
import serial

srl = serial.Serial();

def serialSetUp():
	try:
		srl.port='COM3'
		srl.baudrate=9800
		srl.open()
		print("Serial port Open")
		return True
	except:
		print("Serial port failed to open")
		return False

def serialRead():
	line = srl.readline()
	val = line.decode()
	temp = val.strip()
	f = float(temp)
	return int(f)


