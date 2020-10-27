#Noah Telerman
#19/10/2020

#(abstract) Class to control simple data flow via serial ports
# simple wrapper for pyserial to make things easy

#should implement a feature to keep track of the return <CR><LS> from the
#microscope, to ensure good 'handshaking'

import serial
from serial.tools import list_ports


class SerialCommander:

    def __init__(self, Port_id, baudrate, timeout):
        self.port_id = Port_id
        self.baudrate = baudrate
        self.timeout - timeout
        self.port = serial.Serial(port = Port_id, baudrate = baudrate, timeout = timeout)

    def openPort(self):
        (self.port).open()

    def closePort(self):
        (self.port).close()

    def check_open(self):
        return (self.port).is_open

    def serial_read(self):
        line = (self.port).readline()
        input_decoded = line.decode('ascii')
        return input_decoded

    def serial_write(self, string_input):
        #add new line token to signal end of command
        command = string_input + '\r\n'
        command_encoded = command.encode('ascii')
        (self.port).write(command_encoded)

    def query(self, string_input):
        self.serial_write(string_input)
        output = self.serial_read()
        return output

    def portID(self):
        print(self.port)
        print('\n Port Open: ', (self.port).is_open)

    @staticmethod
    #lists ports available - static, so can be called before instantiating object
    #use before instantiation to see what ports to choose
    def port_finder():
        port_list = [comport.device for comport in list_ports.comports()]
        return port_list
