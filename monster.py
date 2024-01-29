import pygame
from bullet import Bullet 

clock = pygame.time.Clock()

class Monster():
    def __init__(self, x, y):
        self.width          = 60
        self.height         = 40
        self.spawn_position = [x, y]
        self.speed          = 100
        self.delay_attack   = 10000  # 3 seconds
        self.bullet         = None
        self.screen         = None

    def draw(self, screen, bullet):
        self.screen = screen
        self.bullet = bullet
    
        x, y = self.spawn_position
        pygame.draw.rect(self.screen, 'gray', [x, y, self.width, self.height])

    def move(self,  dt, turn):
        x, y = self.spawn_position
        x += self.speed * dt * turn

        self.spawn_position = [x, y]

    def shoot(self):
        self.bullet.shootBullet(self.spawn_position, self.width/2, 'red', -1, self.screen)
        self.delay_attack = 3000  # Reset the delay timer for the next shot
