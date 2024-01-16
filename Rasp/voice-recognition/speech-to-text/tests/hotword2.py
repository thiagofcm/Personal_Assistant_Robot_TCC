import pvporcupine
import speech_recognition as sr
import pyttsx3

#print(pvporcupine.KEYWORDS)
#handle = pvporcupine.create(keywords=['alexa'])
#def get_audio():

def speak(text):
    engine = pyttsx.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print("jarviszazda online: " + text + "\n")
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...", end="")
        audio = r.listen(source)
        query= ''

        try:
            print("Recognizing....", end="")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}")

        except Exception as e:
            print("Exception: " + str(e))

    return query.lower()


def main():
    said = takeCommand()
    speak("I heard you said: " + said)

main()


