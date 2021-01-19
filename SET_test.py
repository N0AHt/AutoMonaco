from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 200)

#values in kHz
RepRate_values = [200, 250, 330, 500, 1000, 2000, 4000, 10000, 50000]


for MRR in RepRate_values:

    laser.status_report()
    laser.set_parameters(pulse_freq = MRR)
    laser.status_report()
    print('FREQUENCY: ',laser.pulse_freq)
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
