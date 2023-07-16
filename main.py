import pygame, os, sys
import random, time
from pygame.locals import *

pygame.init()
pygame.display.set_caption('isometric test')
w, h = 900, 900
screen = pygame.display.set_mode((w, h), 0, 32)
display = pygame.Surface((300, 300))

grass_img = pygame.image.load(os.path.join('Assets', 'grass.png')).convert()
grass_img.set_colorkey((0, 0, 0))  # remove black background in grass.png
compass_img = pygame.image.load(os.path.join('Assets', 'compass.png')).convert()
compass_img = pygame.transform.scale(compass_img, (25, 25))
compass_img.set_colorkey((0, 0, 0))

f = open(os.path.join('Assets', 'map.txt'))  # open a map file
map_data = [[int(c) for c in row] for row in f.read().split('\n')]  # loads map data into integers
f.close()

## preload map orientations
map_orientation = 0  # north=0, east=1, south=2, west=3
north_map = map_data
east_map = [list(row) for row in zip(*north_map[::-1])]
south_map = [list(row) for row in zip(*east_map[::-1])]
west_map = [list(row) for row in zip(*south_map[::-1])]

while True:
    display.fill((0, 0, 0))
    display.blit(compass_img, (250, 30))

    for y, row in enumerate(north_map):  # iterate through map data
        for x, tile in enumerate(row):
            if tile:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)  # render the 2d map

    for y, row in enumerate(map_data):  # iterate through map data
        for x, tile in enumerate(row):
            display.blit(grass_img, (145 + x * 10 - y * 10, 130 + x * 5 + y * 5))  # render isometric tiles base
            if tile:  # render left to right, top to bottom
                display.blit(grass_img, (145 + x * 10 - y * 10, 130 + x * 5 + y * 5 - 14))  # render 2nd level

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LCTRL:
                compass_img = pygame.transform.rotate(compass_img, 90)
                map_orientation -= 1
                if map_orientation < 0:
                    map_orientation = 3
            if event.key == K_RCTRL:
                compass_img = pygame.transform.rotate(compass_img, -90)
                map_orientation += 1
                if map_orientation > 3:
                    map_orientation = 0

    if map_orientation == 0:
        map_data = north_map
    elif map_orientation == 1:
        map_data = east_map
    elif map_orientation == 2:
        map_data = south_map
    elif map_orientation == 3:
        map_data = west_map

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
