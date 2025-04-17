import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    # Creating a group of objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers =(asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    # Create player object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0

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
        
        for asteroid in asteroids:
            if player.collision(asteroid):  # Check if player collides with this asteroid
                print("Game over!")
                sys.exit() 
            
        # Screen is rendered
        pygame.display.flip()
        
if __name__ == "__main__":
    main()


