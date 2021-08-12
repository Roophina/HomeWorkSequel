"""Описание героев: базовый абстрактный класс героя, классы-наследники и абстрактная фабрика."""
from abc import ABC, abstractmethod
from random import randint

from arsenal import Sword
from things import Apple, Arrows


class Hero(ABC):
    """Базовый абстрактный класс героя."""

    sword = Sword(3)
    bow = None
    spellbook = None
    arrows = 0
    totem = None
    upper_limit_sword = 1
    upper_limit_bow = 1
    upper_limit_spellbook = 1
    monster_counter = 0

    def __init__(self) -> None:
        """Переопределение метода конструктора."""
        self.hp = randint(10, 50)

    def attack_with_sword(self) -> int:
        """Метод атаки мечом."""
        return randint(
            int(self.sword.power / 2), self.sword.power * self.upper_limit_sword
        )

    def attack_with_bow(self) -> int:
        """Метод атаки из лука."""
        if self.arrows:
            self.arrows -= 1
            return randint(int(self.bow.power / 2), self.bow.power * self.upper_limit_bow)  # type: ignore
        else:
            print("Sorry, you aren't Legolas, your arrows have limit")
            return 0

    def attack_with_spellbook(self) -> int:
        """Метод атаки с помощью книги заклинаний."""
        return randint(int(self.spellbook.power / 2), self.spellbook.power * self.upper_limit_spellbook)  # type: ignore

    def eat_apple(self, apple: Apple) -> None:
        """Метод поедания яблока."""
        self.hp += apple.dhp

    def take_arrows(self, arrows: Arrows) -> None:
        """Метод взятия стрел."""
        self.arrows += arrows.count

    @abstractmethod
    def type_hero(self) -> None:
        """Абстрактный метод типа героя."""
        pass


class Warrior(Hero):
    """Класс-наследник."""

    def type_hero(self) -> None:
        """Переопределение метода типа героя."""
        print("Вы воин-мечник!")


class Archer(Hero):
    """Класс-наследник."""

    def type_hero(self) -> None:
        """Переопределение метода типа героя."""
        print("Вы меткий лучник!")


class Wizard(Hero):
    """Класс-наследник."""

    def type_hero(self) -> None:
        """Переопределение метода типа героя."""
        print("Вы великий волшебник!")


class HeroFactory(ABC):
    """Абстрактная фабрика героя."""

    @abstractmethod
    def create_hero(self) -> Hero:
        """Создание абстрактного продукта."""
        pass


class WarriorFactory(HeroFactory):
    """Конкретная фабрика героя."""

    def create_hero(self) -> Warrior:
        """Создание конкрентного продукта."""
        return Warrior()


class ArcherFactory(HeroFactory):
    """Конкретная фабрика героя."""

    def create_hero(self) -> Archer:
        """Создание конкрентного продукта."""
        return Archer()


class WizardFactory(HeroFactory):
    """Конкретная фабрика героя."""

    def create_hero(self) -> Wizard:
        """Создание конкрентного продукта."""
        return Wizard()
