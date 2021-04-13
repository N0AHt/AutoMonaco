from ArduinoGate import ArduinoGate
from Monaco import Monaco
import numpy as np
import time
import sys

laser = Monaco(Port_id = 'com1', power = 50.5, pulse_freq = 1000)
gate = ArduinoGate(port ='com4', baudrate = 9600, timeout = 5)

#Laser Set-up
laser.set_parameters(power = 5)
#set single pulse
laser.serial_write('BP=1')

def solve_for_y(poly_coeffs, y):
#stackoverflow: https://stackoverflow.com/questions/16827053/solving-for-x-values-of-polynomial-with-known-y-in-scipy-numpy
    pc = poly_coeffs.copy()
    pc[-1] -= y
    return np.roots(pc)

def Watt2RL(desired_power):
    #desired power must be in range
    polynom = [-3.89619018e-18, 1.43681797e-15, -1.71273526e-13,  8.88299244e-13, 1.54934881e-09, -1.41594079e-07,  4.87160468e-06, -4.11977712e-05, 2.31567217e-04,  2.70908813e-03, -1.08571654e-02]
    roots = solve_for_y(polynom, desired_power)
    #limit roots between 0 and 100, limit no complex values
    rootsReal = [root.real for root in roots if root.imag == 0]
    rootsLimited = [root for root in rootsReal if root >= 0 and root <=100]
    return rootsLimited[0] #round value???

def powerPercent(percentValue):
    maxpower = 5.24
    power = (5.24/100)*percentValue
    return power

def powerfinder(percentValue):
    power = powerPercent(percentValue)
    RL = Watt2RL(power)
    return RL

#start experiment script
startPower = 5
endPower = 100+1
Step = 5

laserPowers = list(range(startPower,endPower,Step))

laser.stop_lasing()
laser.start_lasing()
for powers in laserPowers:

    power = powerfinder(powers)

    laser.set_parameters(power = power)
    #Confirmation
    testpower = laser.query('?RL')
    print('Power (RL): ', testpower)
    print('power (w): ', powerPercent(powers))
    print('power(%): ', powers)
    confirm = input('Fire Laser? (y/n)')

    if confirm == 'y':
        gate.quick_open(500)
        time.sleep(1)
    else:
        laser.stop_lasing()
        sys.exit()

laser.stop_lasing()
