import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.timer = 0
    
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), 2)

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
    keys = pygame.key.get_pressed()
    if self.timer > 0:
      self.timer -= dt
    else:
      self.timer = 0

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

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.timer != 0:
      return
    new_shot = Shot(self.position.x, self.position.y)
    velocity = pygame.Vector2(0, 1)
    velocity = velocity.rotate(self.rotation)
    velocity *= PLAYER_SHOOT_SPEED
    new_shot.velocity = velocity
    self.timer = PLAYER_SHOOT_COOLDOWN

    return new_shot


class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = pygame.Vector2(0, 0)

  def update(self, dt):
    self.position += self.velocity * dt

  def draw(self, screen):
    pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
