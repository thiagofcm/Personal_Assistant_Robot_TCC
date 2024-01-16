import time
import subprocess
import threading
import pyaudio
import pyttsx3
import struct
import speech_recognition as sr
import pvporcupine
import os


# Função para iniciar o servidor Jack
def start_jack_server():
    subprocess.run(['jackd', '-d', 'alsa'])

# Função para o loop de reconhecimento de voz
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening")
        audio = recognizer.listen(source)
        query=''

        try:
            print("Recognizing...", end="")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}")
            
            if "hello" in query:
                print("hot word detected")
                take_new_command()

        except sr.UnknownValueError:
            print("Nao foi possivel entender o audio.")
            
        except sr.RequestError as e:
            print(f"Erro: {e}")
        
    return query.lower()

def speak(text):
    engine = pyttsx3.init('espeak')
    #voices = engine.getProperty('voices')
    engine.setProperty('rate',150)
    print("J.A.R.V.I.S.: " + text + "\n")
    engine.say(text)
    engine.runAndWait()

def ConversationFlow():
    #ouvindo = takeCommand()
    #if "hello" in ouvindo:
    print("conversation start")
    while True:
        userSaid = take_new_command()
        if "bring me" in userSaid:
            speak("okay sir, I will bring it to you")
        if "information" in userSaid:
            speak("okay, the answer is")
        if "follow me" in userSaid:
            speak("i'm following you")
        if "stop" in userSaid:
            speak("stopping")
            break

def take_new_command():
    recognizer_2 = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer_2.adjust_for_ambient_noise(mic, duration=0.2)
        print("Now you are talking to me...")
        audio = recognizer_2.listen(mic)
        text = ''

        try:
            print("Recognizing commands...")
            text = recognizer_2.recognize_google(audio, language='en-US')
            print(f'You said: {text}')

        except sr.UnknownValueError:
            print("i did not understand you")

        except sr.RequestError as e:
            print(f"Error: {e}")

    return text.lower()


def run_assistant():
    recognizer = sr.Recognizer()
    print("listening....")
    while True:
        #print("in loop...")
        try:
            takeCommand()
            #with speech_recognition.Microphone() as mic:
            #    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            #    audio = recognizer.listen(mic)

            #    text = recognizer.recognize_google(audio)
            #    print(f"User said: {text}")
            #    text = text.lower()

            #    if "hello" in text:
            #        audio = recognizer.listen(mic)
            #        text = recognizer.recognize_google(audio)
            #        text = text.lower()
            #        if "stop" in text:
            #            speak("bye")
            #        else:
            #            speak("okay i got it")

        except:
            print("except")

def main():
    ConversationFlow()
    #run_assistant() 
#def main():
#    porcupine = None
#    pa = None
#    audio_stream = None

#    print("jarvis inicializado")

#    try:
#        porcupine = pvporcupine.create(keywords=["jarvis", "ok google"])
#        pa = pyaudio.PyAudio()
#        audio_stream = pa.open(rate=48000,
#                               channels=1,
#                               format=pyaudio.paInt16,
#                               input=True,
#                               frames_per_buffer=porcupine.frame_length)
#        while True:
#            pcm = audio_stream.read(porcupine.frame_length)
#            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
           # result = porcupine.process(pcm)
            #print(result)
#            keyword_index=porcupine.process(pcm)
#            print(keyword_index)
#            if keyword_index >= 0:
#                print("Hot word detected...")
#                ConversationFlow()
#                time.sleep(1)
#                print("awaiting your command")
#    finally:
#        if porcupine is not None:
#            porcupine.delete()

#engine = pyttsx3.init()

# Inicia o servidor Jack em uma thread
jack_thread = threading.Thread(target=start_jack_server, daemon=True)
jack_thread.start()

# Aguarda um momento para garantir que o servidor Jack tenha tempo para inicializar
time.sleep(3)

# Inicia o loop de reconhecimento de voz em uma thread
voice_thread = threading.Thread(target=main, daemon=True)
voice_thread.start()

# Aguarda as threads continuarem em execução (pode ser substituído por outro mecanismo de espera)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("progama vai encerrar")
    pid_jackd = subprocess.run(['pidof','jackd'], capture_output=True)
    pid = pid_jackd.stdout.decode()
    kill_cmd = "kill -9 " + pid
    #print(kill_cmd)
    os.system(kill_cmd) 
    print("Programa encerrado.")
