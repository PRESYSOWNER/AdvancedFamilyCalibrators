from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Sending read setpoint command...')
resp = scpi.sendReadCommand('SOUR:SPO?')
print('Response: ' + resp)

time.sleep(3)

print('Sending read setpoint command...')
resp =scpi.sendReadCommand('SOURce:SetPOint?')
print('Response: ' + resp)
time.sleep(3)

print('Sending a wrong read setpoint command...')
resp = scpi.sendReadCommand('SOURce:SetPOintz?')
print('Response: ' + resp)
resp = scpi.sendReadCommand('SYST:ERR?')
print('Error: ' + resp)

scpi.disconnect

raw_input('Press any key to continue...')



