from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

from logger import log_state
import pygame
import sys

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.display.init()
    clock = pygame.time.Clock()
    dt = 0.0
    time = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  return
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        for check in asteroids:
            if check.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                print(f"Your time was: {round(time, 1)} seconds")
                sys.exit()
        dt = clock.tick(60)/1000
        time += dt

        log_state()
        pygame.display.flip()



if __name__ == "__main__":
    main()
