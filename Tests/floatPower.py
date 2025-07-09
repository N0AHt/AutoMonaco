from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 1000)
error = laser.serial_write('RL=52.713')

print(error)

print('done')

rl = laser.serial_write('?RL')

print('RL =', rl)
print('done')


# laser.start_lasing()
#
# time.sleep(5)
#
# laser.stop_lasing()
