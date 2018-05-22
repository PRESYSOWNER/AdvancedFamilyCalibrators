from scpi import scpi_wrapper

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Sending IDN command...')
resp = scpi.sendReadCommand('*IDN?')
print('Response: ' + resp)

scpi.disconnect

raw_input('Press any key to continue...')



