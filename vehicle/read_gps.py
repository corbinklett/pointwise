import serial

# First, receive data from the pointwise transmitter

with serial.Serial('/dev/tty.usbmodem14301', baudrate=4800, timeout=1) as ser:
    # read 10 lines from the serial output
    for i in range(50):
        #line = ser.readline().decode('ascii', errors='replace')
        #print(line.strip())
        line = ser.readline().decode('ascii',errors='replace')
        sen = line[1:6]
        if sen == 'GPGLL': # or sen == 'GPGGA' or sen == 'GPRMC':
            chunks = line.split(',')
            lat = chunks[1]
            lon = chunks[3]

# Actual position:
# 33.76580151306169, -84.35375312094449

# Reference:
# https://www.rfwireless-world.com/Terminology/GPS-sentences-or-NMEA-sentences.html