from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Sending get last calibration date command...')
resp = scpi.sendReadCommand('CAL:DATE:LAST?')
print('Response: ' + resp)

time.sleep(3)

print('Sending get next calibration date command...')
resp = scpi.sendReadCommand('CAL:DATE:NEXT?')
print('Response: ' + resp)

time.sleep(3)

print('Sending get last calibration date command...')
resp = scpi.sendReadCommand('CALibration:DATE:LAST?')
print('Response: ' + resp)

time.sleep(3)

print('Sending get next calibration date command...')
resp = scpi.sendReadCommand('CALibration:DATE:NEXT?')
print('Response: ' + resp)

scpi.disconnect

raw_input('Press any key to continue...')



