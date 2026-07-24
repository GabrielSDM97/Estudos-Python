import pygame  # Módulo para música, criação de jogos, etc...
from time import sleep  # Módulo para controle de tempo.

''' Exercício 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3. '''

pygame.init()
pygame.mixer.music.load("../0_áudios/music.mp3")
pygame.mixer.music.play()

''' O loop abaixo verifica se o music player está ativo, caso esteja, adiciona 1 segundo para que o mesmo consiga tocar por mais 1 segundo.
Sem esse loop, o music player simplesmente finalizaria instantaneamente antes do arquivo .mp3 começar a tocar.'''

while pygame.mixer.music.get_busy(): 
    sleep(1)

pygame.quit()
