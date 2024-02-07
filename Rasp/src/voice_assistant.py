import speech_recognition as sr
import pyttsx3
import openai
import threading
import subprocess
import time
import os
import pyaudio
from sound_effects import Sound_FX
from serial_rasp_maix import Serial_Commands
from led_control import Led

serial = Serial_Commands()
led = Led()
play = Sound_FX()
flag_init_sys = 0

#Initializing pyttsx3
engine = pyttsx3.init()

#Set your openai api key and customizing the chatgpt role
openai.api_key = "xyz"
messages = [{"role": "system", "content": "Your name is Jarvis and give answers in 2 lines"}]

#Customizing The output voice
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

engine.setProperty('rate', 120)
engine.setProperty('volume', volume)
engine.setProperty('voice', 'brazil')

task_flag=False

class Voice_Assistant():
    def __init__(self):
        """Class Builder"""
        led.green_led_off()
        led.red_led_on()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone() 
        self.run()

    def start_jack_server(self):
        subprocess.run(['jackd', '-d', 'alsa'])

    def get_response(self, user_input):
        messages.append({"role": "user", "content": user_input})
        query = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages
            )
        ChatGPT_reply = query["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})
        print(f"Robô: \"{ChatGPT_reply}\"") 
        return ChatGPT_reply


    def waiting_hotword(self):
        with self.microphone as source:  
            self.recognizer.adjust_for_ambient_noise(source, 5)
            self.recognizer.dynamic_energy_threshold = 4000
            led.green_led_on()
            print('Waiting for wakeword \"robô\"...')
            print()
            
           
            while True:
                audio = self.recognizer.listen(source, phrase_time_limit=10.0)
        
                try: 
                    text = self.recognizer.recognize_google(audio, language='pt-BR')
                    print(text)
                    if 'robô' in text.lower():
                        print('Wake word detected!')
                        led.blue_led_on()
                        play.wake()
                        engine.runAndWait()
                        self.provide_info(source)
                        break

                except sr.UnknownValueError:
                    print('Diga \"Robô\" para me chamar')
                    print()
                    pass
                except sr.WaitTimeoutError:
                    print('Timeout detected')
                    play.end()
                    self.waiting_hotword_2(source)

    def waiting_hotword_2(self,source):

        print('Waiting for wakeword \"robô\"...')
        print()
        led.green_led_on()
        while True:
            audio = self.recognizer.listen(source, phrase_time_limit=10.0)

            try:
                text = self.recognizer.recognize_google(audio, language='pt-BR')
                print(text)
                if 'robô' in text.lower():
                    print('Wake word detected!')
                    led.blue_led_on()
                    play.wake()
                    self.provide_info(source)
                    break

            except sr.UnknownValueError:
                print('Diga \"Robô\" para me chamar.')
                print()
                pass
            except sr.WaitTimeoutError:
                play.end()
                print('Waiting for wake word \"Robô\"...')
                print()
                pass
           

    def provide_info(self,source):

        global task_flag

        while True:
            try:
                print("Listening...")
                print()
                audio = self.recognizer.listen(source, timeout=5.0, phrase_time_limit=10.0)
                print("Recognizing...")
                query = self.recognizer.recognize_google(audio,language='pt-BR')
                print(f"Usuario: {query}.")
                print()

                if 'me trazer' in query and task_flag == False:
                    sentence = query.split()
                    obj = sentence[-1]
                    print(f"Robô: \"Ok, irei levar {obj} à voce.\"")
                    print()
                    engine.say(f'Ok, irei levar {obj} à voce')
                    engine.runAndWait()
                    led.red_led_on()
                    serial.send_bring_cmd(obj)
                    task_flag = True
                    print('Task Mode Activated') #When the robot is in this mode, it just respond to 'parar' and 'obrigado' to finish the task
                    #serial.wait_finish_task()

                elif 'siga-me' in query and task_flag == False:
                    print("Robô: \"Ok, irei te seguir.\"")
                    print()
                    engine.say("Ok, irei te seguir")
                    engine.runAndWait()
                    led.red_led_on()
                    serial.send_follow_cmd()
                    task_flag = True
                    print('Task Mode Activated') #When the robot is in this mode, it just responds to 'parar' and 'obrigado' to finish the task
                    #serial.wait_finish_task()   

                elif 'obrigado' in query:
                    print("Robô: \"Sem problemas.\"")
                    print()
                    engine.say("Sem problemas")
                    engine.runAndWait()
        
                
                elif 'parar' in query:
                    serial.send_stop_cmd()
                    play.end()
                    led.red_led_off()
                    task_flag = False
                    self.waiting_hotword_2(source)
                    

                else:
                    if task_flag == False:
                        response_from_openai = self.get_response(query)
                        engine.say(response_from_openai)
                        engine.runAndWait()

            except sr.UnknownValueError:
                print("Mensagem desconhecida")
                print()
                #engine.say("Não entendi")
                #engine.runAndWait()
            except sr.WaitTimeoutError: 
                if task_flag == True:
                    pass
                else:
                    play.end()
                    self.waiting_hotword_2(source)


    def kill_jackd_server(self):
        pid_jackd = subprocess.run(['pidof', 'jackd'], capture_output=True)
        pid = pid_jackd.stdout.decode()
        kill_cmd = "kill -9 " + pid
        os.system(kill_cmd)
        time.sleep(2)
        print("Program closed")


    def run(self):
        #Starts jack server in a thread:
        jackd_thread = threading.Thread(target=self.start_jack_server, daemon=True)
        jackd_thread.start()

        #Wait 4 seconds to jack server intialize:
        time.sleep(3)

        #Starts provide-information loop:
        info_thread = threading.Thread(target=self.waiting_hotword, daemon=True)
        info_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Closing Program...")
            led.green_led_off()
            self.kill_jackd_server()

