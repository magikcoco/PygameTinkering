import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    run = True
    while run:  # main game loop
        for event in pygame.event.get():  # check for different events in pygame
            if event.type == pygame.QUIT:  # quit event
                run = False

    pygame.quit()  # quit once the while loop ends


if __name__ == "__main__":  # only run the game if this file is run directly
    main()
