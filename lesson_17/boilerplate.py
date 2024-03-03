import sys

import pygame as pg

pg.init()



S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    clock.tick(FPS)

    pg.display.update()
