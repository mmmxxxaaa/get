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
    up_state = GPIO.input(up_button)
    down_state = GPIO.input(down_button)
    if up_state and down_state:
        num = 2**len(leds) - 1
    elif up_state:
        num = (num + 1) % 256
    elif down_state:
        if num != 0:
            num = (num - 1)
    
    print(num, DecToBin(num))
    time.sleep(sleep_time)
    GPIO.output(leds, DecToBin(num))