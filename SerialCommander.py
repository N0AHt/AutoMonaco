#Noah Telerman
#19/10/2020

#(abstract) Class to control simple data flow via serial ports
# simple wrapper for pyserial to make things easy

import serial
from serial.tools import list_ports


class SerialCommander:

    def __init__(self, Port_id, baudrate):
        self.port_id = Port_id
        self.baudrate = baudrate
        self.port = serial.Serial(Port_id)

    def openPort(self):
        (self.port).open()

    def closePort(self):
        (self.port).close()

    def serial_read(self):
        line = (self.port).readline()
        input_decoded = line.decode('utf-8')
        return input_decoded

    #input type will need checking? (b strings used in examples)
    def serial_write(self, string_input):
        #add new line token to signal end of command
        command = string_input + '\n'
        command_encoded = command.encode('utf-8')
        (self.port).write(command_encoded)

    def query(self, string_input):
        self.write(string_input)
        output = self.readline()
        return output

    def portID(self):
        self.port
        print('\n Port Open: ', (self.port).is_open)

    @staticmethod
    #lists ports available - static, so can be called before instantiating object
    #use before instantiation to see what ports to choose
    def port_finder():
        port_list = [comport.device for comport in list_ports.comports()]
        return port_list
