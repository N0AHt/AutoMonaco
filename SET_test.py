from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 200)

#values in kHz - Need to update no. microbusts too!!
RepRate_values = [1000, 500, 330, 250, 200]


for MRR in RepRate_values:

    laser.set_parameters(pulse_freq = MRR)
    laser.status_report()
    print('FREQUENCY: ',laser.pulse_freq)
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
