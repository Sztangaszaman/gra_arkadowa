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
background = pygame.image.load('jungle.jpg')


color_q = (255,10,10)
color_s = (150,234,23)
color_d = (34,123,20)
color_r = (189,13,204)
color_name = (70,30,0)
color_l = (155,25,255)
# light shade of the button
color_light = (200,200,170)

# dark shade of the button
color_dark = (0,0,0)

width = screen.get_width()

height = screen.get_height()

minifont = pygame.font.SysFont('Corbel',25)
smallfont = pygame.font.SysFont('Corbel',36)
bigfont = pygame.font.SysFont('comicsansms',76)

text_s = smallfont.render('difficulty level:' , True , color_s)
text_d = smallfont.render('information' , True , color_d)
text_r = smallfont.render('rules' , True , color_r)
text_b = smallfont.render('quit' , True , color_q)
text_name = bigfont.render('Main Menu', True, color_name)
text_e = minifont.render('easy' , True , color_l)
text_m = minifont.render('medium' , True , color_l)
text_h = minifont.render('hard' , True , color_l)

while True:

    for ev in pygame.event.get():

        # PRZYCISK X
        if ev.type == pygame.QUIT:
            pygame.quit()
            running = False
            sys.exit()

        # KLIKNIĘCIE MYSZY
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # PRZYCISK easy
            if width/2+230 <= mouse[0] <= width/2+320 and height/2.4 - 16 <= mouse[1] <= height/2.4+5:
                call(["python", "easy.py"])

            # przycisk medium
            if width/2+230 <= mouse[0] <= width/2+320 and height/2.4 +6.5 <= mouse[1] <= height/2.4 +29.5:
                call(["python", "medium.py"])

            # przycisk hard
            if width/2+230 <= mouse[0] <= width/2+320 and height/2.4 +29.5 <= mouse[1] <= height/2.4 +50:
                call(["python", "hard.py"])            

            # PRZYCISK rules
            if width/2 <= mouse[0] <= width/2+219 and height/2.03 <= mouse[1] <= height/2.03+45:
                print("RULES CLICKED")
                call(["python", "rules.py"])

            # PRZYCISK information
            if width/2 <= mouse[0] <= width/2+219 and height/1.76 <= mouse[1] <= height/1.76+45:
                call(["python", "information.py"])
                # ToDo - obsłużyć przycisk

            # Przycisk quit
            if width/2 <= mouse[0] <= width/2+219 and height/1.55 <= mouse[1] <= height/1.55+45:
                pygame.quit()
                running = False
                sys.exit()

    mouse = pygame.mouse.get_pos()
    screen.blit(background, (0,0))
    
    pygame.draw.rect(screen,color_dark,[width/2,height/2.4,220,45])
    # rules
    if width/2 <= mouse[0] <= width/2+219 and height/2.03 <= mouse[1] <= height/2.03+45:
        pygame.draw.rect(screen,color_light,[width/2,height/2.03,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/2.03,220,45])
    # Information
    if width/2 <= mouse[0] <= width/2+219 and height/1.76 <= mouse[1] <= height/1.76+45:
        pygame.draw.rect(screen,color_light,[width/2,height/1.76,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/1.76,220,45])
    #quit
    if width/2 <= mouse[0] <= width/2+219 and height/1.55 <= mouse[1] <= height/1.55+45:
        pygame.draw.rect(screen,color_light,[width/2,height/1.55,220,45])

    else:
        pygame.draw.rect(screen,color_dark,[width/2,height/1.55,220,45])
    #easy
    if width/2+230 <= mouse[0] <= width/2+320 and height/2.4 - 16 <= mouse[1] <= height/2.4+5:
        pygame.draw.rect(screen,color_light,[width/2 +230,height/2.4-15.5,89,22])
    else:
        pygame.draw.rect(screen,color_dark,[width/2 +230,height/2.4-15.5,89,22])
    #medium    
    if width/2+230 <= mouse[0] <= width/2+320 and height/2.4 +6.5 <= mouse[1] <= height/2.4 +29.5:
        pygame.draw.rect(screen,color_light,[width/2 +230,height/2.4+7,89,22])
    else:
        pygame.draw.rect(screen,color_dark,[width/2 +230,height/2.4+7,89,22])
    #hard   
    if width/2+230 <= mouse[0] <= width/2+320 and height/2.4 +29.5 <= mouse[1] <= height/2.4 +50:
        pygame.draw.rect(screen,color_light,[width/2 +230,height/2.4+30,89,22])
    else:
        pygame.draw.rect(screen,color_dark,[width/2 +230,height/2.4+30,89,22])

    screen.blit(text_s , (width/2+10,height/2.35))
    screen.blit(text_r , (width/2+70,height/2))
    screen.blit(text_d , (width/2+28,height/1.73))
    screen.blit(text_b , (width/2+75,height/1.53))
    screen.blit(text_name , (width/2.5,height/10))
    screen.blit(text_e , (width/2+250,height/2.4-20))
    screen.blit(text_m , (width/2+233,height/2.35))
    screen.blit(text_h , (width/2+250,height/2.17))
    win.blit(kaczka, (-240,-550))

    pygame.display.update()
