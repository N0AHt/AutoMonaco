import Monaco


port = input('input port: ')

laser = Monaco(port, 19200, 0, 0, 0)

laser.serial_test()
