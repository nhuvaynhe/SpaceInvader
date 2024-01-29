# spaceship.py
import pygame
from bullet import Bullet

screen_width = 1280
screen_height = 720

class SpaceShip:
    def __init__(self,screen, bullet):
        self.ship_width    = 80
        self.ship_height   = 20
        self.screen        = screen
        self.bullet        = bullet
        self.ship_position = [screen_width/2 - self.ship_width/2,
                                screen_height/2 - self.ship_height/2 + 250]
    
    def getPosition(self):
        return self.ship_position
    
    def shoot(self):
        self.bullet.shootBullet(self.ship_position, self.ship_width/2, 0, self.screen)

    def updateBullet(self):
        self.bullet.update()

    def getBulletPosition(self):
        return self.bullet.bullets

    def drawSpaceShip(self):
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

        if keys[pygame.K_w] and y > screen_height/2 + 150:
            y -= 300 * dt
        if keys[pygame.K_s] and y < (screen_height - 30):
            y += 300 * dt
        if keys[pygame.K_a] and x > 0:
            x -= 300 * dt
        if keys[pygame.K_d] and x < (screen_width - 80):
            x += 300 * dt

        # Update the new position
        self.ship_position = [x, y]

    def isHit(self, x, y):
        ship_x, ship_y = self.ship_position
        if ship_x <= x <= ship_x + self.ship_width:
            if ship_y <= y <= ship_y + self.ship_height:
                return True
        return False

    def hit(self, monster_bullet):
        for bullet in monster_bullet:
            x, y = bullet
            if self.isHit(x, y):
                monster_bullet.remove(bullet)
                return True
        return False
        
