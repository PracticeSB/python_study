import serial
import threading
import time

class Laser():
    def __init__(self,com,baudrate):
        self.mySerial = serial.Serial(com,baudrate,timeout = 0,bytesize=serial.EIGHTBITS)
    def SendData(self):
        packet = bytes(bytearray([0x02,0x43,0xB0,0x01,0x03,0xF2]))
        self.mySerial.write(packet)
        print('Send :' + str(packet),'\n')
    def Setup(self,dataPacket):
        packet = bytes(bytearray(dataPacket))
        self.mySerial.write(packet)
        print('Send :' + str(packet))
    def RecvData(self):
        if self.mySerial.readable():
            packet = self.mySerial.readline()
            A = bytearray(packet)
            if len(A) > 6:

            if A[2] >= 127:
                Response = -((255 - (A[2])) * 256 + (255 - A[3])) * 0.01
            else:
                Response = ((A[2]) * 256 + (A[3])) * 0.01
            print('Receive :' + str(A),len(A),'\n')
            print('Response :' + str(Response))

if __name__=='__main__':
    A = Laser("COM5", 115200)
    A.Setup([0x02,0x43,0xA1,0x01,0x03,0xE3])
    time.sleep(1)
    while True:
        t1 = threading.Thread(target=A.SendData)
        t1.start()
        t2 = threading.Thread(target=A.RecvData)
        t2.start()
        time.sleep(0.1)
