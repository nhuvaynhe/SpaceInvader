import pygame
from bullet import Bullet
from spaceship import SpaceShip
from gameplay import GamePlay
from barrier import Barrier

pygame.init()

# pygame setup
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader Game")

running = True
pause = False
win = False
dt = 0

bullet_monster = Bullet('red', -1, 5)  # color, direction, speed
bullet_ship = Bullet('green', 1, 5)
game = GamePlay(screen, bullet_monster)
ship = SpaceShip(screen, bullet_ship)
barrier = Barrier(screen, 3)
game.addMonsters(15)

MONSTER_ATTACK = pygame.USEREVENT + 1
pygame.time.set_timer(MONSTER_ATTACK, 600)  # ms


def display(displayText, fontColor):
    font = pygame.font.SysFont("comicsansms", 115)
    text = font.render(displayText, True, fontColor, (0, 0, 0))
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

    screen.fill((0, 0, 0))  # black

    ship.draw()
    game.drawMonsters()
    if ship.hit(game.getBulletPosition()):
        pause = True

    if pause:
        if win:
            display('You Win', 'green')
        else:
            display('You Lose', 'red')
    else:
        barrier.createBarriers()
        ship.moveSpaceShip(dt)
        ship.updateBullet()
        game.moveMonsters(dt)
        game.updateBullet()
        game.handleMonsterHit(ship.getBulletPosition())
        barrier.hit(game.getBulletPosition())
        barrier.hit(ship.getBulletPosition())
        if game.noMonstersLeft():
            win = True
            pause = True

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
