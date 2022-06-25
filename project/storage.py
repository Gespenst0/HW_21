from abc import ABC, abstractmethod



class Storage(ABC):
    @abstractmethod
    def __init__(self):
        self._items: dict[str: int] = {}
        self._capacity: str = 0

    def __repr__(self):
        return f'Это Storage типа {self.__class__.__name__} с емкостью {self._capacity}'

    @abstractmethod
    def add(self, title: str, quantity: int) -> None:
        """Добавить какое-то количество товаров"""
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int) -> None:
        """Убрать какое-то количество товаров"""
        pass

    @abstractmethod
    def _get_free_space(self) -> int:
        """Получить, сколько свободного места осталось"""
        pass

    @abstractmethod
    def get_items(self) -> dict:
        """Вернуть словарь items"""
        pass

    @abstractmethod
    def _get_unique_items_count(self) -> int:
        """Вернуть число уникалных товаров"""
        pass
