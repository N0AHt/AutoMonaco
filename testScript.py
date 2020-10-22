from Monaco import Monaco

#show available ports
print(Monaco.port_finder())

#input device port
port = input('input port: ')


laser = Monaco(port, 19200, 0, 0)
laser.portID()
laser.serial_test()
