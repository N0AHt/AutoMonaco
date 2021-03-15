#start up for laser

from Monaco import Monaco
import time

#show available ports
print('Port list: ', Monaco.port_finder())
#input device port
port = input('input port: ')

#Open port and check connection is secure
laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
laser.hello_laser()

laser.start_up()

#turn on diodes with continuous pulsing
laser.activate_laser(4)
