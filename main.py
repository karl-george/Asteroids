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
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time

    # Updatable Group
    updatable = pygame.sprite.Group()
    # Drawable group
    drawable = pygame.sprite.Group()
    # Set both groups as containers for the Player
    Player.containers = (updatable, drawable)
    # Create a player and spawn him in centre of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Check to see if user closed the game window with the X. If so end while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Color screen rect
        screen.fill("black")

        # Call update on all updatables in the group
        updatable.update(dt)

        # Call draw on all drawables in the group
        for item in drawable:
            item.draw(screen)

        # Update the screen
        pygame.display.flip()

        # Limit frame rate to 60 fps
        dt = clock.tick(60) / 1000

    # End of while loop


# This if statement ensures the main() function is only called when this file is run directly;
# it won't run if it's imported as a module.
if __name__ == "__main__":
    main()
