import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        # If asteroid was a small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate 2 new random angles for vectors
        random_angle = random.uniform(20, 50)
        random_vector1 = self.velocity.rotate(random_angle)
        random_vector2 = self.velocity.rotate(-random_angle)

        # Compute the new asteroids radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Move new asteroids
        new_asteroid1.velocity = random_vector1 * 1.2
        new_asteroid2.velocity = random_vector2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
