from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

from logger import log_state
import pygame


def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.display.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  return
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        dt = clock.tick(60)/1000

        log_state()
        pygame.display.flip()



if __name__ == "__main__":
    main()
