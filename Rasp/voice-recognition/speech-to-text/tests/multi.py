
from threading import Thread
import time
import subprocess
import os
import keyboard

def task():
    os.system('jackd -d alsa')

    # Inicia a thread em segundo plano
thread = Thread(target=task, daemon=True)
thread.start()
#print("Pressione qualquer tecla para interromper o código.")

# Loop principl
try:
    while True:
        print("normal thread")
        time.sleep(2)

    except KeyboardInterrupt:
        break
