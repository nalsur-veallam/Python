import pygame
from pygame.draw import *



def score(number, score_1, score_2):
    FPS = 60
    finished = False
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    pygame.init()

    font = pygame.font.Font(None, 25)
    screen = pygame.display.set_mode([600, 800])
    screen.fill(WHITE)
    pygame.display.update()
    pygame.display.set_caption("Score")
    clock = pygame.time.Clock()
    while finished == False:
        clock.tick(FPS)
        if number:
            text = font.render("The red player received " + str(score_1) + " points", True, BLACK)
            place = text.get_rect(center=(300, 380))
            screen.blit(text, place)
            text = font.render("The blue player received " + str(score_2) + " points", True, BLACK)
            place = text.get_rect(center=(300, 420))
            screen.blit(text, place)
        else:
            text = font.render("The red player received " + str(score_1) + " points", True, BLACK)
            place = text.get_rect(center=(300, 400))
            screen.blit(text, place)
        text = font.render("Press SPACE to finish", True, BLACK)
        place = text.get_rect(center=(300, 750))
        screen.blit(text, place)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    finished = True
        pygame.display.update()
        screen.fill(WHITE)

    pygame.quit()
