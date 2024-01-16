import speech_recognition as sr
import os
import subprocess as sb

sb.run('jackd -d alsa', shell=True)

r = sr.Recognizer()
mic = sr.Microphone()

print("Start talking!")

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)
    speech = "espeak \"" + words + "\""
    print(speech)
    os.system(speech)
