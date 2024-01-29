# spaceship.py
import pygame
from bullet import Bullet

screen_width = 1280
screen_height = 720

class SpaceShip:
    def __init__(self):
        self.ship_width    = 80
        self.ship_height   = 20
        self.screen        = None
        self.bullet        = None
        self.ship_position = [screen_width/2 - self.ship_width/2,
                                screen_height/2 - self.ship_height/2]
    
    def getPosition(self):
        return self.ship_position
    
    def shoot(self):
        self.bullet.shootBullet(self.ship_position, self.ship_width/2, 'green', 1, self.screen)

    def drawSpaceShip(self, screen, bullet):
        self.screen = screen
        self.bullet = bullet

        x, y = self.ship_position
        pygame.draw.rect(self.screen, 'green', [x, y,
                                           self.ship_width, self.ship_height])
        temp_x = self.ship_width/2
        temp_y = self.ship_height/2
        pygame.draw.rect(self.screen, 'green', [x + temp_x/2, 
                                           y - temp_y,
                                           temp_x, 
                                           temp_y])
    
    def moveSpaceShip(self, dt):
        x, y = self.ship_position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and y > 30:
            y -= 300 * dt
        if keys[pygame.K_s] and y < (screen_height - 30):
            y += 300 * dt
        if keys[pygame.K_a] and x > 0:
            x -= 300 * dt
        if keys[pygame.K_d] and x < (screen_width - 80):
            x += 300 * dt

        # Update the new position
        self.ship_position = [x, y]

