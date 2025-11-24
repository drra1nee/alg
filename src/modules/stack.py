"""
Стек на основе list
"""

from typing import List

class Stack:
    def __init__(self):
        self._data: List = []
        # Вспомогательный стек для минимумов
        self._min_stack: List = []
        self._element_type = None

    def _check_type(self, x) -> None:
        """Метод для проверки типа"""
        if not isinstance(x, (int, float)):
            raise ValueError("Элемент должен быть числом (int/float)")
        # Устанавливаем тип при первом элементе
        if self._element_type is None:
            # Сохраняем тип, запрещая смешивание разных типов
            self._element_type = type(x)
        elif type(x) is not self._element_type:
            raise TypeError(f"Все элементы должны быть типа {self._element_type.__name__}, получено: {type(x).__name__}")

    def push(self, x: int | float) -> None:
        """Добавляет элемент на вершину стека"""
        self._check_type(x)
        self._data.append(x)
        # Обновляем минимум
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> int | float:
        """Удаляет и возвращает элемент с вершины стека"""
        if self.is_empty():
            raise ValueError("В стеке нет элементов, невозможно выполнить pop")
        value = self._data.pop()
        # Если удаляемый элемент был минимумом, удаляем его из min_stack
        if value == self._min_stack[-1]:
            self._min_stack.pop()
        return value

    def peek(self) -> int | float:
        """Возвращает элемент с вершины стека без удаления"""
        if self.is_empty():
            raise ValueError("В стеке нет элементов, невозможно выполнить peek")
        return self._data[-1]

    def is_empty(self) -> bool:
        """Проверяет пуст стек или нет"""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке"""
        return len(self._data)

    def min(self) -> int | float:
        """Возвращает минимальный элемент в стеке"""
        if self.is_empty():
            raise ValueError("В стеке нет элементов, невозможно выполнить min")
        return self._min_stack[-1]

    def clear(self) -> None:
        """Очищает содержимое стека"""
        self._data.clear()
        self._min_stack.clear()
        self._element_type = None

    def show(self) -> str:
        """Возвращает строковое представление стека: от вершины ко дну"""
        if not self._data:
            return "[ ]"
        # Вершина - это последний элемент в _data, поэтому идём в обратном порядке
        items = [str(x) for x in reversed(self._data)]
        return "[" + ", ".join(items) + "]"
