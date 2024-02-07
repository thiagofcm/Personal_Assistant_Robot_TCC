import serial
import time

ser = serial.Serial(port='/dev/ttyS0',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

class Serial_Commands():
    def __init__(self):
        """Class Builder"""
        #ser = serial.Serial(port='/dev/ttyS0',
                           # baudrate=115200,
                           # parity=serial.PARITY_NONE,
                           # bytesize=serial.EIGHTBITS,
                           # timeout=1)

    def send_follow_cmd(self):
        follow_cmd = 'follow'
        ser.write(bytes(follow_cmd, 'utf-8'))
        
    def send_bring_cmd(self,obj):
        if obj == 'carro':
            obj_translated = 'car'
            bring_cmd = 'bring-'+obj_translated
            ser.write(bytes(bring_cmd, 'utf-8'))

    def send_stop_cmd(self):
        stop_cmd = 'stop'
        ser.write(bytes(stop_cmd, 'utf-8'))
   
    #def wait_finish_task(self):
     #   while True:
      #      if ser.in_waiting > 0:
       #         command=ser.readline().decode('utf-8').strip()
        #        if command == 'task-finish':
         #           print('Task Completed or Canceled by the User.')
          #          break
         

