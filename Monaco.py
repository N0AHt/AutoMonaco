#Noah Telerman
#19/10/2020

#Class to interface with Coherent's Monaco laser

from SerialCommander import SerialCommander
import time
import sys

class Monaco(SerialCommander):

    def __init__(self, Port_id, baudrate = 19200, power = 80, pulse_freq = 1000, pulse_width = 286, RepRateDivisor = 1, PulsesPerMicroburst = 1, timeout = 5, EOF_string = '\r\n'):

        super().__init__(Port_id, baudrate, timeout, EOF_string)

        self.power = power
        self.pulse_freq = pulse_freq
        self.pulse_width = pulse_width
        self.RepRateDivisor = RepRateDivisor
        self.PulsesPerMicroburst = PulsesPerMicroburst

        #dictionary of amplifier rep rates with accepted corresponding no. of microbursts
        self.MRR_dictionary = {50000:1, 10000:1, 4000:1, 2000:1, 1000:1, 500:2, 330:3, 250:4, 200:5}

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
        if self.key_status == '1' and self.shutter_position == '0' and self.chiller_status == '1':
            self.laser_ready = True
        else:
            self.laser_ready = False

        #Diode Ready check - ready to open shutters and fire laser
        if self.diode_status == 'On' and self.pulse_status == '1':
            self.diode_ready = True
        else:
            self.diode_ready = False

    def status_report(self):
        self.update_internal_states()
        #display results
        print('KEY STATUS: ', self.key_status)
        print('Shutter Position: ', self.shutter_position)
        print('Chiller Stat: ', self.chiller_status)
        print('Diode Status: ', self.diode_status)
        print('Pulse Mode: ', self.pulse_mode)
        print('Pulse Stat: ', self.pulse_status)
        print('diode ready: ', self.diode_ready)
        print('laser ready: ', self.laser_ready)

    #Pre-flight checks
    def start_up(self):
        # protocol to power on the laser safely - doesnt turn on diodes
        # will need safety checks here

        #review laser status
        self.update_internal_states()

        #Step 1 - Check Chillers Are On
        if self.chiller_status == '1':
            print('CHILLERS: ', self.chiller_status, 'OK \n')
        elif self.chiller_status == '0':
            print('CHILLERS: ', self.chiller_status, 'NOT ENABLED - TURN ON CHILLERS \n')
        else:
            print('Bad Response')

        #Step 2 - check keyswitch
        if self.key_status == '1':
            print('KEY STATUS: ', self.key_status, 'OK \n')
        elif self.key_status == '0':
            print('KEY STATUS: ', self.key_status, 'KEY NOT TURNED ON \n')
        else:
            print('Bad Response')

        #Check for Faults
        faults_status = self.query('?F')
        print('FAULT STATUS: ', faults_status)
        #check for warnings
        warning_status = self.query('?W')
        print('WARNING STATUS: ', warning_status)

        #Close Shutters
        if self.shutter_position == '0':
            print('Shutter Position: ', self.shutter_position, 'CLOSED')
        elif self.shutter_position == '1':
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
            print('pm = ', pulsemode)
            print(self.serial_write(pulse_mode))
            for i in range(5):
                print(self.serial_read())
            print('Pulse Mode: ', self.query('?PM'))

            #set power
            power_command = 'RL=' + str(self.power)
            self.serial_write(power_command)

            #Turn on diodes
            if self.query('?S') == '0':
                self.serial_write('L=1')
            elif self.query('?S') != '0':
                self.serial_write('S=0')
                self.serial_write('L=1')
            print('\n Warming Diodes \n')

            #wait for diodes to warm
            diode_ready = 'OFF'
            while diode_ready != 'On':
                diode_ready = self.query('?ST')
                print('Diode Status: ', diode_ready)
                time.sleep(20)
            print('\n')

            #Turn on pulsing
            self.serial_write('PC=1')

        else:
            print('LASER NOT READY - run start_up step')
            sys.exit()

        self.update_internal_states()

    #Actually projecting the laser beam - safety checks here too
    def start_lasing(self):
        self.update_internal_states()
        if self.diode_ready == True and self.laser_ready == True:
            #manual check:
            lasercheck2 = input('Confirm Start Lasing [y/n] ')
            if lasercheck2 != 'y':
                sys.exit()
            else:
            #Run the Laser:
                #Open the shutters
                self.serial_write('S=1')
        else:
            print('LASER NOT READY')
            sys.exit()

        self.update_internal_states()

    #this is broken since adding set funtion...
    def set_parameters(self, power = None, pulse_freq = None, RRD = None, pulse_width = None, Bursts = None):
        #update internal parameter values
        if power == None:
            power = self.power
        else:
            self.power = power

        if pulse_freq == None:
            pulse_freq = self.pulse_freq
        else:
             self.pulse_freq = pulse_freq

        if pulse_width == None:
            pulse_width = self.pulse_width
        else:
             self.pulse_width = pulse_width

        if RRD == None:
            RRD = self.RepRateDivisor
        else:
             self.RepRateDivisor = RRD

        # if Bursts = None:
        #     Bursts = self.PulsesPerMicroburst
        # else:
        #     self.PulsesPerMicroburst = Bursts

        #set power
        power_command = 'RL=' + str(self.power)
        print('power ok')
        self.serial_write(power_command)

        #set pulse_freq (in kHz) (amplifier rep rate)
        #NOTE: this must be a value selected from the drop down menu with compatible no. of microbursts
        #SET can also be used to change other parameters
        freq_command = 'SET=' + str(self.pulse_freq) + ',' + str(self.pulse_width) + ',' + str(self.RepRateDivisor) + ',' + str(self.MRR_dictionary[self.pulse_freq])
        print('SET: ', freq_command)
        print(self.serial_write(freq_command))

        #wait until diode is ready
        self.update_internal_states()
        while self.diode_ready != True:
            time.sleep(2)
            self.update_internal_states()
            self.status_report()

        self.update_internal_states()


    #essentially just closing the shutters
    def stop_lasing(self):
        print('Closing Shutters')
        self.serial_write('S=0')
        #should wait for crriage return here instead of using sleep
        #(should really do that for all write functions - implement in serial commander)
        time.sleep(2)
        self.update_internal_states()

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

        self.closePort()

    #relinquishes control of the laser from serial port (allows GUI to control laser)
    def laser_unlock(self):
        laser.serial_write('LOCKOUT=0')


#conversion functionality to linearise the RL to watts relationship of the laser
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
