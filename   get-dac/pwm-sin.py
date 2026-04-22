import time
import pwm_dac as pwm
import signal_generator as sg
# import RPi.GPIO as GPIO
# GPIO.setwarnings(False)

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    print("Программа запущена")
    dac = None
    try:
        dac = pwm.PWMDAC(12, 500, 3.290, verbose=False)
        print("Цап инициализирован")

        start = time.time()
        while True:
            t = time.time() - start
            norm = sg.get_sin_wave_amplitude(signal_frequency, t)
            voltage = amplitude * norm                             

            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
    except Exception as e:
        print(f"Ошибка {e}")
    finally:
        if dac is not None:
            dac.deinit()
