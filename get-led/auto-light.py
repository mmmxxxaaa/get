import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
photo_transistor = 6
GPIO.setup(photo_transistor, GPIO.IN)
state = 0

while True:
    GPIO.output(led, GPIO.input(photo_transistor))
    time.sleep(0.05)
