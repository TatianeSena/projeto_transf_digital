#desafio 21 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

#importante instalar o arquivo no pycharm
import pygame (se não tiver fazer a instalação)
         pygame.init()
         pygame.mixer.music.load('nome do arquivo')
         pygame.mixer.music.play()
         pygame.event.wait()
