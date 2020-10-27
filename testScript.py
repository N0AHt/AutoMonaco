from Monaco import Monaco

#show available ports
print('Port list: ', Monaco.port_finder())

#input device port
port = input('input port: ')


laser = Monaco(Port_id = port, power = 0, pulse_freq = 0)
laser.portID()
laser.serial_test()
