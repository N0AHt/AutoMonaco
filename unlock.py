from Monaco import Monaco
import time

#show available ports
print('Port list: ', Monaco.port_finder())
#input device port
port = input('input port: ')

#Open port and check connection is secure
laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
laser.serial_write('LOCKOUT=0')
print('unlocked laser port')
