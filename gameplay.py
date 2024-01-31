import random
from monster import Monster


class GamePlay:
    def __init__(self, screen, bullet):
        self.monster_grid = []
        self.turn = []
        self.bullet = bullet
        self.screen = screen
        self.color = 'gray'
        self.total_monster = 0
        self.num_of_monsters_per_row = 0
        self.space_between_each_monster = 20

    def getBulletPosition(self):
        if len(self.monster_grid) == 0:
            return -1
        for row in self.monster_grid:
            for monster in row:
                return monster.getBulletPosition()

    def addMonsters(self, num_of_monsters):
        self.num_of_monsters_per_row = num_of_monsters
        self.total_monster = num_of_monsters * 3
        for row in range(3):
            monster_row = []
            x = 6
            y = 60 + row * 80
            direction = 1
            for _ in range(self.num_of_monsters_per_row):
                monster = Monster(x, y, self.screen, self.bullet, self.color)
                monster_row.append(monster)
                x += monster.width * 10 + self.space_between_each_monster
            self.monster_grid.append(monster_row)
            self.turn.append(direction)

    def drawMonsters(self):
        for row in self.monster_grid:
            for monster in row:
                monster.draw(self.color)

    def moveMonsters(self, dt):
        for i, row in enumerate(self.monster_grid):
            if len(row) == 0:
                continue
            if self.total_monster <= 15:
                self.color = 'red'
                speed = 300
            else:
                speed = 100
            x1, _ = row[-1].spawn_position
            x2, _ = row[0].spawn_position
            if x1 >= 1220 or x2 <= 5:
                self.turn[i] *= -1
                down = 1
            else:
                self.turn[i] *= 1
                down = 0

            for monster in row:
                monster.move(dt, self.turn[i], down, speed)

    def noMonstersLeft(self):
        if len(self.monster_grid) == 0:
            return True
        return False

    def removeMonster(self, monster):
        for row in self.monster_grid:
            if monster in row:
                row.remove(monster)
                self.total_monster -= 1
            if len(row) == 0:
                self.monster_grid.remove(row)

    def attack(self):
        for row in self.monster_grid:
            if len(row) == 0:
                continue
            monster = random.choice(row)
            monster.shoot()

    def updateBullet(self):
        self.bullet.update()

    def isMonsterHit(self, x, y):
        for row in self.monster_grid:
            for monster in row:
                if monster.hit(x, y):
                    self.removeMonster(monster)
                    return True
        return False

    def handleMonsterHit(self, ship_bullet):
        for bullet in ship_bullet:
            x, y = bullet
            if self.isMonsterHit(x, y):
                ship_bullet.remove(bullet)
