# bullet.py
import pygame


class Bullet():
    def __init__(self, color, direction, speed):
        self.bullet_height = 10
        self.bullet_width = 5
        self.screen = None
        self.bullets = []
        self.direction = 1
        self.color = color
        self.direction = direction
        self.bullet_speed = speed

    def remove(self, bullet):
        return self.bullets.remove(bullet)

    def update(self):
        for bullet in self.bullets:
            bullet[1] -= self.bullet_speed * self.direction

            if bullet[1] > 1280 or bullet[1] < 0:
                self.remove(bullet)

        self.draw()

    def draw(self):
        for bullet in self.bullets:
            x, y = bullet
            pygame.draw.rect(self.screen, self.color, [x, y,
                                                       self.bullet_width,
                                                       self.bullet_height])

    def shootBullet(self, position, offset_x, offset_y, screen):
        self.screen = screen
        x, y = position
        bullet_position = [x + offset_x - self.bullet_width/2,
                           y + offset_y - self.bullet_height]
        self.bullets.append(bullet_position)
