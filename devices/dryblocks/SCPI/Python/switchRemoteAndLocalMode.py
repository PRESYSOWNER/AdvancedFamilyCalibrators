from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Go to remote...')
resp = scpi.sendWriteCommand('SYST:REM')

time.sleep(5)

print('Go to local...')
scpi.sendWriteCommand('SYST:LOC')

time.sleep(5)

print('Go to remote...')
scpi.sendWriteCommand('SYSTem:REMote')

time.sleep(5)

print('Go to local...')
scpi.sendWriteCommand('SYSTem:LOCal')

scpi.disconnect

raw_input('Press any key to continue...')



