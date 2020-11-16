import pygame
from numpy import pi
from pygame.draw import *
from paintbrush import Paintbrush
from classes_of_gun_objects import Gun, Shell, Target, Bomb
from menu import menu
from manual import manual
from score import score


RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
FPS = 50


number_of_guns = menu()
manual(number_of_guns)
target_radius = 50
window_size_x = 1500
window_size_y = 1000
height_above_the_gun = 100
radius_of_gyration_min = 100
radius_of_gyration_max = 300
max_speed = 20
min_speed = 5
move_1 = 0
move_2 = 0
move_angle_1 = 0
move_angle_2 = 0
gun_1_color = RED
gun_2_color = BLUE
power_up = 1
power_up_1 = False
power_up_2 = False
shift_of_gun = 8
angle_of_gun = pi/100
limit_of_power = 100
gun_size_length = 100
gun_size_height = 50
balls = []
number_of_balls = 100
shell_radius = 30
limit_of_speed = 100
acceleration = 4
score_1 = 0
score_2 = 0
speed_bomb = 1
acceleration_bomb = 1/5
radius_bomb = 50
color_period = 1000
existence_1 = True
existence_2 = number_of_guns







def new_ball(gun_x, power, gun_y, angle, max_speed, max_power, acceleration, number, balls, number_of_balls, radius):
    balls.append(Shell(gun_x, gun_y, max_speed*power/max_power, angle, acceleration, number, radius))
    if len(balls) >= number_of_balls:
        balls.pop(0)
        
        

pygame.init()
font = pygame.font.Font(None, 25)
screen = pygame.display.set_mode([window_size_x, window_size_y])
screen.fill(WHITE)

target_1 = Target(1, target_radius, window_size_x, window_size_y, height_above_the_gun, radius_of_gyration_min, radius_of_gyration_max, max_speed, min_speed)
target_2 = Target(2, target_radius, window_size_x, window_size_y, height_above_the_gun, radius_of_gyration_min, radius_of_gyration_max, max_speed, min_speed)
target_3 = Target(3, target_radius, window_size_x, window_size_y, height_above_the_gun, radius_of_gyration_min, radius_of_gyration_max, max_speed, min_speed)
bomb = Bomb(window_size_x, window_size_y, FPS, speed_bomb, acceleration_bomb, radius_bomb, color_period, BLACK, RED)

gun_1 = Gun(0, gun_1_color, pi/2, limit_of_power)
if number_of_guns:
    gun_2 = Gun(window_size_x - gun_size_length, gun_2_color, pi/2, limit_of_power)


