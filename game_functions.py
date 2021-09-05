"""Функции, используемые во время игры."""
from random import choice, randint

from arsenal import SwordFactory, BowFactory, SpellbookFactory
from heroes import WarriorFactory, ArcherFactory, WizardFactory, Hero
from monsters import OrcFactory, DrowFactory, NecromancerFactory
from saving import Totem
from things import Apple, Arrows


def validate_input_12(a: str) -> str:
    """Проверяет введенное пользователем число. Два валидных значения."""
    while a != "1" and a != "2":
        a = input("Ой, кажется, вы ввели что-то не то, попробуйте ещё раз _")
    return a


def validate_input_123(a: str) -> str:
    """Проверяет введенное пользователем число. Три валидных значения."""
    while a != "1" and a != "2" and a != "3":
        a = input("Ой, кажется, вы ввели что-то не то, попробуйте ещё раз _")
    return a


def choose_hero() -> Hero:
    """Выбор класса героя."""
    spawner_to_factory_mapping = {
        "1": WarriorFactory,
        "2": ArcherFactory,
        "3": WizardFactory,
    }
    print("Выберите ГЕРОЯ, за которого хотите поиграть")
    n = input("Ваш выбор: 1-воин, 2-лучник, 3-маг _")
    n = validate_input_123(n)
    spawner = spawner_to_factory_mapping[n]().create_hero()  # type: ignore
    if n == "1":
        spawner.upper_limit_sword = 2
    elif n == "2":
        spawner.upper_limit_bow = 2
    else:
        spawner.upper_limit_spellbook = 2
    return spawner


def battle(hero: Hero) -> None:
    """Сражение с монстром."""
    spawner_to_factory_mapping = {
        "1": OrcFactory,
        "2": DrowFactory,
        "3": NecromancerFactory,
    }
    y = choice(["1", "2", "3"])
    monster = spawner_to_factory_mapping[y]().create_monster()  # type: ignore
    print(
        f"БОЙ! Вы встретили {monster.__class__.__name__} с {monster.monster_hp} жизнями"
    )
    n = input("Ваш выбор: 1-атаковать чудовище, 2-убежать _")
    n = validate_input_12(n)
    if n == "2":
        return
    battle_flag = True
    while battle_flag:
        print("Достать оружие!")
        m = input("Ваш выбор: 1-меч, 2-лук, 3-книга заклинаний")
        m = validate_input_123(m)
        if m == "1":
            if hero.sword:
                monster.monster_hp -= hero.attack_with_sword()
            else:
                print("У вас нет этого типа оружия - вы не можете ударить по монстру!")
        elif m == "2":
            if hero.bow:
                monster.monster_hp -= hero.attack_with_bow()
            else:
                print("У вас нет этого типа оружия - вы не можете ударить по монстру!")
        else:
            if hero.spellbook:
                monster.monster_hp -= hero.attack_with_spellbook()
            else:
                print("У вас нет этого типа оружия - вы не можете ударить по монстру!")
        if monster.monster_hp <= 0:
            hero.monster_counter += 1
            print("Плюс один в копилку монстров")
            return
        else:
            if (
                monster.__class__.__name__ == "Orc"
                and hero.__class__.__name__ == "Warrior"
            ):
                damage = monster.attack() - randint(1, 5)
                if damage < 0:
                    print(
                        f"Невиданное мастерство! Вы отразили атаку монстра и вылечились на {-damage} hp!"
                    )
                hero.hp -= damage
            elif (
                monster.__class__.__name__ == "Drow"
                and hero.__class__.__name__ == "Archer"
            ):
                damage = monster.attack() - randint(1, 7)
                if damage < 0:
                    print(
                        f"Невиданное мастерство! Вы отразили атаку монстра и вылечились на {-damage} hp!"
                    )
                hero.hp -= damage
            elif (
                monster.__class__.__name__ == "Necromancer"
                and hero.__class__.__name__ == "Wizard"
            ):
                damage = monster.attack() - randint(1, 10)
                if damage < 0:
                    print(
                        f"Невиданное мастерство! Вы отразили атаку монстра и вылечились на {-damage} hp!"
                    )
                hero.hp -= damage
            else:
                hero.hp -= monster.attack()
            if hero.hp > 0:
                print(
                    f"Монстр не убит! У вас осталось {hero.hp} жизней, у монстра - {monster.monster_hp} жизней"
                )
                print("Продолжить сражение?")
                k = input("Ваш выбор: 1-да, 2-нет _")
                k = validate_input_12(k)
                if k == "2":
                    print("Вы сбежали от монстра")
                    battle_flag = False

            else:
                print("Монстр вас съел")
                return


def food(hero: Hero) -> None:
    """Увеличение жизни с помощью пищи."""
    apple = Apple()
    print("ЯБЛОЧКО! Время подкрепиться")
    hero.eat_apple(apple)
    print(
        f"Вы увеличили количество ваших жизней на {apple.dhp} и теперь у вас {hero.hp} жизней"
    )
    return


def weapon(hero: Hero) -> None:
    """Возможность получить оружие."""
    spawner_to_factory_mapping = {
        "1": SwordFactory,
        "2": BowFactory,
        "3": SpellbookFactory,
    }
    z = choice(["1", "2", "3"])
    weapon = spawner_to_factory_mapping[z]().create_weapon()  # type: ignore
    if weapon.__class__.__name__ == "Sword":
        print(f"MEЧ! Вам выпало оружие с силой атаки {weapon.power}")
        n = input("Ваш выбор: 1 - взять меч, 2 - оставить прежний _")
        n = validate_input_12(n)
        if n == "2":
            return
        hero.sword = weapon  # type: ignore
    elif weapon.__class__.__name__ == "Bow":
        print(f"ЛУК! Вам выпало оружие с силой атаки {weapon.power}")
        n = input("Ваш выбор: 1 - взять лук, 2 - оставить прежний _")
        n = validate_input_12(n)
        if n == "2":
            return
        hero.bow = weapon  # type: ignore
    elif weapon.__class__.__name__ == "Spellbook":
        print(f"КНИГА ЗАКЛИНАНИЙ! Вам выпало оружие с силой атаки {weapon.power}")
        n = input("Ваш выбор: 1 - взять книгу заклинаний, 2 - оставить прежнюю _")
        n = validate_input_12(n)
        if n == "2":
            return
        hero.spellbook = weapon  # type: ignore
    return


def arrow(hero: Hero) -> None:
    """Нахождение стрел."""
    arrows = Arrows()
    print(f"Вы нашли стрелы: {arrows.count}!")
    n = input("Ваш выбор: 1- подобрать стрелы, 2-пройти мимо _")
    n = validate_input_12(n)
    if n == "2":
        return
    hero.take_arrows(arrows)
    print(f"Теперь количество стрел равно {hero.arrows}")
    return


def find_totem(hero: Hero) -> None:
    """Нахождение тотема."""
    totem = Totem()
    print("Вы наткнулись на тотем!")
    n = input("Ваш выбор: 1-взять тотем, 2-пройти мимо")
    n = validate_input_12(n)
    if n == "2":
        return
    totem.save(hero)
    hero.totem = totem  # type: ignore
    return
