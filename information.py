import pygame, sys
from subprocess import call

pygame.init()
pygame.font.init()

res = (720,720)
win = screen = pygame.display.set_mode(res)

width = screen.get_width()

height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel',36)
bigfont = pygame.font.SysFont('comicsansms',80)
minifont = pygame.font.SysFont('Corbel',30)
mediumfont = pygame.font.SysFont('Corbel',50)
duzyfont = pygame.font.SysFont('comicsansms',50)
color = (0,0,0)

text_q = minifont.render('Rok I Semestr II' , True , color)
text_l = minifont.render('Na potrzeby przedmiotu: programowanie' , True , color)
text_s = smallfont.render('Gra stworzona przez:' , True , color)
text_d = duzyfont.render('Tymon Jastrzębski' , True , color)
text_r = minifont.render('Politechnika Wrocławska' , True , color)
text_b = minifont.render('Wydział Matematyki' , True , color)
text_y = mediumfont.render('UDANEJ ZABAWY' , True , color)
text_i = minifont.render('Kierunek Matematyka Stosowana ' , True , color)
text_name = bigfont.render('Informacje', True, color)
background = pygame.image.load('pergamin.jpg')
screen.blit(background, (-100,-100))


while True:

    for ev in pygame.event.get():

        # PRZYCISK X
        if ev.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()
    screen.blit(text_s , (10,170))
    screen.blit(text_r , (10,350))
    screen.blit(text_d , (120,230))
    screen.blit(text_b , (10,390))
    screen.blit(text_i , (10,430))
    screen.blit(text_q , (10,470))
    screen.blit(text_l , (10,510))
    screen.blit(text_y , (200,610))
    screen.blit(text_name , (width/4,height/10-80))
  

    pygame.display.update()