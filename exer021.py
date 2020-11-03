# TOCANDO UM MP3
# instalado a biblioteca "pygame"
import pygame
# iniciando o pygame
pygame.init()
# utilizando o mixer do pygame pra tocar a musica.
pygame.mixer.music.load("exe021.mp3")
pygame.mixer.music.play()
# para esperar o "evento" terminar e encerrar a musica é usado o "wait"
pygame.event.wait()


