import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOT_SPEED,
    PLAYER_SHOT_COOLDOWN,
    INCREASE_SCORE,
    PLAYER_LIVES,
    PLAYER_GRACE_PERIOD,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.score = 0
        self.lives = PLAYER_LIVES
        self.grace_period = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def take_damage(self):
        self.lives -= 1
        self.grace_period = PLAYER_GRACE_PERIOD

    def shoot(self):
        if self.shot_timer < 0:
            self.shot_timer = PLAYER_SHOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            )
        else:
            return

    def increase_score(self):
        self.score += INCREASE_SCORE

    def update(self, dt):
        self.shot_timer -= dt
        self.grace_period -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
