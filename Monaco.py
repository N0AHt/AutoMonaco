#Noah Telerman
#19/10/2020

#Class to interface with Coherent's Monaco laser

from SerialCommander import SerialCommander

class Monaco(SerialCommander):

    def __init__(self, Port_id, baudrate = 19200, power, pulse_freq, timeout = 2):

        super().__init__(Port_id, baudrate, timeout)

        self.power = power
        self.pulse_freq = pulse_freq

        #check if port is open
        if self.check_open() = False:
            print('Opening Port \n')
            self.openPort()
        else:
            print('Port Open \n')

    #Quick test to make sure serial connection to laser works as expected
    def serial_test(self):
        key_status = self.query('?K')
        print('Key status = ', key_status, '\n')

        laser_temp = self.query('?BT')
        print('Laser temperature = ', laser_temp)

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
