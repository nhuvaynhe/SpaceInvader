import pygame
pygame.init()

# pygame setup
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader Game")

class Bullet():
    def __init__(self): 
        self.bullet_width  = 5
        self.bullet_height = 10
        self.bullet_speed  = 5
        self.color         = 'green'
        self.direction     = 1
        self.bullets       = []

    def update(self):
        for bullet in self.bullets:
            x, y = bullet
            bullet[1] -= self.bullet_speed * self.direction

        self.draw()

    def draw(self):
        for bullet in self.bullets:
            x, y = bullet
            pygame.draw.rect(screen, self.color, [x, y,
                                             self.bullet_width, 
                                             self.bullet_height])
    def shootBullet(self, position, shift, color, direction):
        # direction = 1 -> upward
        self.direction = direction
        self.color     = color
        x, y           = position
        bullet_positon = [x + shift - self.bullet_width/2,
                          y - self.bullet_height]
        self.bullets.append(bullet_positon)
        

class SpaceShip:
    def __init__(self):
        self.ship_width    = 80
        self.ship_height   = 20
        self.ship_position = [screen_width/2 - self.ship_width/2,
                                screen_height/2 - self.ship_height/2]
    
    def getPosition(self):
        return self.ship_position
    
    def shoot(self):
        bullet.shootBullet(self.ship_position, self.ship_width/2, 'green', 1)

    def drawSpaceShip(self):
        x, y = self.ship_position
        pygame.draw.rect(screen, 'green', [x, y,
                                           self.ship_width, self.ship_height])
        temp_x = self.ship_width/2
        temp_y = self.ship_height/2
        pygame.draw.rect(screen, 'green', [x + temp_x/2, 
                                           y - temp_y,
                                           temp_x, 
                                           temp_y])
    
    def moveSpaceShip(self, dt):
        x, y = self.ship_position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and y > 30:
            y -= 300 * dt
        if keys[pygame.K_s] and y < (screen_height - 30):
            y += 300 * dt
        if keys[pygame.K_a] and x > 0:
            x -= 300 * dt
        if keys[pygame.K_d] and x < (screen_width - 80):
            x += 300 * dt

        # Update the new position
        self.ship_position = [x, y]


class GamePlay:
    def __init__(self):
        self.monster_grid               = []
        self.space_between_each_monster = 20
        self.num_of_monsters            = 15
        self.turn                       = []

    def addMonsters(self):
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
                monster.draw()

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
        
    
class Monster(GamePlay):
    def __init__(self, x, y):
        self.width          = 60
        self.height         = 40
        self.spawn_position = [x, y]
        self.speed          = 100
        self.delay_attack   = 10000  # 3 seconds

    def draw(self):
        x, y = self.spawn_position
        pygame.draw.rect(screen, 'gray', [x, y,
                                         self.width, 
                                         self.height])

    def move(self,  dt, turn):
        x, y = self.spawn_position
        x += self.speed * dt * turn

        self.spawn_position = [x, y]

    def shoot(self):
        self.delay_attack -= clock.get_rawtime()
        if self.delay_attack <= 0:
            bullet.shootBullet(self.spawn_position, self.width/2, 'red', -1)
            self.delay_attack = 5000  # Reset the delay timer for the next shot

running  = True
dt       = 0
bullet   = Bullet()
ship     = SpaceShip()
game     = GamePlay()
game.addMonsters()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    screen.fill((0,0,0)) # black

    ship.drawSpaceShip()
    ship.moveSpaceShip(dt)

    game.drawMonsters()
    game.moveMonsters(dt)

    bullet.update()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

