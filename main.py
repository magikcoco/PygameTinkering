import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set dimensions of the window
pygame.display.set_caption("First Game!")  # sets the window title
WHITE = (255, 255, 255)  # rgb color
FPS = 60  # defines how many frames per second the game updates
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = WIDTH/18, HEIGHT/12
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))  # OS neutral path definition
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(yellow, red):
    WIN.fill(WHITE)  # fill the screen with a specific color using RGB
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # add an image
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()  # update after any change to the display


def handle_yellow_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_a]:  # a key is left
        spaceship.x -= VEL
    if keys_pressed[pygame.K_d]:  # d key is right
        spaceship.x += VEL
    if keys_pressed[pygame.K_w]:  # w key is up
        spaceship.y -= VEL
    if keys_pressed[pygame.K_s]:  # s key is down
        spaceship.y += VEL


def handle_red_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_LEFT]:
        spaceship.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        spaceship.x += VEL
    if keys_pressed[pygame.K_UP]:
        spaceship.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        spaceship.y += VEL


def main():
    yellow = pygame.Rect(WIDTH / 4 - SPACESHIP_WIDTH, HEIGHT / 2 - SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # x, y, width, height
    red = pygame.Rect((WIDTH/4 * 3)-SPACESHIP_WIDTH, HEIGHT/2-SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:  # main game loop
        clock.tick(FPS)  # control framerate, cap it at 60
        for event in pygame.event.get():  # check for different events in pygame
            if event.type == pygame.QUIT:  # quit event
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        draw_window(yellow, red)

    pygame.quit()  # quit once the while loop ends


if __name__ == "__main__":  # only run the game if this file is run directly
    main()
