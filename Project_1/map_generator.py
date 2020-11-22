import random
import numpy as np
from math import log
from matplotlib.pyplot import imshow, show, colorbar


def generate_map(seed, size, sharp = 2, h_max = 200):
    random.seed(seed)
    
    map = np.zeros((1,1))
    iters = round(log(size, sharp))
    
    for g in range(iters):
        size_new = sharp**(g+1)
        map_new = np.empty((size_new, size_new))
        
        
        for i in range(size_new):
            for j in range(size_new):
                map_new[i][j] = map[i//sharp][j//sharp]
        
        for i in range(1, size_new, 2):
            for j in range(1, size_new, 2):
                map_new[i][j] = map_new[i][j] + (random.random()*2-1)*(2**(-g))*h_max
        
        for i in range(0, size_new, 2):
            for j in range(1, size_new, 2):
                map_new[i][j] = (map_new[i-1][j] + map_new[-size_new + i + 1][j])/2
        
        for i in range(1, size_new, 2):
            for j in range(0, size_new, 2):
                map_new[i][j] = (map_new[i][j-1] + map_new[i][-size_new + j + 1])/2
        
        for i in range(0, size_new, 2):
            for j in range(0, size_new, 2):
                map_new[i][j] = (map_new[i][j-1] + map_new[i][-size_new + j + 1] + map_new[i-1][j] + map_new[-size_new + i + 1][j])/4
                
        map = map_new
        
    return map


'''map = generate_map(6, 1024)

imshow(map)
colorbar()
show()'''
