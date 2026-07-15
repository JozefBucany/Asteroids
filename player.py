import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x: float, y:float):
        super().__init__(x,y, 0.0)
        self.radius = PLAYER_RADIUS
        self.rotation = 0.0
        self.swap = True
        self.swap_cooldown = 0.5


    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        self.speed = PLAYER_SPEED
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        reverse = -1 if keys[pygame.K_s] and self.swap else 1
        self.swap_cooldown -= dt
        if keys[pygame.K_r] and self.swap_cooldown < 0:
            self.swap_cooldown = 0.5
            if self.swap:
                self.swap = False
            else:
               self.swap = True
        if self.swap_cooldown < -1000: self.swap_cooldown = 0

        if keys[pygame.K_a]:
            self.rotate(-dt * reverse)
        if keys[pygame.K_d]:
            self.rotate(dt * reverse)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
