from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Sending get probes command...')
resp = scpi.sendReadCommand('SOUR:MEAS?')
print('Response: ' + resp)
time.sleep(3)

print('Sending get probes command...')
resp =scpi.sendReadCommand('SOURce:MEASure?')
print('Response: ' + resp)
time.sleep(3)

scpi.disconnect

raw_input('Press any key to continue...')



