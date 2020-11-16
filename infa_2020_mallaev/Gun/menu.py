import pygame
from pygame.draw import *
def menu():
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    FPS = 60
    finished = False

    pygame.init()

    font_0 = pygame.font.Font(None, 50)
    font = pygame.font.Font(None, 25)
    screen = pygame.display.set_mode([600, 800])
    screen.fill(WHITE)
    pygame.display.update()
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()

    while finished==False:
        clock.tick(FPS)
        text = font_0.render("SELECT THE GAME MODE", True, RED)
        place = text.get_rect(center=(300, 200))
        screen.blit(text, place)
        rect(screen, BLACK, (200,250,200,100), 5)
        text = font.render("SINGLE PLAYER GAME", True, BLACK)
        place = text.get_rect(center=(300, 300))
        screen.blit(text, place)
        rect(screen, BLACK, (200,400,200,100), 5)
        text = font.render("TWO PLAYERS GAME", True, BLACK)
        place = text.get_rect(center=(300, 450))
        screen.blit(text, place)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coord = event.pos
                if coord[0] > 200 and coord[0] < 400:
                    if coord[1] > 250 and coord[1] < 350:
                        finished = True
                        return False
                    elif coord[1] > 400 and coord[1] < 500:
                        finished = True
                        return True
                    
        pygame.display.update()
        screen.fill(WHITE)

    pygame.quit()
