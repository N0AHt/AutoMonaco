from Monaco import Monaco

#show available ports
print('Port list: ', Monaco.port_finder())

#input device port
port = input('input port: ')


laser = Monaco(port, baudrate = 19200, 0, 0, timeout = 2)
laser.portID()
laser.serial_test()
