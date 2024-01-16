import time
import subprocess
import threading
import speech_recognition as sr

# Função para iniciar o servidor Jack
def start_jack_server():
    subprocess.run(['jackd', '-d', 'alsa'])

# Função para o loop de reconhecimento de voz
def voice_recognition_loop():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("diga algo")
            audio = recognizer.listen(source)
            #time.sleep(2)

            try:
                text = recognizer.recognize_google(audio)
                print("Voce disse: ", text)
            except sr.UnknownValueError:
                print("Nao foi possivel entender o audio.")
            except sr.RequestError as e:
                print(f"Erro: {e}")

# Inicia o servidor Jack em uma thread
jack_thread = threading.Thread(target=start_jack_server, daemon=True)
jack_thread.start()

# Aguarda um momento para garantir que o servidor Jack tenha tempo para inicializar
time.sleep(5)

# Inicia o loop de reconhecimento de voz em uma thread
voice_thread = threading.Thread(target=voice_recognition_loop, daemon=True)
voice_thread.start()

# Aguarda as threads continuarem em execução (pode ser substituído por outro mecanismo de espera)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Programa encerrado.")
