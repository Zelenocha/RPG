"""
Главный файл для запуска игры

Запускать напрямую для запуска игры
"""
import pygame as pg
from settings import *
from helper import res
from player import Player


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(GAME_TITLE)
        pg.display.set_icon(pg.image.load(res / "sprites" / "player_sheet.png").subsurface(0, 0, 32, 32))
        self.running = True

    def new(self):
        self.player = Player(res / "sprites" / "player_sheet.png", (100, 100))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(self.player)

    def _events(self):
        """
        Обратывает события
        :return:
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def _update(self):
        """
        Обновляет спрайты
        :return:
        """
        self.all_sprites.update()

    def _draw(self):
        """
        Отрисовывает спрайты
        :return:
        """
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def run(self):
        """
        Звпускает игровой цикл
        :return:
        """
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()


if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
#     print(__name__)

