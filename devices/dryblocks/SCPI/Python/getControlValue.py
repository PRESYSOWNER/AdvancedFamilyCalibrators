from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Sending get control temperature command...')
resp = scpi.sendReadCommand('SOUR:READ?')
print('Response: ' + resp)
time.sleep(3)

print('Sending get control temperature command...')
resp =scpi.sendReadCommand('SOURce:READ?')
print('Response: ' + resp)
time.sleep(3)

scpi.disconnect

raw_input('Press any key to continue...')



