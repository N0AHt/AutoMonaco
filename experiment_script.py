from ArduinoGate import ArduinoGate
from Monaco import Monaco
import time

#Instantiate Classes
laser = Monaco(Port_id = 'com1', power = 80, pulse_freq = 1000)
gate = ArduinoGate(port ='com4', baudrate = 9600, timeout = 5)

#Laser Set-up
laser.set_parameters(power = 5, RRD = 4)
laser.serial_write('BP=1')

#Begin test
startPower = 5
endPower = 100
Step = 2

laserPowers = list(range(startPower,endPower,Step))

laser.start_lasing()
for power in laserPowers:

    laser.set_parameters(power = power)
    #Confirmation
    print('Power: ', power)
    confirm = input('Fire Laser? (y/n)')

    if confirm == 'y':
        gate.quick_open(500)
        time.sleep(1)
    else:
        laser.stop_lasing()
        sys.exit()

laser.stop_lasing()
