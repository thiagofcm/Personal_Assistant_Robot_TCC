import serial
import time

ser = serial.Serial(port='/dev/ttyS0',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

class Serial_Commands():
    def __init__(self):
        """Class Builder"""

    def send_follow_cmd(self):
        follow_cmd = 'follow'
        ser.write(bytes(follow_cmd, 'utf-8'))
        
    def send_bring_cmd(self,obj):
        bring_cmd = 'bring-'+obj
        ser.write(bytes(bring_cmd, 'utf-8'))

    def send_stop_cmd(self):
        stop_cmd = 'stop'
        ser.write(bytes(stop_cmd, 'utf-8'))
    

