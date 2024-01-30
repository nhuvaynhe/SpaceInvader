import pygame

clock = pygame.time.Clock()


class Monster():
    def __init__(self, x, y, screen, bullet):
        self.width = 60
        self.height = 40
        self.screen = screen
        self.bullet = bullet
        self.delay_attack = 3000  # 3 seconds
        self.spawn_position = [x, y]

    def getBulletPosition(self):
        return self.bullet.bullets

    def draw(self):
        x, y = self.spawn_position
        pygame.draw.rect(self.screen, 'gray', [x, y, self.width, self.height])

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
        if monster_x <= x <= monster_x + self.width:
            if monster_y <= y <= monster_y + self.height:
                return True
        return False
