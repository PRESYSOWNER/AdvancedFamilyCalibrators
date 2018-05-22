from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Stop Heater...')
scpi.sendWriteCommand('SOUR:OUTP OFF')

time.sleep(5)

print('Start Heater...')
scpi.sendWriteCommand('SOURce:OUTPut ON')

time.sleep(5)

print('Stop Heater...')
scpi.sendWriteCommand('SOURce:OUTPut OFF')

time.sleep(5)

print('Start Heater...')
scpi.sendWriteCommand('SOUR:OUTP ON')

scpi.disconnect

raw_input('Press any key to continue...')



