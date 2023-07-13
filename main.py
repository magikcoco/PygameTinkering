import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set dimensions of the window
pygame.display.set_caption("First Game!")  # sets the window title
WHITE = (255, 255, 255)  # rgb color
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
FPS = 60  # defines how many frames per second the game updates
VEL = 5
BUL_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = WIDTH//18, HEIGHT//12
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))  # OS neutral path definition
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
YELLOW_HIT, RED_HIT = pygame.USEREVENT + 1, pygame.USEREVENT + 2


def draw_window(yellow, red, yellow_bullets, red_bullets):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)  # draw the border
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  # add an image
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    pygame.display.update()  # update after any change to the display


def handle_yellow_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_a] and spaceship.x - VEL > 0:  # a key is left
        spaceship.x -= VEL
    if keys_pressed[pygame.K_d] and spaceship.x + VEL + spaceship.width < BORDER.x:  # d key is right
        spaceship.x += VEL
    if keys_pressed[pygame.K_w] and spaceship.y - VEL > 0:  # w key is up
        spaceship.y -= VEL
    if keys_pressed[pygame.K_s] and spaceship.y + VEL + spaceship.height < HEIGHT - 11:  # s key is down
        spaceship.y += VEL


def handle_red_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_LEFT] and spaceship.x - VEL > BORDER.x + 15:
        spaceship.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and spaceship.x + VEL + spaceship.width < WIDTH + 5:
        spaceship.x += VEL
    if keys_pressed[pygame.K_UP] and spaceship.y - VEL > 0:
        spaceship.y -= VEL
    if keys_pressed[pygame.K_DOWN] and spaceship.y + VEL + spaceship.height < HEIGHT - 11:
        spaceship.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BUL_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BUL_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def main():
    yellow = pygame.Rect(WIDTH / 4 - SPACESHIP_WIDTH, HEIGHT / 2 - SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  # x, y, width, height
    red = pygame.Rect((WIDTH/4 * 3)-SPACESHIP_WIDTH, HEIGHT/2-SPACESHIP_HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    red_bullets = []
    yellow_health, red_health = 10, 10

    clock = pygame.time.Clock()
    run = True
    while run:  # main game loop
        clock.tick(FPS)  # control framerate, cap it at 60
        for event in pygame.event.get():  # check for different events in pygame
            if event.type == pygame.QUIT:  # quit event
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 + 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 + 2, 10, 5)
                    red_bullets.append(bullet)
            if event.type == RED_HIT:
                red_health -= 1
            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0 < yellow_health:
            winner_text = "Yellow Wins!"
        elif red_health > 0 >= yellow_health:
            winner_text = "Red Wins!"
        elif red_health <= 0 and yellow_health <= 0:
            winner_text = "It's a Tie!"

        if winner_text != "":
            pass  # Someone won the game

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(yellow, red, yellow_bullets, red_bullets)

    pygame.quit()  # quit once the while loop ends


if __name__ == "__main__":  # only run the game if this file is run directly
    main()
