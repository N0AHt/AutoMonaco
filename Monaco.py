#Noah Telerman
#19/10/2020

#Class to interface with Coherent's Monaco laser

from SerialCommander import SerialCommander

class Monaco(SerialCommander):

    def __init__(self, Port_id, baudrate, power, pulse_freq):

        super().__init__(Port_id, baudrate)

        self.power = power
        self.pulse_freq = pulse_freq

        #move this to the power function?
        #self.openPort()


    def serial_test(self):
        self.serial_write('?HV')
        print('sent...')
        #print(self.serial_read())
        print('\nrecieved')

        self.serial_write('?LM')
        print(self.readline())

        self.write('?L')
        print(self.readline())
    #
    # def power_on(self):
    #     # protocol to power on the laser safely
    #     # will need many safety checks here
    #
    #     #Activate chillers
    #     self.write('CHEN=1')
    #     #Note time of activation
    #
    #     #check keyswitch
    #     self.write('?k')
    #     if self.readline() != 1:
    #         print('\n keyswitch off \n')
    #         keycheck = input('turn keyswitch on [y/n]')
    #
    #     #Wait Cycle (3 mins?)
    #
    #     #Manual check
    #     laserCheck = 'n'
    #     while laserCheck != 'y':
    #         laserCheck = input('\n !Confirm Laser Ready! [y/n] \n')
    #
    #     #turn on laser
    #     self.write()
    #
    # def power_off(self):
    #     #protocol for turning off the laser
    #     #probably will need safety protocols here too
    #
    #     #lasers off
    #     self.write()
    #
    #     #Chillers off
    #     self.write()
    #
    #     #close port
    #     self.closePort()
    #
    # def run_laser(self):
    #     #run a set laser protocol
    #     #open the shutters and run the laser at set parameters
    #
    #     self.write()
    #
    # def set_parameters(self, power = self.power, pulse_freq = self.pulse_freq, wavelength = self.wavelength):
    #     #update internal parameter values
    #     self.power = power
    #     self.pulse_freq = pulse_freq
    #     self.wavelength = wavelength
    #
    #     #set power
    #     self.write()
    #
    #     #set freq
    #     self.write()
    #
    #     #set wavelength
    #     self.write()
