import random
import unittest
from typing import Iterable
from unittest import TestCase
from unittest.mock import patch

import importlib

rpg = importlib.import_module("main")


class RpgTestCase(TestCase):
    """Юнит тест."""

    def setUp(self) -> None:
        """Начальные условия для тестов."""
        self.input = ""
        self.victory_count = 0
        self.fail_count = 0

    def fake_io_with_asserts(self, *args: Iterable) -> str:
        """Обработка print() и input() в программе с проверками результата."""
        last_io = "".join(args)  # type: ignore
        if "ГЕРОЯ" in last_io:
            self.input = random.choice(["1", "2", "3"])
        elif "БОЙ" in last_io:
            self.input = random.choice(["1", "2"])
        elif "Достать" in last_io:
            self.input = random.choice(["1", "2", "3"])
        elif "Продолжить" in last_io:
            self.input = random.choice(["1", "2"])
        elif "MEЧ" in last_io:
            self.input = random.choice(["1", "2"])
        elif "ЛУК" in last_io:
            self.input = random.choice(["1", "2"])
        elif "КНИГА ЗАКЛИНАНИЙ" in last_io:
            self.input = random.choice(["1", "2"])
        elif "тотем" in last_io:
            self.input = random.choice(["1", "2"])
        elif "нашли стрелы" in last_io:
            self.input = random.choice(["1", "2"])
        elif "ПОБЕДА" in last_io:
            self.victory_count += 1
            self.input = "\n"
        elif "ПОРАЖЕНИЕ" in last_io:
            self.fail_count += 1
            self.input = "\n"
        else:
            self.input = "\n"
        return last_io

    def test_game_e2e(self) -> None:
        """Тест, выполняющий полностью прохождение игры."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                with self.assertRaises(SystemExit):
                    rpg.game()  # type: ignore

    def test_game_e2e_until_at_least_one_victory(self) -> None:
        """Тест, проверяющий что в игру возможно когда-нибудь выиграть."""
        with patch("builtins.print", new=self.fake_io_with_asserts):
            with patch("builtins.input", side_effect=lambda _: self.input):
                while self.victory_count == 0:
                    with self.assertRaises(SystemExit):
                        rpg.game()  # type: ignore
        self.assertEqual(self.victory_count, 1)


if __name__ == "__main__":
    unittest.main()
