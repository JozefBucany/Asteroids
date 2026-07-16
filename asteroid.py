import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
           return
        log_event("asteroid_split")
        a = random.uniform(20,50)
        velocity = self.velocity.rotate(a)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity = velocity
        a = random.uniform(20,50)
        velocity = self.velocity.rotate(-a)
        asteroid = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid.velocity = velocity
