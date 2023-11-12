import config_activate, objects
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
pygame.init()

def rep():
    if config_activate.glitter[0]:
        objects.alldata.set(objects.alldata.get())
        objects.alldata.set(config_activate.glitter[1])
        config_activate.glitter[1] -= 1
        if config_activate.glitter[1] < 0:
            config_activate.glitter[2] = True; config_activate.glitter[0] = False
            objects.alldata.set('Время вышло!')
            pygame.mixer.init()
            pygame.mixer.music.load('sounds/sound.mp3')
            pygame.mixer.music.play()

            objects.btn2.pack(pady=10)

    if objects.stop:
        pygame.mixer.music.stop()
        objects.stop = False
    config_activate.win.after(1000, rep)


config_activate.win.after(1000, rep)