import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time


        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        bits = [int(b) for b in bin(number)[2:].zfill(8)] # Преобразуем число в список из 8 бит (старший бит — первый в списке)
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for code in range(256):
            self.number_to_dac(code)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:     # Компаратор выдаёт 1, когда DAC > SIG 
                if self.verbose:
                    print(f"Превышение при коде {code}")
                return code
        
        if self.verbose:                            # Если ни разу не превысило (входное напряжение >= максимума ЦАП)
            print("Превышения не произошло, возвращаем 255")
        return 255

    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = (code / 255.0) * self.dynamic_range
        if self.verbose:
            print(f"Код: {code}, напряжение: {voltage:.3f} В")
        return voltage


if __name__ == "__main__":
    adc = None
    try:
        adc = R2R_ADC(dynamic_range=3.29, compare_time=0.01, verbose=True)

        while True:
            voltage = adc.get_sc_voltage()
            print(f"{voltage:.3f} В")
            time.sleep(0.5)

    finally:
        if adc is not None:
            adc.deinit()