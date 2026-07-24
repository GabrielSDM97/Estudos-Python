from time import sleep
import pygame

# Variáveis de cores
limpar = '\033[m'
verde = '\033[92m'
ciano = '\033[96m'

''' Exercício 46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles. '''

pygame.init()
pygame.mixer.music.load("audios/beep.mp3")
pygame.mixer.music.set_volume(0.5)

for contagem in range(10, -1, -1):
    print(f'{ciano}{contagem}{limpar}')
    pygame.mixer.music.play()
    sleep(1)
print(f'\n{verde}Feliz ano novo{limpar}!')

pygame.mixer.music.load("audios/fireworks.mp3")
pygame.mixer.music.play()
sleep(6)
