# bullet.py 
import pygame

class Bullet():
    def __init__(self): 
        self.bullet_width  = 5
        self.bullet_height = 10
        self.bullet_speed  = 5
        self.color         = 'green'
        self.direction     = 1
        self.bullets       = []
        self.screen        = None

    def update(self):
        for bullet in self.bullets:
            x, y = bullet
            bullet[1] -= self.bullet_speed * self.direction

        self.draw()

    def draw(self):
        for bullet in self.bullets:
            x, y       = bullet
            pygame.draw.rect(self.screen, self.color, [x, y,
                                             self.bullet_width, 
                                             self.bullet_height])
    def shootBullet(self, position, shift, color, direction, screen):
        # direction    = 1 -> upward
        self.direction = direction
        self.color     = color
        self.screen    = screen
        x, y           = position
        bullet_positon = [x + shift - self.bullet_width/2,
                          y - self.bullet_height]
        self.bullets.append(bullet_positon)
