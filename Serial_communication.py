import serial
import threading
class Laser():
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
        print('Receive :' + str(packet))
        return packet
    def run(self):
        while True:
            self.RecvData()

if __name__=='__main__':
    mySerial = Laser("COM3", 115200)
    t1 = threading.Thread(target=mySerial.RecvData, args=())
    while True:
        mySerial.SendData(adsfsdf)
