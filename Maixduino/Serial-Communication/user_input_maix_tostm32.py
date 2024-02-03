from fpioa_manager import fm
from machine import UART
import utime

fm.register(23, fm.fpioa.UART1_TX, force=True)
fm.register(22, fm.fpioa.UART1_RX, force=True)

uart = UART(UART.UART1, 115200, 8, None, 1, timeout=1000, read_buf_len=4096)

#uart.write(b'hello world')
#x = 10
#init_message = 'a'
#uart.write(init_message) # send data back

while True:
    #read_data = '(' + str(x) + ',20,23)'
    ##if read_data:
        ##print("recv:", read_data)
    #uart.write(read_data) # send data back
    #print(read_data)
    #x = x +1
    #utime.sleep_ms(2000)
    x = input("Digite uma mensagme a ser enviada:")
    x = x.encode('ascii')
    uart.write(x) # send data back
    #utime.sleep_ms(2000)
    print('comando enviado')

