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
        self.sprite_sheet = SpriteSheet(sprite_sheet_path)
        self.image = self.sprite_sheet.get_image(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = Vector2(0,0)

    def update(self):
        """
        Обновляет состояние игрока

        :return: None
        """
        self._move()

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

