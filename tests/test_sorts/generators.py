"""
Генератор тест кейсов для сортировок
"""

import random
from typing import List, Optional

def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed: Optional[int] = None) -> List[int]:
    """Генерирует массив из n случайных целых чисел в диапазоне [lo, hi]"""
    if seed is not None:
        random.seed(seed)
    if distinct:
        if hi - lo + 1 < n:
            raise ValueError(f"Невозможно сгенерировать {n} уникальных чисел в [{lo}, {hi}]")
        return random.sample(range(lo, hi + 1), n)
    return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int = 5, *, seed: Optional[int] = None) -> List[int]:
    """Генерирует отсортированный массив, затем выполняются swaps - случайные обмены пар элементов"""
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def many_duplicates(n: int, k_unique: int = 5, *, seed: Optional[int] = None) -> List[int]:
    """Генерирует массив длины n, содержащий только k_unique различных значений"""
    if seed is not None:
        random.seed(seed)
    if k_unique <= 0:
        raise ValueError("k_unique must be > 0")
    values = list(range(k_unique))
    return [random.choice(values) for _ in range(n)]

def reverse_sorted(n: int) -> List[int]:
    """Генерирует массив в строго убывающем порядке"""
    return list(range(n - 1, -1, -1))

def rand_float_array(n: int, lo: float = 0.0, hi: float = 1.0, *, seed: Optional[int] = None) -> List[float]:
    """Генерирует массив из n случайных вещественных чисел в диапазоне [lo, hi]"""
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]
