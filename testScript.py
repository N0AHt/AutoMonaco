from Monaco import Monaco

print(Monaco.port_finder())

port = input('input port: ')

laser = Monaco(port, 19200, 0, 0)

laser.serial_test()
