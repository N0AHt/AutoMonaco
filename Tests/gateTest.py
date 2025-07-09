from ArduinoGate import ArduinoGate
import time

#show available ports
print('Port list: ', ArduinoGate.port_finder())
#input device port
port_id = input('input port: ')

# gate_decoy = ArduinoGate(port, 9600, 1000)
# time.sleep(5)
gate = ArduinoGate(port = port_id, baudrate = 9600, timeout = 5)

for i in range(5):
    delay = input('delay: ')
    gate.quick_open(int(delay))
    time.sleep(1)
    print('output: ', gate.serial_read())
    #time.sleep(3)

# print('Here')
#
# gate.SetOpenDuration(5000)
# gate.SetClosedDuration(5000)
#
# gate.OpenGate()
#
# time.sleep(5)
#
# print('here')
