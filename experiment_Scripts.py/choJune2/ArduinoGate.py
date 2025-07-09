from SerialCommander import SerialCommander

class ArduinoGate(SerialCommander):

    def __init__(self, port, baudrate = 9600, timeout = 5, EOF_string = '\r\n', OpenDuration = 1000, ClosedDuration = 1000):

        super().__init__(port, baudrate, timeout, EOF_string)

        self.OpenDuration = OpenDuration
        self.ClosedDuration = ClosedDuration

    def OpenGate(self):
        #input is 0 or 1 for on and off
        print('gatefunc')
        self.serial_write('G=1')
        print('openedgate')

    def CloseGate(self):
        self.serial_write('G=0')

    def SetOpenDuration(self, input):
        #input in ms
        self.OpenDuration = input
        input_string = 'OT' + str(input)
        self.serial_write(input_string)
        output = self.serial_read()
        print(output)

    def SetClosedDuration(self, input):
        self.ClosedDuration = input
        input_string = 'CT' + str(input)
        self.serial_write(input_string)

    def quick_open(self, duration):
        (self.port).write((str(duration)+'\r\n').encode('ascii'))
