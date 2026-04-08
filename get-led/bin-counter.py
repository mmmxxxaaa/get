import RPi.GPIO as GPIO
import time

leds = [16, 12, 25, 17, 27, 23, 22, 24]
num = 0
sleep_time = 0.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up_button = 9
down_button = 10
GPIO.setup(up_button, GPIO.IN)
GPIO.setup(down_button, GPIO.IN)

def DecToBin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(up_button):
        num = (num + 1) % 256
    
    elif GPIO.input(down_button):
        if num != 0:
            num = (num - 1)
    
    print(num, DecToBin(num))
    time.sleep(sleep_time)
    GPIO.output(leds, DecToBin(num))