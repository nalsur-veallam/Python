import pygame
from pygame.draw import *



def manual(number):
    FPS = 60
    finished = False
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    pygame.init()

    font = pygame.font.Font(None, 25)
    screen = pygame.display.set_mode([600, 800])
    screen.fill(WHITE)
    pygame.display.update()
    pygame.display.set_caption("Manual")
    clock = pygame.time.Clock()
    while finished == False:
        clock.tick(FPS)
        if number:
            text = font.render("For the player with the red gun:", True, BLACK)
            place = text.get_rect(center=(300, 100))
            screen.blit(text, place) 
            text = font.render("move the gun to the left - A", True, BLACK)
            place = text.get_rect(center=(300, 135))
            screen.blit(text, place) 
            text = font.render("move the gun to the right - D", True, BLACK)
            place = text.get_rect(center=(300, 170))
            screen.blit(text, place) 
            text = font.render("turn the muzzle counterclockwise - W", True, BLACK)
            place = text.get_rect(center=(300, 205))
            screen.blit(text, place) 
            text = font.render("turn the muzzle clockwise - s", True, BLACK)
            place = text.get_rect(center=(300, 240))
            screen.blit(text, place) 
            text = font.render("shoot - HOLD_DOWN_THE_V_KEY", True, BLACK)
            place = text.get_rect(center=(300, 275))
            screen.blit(text, place)
            
            text = font.render("For the player with the blue gun:", True, BLACK)
            place = text.get_rect(center=(300, 375))
            screen.blit(text, place) 
            text = font.render("move the gun left - ARROW-LEFT", True, BLACK)
            place = text.get_rect(center=(300, 410))
            screen.blit(text, place) 
            text = font.render("move the gun right - ARROW-RIGHT", True, BLACK)
            place = text.get_rect(center=(300, 445))
            screen.blit(text, place) 
            text = font.render("turn the muzzle counterclockwise - ARROW-UP", True, BLACK)
            place = text.get_rect(center=(300, 480))
            screen.blit(text, place) 
            text = font.render("turn the muzzle clockwise - ARROW-DOWN", True, BLACK)
            place = text.get_rect(center=(300, 515))
            screen.blit(text, place) 
            text = font.render("shoot - HOLD_down_the_P_KEY", True, BLACK)
            place = text.get_rect(center=(300, 550))
            screen.blit(text, place)
        else:
            text = font.render("For the player with the red gun:", True, BLACK)
            place = text.get_rect(center=(300, 200))
            screen.blit(text, place) 
            text = font.render("move the gun to the left - A", True, BLACK)
            place = text.get_rect(center=(300, 235))
            screen.blit(text, place) 
            text = font.render("move the gun to the right - D", True, BLACK)
            place = text.get_rect(center=(300, 270))
            screen.blit(text, place) 
            text = font.render("turn the muzzle counterclockwise - W", True, BLACK)
            place = text.get_rect(center=(300, 305))
            screen.blit(text, place) 
            text = font.render("turn the muzzle clockwise - s", True, BLACK)
            place = text.get_rect(center=(300, 340))
            screen.blit(text, place) 
            text = font.render("shoot - HOLD_DOWN_THE_V_KEY", True, BLACK)
            place = text.get_rect(center=(300, 375))
            screen.blit(text, place)
        text = font.render("Press SPACE to go to the game", True, BLACK)
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
