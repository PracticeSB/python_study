import serial
import threading
import time

#Buffer for memorizing sensor data
Data = []

class Laser():
    def __init__(self,com,baudrate):
        self.mySerial = serial.Serial(com,baudrate,timeout = 0,bytesize=serial.EIGHTBITS)
    def SendData(self):
        packet = bytes(bytearray([0x02,0x43,0xB0,0x01,0x03,0xF2]))
        self.mySerial.write(packet)
        print('Send :' + str(packet))
    def Setup(self,dataPacket):
        packet = bytes(bytearray(dataPacket))
        self.mySerial.write(packet)
        print('Send :' + str(packet))
    def RecvData(self):
        global Buffer
        if self.mySerial.readable():
            A = bytearray(self.mySerial.readline())
            if len(A) < 6:
                B = self.mySerial.read(size=6-len(A))
                A.extend(B)
                print('Additional' + str(A) , len(A))
            #### 만약에 6보다 긴 경우가 많이 나오면 수정해야할 부분
            # if len(A) > 6:
            #     for i in range(len(A) - 1):
            #         if A[i] == bytes(0x02):
            #             for count in range(4):
            #                 Data.append(A[i+count])
            #                 print('Over 6' + Data)
            if A[2] >= 127:
                Response = -((255 - (A[2])) * 256 + (255 - A[3])) * 0.01
            else:
                Response = ((A[2]) * 256 + (A[3])) * 0.01
            print(A,len(A))
            print('Response: ', Response ,'\n')


if __name__=='__main__':
    A = Laser("COM5", 115200)
    A.Setup([0x02,0x43,0xA1,0x01,0x03,0xE3])
    time.sleep(1)
    while True:
        t1 = threading.Thread(target=A.SendData)
        t1.start()
        t2 = threading.Thread(target=A.RecvData)
        t2.start()
        time.sleep(0.01)
