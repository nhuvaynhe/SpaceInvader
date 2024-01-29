import pygame, random
from monster import Monster
from bullet import Bullet

class GamePlay:
    def __init__(self, screen, bullet):
        self.monster_grid               = []
        self.space_between_each_monster = 20
        self.num_of_monsters            = None
        self.turn                       = []
        self.bullet                     = bullet
        self.screen                     = screen

    def getBulletPosition(self):
        for row in self.monster_grid:
            for monster in row:
                return monster.getBulletPosition()

    def addMonsters(self, num_of_monsters):
        self.num_of_monsters = num_of_monsters
        for row in range(3):  
            monster_row = []
            x = 6
            y = 40 + row * 60  
            direction = -1 if row % 2 == 1 else 1
            if row % 2 == 1:
                x = 95
            for _ in range(self.num_of_monsters):
                monster = Monster(x, y, self.screen, self.bullet)
                monster_row.append(monster)
                x += monster.width + self.space_between_each_monster
            self.monster_grid.append(monster_row)
            self.turn.append(direction)
    
    def drawMonsters(self):
        for row in self.monster_grid:
            for monster in row:
                monster.draw()

    def moveMonsters(self, dt):
        for i, row in enumerate(self.monster_grid):
            x, _ = row[0].spawn_position  
            self.turn[i] *= -1 if x >= 95 or x <= 5 else 1

            for monster in row:
                monster.move(dt, self.turn[i])
    
    def win(self):
        if len(self.monster_grid) == 0:
            return True
        return False

    def removeMonster(self, monster):
        for row in self.monster_grid:
            if monster in row:
                row.remove(monster)

    def attack(self):
        for row in self.monster_grid:
            monster = random.choice(row)
            monster.shoot()

    def updateBullet(self):
        self.bullet.update()

    def isHit(self, x, y):
        for row in self.monster_grid:
            for monster in row:
                if monster.getHit(x, y):
                    self.removeMonster(monster)
                    return True
        return False

    def hit(self, ship_bullet):
        for bullet in ship_bullet:
            x, y = bullet
            if self.isHit(x, y):
                ship_bullet.remove(bullet)

