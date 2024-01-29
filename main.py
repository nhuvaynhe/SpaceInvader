import pygame
from bullet import Bullet
from spaceship import SpaceShip
from gameplay import GamePlay

pygame.init()

# pygame setup
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader Game")
        
running  = True
dt       = 0
ship     = SpaceShip()
game     = GamePlay()
bullet_monster = Bullet()
bullet_ship = Bullet()
game.addMonsters(screen, bullet_monster)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

    screen.fill((0,0,0)) # black

    ship.drawSpaceShip(screen, bullet_ship)
    ship.moveSpaceShip(dt)

    game.drawMonsters()
    game.moveMonsters(dt)

    bullet_ship.update()
    bullet_monster.update()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

