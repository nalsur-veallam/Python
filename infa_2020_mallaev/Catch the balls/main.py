import pygame
from pygame.draw import *
from random import randint
print("Who will history remember you for?")
name = input()
print("You have 60 seconds to set your record. Are you ready?")
j = input()

pygame.init()
font = pygame.font.Font(None, 25)
font1 = pygame.font.Font(None, 50)
c = 0
score = 0
e = 1
a = 0
t = [0,0,0,0,0,0,0,0,0,0]
m = [10, 20, 30, 40 ,50]
p = [0,0,0,0,0,0,0,0,0,0]
b = 0
ballscoordx = []
ballscoordy = []
ballsrad = []
ballsspeedx = []
ballsspeedy = []
ballscolor = []

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(n):
    '''рисует новый шарик '''
    ballscoordx[n] = randint(200, 1000)
    ballscoordy[n] = randint(200, 700)
    ballsrad[n] = randint(10, 100)
    ballscolor[n] = COLORS[randint(0, 5)]
    ballsspeedx[n] = randint(-100, 100)
    ballsspeedy[n] = randint(-100, 100)
    circle(screen, ballscolor[n], (int(ballscoordx[n]), int(ballscoordy[n])),ballsrad[n])
    
def new(n):
    ballscoordx.append(float(randint(200, 1000)))
    ballscoordy.append(float(randint(200, 700)))
    ballsrad.append(randint(10, 100))
    ballscolor.append(COLORS[randint(0, 5)])
    ballsspeedx.append(randint(-100, 100))
    ballsspeedy.append(randint(-100, 100))
    circle(screen, ballscolor[n], (int(ballscoordx[n]), int(ballscoordy[n])),ballsrad[n])

def draw():
    for i in range(0, 9):
        if(ballscoordx[i]+ballsrad[i] >= 1100) or (ballscoordx[i]-ballsrad[i] <= 100):
            if(ballscoordx[i]+ballsrad[i] >= 1100):
                ballsspeedx[i] = randint(0, 100)*(-1)
            else:
                ballsspeedx[i] = randint(0, 100)
        if(ballscoordy[i]+ballsrad[i] >= 800) or (ballscoordy[i]-ballsrad[i] <= 100):
            if(ballscoordy[i]+ballsrad[i] >= 800):
                ballsspeedy[i] = randint(0, 100)*(-1)
            else:
                ballsspeedy[i] = randint(0, 100)
        ballscoordx[i] = ballscoordx[i] + float(ballsspeedx[i])/10
        ballscoordy[i] = ballscoordy[i] + float(ballsspeedy[i])/10
        circle(screen, ballscolor[i], (int(ballscoordx[i]), int(ballscoordy[i])),ballsrad[i])
        pygame.draw.line(screen, (255, 255, 255), [100, 100], [100,800], 3)
        pygame.draw.line(screen, (255, 255, 255), [100, 100], [1100,100], 3)
        pygame.draw.line(screen, (255, 255, 255), [1100,100], [1100,800], 3)
        pygame.draw.line(screen, (255, 255, 255), [1100, 800], [100,800], 3)






def meteors(c):
    for i in range(0,5):
        if(c/60>=m[i]) and (c/60 <=m[i] + 2):
            if(float(c/60) ==float(m[i])):
                for j in range (0, 9):
                    t[j] = randint(100,1050)
            else:
                b = 1
                for j in range (0, 9):
                    pygame.draw.rect(screen, COLORS[randint(0, 5)], (t[j], int(100+5.42*(c - m[i]*60)), 50, 50))
                    p[j] = int(100+5.42*(c - m[i]*60))
        else:
            b = 0

pygame.display.update()
pygame.display.set_caption("Игра века")
clock = pygame.time.Clock()
finished = False
for i in range(0,9):
    new(i)


while c < 3600:
    clock.tick(60)
    draw()
    meteors(c)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c = 3600
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coord = event.pos
            
            
            
            for j in range(0,5):
                if(c/60>=m[j]) and (c/60 <=m[j] + 2):
                    if(c != m[j]*60):
                        for i in range(0,9):
                            x = coord[0]
                            y = coord[1]
                            if(x>t[i])and(x<(t[i]+50))and(y>p[j]) and(y<(p[j]+50)):
                                score +=3
                                t[i] = -100
            
            
            
            for i in range(0,9):
                x = coord[0] - ballscoordx[i]
                y = coord[1] - ballscoordy[i]
                if((x**2 + y**2) <= ballsrad[i]**2):
                    score +=1
                    new_ball(i)
                    break
    
    
    
    
    
    
    for i in range(0,5):
        if(c/60>=m[i]-4) and (c/60 <m[i]):
            text = font1.render("Attention! Meteors will fall in " + str(int(m[i] - float(c)/60)) + " seconds!", True, (255,255,255))
            screen.blit(text, [270,40])
    text = font.render("You have "+str(60 - int(c/60))+" second left",True,(255, 255, 255))
    screen.blit(text, [0,0])
    text1 = font.render("Score: "+ str(score),True,(255, 255, 255))
    screen.blit(text1, [0,20])
    pygame.display.update()
    screen.fill(BLACK)
    c += 1

pygame.quit()





#Работаем с рейтингом
def clean():
    f = open('rating.txt', 'w+')
    f.seek(0)
    f.close()


f = open('rating.txt', 'r+')
try:
    d = 0
    g = 0
    str1 = f.readlines()
    strx = ""
    for i in range(0, len(str1)):
        str2 = str1[i]
        if((str1[i] == '\n')or(str1[i] == "")) and (g ==0) and (d == 0):
            strx = strx + str(name) + '\n'
            strx = strx + str(score) + '\n' + '\n'
            g = 1
        elif(i%2 != 0) and (g == 0) and (d == 0):
            if(int(str2) <= score)and(d==0):
                k = len(str1[i-1])
                strx = strx[0:-k]
                strx = strx + str(name) + '\n'
                strx = strx + str(score) + '\n'
                strx = strx + str1[i-1]
                strx = strx + str1[i]
                d = 1
            else:
                strx = strx + str1[i]
        elif(g == 0):
            strx = strx + str1[i]
    strx = strx + '\n'
    clean()
    f.seek(0)
    f.write(strx)
finally:
   f.close()
