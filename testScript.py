from Monaco import Monaco
import time

#show available ports
print('Port list: ', Monaco.port_finder())

#input device port
port = input('input port: ')


laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
laser.portID()
laser.serial_test()

laser.start_up()
laser.activate_laser(0)
laser.start_lasing()

retry = 'y'
while retry == 'y':
    laser.serial_write('S=1')
    time.sleep(10)
    laser.serial_write('S=0')
    laser.serial_write('RL=50')
    retry = input('retry? [y/n]')

laser.stop_lasing()
