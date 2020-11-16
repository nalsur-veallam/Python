from numpy import pi
from random import randint, randrange
import numpy as np


class Gun:
    def __init__(self, x_pos, color, angle_of_slope, limit_of_power):
        self.x_pos = x_pos
        self.color = color
        self.angle_of_slope = angle_of_slope
        self.power_of_shot = 0
        self.limit_of_power = limit_of_power

    def shot(self):
        power = self.power_of_shot
        self.power_of_shot = 0
        return self.x_pos, self.angle_of_slope, power

    def move(self, shift, window_size_x, gun_size_length):
        if self.x_pos + shift + gun_size_length <= window_size_x and self.x_pos + shift >= 0:
            self.x_pos = self.x_pos + shift

    def turn(self, angle):
        if self.angle_of_slope + angle >= pi - pi/15:
            pass
        elif self.angle_of_slope + angle <= 0 + pi/15:
            pass
        else:
            self.angle_of_slope = self.angle_of_slope + angle

    def increase_power(self, power):
        if self.power_of_shot + power >= self.limit_of_power:
            self.power_of_shot = self.limit_of_power
        else:
            self.power_of_shot = self.power_of_shot + power
            
    def get_parameters(self):
        return self.x_pos, self.angle_of_slope, self.color
    
    def power(self):
        return self.power_of_shot


class Shell:
    def __init__(self,  x_pos, y_pos, speed, angle, acceleration, number, radius):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.number = number
        self.acceleration = acceleration
        self.x_speed = float(speed)*float(np.cos(angle))
        self.y_speed = float(-1*speed)*float(np.sin(angle))

    def get_parameters(self):
        return int(self.x_pos), int(self.y_pos), self.number
        
    def move(self, window_size_x):
        if self.x_pos - self.radius <= 0 or self.x_pos + self.radius >= window_size_x:
            self.x_speed = -1*self.x_speed
        if self.y_pos + self.radius <= 0:
            self.y_speed = -1*self.y_speed
        self.y_speed += self.acceleration
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed



class Target:     
    def __init__(self, type, radius, window_size_x, window_size_y, height_above_the_gun, radius_of_gyration_min, radius_of_gyration_max, max_speed, min_speed):
            self.radius = radius
            self.min_speed = min_speed
            self.max_speed = max_speed
            self.radius_of_gyration_max = radius_of_gyration_max
            self.radius_of_gyration_min = radius_of_gyration_min
            self.height_above_the_gun = height_above_the_gun
            self.window_size_x = window_size_x
            self.window_size_y = window_size_y
            self.type = type
            if(type == 1) or (type == 2):
                self.x_pos = randint(0 + radius*2, window_size_x - radius*2)
                self.y_pos = randint(0 + radius*2, window_size_y - radius*2 - height_above_the_gun)
            if(type == 2):
                self.speed = randrange(-1,1,2)*randint(min_speed,max_speed)
            if(type == 3):
                self.speed = randrange(-1,1,2)*randint(1,int(pi*2+1))
                self.radius_of_gyration = randint(radius_of_gyration_min, radius_of_gyration_max)
                self.center_x = randint(0 + radius_of_gyration_max + radius*2, window_size_x - radius_of_gyration_max - radius*2)
                self.center_y = randint(0 + radius_of_gyration_max + radius*2,window_size_y - radius_of_gyration_max - radius*2 - height_above_the_gun)
                self.angle_of_gyration = randint(0,int(pi*10))
                self.x_pos = self.center_x + int(self.radius_of_gyration*np.cos(self.angle_of_gyration/10))
                self.y_pos = self.center_y + int(self.radius_of_gyration*np.sin(self.angle_of_gyration/10))
    
    def hit(self,ball_x,ball_y,ball_rad):
        if(ball_rad + self.radius > np.sqrt((self.x_pos - ball_x)**2 + (self.y_pos - ball_y)**2)):
            if(self.type == 1) or (self.type == 2):
                self.x_pos = randint(0 + self.radius*2, self.window_size_x - self.radius*2)
                self.y_pos = randint(0 + self.radius*2, self.window_size_y - self.radius*2 - self.height_above_the_gun)
            if(self.type == 2):
                self.speed = randrange(-1,1,2)*randint(self.min_speed,self.max_speed)
            if(self.type == 3):
                self.speed = randrange(-1,1,2)*randint(1,int(pi*2+1))
                self.radius_of_gyration = randint(self.radius_of_gyration_min, self.radius_of_gyration_max)
                self.center_x = randint(0 + self.radius_of_gyration_max + self.radius*2, self.window_size_x - self.radius_of_gyration_max - self.radius*2)
                self.center_y = randint(0 + self.radius_of_gyration_max + self.radius*2,self.window_size_y - self.radius_of_gyration_max - self.radius*2 - self.height_above_the_gun)
                self.angle_of_gyration = randint(0,int(pi*10))
                self.x_pos = self.center_x + int(self.radius_of_gyration*np.cos(self.angle_of_gyration/10))
                self.y_pos = self.center_y + int(self.radius_of_gyration*np.sin(self.angle_of_gyration/10))
            return True
            
        else:
            return False
    
    def turn(self):
        if(self.type == 2):
            if(self.x_pos <= 0 + self.radius)or(self.x_pos >= self.window_size_x - self.radius):
                self.speed = -1*self.speed
            self.x_pos += int(self.speed)
        elif(self.type == 3):
            self.angle_of_gyration += self.speed/10
            self.x_pos = self.center_x + int(self.radius_of_gyration*np.cos(self.angle_of_gyration/10))
            self.y_pos = self.center_y + int(self.radius_of_gyration*np.sin(self.angle_of_gyration/10))
    
    def get_parameters(self):
        return self.x_pos, self.y_pos

