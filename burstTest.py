from ArduinoGate import ArduinoGate
from Monaco import Monaco
import time

laser = Monaco(Port_id = 'com1', power = 80, pulse_freq = 1000)
gate = ArduinoGate(port ='com4', baudrate = 9600, timeout = 5)

laser.set_parameters(RRD = 1)
laser.status_report()
laser.stop_lasing()
laser.start_lasing()

time.sleep(5)

laser.stop_lasing()

print('opening gate')

gate.quick_open(5000)

time.sleep(10)