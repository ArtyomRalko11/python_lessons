import sys
import random

import pygame as pg
import game_functions as gf

pg.init()

#цвета
WHITE = (255, 255, 255)
RED = (245, 76, 58)
BROWN = (69, 54, 43)



S_WIDTH = 1280
S_HEIGHT = 720
screen = pg.display.set_mode((S_WIDTH, S_HEIGHT))

FPS = 60
clock = pg.time.Clock()
pg.display.update()

#игровые переменные
speed = 2
apple_speed = speed * 5
player_speed = 0
missed_apples = 0
score = 0

#игровые объекты
player = pg.Rect(0, S_HEIGHT - 50, S_WIDTH * 0.12, S_HEIGHT * 0.04)
player.centerx = S_WIDTH // 2
apple = pg.Rect(random.randint(50, S_WIDTH - 50), 40, 40, 40)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    clock.tick(FPS)
    screen.fill(WHITE)
    pg.draw.rect(screen, BROWN, player)
    pg.draw.circle(screen, RED, (apple.x, apple.y), 20)

    pg.display.update()

    #обрабатываем логику игры
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player_speed -= speed
    elif keys[pg.K_RIGHT]:
        player_speed += speed
    else:
        player_speed = 0

    gf.player_motion(player, screen, player_speed)
    apple_catch = gf.non_playable_obj_move(apple, player, screen, apple_speed)

    if apple_catch == 'miss':
        missed_apples += 1
    elif apple_catch == 'catch':
        score += 1

    print('Score:', score)
    print('missed apples:', missed_apples)

    if missed_apples >= 3:
        sys.exit()

