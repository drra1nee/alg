"""
Тестирование факториалов и Фибоначчи
"""
import pytest
from src.modules.math_functions import factorial, factorial_recursive, fibo, fibo_recursive

@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (5, 120), (10, 3628800)
])
def test_factorial(n, expected):
    assert factorial(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (5, 120), (8, 40320)
])
def test_factorial_recursive(n, expected):
    assert factorial_recursive(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError, match="Факториал не определён для отрицательных чисел"):
        factorial(-1)
    with pytest.raises(ValueError, match="Факториал не определён для отрицательных чисел"):
        factorial_recursive(-5)

@pytest.mark.parametrize("n, expected", [
    (0, 0), (1, 1), (2, 1), (3, 2), (10, 55), (20, 6765)
])
def test_fibo(n, expected):
    assert fibo(n) == expected

@pytest.mark.parametrize("n, expected", [
    (0, 0), (1, 1), (5, 5), (15, 610)
])
def test_fibo_recursive(n, expected):
    assert fibo_recursive(n) == expected

def test_fibo_negative():
    with pytest.raises(ValueError, match="Индекс Фибоначчи не может быть отрицательным"):
        fibo(-1)
    with pytest.raises(ValueError, match="Индекс Фибоначчи не может быть отрицательным"):
        fibo_recursive(-10)

def test_fibo_recursive_performance():
    # Проверяем, что мемоизация работает — должен завершиться быстро
    assert fibo_recursive(50) == 12586269025
