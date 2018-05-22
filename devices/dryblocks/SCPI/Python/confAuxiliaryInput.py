from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key to continue...')
    quit()

print('Set Auxiliary input to mA...')
scpi.sendWriteCommand('CONF:CURR')
time.sleep(10)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(5)

print('Set Auxiliary input to mV...')
scpi.sendWriteCommand('CONF:VOLT')
time.sleep(10)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(5)

print('Set Auxiliary input to switch...')
scpi.sendWriteCommand('CONF:SW')
time.sleep(10)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(5)

print('Set Auxiliary input to default resistance...')
scpi.sendWriteCommand('CONF:RES')
time.sleep(15)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(5)

print('Set Auxiliary input to resistance 2 wires...')
scpi.sendWriteCommand('CONF:RES 2')
time.sleep(15)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(5)

print('Set Auxiliary input to default RTD...')
scpi.sendWriteCommand('CONF:RTD')
time.sleep(15)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(10)

print('Set Auxiliary input to RTD Pt-1000 IPTS-68 3 wires...')
scpi.sendWriteCommand('CONF:RTD Pt-1000 IPTS-68 3')
time.sleep(15)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(10)

print('Set Auxiliary input to default TC...')
scpi.sendWriteCommand('CONF:TC')
time.sleep(15)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(10)

print('Set Auxiliary input to TC-S IPTS-68 MANUAL 27°C ...')
scpi.sendWriteCommand('CONF:TC TC-S IPTS-68 MANUAL 27')
time.sleep(15)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(10)

print('Set Auxiliary input to none...')
scpi.sendWriteCommand('CONF:NONE')
time.sleep(10)
resp = scpi.sendReadCommand('READ?')
print('Reponse: ' + resp)
time.sleep(5)


scpi.disconnect

raw_input('Press any key to continue...')



