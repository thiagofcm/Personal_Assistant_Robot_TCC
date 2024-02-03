from machine import UART
import machine
from fpioa_manager import fm
from Maix import GPIO
from fpioa_manager import fm
import utime
import _thread


#Define uart pins and configurations
fm.register(24, fm.fpioa.UART1_RX, force=True)
fm.register(32, fm.fpioa.UART1_TX, force=True)
uart = UART(UART.UART1, 115200, read_buf_len=4096)


#Define LED pin
LED_B=GPIO(GPIO.GPIO0,GPIO.OUT,value=1)

def serial_decision():

    try:
        text=uart.read()
        print(text)

        if text:
            word = (text.decode('utf-8'))

            if word == 'bring-agasalho':
                interrupt_third_decision = False
                print('1')
                uart.write('I got 1')
                LED_B.value(1)

            elif word == 'follow':
                interrupt_third_decision = False
                print('2')
                LED_B.value(0)
                uart.write('I got 2')

            elif word == 'stop':
                print('3')
                uart.write('I got 3')
                #_thread.start_new_thread(third_decision, ("2",))
                third_decision()

        else:
            print('no serial data received')
    except:
        print('nao deu pra ler')
    finally:
        uart.read()
        #utime.sleep_ms(1000)
        #SIG_INPUT.value(0)

def serial_loop(nothing):
    while True:
        if uart.any():
            print('tem mensagem')
            serial_decision()
        else:
            print('nao tem mensagem')

def third_decision():
    global interrupt_third_decision
    while True:
        LED_B.value(1)
        utime.sleep_ms(500)
        LED_B.value(0)
        utime.sleep_ms(500)

        if uart.any():
            break;


#def interrupt():
    #while True:
        #if uart.any():
            #print('tem mensagem')
            #SIG_INPUT.value(1)

        #else:
            #print('tem nada')


## #中断回调函数
## def fun(KEY):
##     global state
##     utime.sleep_ms(10) #消除抖动
##     if KEY.value()==0: #确认按键被按下
##         state = not state
##         LED_B.value(state)

## #开启中断，下降沿触发
##KEY.irq(fun, GPIO.IRQ_FALLING)
#SIG_INPUT.irq(serial, GPIO.IRQ_FALLING)


_thread.start_new_thread(serial_loop, ("1",))

#while True:
    #interrupt()
    ## Add a suitable delay here if needed
    #utime.sleep_ms(100)

while True:
    pass


