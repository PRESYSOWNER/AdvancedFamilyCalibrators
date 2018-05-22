from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Sending change setpoint command to 1.23...')
scpi.sendWriteCommand('SOUR:SPO 1.23')
time.sleep(3)

print('Sending change setpoint command to 56.41...')
scpi.sendWriteCommand('SOURce:SetPOint 56.41')
time.sleep(3)

print('Sending a wrong write setpoint command...')
scpi.sendWriteCommand('SOURce:SetPOint 100000')
resp = scpi.sendReadCommand('SYST:ERR?')
print('Error: ' + resp)

scpi.disconnect

raw_input('Press any key to continue...')



