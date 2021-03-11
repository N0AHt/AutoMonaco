from ArduinoGate import ArduinoGate
from Monaco import Monaco
import time

laser = Monaco(Port_id = 'com1', power = 80, pulse_freq = 1000)
gate = ArduinoGate(port ='com4', baudrate = 9600, timeout = 5)

laser.set_parameters(RRD = 1)
laser.activate_laser(1) #gated Mode

laser.start_lasing()

for i in range(5):
    open_time = input('Delay: ')
    gate.quick_open(open_time)
    time.sleep((open_time/1000)*1.2)
    print('output: ', gate.serial_read())

laser.stop_lasing()
