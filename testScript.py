from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
RL_values = [10,20,30,40,50,60,70,80,90,100]



for RL in RL_values:
    print('diode ready: ', laser.diode_ready)
    print('laser ready: ', laser.laser_ready)
    print('diode: ', laser.diode_status)
    print('shutter position: ', laser.shutter_position)
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
