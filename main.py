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
        
running        = True
pause          = False
dt             = 0
bullet_monster = Bullet('red', -1, 5) # color, direction, speed
bullet_ship    = Bullet('green', 1, 5)
game           = GamePlay(screen, bullet_monster)
ship           = SpaceShip(screen, bullet_ship)
game.addMonsters(5)

MONSTER_ATTACK = pygame.USEREVENT + 1
pygame.time.set_timer(MONSTER_ATTACK, 600) #ms

def display(displayText):
    font = pygame.font.SysFont("comicsansms", 115)
    text = font.render(displayText, True, 'green', 'blue') 
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text, textRect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

        if event.type == MONSTER_ATTACK:
            game.attack()

    screen.fill((0,0,0)) # black

    ship.drawSpaceShip()
    game.drawMonsters()
    if ship.hit(game.getBulletPosition()):
        pause = True

    if pause:
        display('You Lose')
    else:
        ship.moveSpaceShip(dt)
        ship.updateBullet()
        game.moveMonsters(dt)
        game.updateBullet()
        game.hit(ship.getBulletPosition())
        if game.win():
            display('You Win')

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

