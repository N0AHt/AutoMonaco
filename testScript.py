from Monaco import Monaco
import time


retry = 'y'
while retry == 'y':
    laser.serial_write('S=1')
    time.sleep(10)
    laser.serial_write('S=0')
    laser.serial_write('RL=50')
    retry = input('retry? [y/n]')
