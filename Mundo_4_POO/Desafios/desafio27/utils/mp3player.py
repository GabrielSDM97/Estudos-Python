import pygame
from time import sleep

def mp3(caminho):
    pygame.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy(): 
        sleep(1)

    pygame.quit()
