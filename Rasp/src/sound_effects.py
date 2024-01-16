import pygame

path = "/home/thiagofcm/ufu/tcc/desenvolvimento/oriented-obj/rigtones/"
wake = "wake.wav"
end = "end.wav"

class Sound_FX():
    def __init__(self):
        """ Class Builder """
        pygame.mixer.init()
        speaker_volume = 2.0
        pygame.mixer.music.set_volume(speaker_volume)

    def wake(self):
        pygame.mixer.music.load(path + wake)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    def end(self):
        pygame.mixer.music.load(path + end)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
