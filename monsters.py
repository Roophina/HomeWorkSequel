"""Описание монстров: базовый абстрактный класс монстра, классы-наследники и абстрактная фабрика."""
from abc import ABC, abstractmethod
from random import randint


class Monster(ABC):
    """Абстрактный класс монстра."""

    def __init__(self) -> None:
        """Переопределение метода конструктора."""
        self.monster_hp = randint(10, 15)

    @abstractmethod
    def attack(self) -> int:
        """Метод, наличие которого обязательно у всех."""
        pass


class Orc(Monster):
    """Чудовище с мечом."""

    def attack(self) -> int:
        """Переопределение метода атаки."""
        monster_attack = randint(1, 5)
        print(f"Орк бьет мечом с атакой {monster_attack}")
        return monster_attack


class Drow(Monster):
    """Чудовище с луком."""

    def attack(self) -> int:
        """Переопределение метода атаки."""
        monster_attack = randint(1, 7)
        print(f"Дроу стреляет из лука с атакой {monster_attack}")
        return monster_attack


class Necromancer(Monster):
    """Чудовище с магией."""

    def attack(self) -> int:
        """Переопределение метода атаки."""
        monster_attack = randint(1, 10)
        print(f"Некромант колдует с атакой {monster_attack}")
        return monster_attack


class MonsterFactory(ABC):
    """Абстрактная фабрика чудовища."""

    @abstractmethod
    def create_monster(self) -> Monster:
        """Создание абстрактного продукта."""
        pass


class OrcFactory(MonsterFactory):
    """Конкретная фабрика чудовища."""

    def create_monster(self) -> Orc:
        """Создание конкрентного продукта."""
        return Orc()


class DrowFactory(MonsterFactory):
    """Конкретная фабрика чудовища."""

    def create_monster(self) -> Drow:
        """Создание конкрентного продукта."""
        return Drow()


class NecromancerFactory(MonsterFactory):
    """Конкретная фабрика чудовища."""

    def create_monster(self) -> Necromancer:
        """Создание конкрентного продукта."""
        return Necromancer()
