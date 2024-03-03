import sys

import pygame as pg

pg.init()

#создать экран игры

S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()

x = 10
y = 10
w = 25
h = 99

pg.display.update()     #если надо что-то показать до начала игры

while True:     #главный цикл игры
    for event in pg.event.get(): #отслеживает события в игре
        if event.type == pg.QUIT:   #если окно игры закрывают крестиком
            sys.exit()      #выйти из игры

    clock.tick(FPS)     #сменяет кадры в игре

    screen.fill((255, 255, 255))        #заливка экрана белым

    pg.draw.rect(screen, (79, 146, 255), (x, y, 100, 75), )     #создать прямоугольник: координаты x 10 , y 10 ; ширина 100, высота 75

    pg.display.update()

    x += 2
    y += 2
    w



