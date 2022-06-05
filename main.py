"""
Главный файл для запуска игры

Запускать напрямую для запуска игры
"""
import pygame as pg
from settings import *
from helper import res
from player import Player


pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(GAME_TITLE)
pg.display.set_icon(pg.image.load(res/"sprites"/"player_sheet.png").subsurface(0, 0, 32, 32))

player = Player(res/"sprites"/"player_sheet.png", (100, 100))
help(player)
print(repr(player))
all_sprites = pg.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    clock.tick(FPS)
    pg.display.flip()
