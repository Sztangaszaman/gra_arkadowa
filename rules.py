import pygame, sys
from subprocess import call

pygame.init()
pygame.font.init()

res = (720,720)
win = screen = pygame.display.set_mode(res)

width = screen.get_width()

height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel',36)
bigfont = pygame.font.SysFont('comicsansms',76)
minifont = pygame.font.SysFont('Corbel',30)
mediumfont = pygame.font.SysFont('Corbel',50)
color = (0,0,0)

text_q = minifont.render('Przegrywasz wpadając na wroga lub gdy wróg całkowicie' , True , color)
text_l = minifont.render('przeleci na lewą stronę mapy.' , True , color)
text_x = minifont.render('Po zdobytych  10  punktach wrogowie przyspieszają.' , True , color)
text_s = smallfont.render('- to twoja postać' , True , color)
text_d = smallfont.render('- to postać wroga' , True , color)
text_r = minifont.render('Ruch twojej postaci odbywa się za pomocą kursora.' , True , color)
text_b = minifont.render('Strzelasz dowolnym przyciskiem myszki.' , True , color)
text_y = mediumfont.render('UDANEJ ZABAWY' , True , color)
text_i = minifont.render('Zdobywasz  1  punkt za każdego ustrzelongo wroga.' , True , color)
text_name = bigfont.render('ZASADY', True, color)
background = pygame.image.load('pergamin.jpg')
screen.blit(background, (-100,-100))
kaczka = pygame.image.load('kaczka_2.png')
wilk = pygame.image.load('wilk.png')

while True:

    for ev in pygame.event.get():

        # PRZYCISK X
        if ev.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()
    screen.blit(text_s , (150,170))
    screen.blit(text_r , (10,350))
    screen.blit(text_d , (150,260))
    screen.blit(text_b , (10,390))
    screen.blit(text_i , (10,430))
    screen.blit(text_q , (10,470))
    screen.blit(text_l , (10,510))
    screen.blit(text_x , (10,550))
    screen.blit(text_y , (200,610))
    screen.blit(text_name , (width/3.1,height/10-80))
    win.blit(kaczka, (5, 120))
    win.blit(wilk, (20, 250))

    pygame.display.update()
