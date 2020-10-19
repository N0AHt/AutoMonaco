#Noah Telerman
#19/10/2020

#(abstract) Class to control simple data flow via serial ports
# wrapper for pyserial to make things easy

import serial

class SerialCommander:

    def __init__(self,Port_id, baudrate):
        self.port_id = Port_id
        self.baudrate = baudrate
        self.port = serial.Serial(port_id)

    def openPort():
        (self.port).open()

    def closePort():
        (self.port).close()

    def readline():
        (self.port).readline()

    def write(string_input):
        (self.port).write(str(string_input))

    def portID():
        self.port
        print('\n Port Open: ', (self.port).is_open)

    
