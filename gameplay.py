import pygame
from monster import Monster
from bullet import Bullet

bullet   = Bullet()

class GamePlay:
    def __init__(self):
        self.monster_grid               = []
        self.space_between_each_monster = 20
        self.num_of_monsters            = 15
        self.turn                       = []
        self.bullet                     = None
        self.screen                     = None

    def addMonsters(self, screen, bullet):
        self.bullet = bullet
        self.screen = screen
        for row in range(3):  
            monster_row = []
            x = 6
            y = 40 + row * 60  
            direction = -1 if row % 2 == 1 else 1
            if row % 2 == 1:
                x = 95
            for _ in range(self.num_of_monsters):
                monster = Monster(x, y)
                monster_row.append(monster)
                x += monster.width + self.space_between_each_monster
            self.monster_grid.append(monster_row)
            self.turn.append(direction)
    
    def drawMonsters(self):
        for row in self.monster_grid:
            for monster in row:
                monster.draw(self.screen, self.bullet)

    def moveMonsters(self, dt):
        for i, row in enumerate(self.monster_grid):
            x, _ = row[0].spawn_position  
            self.turn[i] *= -1 if x >= 95 or x <= 5 else 1

            for monster in row:
                monster.move(dt, self.turn[i])
                self.attack()

    def removeMonster(self, monster):
        for row in self.monster_grid:
            if monster in row:
                row.remove(monster)

    def attack(self):
        for row in reversed(self.monster_grid):
            for  monster in row:
                if monster is not None:
                    monster.shoot()

            break
