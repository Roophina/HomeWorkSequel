"""Описание найденных в игре предметов."""
from random import randint


class Apple:
    """Класс яблока."""

    def __init__(self) -> None:
        """Переопределение метода конструктора."""
        self.dhp = randint(1, 50)


class Arrows:
    """Класс стрел."""

    def __init__(self) -> None:
        """Переопределение метода конструктора."""
        self.count = randint(1, 5)
