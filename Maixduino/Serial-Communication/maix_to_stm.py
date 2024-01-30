from fpioa_manager import fm
from machine import UART
import utime

# need your connect hardware IO 10/11 to loopback
fm.register(23, fm.fpioa.UART1_TX, force=True)
fm.register(22, fm.fpioa.UART1_RX, force=True)

uart = UART(UART.UART1, 115200, 8, 1, 0, timeout=1000, read_buf_len=4096)

uart.write(b'hello world')
x = 14

while True:
    read_data = '(' + str(x) + ',20,43)'
    #decoded_data = read_data.encode('utf-8')
    #if read_data:
        #print("recv:", read_data)
    uart.write(read_data) # send data back
    print(read_data)
    x = x+1
    utime.sleep_ms(2000)

uart.deinit()
del uart
