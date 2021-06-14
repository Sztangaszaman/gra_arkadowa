import pygame
import sys

pygame.init()
pygame.font.init()

color_name = (0,0,0)
color_d = (255,255,255)

while True:

    for ev in pygame.event.get():

        # PRZYCISK X
        if ev.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()

    res = (720,720)
    win = screen = pygame.display.set_mode(res)
    width = screen.get_width()
    height = screen.get_height()
    bigfont = pygame.font.SysFont('comicsansms',76)
    smallfont = pygame.font.SysFont('Corbel',36)
    text_name = bigfont.render('INSTRUCTION', True, color_name)
    text_d = smallfont.render('Treść' , True , color_d)
    screen.fill((148,0,206))
    screen.blit(text_name , (width/7,height/10-80))
    screen.blit(text_d , (width/9-50,height/6))
    pygame.display.update()

