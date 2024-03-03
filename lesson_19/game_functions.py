import random

def reset_obj_position(obj, screen_rect):
        obj.x = random.randint(50, screen_rect.right - 50)
        obj.y = -20


def check_screen_collision(obj, screen_rect):
        return obj.bottom >= screen_rect.bottom

def check_player_collision(obj, player):
        return obj.colliderect(player)


def non_playable_obj_move(obj, player, screen, speed_y):
        obj.y += speed_y
        screen_rect = screen.get_rect() #получить колижн модель экрана
        if check_screen_collision(obj, screen_rect):
                reset_obj_position(obj, screen_rect)
                return 'miss'
        if check_player_collision(obj, player):
                reset_obj_position(obj, screen_rect)
                return 'catch'

        return None

def player_motion(obj, screen, speed_x):
        obj.x += speed_x
        screen_rect = screen.get_rect()
        if obj.right >= screen_rect.right:
                obj.right = screen_rect.right
        elif obj.left <= screen_rect.left:
                obj.left = screen_rect.left


