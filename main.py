"""Сиквел игры про героя и монстров."""
import sys
from random import choice

from game_functions import (
    choose_hero,
    battle,
    food,
    weapon,
    arrow,
    find_totem,
    validate_input_12,
)
from saving import Totem


def game() -> None:
    """Игра с пятью событиями."""
    username = choose_hero()
    username.type_hero()
    print(f"с количеством жизней {username.hp}, " f"сила меча {username.sword.power}")
    events = ["monster", "apple", "weapon", "arrows", "totem"]
    while username.monster_counter < 10 and username.hp > 0:
        x = choice(events)
        if "monster" in x:
            battle(username)
        elif "apple" in x:
            food(username)
        elif "weapon" in x:
            weapon(username)
        elif "arrows" in x:
            arrow(username)
        elif "totem" in x:
            find_totem(username)
        if username.hp <= 0 and username.totem:
            print("Вы убиты, но есть тотем, хотите воспользоваться?")
            t = input("1-да, 2-нет _")
            t = validate_input_12(t)
            if t == "1":
                username = username.totem.load()
    if username.hp <= 0:
        print("ПОРАЖЕНИЕ! Вы убиты, Игра окончена")
    if username.monster_counter == 10:
        print("ПОБЕДА! Вы сразили 10 монстров")
    sys.exit()


if __name__ == "__main__":
    game()
