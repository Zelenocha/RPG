import pygame as pg
from helper import SpriteSheet
from pygame.math import Vector2


class Player(pg.sprite.Sprite):
    """
    Класс для хранения всех атрибутов связанных с игроком
    """
    speed = 5

    def __init__(self, sprite_sheet_path, pos):
        """
        Инициализирует необходимые атрибуты

        :param sprite_sheet_path: Путь до листа со спрайтами игрока
        :param pos: Картеж с начальными координатами игрока
        """
        super().__init__()
        self.sprite_sheet = SpriteSheet(sprite_sheet_path, 2)
        self.cycle_len = 4
        self. _load_images(self.sprite_sheet)
        self.image = self.walkdown[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = Vector2(0,0)
        self.last_update = 0
        self.frame = 0


    def update(self):
        """
        Обновляет состояние игрока

        :return: None
        """
        self._move()
        self.animate()

    def _move(self):
        """
        Двигает игрока

        Перемещает игрока по вектору в соответсвии с нажатами клавишами

        :return: None
        """
        self.velocity.update(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.velocity.y = -1
        if keys[pg.K_s]:
            self.velocity.y = 1
        if keys[pg.K_a]:
            self.velocity.x = -1
        if keys[pg.K_d]:
            self.velocity.x = 1

        # Сбрасываем скорость по иксу при попытке двигаться по диагонали,нельзя по диагонали
        if self.velocity.length() > 1:
            self.velocity.x = 0

        self.velocity *= Player.speed
        self.rect.center += self.velocity

    def _load_images(self,sheet):
        """
        Загружаем картинки анимации игрока
        """

        self.walkup = []
        self.walkdown = []
        self.walkright = []
        self.walkleft = []
        w = sheet.w//self.cycle_len
        h = sheet.h//self.cycle_len
        for x in range(0,sheet.w, w):
            self.walkdown.append(sheet.get_image(x, 0, w, h))
            self.walkleft.append(sheet.get_image(x, h, w, h))
            self.walkright.append(sheet.get_image(x, h * 2, w, h))
            self.walkup.append(sheet.get_image(x, h * 3, w, h))

    def animate(self,frame_len = 100):
        """
        Анимация движения игрока
        :param frame_len: длина анимации в милисикундах
        :return: None
        """
        now = pg.time.get_ticks()
        if now - self.last_update > frame_len and self.velocity.length() > 0:
            self.last_update = now
            if self.velocity.x > 0:
                self.animation_cycle = self.walkright
            elif self.velocity.x < 0:
                self.animation_cycle = self.walkleft
            elif self.velocity.y > 0:
                self.animation_cycle = self.walkdown
            elif self.velocity.y < 0:
                self.animation_cycle = self.walkup

            self.frame = (self.frame + 1) % self.cycle_len

            self.image = self.animation_cycle[self.frame]