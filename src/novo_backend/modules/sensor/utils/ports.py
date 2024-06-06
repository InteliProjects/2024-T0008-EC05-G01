import sys
import glob
import serial
from serial.tools import list_ports

def serial_ports():
	"""
		Devolve os dispositivos seriais disponíveis no sistema que se identificam como Raspberry Pi Pico

		:raises EnvironmentError:
			Em caso de erro na detecção do sistema operacional
		:returns:
			Uma lista de portas seriais disponíveis
	"""

	#? Windows
	ports = list_ports.comports()

	rpi_ports = [
		port for port in ports if (
			#? Fonte: https://github.com/raspberrypi/usb-pid
			port.vid == 11914 #? "Vendor-ID = 0x2E8A"
			and port.pid == 5 #? 0x0005 	Raspberry Pi 	Raspberry Pi Pico MicroPython firmware (CDC)
		)
	]

	return [port.device for port in rpi_ports]

serial_ports()