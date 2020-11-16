import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 560))


################################################################################
def draw_house(x, y, k):
    polygon(screen, (255, 204, 0),
            [(x - int(30 * k), y - int(40 * k)), (x + int(40 * k), y - int(30 * k)), (x + int(40 * k), y + int(40 * k)),
             (x - int(30 * k), y + int(30 * k))], 0)
    polygon(screen, (0, 0, 0),
            [(x - int(30 * k), y - int(40 * k)), (x + int(40 * k), y - int(30 * k)), (x + int(40 * k), y + int(40 * k)),
             (x - int(30 * k), y + int(30 * k))], 1)
    polygon(screen, (255, 204, 0),
            [(x + int(40 * k), y - int(30 * k)), (x + int(70 * k), y - int(50 * k)), (x + int(70 * k), y + int(20 * k)),
             (x + int(40 * k), y + int(40 * k))], 0)
    polygon(screen, (0, 0, 0),
            [(x + int(40 * k), y - int(30 * k)), (x + int(70 * k), y - int(50 * k)), (x + int(70 * k), y + int(20 * k)),
             (x + int(40 * k), y + int(40 * k))], 1)
    polygon(screen, (255, 153, 0), [(x - int(30 * k), y - int(40 * k)), (x + int(10 * k), y - int(90 * k)),
                                    (x + int(40 * k), y - int(30 * k))], 0)
    polygon(screen, (0, 0, 0), [(x - int(30 * k), y - int(40 * k)), (x + int(10 * k), y - int(90 * k)),
                                (x + int(40 * k), y - int(30 * k))], 1)
    polygon(screen, (255, 153, 0), [(x + int(10 * k), y - int(90 * k)), (x + int(40 * k), y - int(110 * k)),
                                    (x + int(70 * k), y - int(50 * k)), (x + int(40 * k), y - int(30 * k))], 0)
    polygon(screen, (0, 0, 0), [(x + int(10 * k), y - int(90 * k)), (x + int(40 * k), y - int(110 * k)),
                                (x + int(70 * k), y - int(50 * k)), (x + int(40 * k), y - int(30 * k))], 1)
    circle(screen, (0, 0, 0), (x, y), int(20 * k), 0)


################################################################################
def draw_fence(x, y, k):
    for i in range(20):
        rect(screen, (255, 204, 102), (x + int(i * 20 * k), y, int(20 * k), int(240 * k)), 0)
        rect(screen, (0, 0, 0), (x + int(i * 20 * k), y, int(20 * k), int(240 * k)), 1)


################################################################################
def draw_dog(x, y, k, orientation):
    if orientation == True:
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y - int(40 * k), int(120 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(100 * k), y - int(50 * k), int(60 * k), int(40 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(110 * k), y - int(30 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(110 * k), y - int(10 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y - int(30 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(110 * k), y + int(30 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y + int(10 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(30 * k), y - int(30 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(10 * k), y - int(10 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y + int(20 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x, y + int(40 * k), int(30 * k), int(10 * k)), 0)
        rect(screen, (128, 128, 128), (x, y - int(60 * k), int(50 * k), int(50 * k)), 0)
        rect(screen, (0, 0, 0), (x, y - int(60 * k), int(50 * k), int(50 * k)), 1)
        ellipse(screen, (255, 0, 0), (x + int(20 * k), y - int(30 * k), int(10 * k), int(17 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(10 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(10 * k), y - int(50 * k), int(30 * k), int(30 * k)), 1)
        rect(screen, (128, 128, 128), (x + int(10 * k), y - int(50 * k), int(30 * k), int(20 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(40 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (128, 128, 128), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (255, 255, 255), (x + int(30 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(30 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (255, 255, 255), (x + int(10 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(10 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (0, 0, 0), (x + int(13 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(33 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)

    elif orientation == False:
        ellipse(screen, (128, 128, 128), (x - int(50 * k), y - int(40 * k), int(120 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y - int(50 * k), int(60 * k), int(40 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(80 * k), y - int(30 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(100 * k), y - int(10 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(60 * k), y - int(30 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(80 * k), y + int(30 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y + int(10 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(60 * k), y - int(30 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(20 * k), y - int(10 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y + int(20 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(30 * k), y + int(40 * k), int(30 * k), int(10 * k)), 0)
        rect(screen, (128, 128, 128), (x - int(50 * k), y - int(60 * k), int(50 * k), int(50 * k)), 0)
        rect(screen, (0, 0, 0), (x - int(50 * k), y - int(60 * k), int(50 * k), int(50 * k)), 1)
        ellipse(screen, (255, 0, 0), (x - int(30 * k), y - int(30 * k), int(10 * k), int(17 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(40 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(40 * k), y - int(50 * k), int(30 * k), int(30 * k)), 1)
        rect(screen, (128, 128, 128), (x - int(40 * k), y - int(50 * k), int(30 * k), int(20 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(60 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(60 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (128, 128, 128), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (255, 255, 255), (x - int(40 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(40 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (255, 255, 255), (x - int(20 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(20 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (0, 0, 0), (x - int(37 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(17 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)


################################################################################

rect(screen, (51, 255, 255), (0, 0, 400, 280), 0)  # sky
rect(screen, (102, 255, 51), (0, 280, 400, 280), 0)  # grass

draw_fence(80, 8, 1.3)
draw_fence(0, 130, 0.8)
draw_fence(0, 220, 0.6)
draw_fence(260, 180, 0.8)
draw_dog(360, 340, 0.7, True)
draw_house(280, 390, 1)
draw_dog(70, 350, 1, False)
draw_dog(130, 500, 1, True)
draw_dog(380, 560, 3, False)
################################################################################

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
