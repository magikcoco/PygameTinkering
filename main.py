import pygame, os, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('isometric test')
w, h = 900, 900
screen = pygame.display.set_mode((w, h), 0, 32)
display = pygame.Surface((300, 300))

grass_img = pygame.image.load(os.path.join('Assets', 'grass.png')).convert()
grass_img.set_colorkey((0, 0, 0))  # remove black background in grass.png

f = open(os.path.join('Assets', 'map.txt'))  # open a map file
map_data = [[int(c) for c in row] for row in f.read().split('\n')]  # loads map data into integers
f.close()

while True:
    display.fill((0, 0, 0))

    for y, row in enumerate(map_data):  # iterate through map data
        for x, tile in enumerate(row):
            if tile:
                pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)  # render the tiles

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
