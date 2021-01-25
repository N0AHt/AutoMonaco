from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 1000)

#values in kHz - Need to update no. microbusts too!!
divider_values = range(1,10)


for RRD in divider_values:

    laser.set_parameters(divider = RRD)
    laser.status_report()
    print('Frequence: ',(laser.pulse_freq/RRD))
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
