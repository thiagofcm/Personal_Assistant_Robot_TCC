import serial
import time


#if __name__ == '__main__':
#    ser = serial.Serial('/dev/ttyS0', 115200, timeout=1) 
    #ser.reset_input_buffer()
ser = serial.Serial(port='/dev/ttyS0',baudrate = 115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS, timeout=1)

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
    #cmd = 'hello from rasp'
    #ser.write(bytes(cmd, 'utf-8'))
    #print('comando enviado')
    #time.sleep(2)
    #time.sleep(2)
    #ser.write(b"Hello")
