"""Описание оружия: классы и абстрактная фабрика."""
from abc import ABC, abstractmethod
from random import randint


class Weapon:
    """Общий класс оружия."""

    def __init__(self, power: int):
        """Переопределение метода конструктора."""
        self.power = power


class Sword(Weapon):
    """Класс оружия, наследуемый от общего класса."""

    pass


class Bow(Weapon):
    """Класс оружия, наследуемый от общего класса."""

    pass


class Spellbook(Weapon):
    """Класс оружия, наследуемый от общего класса."""

    pass


class WeaponFactory(ABC):
    """Абстрактная фабрика оружия."""

    @abstractmethod
    def create_weapon(self) -> Weapon:
        """Создание абстрактного продукта."""
        pass


class SwordFactory(WeaponFactory):
    """Конкрентная фабрика оружия."""

    def create_weapon(self) -> Sword:
        """Создание конкрентного продукта."""
        return Sword(randint(1, 5))


class BowFactory(WeaponFactory):
    """Конкрентная фабрика оружия."""

    def create_weapon(self) -> Bow:
        """Создание конкрентного продукта."""
        return Bow(randint(5, 10))


class SpellbookFactory(WeaponFactory):
    """Конкрентная фабрика оружия."""

    def create_weapon(self) -> Spellbook:
        """Создание конкрентного продукта."""
        return Spellbook(randint(10, 15))
