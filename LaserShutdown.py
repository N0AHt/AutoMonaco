from Monaco import Monaco
import time

#show available ports
print('Port list: ', Monaco.port_finder())

#input device port
port = input('input port: ')


laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)

laser.stop_lasing()
laser.deactivate_laser()
