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
        return (self.port).readline()

    #input type will need checking? (b strings used in examples)
    def write(string_input):
        #add new line token to signal end of command
        command = string_intput + ' \n'
        (self.port).write(command)

    def query(string_input):
        self.write(string_input)
        output = self.readline()
        print(output)
        return output 

    def portID():
        self.port
        print('\n Port Open: ', (self.port).is_open)
