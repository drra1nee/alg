"""
Реализация сортировок, имеющие вспомогательные функции
"""

from typing import List

def _sort_radix(arr: List[int], base: int) -> List[int]:
    """Вспомогательная сортировка для radix"""
    if not arr:
        return []
    max_val = max(arr)
    exp = 1 # Текущая степень основания
    arr = arr[:]
    # Пока в массиве есть нерассмотренные разряды
    while max_val // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * base
        # Подсчитываем сколько раз каждая цифра встречается в текущем разряде
        for num in arr:
            digit = (num // exp) % base
            count[digit] += 1
        # Преобразуем счётчики в префиксные суммы
        for i in range(1, base):
            count[i] += count[i - 1]
        # Заполняем output отсортированными по разряду числами
        for i in range(n - 1, -1, -1):
            digit = (arr[i] // exp) % base
            count[digit] -= 1
            output[count[digit]] = arr[i]
        arr = output
        exp *= base
    return arr

def radix_sort(a: List[int], base: int = 10) -> List[int]:
    """Поразрядная сортировка"""
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not all(isinstance(x, int) for x in a):
        raise ValueError("Все элементы списка должны быть целыми числами")
    if base < 2:
        raise ValueError("Основание системы счисления должно быть >= 2")
    if len(a) <= 1:
        return a[:]
    # Разделение на отрицательные и неотрицательные числа
    negatives = [-x for x in a if x < 0]
    positives = [x for x in a if x >= 0]
    # Сортируем обе части
    sorted_pos = _sort_radix(positives, base)
    sorted_neg_abs = _sort_radix(negatives, base)
    # Восстанавливаем отрицательные числа
    sorted_neg = [-x for x in reversed(sorted_neg_abs)]
    return sorted_neg + sorted_pos


def _insertion_sort(a: List[float]) -> List[float]:
    """Вспомогательная сортировка вставкой для блочной сортировки"""
    arr = a[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(a: List[float], buckets: int | None = None) -> List[float]:
    """Блочная сортировка с нормализацией"""
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not all(isinstance(x, (int, float)) for x in a):
        raise ValueError("Все элементы списка должны быть числами (int/float)")
    min_val = min(a)
    max_val = max(a)
    n = len(a)
    if n == 0:
        return []
    # Определяем число блоков
    bucket_count = buckets if buckets is not None else n
    if bucket_count < 1:
        raise ValueError("Число блоков должно быть >= 1")
    # Нормализуем, если элементы не в [0, 1)
    needs_norm = not all(0 <= x < 1 for x in a)
    if needs_norm:
        if min_val == max_val:
            return a[:]
        arr = [(x - min_val) / (max_val - min_val) for x in a]
    else:
        arr = a[:]
    # Создаём блоки
    bucket_list: List[List[float]] = [[] for _ in range(bucket_count)]
    # Распределяем по блокам
    for x in arr:
        idx = min(int(x * bucket_count), bucket_count - 1)
        bucket_list[idx].append(x)
    # Сортируем блоки и собираем
    result_norm = []
    for bucket in bucket_list:
        if bucket:
            result_norm.extend(_insertion_sort(bucket))
    # Обратная нормализация
    if needs_norm:
        result = [min_val + x * (max_val - min_val) for x in result_norm]
    else:
        result = result_norm
    return result


def _heapify(arr: List[int], start: int, end: int) -> None:
    """Преобразование в двоичную кучу поддерева(max-heap)"""
    root = start
    while True:
        child = 2 * root + 1
        if child >= end:
            break
        # Выбираем большего из потомков
        if child + 1 < end and arr[child] < arr[child + 1]:
            child += 1
        # Если корень не меньше потомка, стоп
        if arr[root] >= arr[child]:
            break
        # Иначе переставляем и меняем корень
        arr[root], arr[child] = arr[child], arr[root]
        root = child

def heap_sort(a: List[int]) -> List[int]:
    """Пирамидальная сортировка"""
    if not isinstance(a, list):
        raise TypeError("Аргумент должен быть списком")
    if not all(isinstance(x, int) for x in a):
        raise ValueError("Все элементы должны быть целыми числами")
    if len(a) <= 1:
        return a[:]
    arr = a[:]
    n = len(arr)
    # Построение max-heap
    for i in range((n - 2) // 2, -1, -1):
        _heapify(arr, i, n)
    # Извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # Восстанавливаем отсортированную кучу
        _heapify(arr, 0, i)
    return arr
