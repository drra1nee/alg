"""
Реализация функций факториала и Фибоначчи
"""

def factorial(n: int) -> int:
    """Итеративное вычисление факториала"""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def factorial_recursive(n: int) -> int:
    """Рекурсивное вычисление факториала"""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    """Итеративное вычисление числа Фибоначчи """
    if n < 0:
        raise ValueError("Индекс Фибоначчи не может быть отрицательным")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibo_recursive(n: int) -> int:
    """Рекурсивное вычисление числа Фибоначчи"""
    if n < 0:
        raise ValueError("Индекс Фибоначчи не может быть отрицательным")

    # Кэшируем результаты, чтобы каждое F(k) вычислялось один раз
    memo = {0: 0, 1: 1}
    def fib(k):
        if k in memo:
            return memo[k]
        memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return fib(n)
