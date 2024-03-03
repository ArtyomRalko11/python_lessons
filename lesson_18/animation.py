import sys
import pygame as pg

pg.init()


S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()

player = pg.Rect(0, 0, 100, 100)
hor_speeed = 5
ver_speed = 5

pg.display.update()     #если надо что-то показать до начала игры

while True:     #главный цикл игры
    for event in pg.event.get(): #отслеживает события в игре
        if event.type == pg.QUIT:   #если окно игры закрывают крестиком
            sys.exit()      #выйти из игры

    clock.tick(FPS)     #сменяет кадры в игре

    screen.fill((66, 66, 66))

    pg.draw.rect(screen, (255, 0, 0), player)
    pg.display.update()

    player.x += hor_speeed
    player.y += ver_speed
    if player.right > S_WIDTH or player.left < 0:
        hor_speeed *= -1
    elif player.bottom > S_HEIGHT or player.top < 0:
        ver_speed *= -1

