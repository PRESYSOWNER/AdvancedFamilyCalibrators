import serial
import time

class scpi_wrapper:
    def __init__(self,port,baudrate=57600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,timeout=1):
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = baudrate
        ser.bytesize = bytesize
        ser.parity = parity
        ser.stopbits = stopbits
        ser.timeout = timeout
        self.ser = ser

    def connect(self): 
        try:
            self.ser.open()
            return True
        except:           
            return False

    def disconnect(self):
        self.ser.close()

    def sendWriteCommand(self,command):        
        self.ser.write(command)
        time.sleep(1)

    def sendReadCommand(self,command):
        self.sendWriteCommand(command)
        resp = self.ser.readline()        
        return resp
        


