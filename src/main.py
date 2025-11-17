from src.modules.math_functions import factorial, factorial_recursive, fibo, fibo_recursive

def main():
    print("Выберите функцию:")
    print("1 — factorial(n)           (итеративный факториал)")
    print("2 — factorial_recursive(n) (рекурсивный факториал)")
    print("3 — fibo(n)                (итеративный Фибоначчи)")
    print("4 — fibo_recursive(n)      (рекурсивный Фибоначчи)")

    try:
        choice = input("Введите номер функции (1–4): ").strip()
        if choice not in ('1', '2', '3', '4'):
            raise ValueError("Неверный номер функции. Допустимы: 1, 2, 3, 4")

        n_input = input("Введите целое число n: ").strip()
        n = int(n_input)

        func_map = {
            '1': factorial,
            '2': factorial_recursive,
            '3': fibo,
            '4': fibo_recursive
        }

        func = func_map[choice]
        result = func(n)
        print(f"Результат: {result}")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Ошибка: n должно быть целым числом")
        else:
            print(f"Ошибка: {e}")
    except RecursionError:
        print("Ошибка: Слишком большое n для рекурсивной функции")

if __name__ == "__main__":
    main()
