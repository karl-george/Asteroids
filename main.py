# This allows us to use code from the pygame library
import pygame

# from [filename] import [functions, variables] etc
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time

    while True:
        # Check to see if user closed the game window with the X. If so end while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Color screen rect
        screen.fill("black")

        # Update the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    # End of while loop


# This if statement ensures the main() function is only called when this file is run directly;
# it won't run if it's imported as a module.
if __name__ == "__main__":
    main()
