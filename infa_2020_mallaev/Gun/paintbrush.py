import pygame
from pygame.draw import *
import numpy as np

class Paintbrush():
    def __init__(self, screen, window_height, gun_size_height, gun_size_length, target_radius, color_of_target_1, color_of_target_2, color_of_target_3, shell_radius, color_of_shell):
        self.screen = screen
        self.window_height = window_height
        self.gun_size_height = gun_size_height
        self.gun_size_length = gun_size_length
        self.target_radius = target_radius
        self.color_of_target_1 = color_of_target_1
        self.color_of_target_2 = color_of_target_2
        self.color_of_target_3 = color_of_target_3
        self.shell_radius = shell_radius
        self.color_of_shell = color_of_shell
        
    def gun_draw(self, angle_of_slope, x_pos, color_of_gun, color_of_wheel):
        rect(self.screen, color_of_gun, (x_pos, self.window_height - 1.5*self.gun_size_height, self.gun_size_length, self.gun_size_height))
        circle(self.screen, color_of_wheel, (x_pos + int(0.5*self.gun_size_height), self.window_height - int(0.5*self.gun_size_height)),int(0.5*self.gun_size_height))
        circle(self.screen, color_of_wheel, (x_pos + self.gun_size_length - int(0.5*self.gun_size_height), self.window_height - int(0.5*self.gun_size_height)),int(0.5*self.gun_size_height))
        polygon(self.screen, color_of_gun,[[x_pos + self.gun_size_length/2 - self.gun_size_length/8/np.sin(angle_of_slope), self.window_height - 1.5*self.gun_size_height],
                                                [x_pos + self.gun_size_length/2 + self.gun_size_length/8/np.sin(angle_of_slope), self.window_height - 1.5*self.gun_size_height],
                                                [x_pos + self.gun_size_length/2 + self.gun_size_length/2*np.cos(angle_of_slope) + self.gun_size_length*np.sin(angle_of_slope)/8, self.window_height - 1.5*self.gun_size_height - self.gun_size_length/2*np.sin(angle_of_slope) + self.gun_size_length*np.cos(angle_of_slope)/8],
                                                [x_pos + self.gun_size_length/2 + self.gun_size_length/2*np.cos(angle_of_slope) - self.gun_size_length*np.sin(angle_of_slope)/8, self.window_height - 1.5*self.gun_size_height - self.gun_size_length/2*np.sin(angle_of_slope) - self.gun_size_length*np.cos(angle_of_slope)/8]])
    
    def target_draw(self, center_x, center_y):
        circle(self.screen, self.color_of_target_1, (center_x, center_y),self.target_radius)
        circle(self.screen, self.color_of_target_2, (center_x, center_y),self.target_radius, int(self.target_radius/10))
        circle(self.screen, self.color_of_target_3, (center_x, center_y),int(self.target_radius/2))
        circle(self.screen, self.color_of_target_2, (center_x, center_y),int(self.target_radius/2), int(self.target_radius/10))
        circle(self.screen, self.color_of_target_2, (center_x, center_y),int(self.target_radius*4/25))
        
    def shell_draw(self, center_x, center_y):
        circle(self.screen, self.color_of_shell, (center_x, center_y), self.shell_radius)
        
    def scale(self, power, max_power, number, window_size_x, color_1, color_2):
        scale = int(power*100/max_power)
        if number == 1:
            rect(self.screen, color_1,(0,0,100,20), 5)
            rect(self.screen, color_2,(0,0,scale,20))
        if number == 2:
            rect(self.screen, color_1,(window_size_x - 100,0,100,20), 5)
            rect(self.screen, color_2,(window_size_x - 100,0,scale,20))
        
        
        
