import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac_bits = [16, 20, 21, 25, 26, 17, 27, 22] # На плате опечатка // не то выводится
GPIO.setup(dac_bits, GPIO.OUT)

dynamic_range = 3.3 #возможно не то 

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 B")
        return 0
    
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):

    if number < 0:
        number = 0
    if number > 255:
        number = 255
    
    bits = [int(x) for x in bin(number)[2:].zfill(8)]
    GPIO.output(dac_bits, bits)
    print(f"Число на вход ЦАП: {number}, биты: {bits}")

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз")
    
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()