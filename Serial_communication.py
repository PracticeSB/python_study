import serial
import threading
class Serialtest():
    def __init__(self,com,baudrate):
        self.mySerial = serial.Serial(com,baudrate,timeout = 0)
    def SendData(self,dataPacket):
        packet = bytearray(dataPacket)
        self.mySerial.write(packet)
        print('Send :' + str(packet))
    def Setup(self,dataPacket):
        packet = bytearray(dataPacket)
        self.mySerial.write(packet)
        print('Send :' + str(packet))
    def RecvData(self):

        packet = self.mySerial.read()
    def run(self):
        while True:
            self.RecvData()
port = "COM3"
baud = 115200
timeout = 1
mySerial = serial.Serial = (port, baud, timeout)