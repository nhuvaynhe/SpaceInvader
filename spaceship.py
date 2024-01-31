# spaceship.py
import pygame

screen_width = 1280
screen_height = 720
BLACK = (0, 0, 0)

spaceship = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]


class SpaceShip:
    def __init__(self, screen, bullet):
        self.width = 6
        self.height = 6
        self.screen = screen
        self.bullet = bullet
        self.matrix = spaceship
        self.spawn_x = screen_width/2 - self.width/2
        self.spawn_y = screen_height/2 - self.height/2 + 250
        self.position = [self.spawn_x, self.spawn_x]

    def shoot(self):
        self.bullet.shootBullet(self.position,
                                self.width/2, 0, self.screen)

    def updateBullet(self):
        self.bullet.update()

    def getBullets(self):
        return self.bullet.bullets

    def draw(self):
        x, y = self.position
        for row in range(9):
            for col in range(11):
                color = BLACK
                if self.matrix[row][col] == 1:
                    color = 'green'
                pygame.draw.rect(self.screen,
                                 color,
                                 [x + self.width * col,
                                  y + self.height * row,
                                  self.width,
                                  self.height])

    def moveSpaceShip(self, dt):
        x, y = self.position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and y > screen_height/2 + 250:
            y -= 300 * dt
        if keys[pygame.K_s] and y < (screen_height - 60):
            y += 300 * dt
        if keys[pygame.K_a] and x > 0:
            x -= 300 * dt
        if keys[pygame.K_d] and x < (screen_width - 80):
            x += 300 * dt

        # Update the new position
        self.position = [x, y]

    def isHit(self, x, y):
        ship_x, ship_y = self.position
        if ship_x <= x <= ship_x + self.width * 11:
            if ship_y <= y <= ship_y + self.height * 9:
                return True
        return False

    def hit(self, monster_bullet):
        if monster_bullet == -1:
            return False

        for bullet in monster_bullet:
            x, y = bullet
            if self.isHit(x, y):
                monster_bullet.remove(bullet)
                return True
        return False
