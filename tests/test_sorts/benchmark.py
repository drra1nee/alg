"""
Реализация бенчмарка в тестах сортировок
"""
import time

def timeit_once(func, *args, **kwargs) -> float:
    """Выполняет функцию сортировки и возвращает время в секундах потраченное на выполнение сортировки"""
    start = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start
