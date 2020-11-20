#Noah Telerman
#19/10/2020

#Class to interface with Coherent's Monaco laser

from SerialCommander import SerialCommander
import time
import sys

import numpy as np

class Monaco(SerialCommander):

    def __init__(self, Port_id, baudrate = 19200, power = 80, pulse_freq = 0, timeout = 5):

        super().__init__(Port_id, baudrate, timeout)

        self.power = power
        self.pulse_freq = pulse_freq

        #internal checks - find out the current state of the laser
        self.update_internal_states()

        #check if serial port is open
        if self.check_open() == False:
            print('Opening Port \n')
            self.openPort()
        else:
            print('Port Open \n')

    #Quick test to make sure serial connection to laser works as expected
    #Gives basic info re the laser
    def hello_laser(self):
        laser_model = self.query('?LM')
        print('Laser Model = ', laser_model)

        laser_temp = self.query('?BT')
        print('Laser temperature = ', laser_temp)

    def update_internal_states(self):
        self.key_status = self.query('?K')
        self.shutter_position = self.query('?S')
        self.chiller_status = self.query('?CHEN')
        self.diode_status = self.query('?ST')
        self.pulse_mode = self.query('?PM')
        self.pulse_status = self.query('?PC')

        #laser ready check - ready to turn on diodes
        if self.key_status == '1\r\n' and self.shutter_position == '0\r\n' and self.chiller_status == '1\r\n':
            self.laser_ready = True
        else:
            self.laser_ready = False

        #Diode Ready check - ready to open shutters and fire laser
        if self.diode_status == '1\r\n' and self.pulse_status == '1\r\n':
            self.diode_ready = True
        else:
            self.diode_ready = False

    # def status_report(self):
    #     self.update_internal_states()
    #     #display results
    #     print('KEY STATUS: ')

    #Pre-flight checks
    def start_up(self):
        # protocol to power on the laser safely - doesnt turn on diodes
        # will need safety checks here

        #review laser status
        self.update_internal_states()

        #Step 1 - Check Chillers Are On
        if self.chiller_status == '1\r\n':
            print('CHILLERS: ', self.chiller_status, 'OK \n')
        elif self.chiller_status == '0\r\n':
            print('CHILLERS: ', self.chiller_status, 'NOT ENABLED - TURN ON CHILLERS \n')
        else:
            print('Bad Response')

        #Step 2 - check keyswitch
        if self.key_status == '1\r\n':
            print('KEY STATUS: ', self.key_status, 'OK \n')
        elif self.key_status == '0\r\n':
            print('KEY STATUS: ', self.key_status, 'KEY NOT TURNED ON \n')
        else:
            print('Bad Response')

        #Check for Faults
        faults_status = self.query('?F')
        print('FAULT STATUS: \n', faults_status)
        #check for warnings
        warning_status = self.query('?W')
        print('WARNING STATUS: \n', warning_status)

        #Close Shutters
        if self.shutter_position == '0\r\n':
            print('Shutter Position: ', self.shutter_position, 'CLOSED')
        elif self.shutter_position == '1\r\n':
            print('Shutter Position: ', self.shutter_position, 'OPEN')
            self.serial_write('P=0')
        else:
            print('Bad Response')

        #Final Laser Checks
        print('LASER READY: ', self.laser_ready)
        if self.laser_ready == False:
            sys.exit()
        else:
            #Manual Confirmation
            laserCheck = input('\n !Confirm Laser Ready! [y/n] \n')
            if laserCheck != 'y':
                sys.exit()

        #Update Laser States (mostly redundant)
        self.update_internal_states()


    #needs to be run AFTER the setup function, should include checks or include in
    #the same function as start_up()
    def activate_laser(self, pulsemode):
        self.update_internal_states()
        if self.laser_ready == True:
            #set pulse mode - should add a valueSet function to serial commander to handle this concatonation
            pulse_mode = 'PM=' + str(pulsemode)
            self.serial_write(pulse_mode)
            print('Pulse Mode: ', self.query('?PM'))

            #should update to use the self.power attribute at some point
            self.serial_write('RL=80')

            #Turn on diodes
            if self.query('?S') == '0\r\n':
                self.serial_write('L=1')
            elif self.query('?S') != '0\r\n':
                self.serial_write('S=0')
                self.serial_write('L=1')
            print('\n Warming Diodes \n')

            #wait for diodes to warm
            diode_ready = 'OFF'
            while diode_ready != 'On\r\n':
                diode_ready = self.query('?ST')
                print('Diode Status: ', diode_ready)
                time.sleep(20)
            print('\n')

        else:
            print('LASER NOT READY - run start_up step')
            sys.exit()

        self.update_internal_states()

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
        print('fake code')
        #code here

    #fully shuts down the laser working?
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
