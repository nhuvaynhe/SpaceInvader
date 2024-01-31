import pygame
import copy

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
        self.matrix = []
        self.screen = screen
        self.barriers = []
        self.num_of_barriers = num_of_barriers

    def draw(self, ite):
        offset_x, offset_y = self.barriers[ite]
        matrix = self.matrix[ite]
        for row in range(10):
            for col in range(10):
                color = BLACK
                if matrix[row][col] == 1:
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
            self.matrix.append(copy.deepcopy(barrier))
            self.draw(i)

    def checkEachCell(self, bullet, i):
        offset_x, offset_y = self.barriers[i]
        bullet_x, bullet_y = bullet
        barrier = self.matrix[i]
        for col in range(0, 10):
            for row in range(0, 10):
                block_x = offset_x + col * self.width
                block_y = offset_y + row * self.height

                if block_x <= bullet_x <= block_x + self.width and \
                   block_y <= bullet_y <= block_y + self.height and \
                   barrier[row][col] == 1:
                    barrier[row][col] = 0
                    return True
        return False

    def hit(self, bullets):
        for bullet in bullets:
            x, y = bullet
            if 400 <= y <= 520:
                for i in range(len(self.barriers)):
                    offset_x, _ = self.barriers[i]
                    if offset_x <= x <= offset_x + 10 * self.width:
                        if self.checkEachCell(bullet, i):
                            bullets.remove(bullet)
                            break
                        else:
                            break
