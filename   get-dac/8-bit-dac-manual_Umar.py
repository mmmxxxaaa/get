import RPi.GPIO as GPIO

dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac_pins, GPIO.OUT)
dac_drange_v = 3.3
DAC_DEPTH = 8

def voltage_to_number(voltage):
	if not (0.0 <= voltage <= dac_drange_v):
		print(f'Voltage out of DAC dynamic range [0.0,{dac_drange_v}]V')
		print('0.0V set')
		return 0
	return int(voltage / dac_drange_v * 2**DAC_DEPTH)

def number_to_dac(num: int):
	bits = [int(bit) for bit in bin(num)[2:].zfill(DAC_DEPTH)]
	GPIO.output(dac_pins, bits)

try:
	while True:
		try:
			voltage = float(input("Enter voltage [V]:"))
			num = voltage_to_number(voltage)
			number_to_dac(num)
		except ValueError:
			print("Try again")
finally:
	GPIO.output(dac_pins, 0)
	GPIO.cleanup()

