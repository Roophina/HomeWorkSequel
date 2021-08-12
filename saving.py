"""Описание тотема."""
from typing import Optional

from heroes import Hero


class Totem:
    """Класс тотема."""

    hero = None

    def save(self, hero: Hero) -> None:
        """Метод сохранения игры."""
        self.hero = hero

    def load(self) -> Optional[Hero]:
        """Метод загрузки сохраненной игры."""
        return self.hero
