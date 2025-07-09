from ArduinoGate import ArduinoGate
from Monaco import Monaco
import time

laser = Monaco(Port_id = 'com1', power = 50.5, pulse_freq = 1000)
gate = ArduinoGate(port ='com4', baudrate = 9600, timeout = 5)

#laser.activate_laser(5)

laser.set_parameters(RRD = 4)
#laser.activate_laser(4)
bursts = input('No. Pulses: ')
laser.serial_write('BP=' + str(bursts))

laser.status_report()

laser.start_lasing()

#time.sleep(5)



print('opening gate')

gate.quick_open(5000)

time.sleep(10)

gate.quick_open(1000)
time.sleep(5)

laser.stop_lasing()
