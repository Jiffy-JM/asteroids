import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Creating a group of objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Create player object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")
        dt = clock.tick(60) / 1000

        # Obejcts
        for object in drawable:
            object.draw(screen)
        
        # Screen is rendered
        pygame.display.flip()
        
if __name__ == "__main__":
    main()