pygame.display.update()
pygame.display.set_caption("Gun")
clock = pygame.time.Clock()
finished = False
paintbrush = Paintbrush(screen, window_size_y, gun_size_height, gun_size_length, target_radius, RED, BLACK, WHITE, shell_radius, BLACK)
while finished == False:
    x1, y1, color = bomb.start()
    if(y1 + radius_bomb >= window_size_y - 1.5*gun_size_height):
        x2, angle, color = gun_1.get_parameters()
        if number_of_guns:
            x3, angle, color = gun_2.get_parameters()
            if(x1 + radius_bomb > x3) and (x1 - radius_bomb < x3 + gun_size_length) and number_of_guns:
                existence_2 = False
        if(x1 + radius_bomb > x2) and (x1 - radius_bomb < x2 + gun_size_length):
            existence_1 = False
    
    if existence_1 == False and existence_2 == False:
        finished = True
    
    
    clock.tick(FPS)
    target_1.turn()
    target_2.turn()
    target_3.turn()
    for i in range(0, len(balls)):
        x, y, number = balls[i].get_parameters()
        if target_1.hit(x,y, shell_radius):
            balls.pop(i)
            if number == 1:
                score_1 += 1
            else:
                score_2 += 1
        elif target_2.hit(x,y, shell_radius):
            balls.pop(i)
            if number == 1:
                score_1 += 2
            else:
                score_2 += 2
        elif target_3.hit(x,y, shell_radius):
            balls.pop(i)
            if number == 1:
                score_1 += 3
            else:
                score_2 += 3
        else:
            balls[i].move(window_size_x)
            if y > window_size_y:
                balls.pop(i)
            else:
                paintbrush.shell_draw(x, y)
    x, angle, color = gun_1.get_parameters()
    power = gun_1.power()
    paintbrush.scale(power, limit_of_power, 1, window_size_x, BLACK, RED)
    text = font.render("Score: " + str(score_1), True, BLACK)
    place = text.get_rect(center=(50, 35))
    screen.blit(text, place)
    if number_of_guns:
        text = font.render("Score: " + str(score_2), True, BLACK)
        place = text.get_rect(center=(window_size_x - 50, 35))
        screen.blit(text, place)
    if number_of_guns:
        power = gun_2.power()
        paintbrush.scale(power, limit_of_power, 2, window_size_x, BLACK, RED)
    if existence_1:
        paintbrush.gun_draw(angle, x, BLACK, color)
    if existence_2:
        x, angle, color = gun_2.get_parameters()
        paintbrush.gun_draw(angle, x, BLACK, color)
    x, y = target_1.get_parameters()
    paintbrush.target_draw(x, y)
    x, y = target_2.get_parameters()
    paintbrush.target_draw(x, y)
    x, y = target_3.get_parameters()
    paintbrush.target_draw(x, y)
    
    x, y, color = bomb.start()
    paintbrush.bomb_draw(x, y, radius_bomb, color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_2 = -1
            elif event.key == pygame.K_RIGHT:
                move_2 = 1
            if event.key == pygame.K_a:
                move_1 = -1
            elif event.key == pygame.K_d:
                move_1 = 1
            if event.key == pygame.K_w:
                move_angle_1 = 1
            elif event.key == pygame.K_s:
                move_angle_1 = -1
            if event.key == pygame.K_UP:
                move_angle_2 = 1
            elif event.key == pygame.K_DOWN:
                move_angle_2 = -1
                
            if event.key == pygame.K_v:
                power_up_1 = True
            if event.key == pygame.K_p:
                power_up_2 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and move_2 != 0:
                move_2 = 0
            elif event.key == pygame.K_RIGHT and move_2 != 0:
                move_2 = 0
            if event.key == pygame.K_a and move_1 != 0:
                move_1 = 0
            elif event.key == pygame.K_d and move_1 != 0:
                move_1 = 0
            if event.key == pygame.K_w and move_angle_1 != 0:
                move_angle_1 = 0
            elif event.key == pygame.K_s  and move_angle_1 != 0:
                move_angle_1 = 0
            if event.key == pygame.K_UP and move_angle_2 != 0:
                move_angle_2 = 0
            elif event.key == pygame.K_DOWN  and move_angle_2 != 0:
                move_angle_2 = 0
                
            if event.key == pygame.K_v and power_up_1:
                power_up_1 = False
                x, angle, power = gun_1.shot()
                if existence_1:
                    new_ball(x + gun_size_length/2, power, window_size_y - gun_size_height*3/2, angle, limit_of_speed, limit_of_power, acceleration, 1, balls, number_of_balls, shell_radius)
            if event.key == pygame.K_p and power_up_2:
                power_up_2 = False
                if number_of_guns:
                    x, angle, power = gun_2.shot()
                    if existence_2:
                        new_ball(x + gun_size_length/2, power, window_size_y - gun_size_height*3/2, angle, limit_of_speed, limit_of_power, acceleration, 2, balls, number_of_balls, shell_radius)
    gun_1.move(move_1*shift_of_gun, window_size_x, gun_size_length)
    gun_1.turn(move_angle_1*angle_of_gun)
    if power_up_1:
        gun_1.increase_power(power_up)
    if number_of_guns:
        gun_2.move(move_2*shift_of_gun, window_size_x, gun_size_length)
        gun_2.turn(move_angle_2*angle_of_gun)
        if power_up_2:
            gun_2.increase_power(power_up)
    pygame.display.update()
    screen.fill(WHITE)
pygame.quit()

score(number_of_guns, score_1, score_2)
