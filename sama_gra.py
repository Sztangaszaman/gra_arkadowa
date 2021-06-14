import pygame, sys
import random
import math
from subprocess import call
from pygame import mixer

pygame.font.init()
font = pygame.font.SysFont('Corbel',80)
color_name = (255,0,0)
bigfont = pygame.font.SysFont('comicsansms',200)
text_name = bigfont.render('Game over', True, color_name)


textX = 10
textY = 10
score_value = 0
def show_score(x,y):
    score = font.render("score :" + str(score_value),True, (0,0,0))
    screen.blit(score, (x,y))

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('wilk.png'))
    enemyX.append(random.randint(1400,1550))
    enemyY.append(random.randint(0,1000))
    enemyX_change.append(-50)
    enemyY_change.append(5)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kaczka_2.png")
        #self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center = (screen_width/2,screen_height/2))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

        if self.rect.x >= screen_width/1.15:
            self.rect.x = screen_width/1.15
        #if self.rect.x <= screen_width/5 - 200:
         #   self.rect.x = screen_width/5 - 200

    def getX(self):
        return self.rect.x

    def setX(self, x):
        self.rect.x = x

    def getY(self):
        return self.rect.y

    def setY(self, y):
        self.rect.y = y

    def create_bullet(self, bullet_number):
        return Bullet(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], bullet_number)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y, bullet_number):
        super().__init__()
        self.image = pygame.Surface((30,5))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x,pos_y))
        self.bullet_number = bullet_number

    def update(self):
        self.rect.x += 5

    def getX(self):
        return self.rect.x

    def setX(self, x):
        self.rect.x = x

    def getY(self):
        return self.rect.y

    def setY(self, y):
        self.rect.y = y
        
    def getBulletNumber(self):
        return self.bullet_number

        if self.rect.x >= screen_width + 200:
            self.kill()

def isCollision(enemyX,enemyY,bullets):

    for bullet in bullets:
        if (bullet.getX() <= screen_width):
            # wypisz pozycje poki na ekranie, ToDo - sprawdzaj tutaj kolizje
            #print(enemyX, enemyY, "pozycja x,y kuli nr", bullet.getBulletNumber(), bullet.getX(), bullet.getY())
            distance = math.sqrt((math.pow(enemyX-bullet.getX(),2)) + (math.pow(enemyY-bullet.getY(),2)))
            if distance < 50:
                return True
            else:
                return False

def game_over(enemyX,enemyY,players):

    for player in players:
            # wypisz pozycje poki na ekranie, ToDo - sprawdzaj tutaj kolizje
            #print(enemyX, enemyY, "pozycja x,y kuli nr", bullet.getBulletNumber(), bullet.getX(), bullet.getY())
            distance = math.sqrt((math.pow(enemyX-player.getX(),2)) + (math.pow(enemyY-player.getY(),2)))
            if distance < 50:
                return True
            else:
                return False

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1600,1000
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('jungle.jpg')
pygame.mouse.set_visible(False)
mixer.music.load('background_music.wav')
mixer.music.play(-1)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_Sound = mixer.Sound('gun_sound.wav')
            bullet_Sound.play()
            bullet_group.add(player.create_bullet(len(bullet_group)))
            
    screen.blit(background, (0,0))
    bullet_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    bullet_group.update()

    for i in range(num_of_enemies):
        enemyY[i] += enemyY_change[i]
        if enemyY[i] <= 0:
            enemyY_change[i] = 5
            enemyX[i] += enemyX_change[i]
        elif enemyY[i] >= 950:
            enemyY_change[i] = -5
            enemyX[i] += enemyX_change[i]

        collision = isCollision(enemyX[i],enemyY[i],bullet_group)
        if collision:
            colision_Sound = mixer.Sound('colision_sound.wav')
            colision_Sound.play()
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(1400, 1550)
            enemyY[i] = random.randint(0, 1000)
        enemy(enemyX[i],enemyY[i], i)
            
        gameover = game_over(enemyX[i],enemyY[i],player_group)
        if gameover:
            pygame.quit
            running = False
            screen.blit(text_name , (screen_width/3-150,screen_height/3-50))
            print("GAME OVER")
    show_score(textX,textY)
    pygame.display.flip()
    clock.tick(120)



