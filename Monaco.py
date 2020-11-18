#Noah Telerman
#19/10/2020

#Class to interface with Coherent's Monaco laser

from SerialCommander import SerialCommander
import time

class Monaco(SerialCommander):

    def __init__(self, Port_id, baudrate = 19200, power = 80, pulse_freq = 0, timeout = 2):

        super().__init__(Port_id, baudrate, timeout)

        self.power = power
        self.pulse_freq = pulse_freq

        #internal checks
        self.shutter_position = None
        self.laser_ready = False
        self.diodes_on = False

        #check if port is open
        if self.check_open() == False:
            print('Opening Port \n')
            self.openPort()
        else:
            print('Port Open \n')

    def update_internal_states(self):
        self.key_status = self.query()
        self.shutter_position = self.query('S?')
        self.chiller_status = self.query()
        self.diode_status = self.query()
        self.pulse_mode = self.query()
        self.pulse_status = self.query()

    def status_report(self):
        self.update_internal_states()
        #display results

    #Quick test to make sure serial connection to laser works as expected
    def serial_test(self):
        key_status = self.query('?K')
        print('Key status = ', key_status, '\n')

        laser_temp = self.query('?BT')
        print('Laser temperature = ', laser_temp)

#Pre-flight checks
    def start_up(self):
        # protocol to power on the laser safely - doesnt turn on diodes
        # will need safety checks here

        #Step1 - Chillers on (should just be a check)
        self.serial_write('CHEN=1')

        #Wait Cycle (3 mins?)
        #time.sleep(180)

        #check keyswitch
        keycheck = self.query('?k')
        print(keycheck)
        # while keycheck != 1:
        #     print('\n keyswitch off \n')
        #     print('key stat: '. keycheck)
        #     input('turn keyswitch on [y/n]')
        #     keycheck = self.query('?k')

        #check for faults
        faults_status = self.query('?F')
        print(faults_status)
        #check for warnings
        warning_status = self.query('?W')
        print(warning_status)

        #Close Shutters
        self.serial_write('S=0')
        self.shutter_position = self.query('?S')
        print('shutter_position: ', self.shutter_position)

        #Manual check
        laserCheck = 'n'
        while laserCheck != 'y':
            laserCheck = input('\n !Confirm Laser Ready! [y/n] \n')
        self.laser_ready = True

#needs to be run AFTER the setup function, should include checks or include in
#the same function as start_up()
    def activate_laser(self, pulsemode):
        if self.laser_ready == True:
            #set pulse mode
            pulse_mode = 'PM=' + str(pulsemode)
            self.serial_write(pulse_mode)
            print('Pulse Mode ', self.query('?PM'))

            self.serial_write('RL=80')

            #Turn on diodes
            if self.query('?S') == 0:
                self.serial_write('L=1')
            elif self.query('?S') != 0:
                self.serial_write('S=0')
                self.serial_write('L=1')
            print('\n Warming Diodes \n')

            #wait for diodes to warm
            # diode_ready = 'OFF'
            # while diode_ready != 'On':
            #     diode_ready = self.query('?ST')
            #     print(diode_ready)
            #     time.sleep(10)
            # print('\n')

            self.diodes_on = True
            diode_ready = self.query('?ST')
            print(diode_ready)


        else:
            print('LASER NOT READY - run start_up step')

#Actually projecting the laser beam - safety checks here too
    def start_lasing(self):
        if (self.diodes_on == True) and (self.laser_ready == True):

            #manual check
            lasercheck2 = 'n'
            while lasercheck2 != 'y':
                lasercheck2 = input('Confirm Start Lasing [y/n] ')

            #turn on pulses
            self.serial_write('PC=1')

            #Open the shutters
            #self.serial_write('S=1')

            #monitoring system during lasing?

        else:
            print('LASER NOT READY')

#essentially just closing the shutters
    def stop_lasing(self):

#fully shuts down the laser
    def deactivate_laser(self):
        #close the shutters
        self.serial_write('S=0')
        #turn off the diodes_on
        self.serial_write('L=0')
        #turn off pulsing
        self.serial_write('PC=0')

        #check if lasers are cool - make method for continuously testing this
        laser_cool = self.query('?ST')
        print(laser_cool)

        self.diodes_on = False


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
