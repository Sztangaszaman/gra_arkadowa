import pygame
import sys
from subprocess import call
from pygame import mixer


pygame.init()
pygame.font.init()

res = (720,720)

mixer.music.load('background_music.wav')
mixer.music.play(-1)

win = screen = pygame.display.set_mode(res)
kaczka = pygame.image.load('kaczka_armed.png')

color_q = (255,10,10)
color_s = (150,234,23)
color_d = (34,123,20)
color_r = (189,13,204)
color_b = (89,213,100)
color_i = (200,80,160)
color_name = (70,30,0)

# light shade of the button
color_light = (200,200,170)

# dark shade of the button
color_dark = (0,0,0)

width = screen.get_width()

height = screen.get_height()

smallfont = pygame.font.SysFont('Corbel',36)
bigfont = pygame.font.SysFont('comicsansms',76)

text_q = smallfont.render('quit' , True , color_q)
text_s = smallfont.render('start' , True , color_s)
text_d = smallfont.render('difficulty level' , True , color_d)
text_r = smallfont.render('rules' , True , color_r)
text_b = smallfont.render('best results' , True , color_b)
text_i = smallfont.render('information' , True , color_i)
text_name = bigfont.render('The Hunter', True, color_name)

while True:

    for ev in pygame.event.get():

        # PRZYCISK X
        if ev.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()

        # KLIKNIĘCIE MYSZY
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # PRZYCISK QUIT
            if width/2 <= mouse[0] <= width/2+219 and height/1.26 <= mouse[1] <= height/1.26+45:
                pygame.quit()
                running = False
                sys.exit()

            # PRZYCISK START
            if width/2 <= mouse[0] <= width/2+219 and height/2.4 <= mouse[1] <= height/2.4+45:
                call(["python", "sama_gra.py"])

            # PRZYCISK ZASADY
            if width/2 <= mouse[0] <= width/2+219 and height/2.03 <= mouse[1] <= height/2.03+45:
                print("RULES CLICKED")
                

            # PRZYCISK POZIOM TRUDNOŚCI
            if width/2 <= mouse[0] <= width/2+219 and height/1.76 <= mouse[1] <= height/1.76+45:
                print("DIFFICULTY LEVEL CLICKED")
                # ToDo - obsłużyć przycisk

            # PRZYCISK NAJLEPSZE WYNIKI
            if width/2 <= mouse[0] <= width/2+219 and height/1.55 <= mouse[1] <= height/1.55+45:
                print("BEST RESULTS CLICKED")
                # ToDo - obsłużyć przycisk

            # PRZYCISK INFORMACJE
            if width/2 <= mouse[0] <= width/2+219 and height/1.39 <= mouse[1] <= height/1.39+45:
                print("INFORMATION CLICKED")
                call(["python","gameInstructions.py"])

    # fills the screen with a color
    screen.fill((148,0,206))
    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # start
    if width/2 <= mouse[0] <= width/2+219 and height/2.4 <= mouse[1] <= height/2.4+45:
        pygame.draw.rect(screen,color_light,[width/2,height/2.4,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2.4,220,45])
    # rules
    if width/2 <= mouse[0] <= width/2+219 and height/2.03 <= mouse[1] <= height/2.03+45:
        pygame.draw.rect(screen,color_light,[width/2,height/2.03,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2.03,220,45])
    # difficulty level
    if width/2 <= mouse[0] <= width/2+219 and height/1.76 <= mouse[1] <= height/1.76+45:
        pygame.draw.rect(screen,color_light,[width/2,height/1.76,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/1.76,220,45])
    # best results
    if width/2 <= mouse[0] <= width/2+219 and height/1.55 <= mouse[1] <= height/1.55+45:
        pygame.draw.rect(screen,color_light,[width/2,height/1.55,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/1.55,220,45])
    # information
    if width/2 <= mouse[0] <= width/2+219 and height/1.39 <= mouse[1] <= height/1.39+45:
        pygame.draw.rect(screen,color_light,[width/2,height/1.39,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/1.39,220,45])
    # quit
    if width/2 <= mouse[0] <= width/2+219 and height/1.26 <= mouse[1] <= height/1.26+45:
        pygame.draw.rect(screen,color_light,[width/2,height/1.26,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/1.26,220,45])
    # superimposing the text onto our button
    screen.blit(text_s , (width/2+70,height/2.37))
    screen.blit(text_r , (width/2+70,height/2))
    screen.blit(text_d , (width/2+10,height/1.73))
    screen.blit(text_b , (width/2+30,height/1.53))
    screen.blit(text_i , (width/2+28,height/1.37))
    screen.blit(text_q , (width/2+75,height/1.25))
    screen.blit(text_name , (width/2.5,height/10))
    win.blit(kaczka, (-240,-550))
    #win.blit(wilk, (-20, -50))
    # updates the frames of the game
    pygame.display.update()
