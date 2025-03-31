import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  shots = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  
  Shot.containers = (shots, updatables, drawables)
  Asteroid.containers = (asteroids, updatables, drawables)
  Player.containers = (updatables, drawables)
  AsteroidField.containers = (updatables)

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  asteroid_field = AsteroidField()
  
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill("#000000")

    updatables.update(dt)
    for drawable in drawables:
      drawable.draw(screen)
    for asteroid in asteroids:
      if asteroid.checkCollision(player):
        print("Game Over!")
        sys.exit()
      for shot in shots:
        if asteroid.checkCollision(shot):
          asteroid.kill()
          shot.kill()

    dt = clock.tick(60) / 1000
    pygame.display.flip()

if __name__ == "__main__":
  main()