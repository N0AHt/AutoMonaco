from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 80, pulse_freq = 1000)

#values in kHz - Need to update no. microbusts too!!
freq_values = [1,2,4,10,50]
print(freq_values)


for freq in freq_values:

    laser.set_parameters(pulse_freq = freq)
    laser.status_report()
    print('Frequence: ',(laser.pulse_freq))
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
