import pygame

clock = pygame.time.Clock()
BLACK = (0, 0, 0)

monster = [[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
           [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
           [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
           [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]]


class Monster():
    def __init__(self, x, y, screen, bullet, color):
        self.width = 6
        self.height = 6
        self.screen = screen
        self.bullet = bullet
        self.matrix = monster
        self.color = color
        self.delay_attack = 3000  # 3 seconds
        self.spawn_position = [x, y]

    def getBulletPosition(self):
        return self.bullet.bullets

    def draw(self, arg):
        self.color = arg
        x, y = self.spawn_position
        for row in range(9):
            for col in range(10):
                color = BLACK
                if self.matrix[row][col] == 1:
                    color = self.color
                pygame.draw.rect(self.screen,
                                 color,
                                 [x + self.width * col,
                                  y + self.height * row,
                                  self.width,
                                  self.height])

    def move(self,  dt, turn, down, speed):
        x, y = self.spawn_position
        x += speed * dt * turn
        y += down * 10

        self.spawn_position = [x, y]

    def shoot(self):
        self.bullet.shootBullet(self.spawn_position,
                                self.width/2,
                                self.height,
                                self.screen)

    def hit(self, x, y):
        monster_x, monster_y = self.spawn_position
        if monster_x <= x <= monster_x + self.width * 10:
            if monster_y <= y <= monster_y + self.height * 10:
                return True
        return False
