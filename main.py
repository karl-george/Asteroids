# This allows us to use code from the pygame library
import pygame
import sys

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
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0  # delta time

    # Updatable Group
    updatable = pygame.sprite.Group()
    # Drawable group
    drawable = pygame.sprite.Group()
    # Asteroids group
    asteroids = pygame.sprite.Group()

    # Set updatable and drawable groups as containers for the Player
    Player.containers = (updatable, drawable)

    # Set updatable, drawable and asteroids groups as container for asteroids
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set asteroid field to updatable
    AsteroidField.containers = updatable

    # Create a player and spawn him in centre of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create an asteroid field
    asteroid_field = AsteroidField()

    while True:
        # Check to see if user closed the game window with the X. If so end while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Color screen rect
        screen.fill("black")

        # Call update on all updatables in the group
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()

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
