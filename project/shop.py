from project.storage import Storage
from project.exceptions import StorageFull, ItemsNotFound


class Shop(Storage):
    """Shop - не может быть наполнен, если свободное место закончилось или в нем уже есть 5 разных товаров."""

    def __init__(self):
        super().__init__()
        self._capacity: str = 20

    def add(self, title: str, quantity: int) -> None:
        if self._get_unique_items_count() >= 5:
            raise StorageFull('В магазине нельзя хранить более 5 наименований товаров')
        if self._get_free_space() < quantity:
            raise StorageFull('Нет свободного места')
        self._items[title] = self._items.get(title, 0) + quantity

    def remove(self, title: str, quantity: int) -> None:
        if title not in self._items.keys():
            raise ItemsNotFound(f'Товар с наименованием {title} не найден')
        if quantity > self._items.get(title):
            raise ItemsNotFound(f'Нет нужного количества товара с наименованием {title}')

        self._items[title] = self._items.get(title) - quantity
        if self._items[title] == 0:
            del self._items[title]

    def _get_free_space(self) -> int:
        taken_space = sum([item for item in self._items.values()])
        return self._capacity - taken_space

    def get_items(self) -> dict:
        return self._items

    def _get_unique_items_count(self) -> int:
        return len([item for item in self._items.keys()])
