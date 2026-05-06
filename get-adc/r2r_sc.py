import r2r_adc
import adc_plot
import time

if __name__ == "__main__":
    try:
        max_voltage = 3.296

        adc = r2r_adc.R2R_ADC(max_voltage, compare_time=0.0001)

        voltage_values = []
        time_values    = []
        duration       = 3.0

        time_start   = time.monotonic()
        time_current = 0.0 

        while time_current < duration:
            time_current = time.monotonic() - time_start
            voltage      = adc.get_sc_voltage()

            voltage_values.append(voltage)
            time_values.append(time_current)

        adc_plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage)
        
        print(voltage_values)
        print(time_values)

        adc_plot.plot_sampling_period_hist(time_values)
    
    except KeyboardInterrupt:
        print("\nEnd")

    finally:
        adc.__dtor__()