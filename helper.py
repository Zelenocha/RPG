"""
Файл помошник для игры

Имеет класс для работы с листами спрайтов и  переменную с путём до папки с ресурсами
"""
import pygame as pg
from pathlib import Path


class SpriteSheet:
    """
    Класс для хранения и управления листами спрайтов
    """
    def __init__(self, file_path):
        """
        Конструктор загружает  лист со спрайтами из полученной директории

        :param file_path:  путь до файла с литстом спрайтов
        """
        self.sheet = pg.image.load(file_path).convert_alpha()

    def get_image(self, x, y, width, height):
        """
        Вырезает и возвращает часть картинки из листа со спрайтами

        :param x: Начальная кордината по иксу
        :param y: Начальная кордината по игрику
        :param width: Ширина необходимого изображения
        :param height: Высота необходимого изображения
        :return: Возвращает нарезанное изображение
        """
        return self.sheet.subsurface(x, y, width, height)


res = Path("res")