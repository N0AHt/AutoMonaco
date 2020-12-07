from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
RepRates = [1000, 750, 500, 250, 100]



for RR in RepRates:

    #laser.status_report()
    laser.set_parameters(power = 80, pulse_freq = RR)
    print(laser.pulse_freq)
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
