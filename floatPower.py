from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 1000)
laser.serial_write('RL=50.5')
laser.start_lasing()

time.sleep(5)

laser.stop_lasing()
