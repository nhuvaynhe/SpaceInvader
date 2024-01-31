import pygame

BLACK = (0, 0, 0)
barrier = [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
           [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
           [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]


class Barrier:
    def __init__(self, screen, num_of_barriers):
        self.width = 15
        self.height = 12
        self.matrix = barrier
        self.screen = screen
        self.barriers = []
        self.num_of_barriers = num_of_barriers

    def draw(self, ite):
        offset_x, offset_y = self.barriers[ite]
        for row in range(10):
            for col in range(10):
                color = BLACK
                if self.matrix[row][col] == 1:
                    color = 'gray'
                pygame.draw.rect(self.screen,
                                 color,
                                 [offset_x + self.width * col,
                                  offset_y + self.height * row,
                                  self.width,
                                  self.height])

    def createBarriers(self):
        for i in range(self.num_of_barriers):
            offset_x = 300 + 300 * i
            offset_y = 400

            barrier_offset = [offset_x, offset_y]
            self.barriers.append(barrier_offset)
            self.draw(i)

    def destroyBarrier(self, bullet_x, offset_x):
        for row in range(0, 10):
            for col in range(0, 10):
                if offset_x <= bullet_x <= offset_x + col * self.width and self.matrix[row][col] == 1:
                    self.matrix[row][col] = 0
                    return True

    def isHit(self, bullet_x, bullet_y):
        for i in range(len(self.barriers)):
            offset_x, _ = self.barriers[i]
            if offset_x <= bullet_x <= offset_x + 9 * self.width:
                if self.destroyBarrier(bullet_x, offset_x):
                    return True

    def hit(self, monster_bullet):
        for bullet in monster_bullet:
            x, y = bullet
            if 400 <= y <= 520:
                if self.isHit(x, y):
                    monster_bullet.remove(bullet)
