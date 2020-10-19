#Noah Telerman
#19/10/2020

#Class to interface with Coherent's Monaco laser

import SerialCommander as sc

class Monaco(AutoMonaco.SerialCommander):

    def __init__(self, Port_id, baudrate, power, pulse_freq):
        self.power = power
        self.pulse_freq = pulse_freq

        self.openPort()


    def power_on():
        # protocol to power on the laser safely
        # will need many safety checks here

        #Activate chillers
        self.write()
        #Note time of activation

        #Wait Cycle (3 mins?)

        #Manual check
        laserCheck = 'n'
        while laserCheck != 'y':
            laserCheck = input('\n !Confirm Laser Ready! [y/n] \n')

        #turn on laser
        self.write()

    def power_off():
        #protocol for turning off the laser
        #probably will need safety protocols here too

        #lasers off
        self.write()

        #Chillers off
        self.write()

        #close port
        self.closePort()

    def run():
        #run a set laser protocol
        #open the shutters and run the laser at set parameters

        self.write()

    def set_parameters(power, pulse_freq):
        self.power = power
        self.pulse_freq = pulse_freq

        #set power
        self.write()

        #set freq
        self.write()
