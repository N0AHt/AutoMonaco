from Monaco import Monaco
import time

#show available ports
print('Port list: ', Monaco.port_finder())
#input device port
port = input('input port: ')

#Open port and check connection is secure
laser = Monaco(Port_id = port)
laser.laser_unlock()
print('unlocked laser port')
