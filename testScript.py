from Monaco import Monaco
import time

port = 'com1'
laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
RL_values = [5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]



for RL in RL_values:

    #laser.status_report()
    #laser.set_parameters(power = RL)
    print(laser.power)
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
