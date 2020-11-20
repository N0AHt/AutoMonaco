from Monaco import Monaco
import time

laser = Monaco(Port_id = port, power = 10, pulse_freq = 10)
RL_values = [10,20,30,40,50,60,70,80,90,100]

for RL in Rl_values:
    laser.start_lasing()
    time.sleep(10)
    laser.stop_lasing()
