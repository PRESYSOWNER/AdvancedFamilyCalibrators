from scpi import scpi_wrapper
import time

SERIALPORT="COM3"

print('Opening serial port ' + SERIALPORT + ' ...')
scpi = scpi_wrapper(SERIALPORT)
if scpi.connect() == False:
    print('Cannot open serial port ' + SERIALPORT)
    raw_input('Press any key as continue...')
    quit()

print('Meas Auxiliary input as mA...')
resp = scpi.sendReadCommand('MEAS:CURR?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:CURRent?')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as mV...')
resp = scpi.sendReadCommand('MEAS:VOLT?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:VOLTage?')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as switch...')
resp = scpi.sendReadCommand('MEAS:SW?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:SWitch?')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as default resistance...')
resp = scpi.sendReadCommand('MEAS:RES?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:RESistance?')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as resistance 2 wires...')
resp = scpi.sendReadCommand('MEAS:RES? 2')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:RESistance? 2')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as default RTD...')
resp = scpi.sendReadCommand('MEAS:RTD?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:RTD?')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as RTD Pt-1000 IPTS-68 3 wires...')
resp = scpi.sendReadCommand('MEAS:RTD? Pt-1000 IPTS-68 3')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:RTD? Pt-1000 IPTS-68 3')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as default TC...')
resp = scpi.sendReadCommand('MEAS:TC?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:TC?')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as TC-S IPTS-68 MANUAL 27°C ...')
resp = scpi.sendReadCommand('MEAS:TC? TC-S IPTS-68 MANUAL 27')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:TC? TC-S IPTS-68 MANUAL 27')
print('Reponse: ' + resp)
time.sleep(10)

print('Meas Auxiliary input as none...')
resp = scpi.sendReadCommand('MEAS:NONE?')
print('Reponse: ' + resp)
time.sleep(10)
resp = scpi.sendReadCommand('MEASure:NONE?')
print('Reponse: ' + resp)
time.sleep(10)

scpi.disconnect

raw_input('Press any key as continue...')



