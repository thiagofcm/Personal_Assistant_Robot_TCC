# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd
import KPU as kpu
from Maix import GPIO
from fpioa_manager import fm
from board import board_info
import time
from machine import UART

fm.register(14, fm.fpioa.UART1_TX, force=True)
fm.register(13, fm.fpioa.UART1_RX, force=True)

uart = UART(UART.UART1, 115200, 8, 1, 0)

# String para ser enviada
data_to_send = "hello world"

# Codificar a string em bytes usando UTF-8
#encoded_data = data_to_send.encode('utf-8')

while True:
    uart.write(b"hello")
    time.sleep(3)

## Configurar o pino GPIO para o LED
#fm.register(3, fm.fpioa.GPIO3)
#led_pin = GPIO(GPIO.GPIO3, GPIO.OUT)

#while True:
    ## Liga o LED
    #led_pin.value(1)
    ##uart.write(b'hello world')
    #time.sleep(1)

    ## Desliga o LED
    #led_pin.value(0)
    #time.sleep(1)



#fm.register(13, fm.fpioa.gpio(13))
#led_r=GPIO(GPIO.GPIO13,GPIO.OUT)
#utime.sleep_ms(500)
#led_r.value(0)
#fm.unregister(board_info.LED_R)

#lcd.init(freq=15000000)
#sensor.reset()
#sensor.set_pixformat(sensor.RGB565)
#sensor.set_framesize(sensor.QVGA)

#sensor.set_vflip(1)
#sensor.run(1)
#clock = time.clock()
##sensor.skip_frames(time = 2000)
#classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable','dog','horse','motorbike', 'person','pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
#task = kpu.load(0x500000)
#anchor = (1.889,2.5245, 2.9465, 3.94056, 3.99987, 5.3658, 5.155437, 6.92275, 6.710375, 9.01025)
#a = kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

#while(True):
    #clock.tick()
     #img = sensor.snapshot()
    #code = kpu.run_yolo2(task,img)
    #print(clock.fps())
    #if code:
        #for i in code:
            #a=img.draw_rectangle(i.rect())
            #a = lcd.display(img)
            #for i in code:
                #lcd.draw_string(i.x(), i.y(), classes[i.classid()], lcd.RED, lcd.WHITE)
                #lcd.draw_string(i.x(), i.y()+12, '%f1.3'%i.value(), lcd.RED, lcd.WHITE)
    #else:
        #a = lcd.display(img)
#a = kpu.deinit(task)

