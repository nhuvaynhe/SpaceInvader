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
monsters = GamePlay(screen, bullet_monster)
ship = SpaceShip(screen, bullet_ship)
barrier = Barrier(screen, 4)
monsters.addMonsters(10)

MONSTER_ATTACK = pygame.USEREVENT + 1
pygame.time.set_timer(MONSTER_ATTACK, 600)  # ms


def display(position, displayText, fontColor, fontsize=115):
    x, y = position
    font = pygame.font.SysFont("comicsansms", fontsize)
    text = font.render(displayText, True, fontColor, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def displayScore(score):
    text = 'Your score: ' + str(score)
    offset_x = 1200
    offset_y = 20
    pos = (offset_x, offset_y)
    display(pos, text, 'green', 30)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.shoot()

        if event.type == MONSTER_ATTACK:
            monsters.attack()

    screen.fill((0, 0, 0))  # black
    displayScore(monsters.monster_destroyed)

    if ship.hit(monsters.getBullets()):
        monsters.state = 2
        pause = True

    ship.draw()
    monsters.drawMonsters()
    if pause:
        x = screen_width // 2
        y = screen_height // 2
        pos = (x, y)
        if win:
            display(pos, 'You Win', 'green')
        else:
            display(pos, 'You Lose', 'red')
    else:
        ship.moveSpaceShip(dt)
        ship.updateBullet()

        monsters.moveMonsters(dt)
        monsters.updateBullet()
        monsters.hit(ship.getBullets())

        barrier.createBarriers()
        barrier.hit(monsters.getBullets())
        barrier.hit(ship.getBullets())

        if monsters.noMonstersLeft():
            win = True
            pause = True

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
