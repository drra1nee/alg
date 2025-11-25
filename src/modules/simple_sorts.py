"""
Реализация сортировок без вспомогательных функций
"""

from typing import List

def bubble_sort(a: List[int | float]) -> List[int | float]:
    """Пузырьковая сортировка"""
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not all(isinstance(x, (int, float)) for x in a):
        raise ValueError("Все элементы списка должны быть числами (int/float)")
    n = len(a)
    arr = a[:]
    # Внешний цикл: итерация по всей длине списка
    for i in range(n):
        swap = False # Флаг перестановки
        # Внутренний цикл: проталкиваем максимальный элемент к правой границе
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    return arr


def quick_sort(a: List[int | float]) -> List[int | float]:
    """Быстрая сортировка"""
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not all(isinstance(x, (int, float)) for x in a):
        raise ValueError("Все элементы списка должны быть числами (int/float)")
    arr = a[:]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Опорный элемент
    # Делаем левый, центральный и правый массив
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Рекурсивно сортируем левый и правый массив и объединяем
    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(a: List[int]) -> List[int]:
    """Сортировка подсчётом, есть поддержка отрицательных чисел"""
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not all(isinstance(x, int) for x in a):
        raise ValueError("Все элементы списка должны быть целыми числами")
    if len(a) == 0:
        return []
    # Находим минимум, максимум и размер вспомогательного массива
    min_val = min(a)
    max_val = max(a)
    range_size = max_val - min_val + 1
    # Вспомогательный массив счётчиков
    count = [0] * range_size
    # Подсчитываем количество встречи одних и тех же чисел в основном массиве
    for x in a:
        count[x - min_val] += 1
    # Делаем отсортированный список
    result = []
    for i in range(range_size):
        value = i + min_val
        k = count[i]
        result.extend([value] * k)
    return result
