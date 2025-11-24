from src.modules.math_functions import factorial, factorial_recursive, fibo, fibo_recursive
from src.modules.simple_sorts import quick_sort, bubble_sort, counting_sort
from src.modules.complex_sort import radix_sort, bucket_sort, heap_sort
from src.modules.stack import Stack
from typing import List

def parse_numbers(s: str):
    """Преобразует строку в массив чисел"""
    if not s.strip():
        raise ValueError("Пустой ввод")
    parts = s.strip().split()
    res: List[float] = []
    for part in parts:
        try:
            # Сначала int, если нет точки
            if '.' not in part:
                res.append(int(part))
            else:
                res.append(float(part))
        except ValueError:
            raise ValueError(f"Некорректное число: '{part}'")
    return res

def stack_inter():
    """Интерактивное взаимодействие со стеком"""
    stack = Stack()
    print("\nStack")
    print("Доступные команды:")
    print("  push <число>    - добавить число (int/float)")
    print("  pop             - извлечь верхний элемент")
    print("  peek            - посмотреть верхний элемент")
    print("  min             - текущий минимум")
    print("  len             - количество элементов")
    print("  empty           - проверить, пуст ли стек")
    print("  clear           - очистить стек")
    print("  show            - показать строковое представление стека(от вершины до дна)")
    print("  quit            - выйти в главное меню")
    print("Примечание: после первого push тип фиксируется (int или float)\n")

    while True:
        try:
            line = input("stack> ").strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
            cmd = parts[0].lower()

            if cmd == "quit":
                print("Выход из Stack")
                break

            elif cmd == 'push':
                if len(parts) < 2:
                    print("Ошибка: укажите число, например: push 42")
                    continue
                try:
                    # Пытаемся спарсить как int или float
                    arg = parts[1].strip()
                    if '.' in arg in arg.lower():
                        val = float(arg)
                    else:
                        val = int(arg)
                    stack.push(val)
                    print(f"push({val}) выполнено")
                except TypeError as e:
                    print("Ошибка типа:", e)

            elif cmd == 'pop':
                try:
                    val = stack.pop()
                    print(f"{val}")
                except ValueError as e:
                    print("Ошибка:", e)

            elif cmd == 'peek':
                try:
                    val = stack.peek()
                    print(f"{val}")
                except ValueError as e:
                    print("Ошибка:", e)

            elif cmd == 'min':
                try:
                    val = stack.min()
                    print(f"min() {val}")
                except ValueError as e:
                    print("Ошибка:", e)

            elif cmd == 'len':
                print(f"{len(stack)}")

            elif cmd == 'empty':
                print(f"{stack.is_empty()}")

            elif cmd == 'clear':
                stack.clear()
                print("Стек очищен")
            elif cmd == 'show':
                print("stack =", stack.show())
            else:
                print(f"Неизвестная команда: '{cmd}'")

        except Exception as e:
            print("Неожиданная ошибка:", type(e).__name__, "—", e)

def main():
    while True:
        print("Выберите функцию:")
        print("1 - factorial(n)")
        print("2 - factorial_recursive(n)")
        print("3 - fibo(n)")
        print("4 - fibo_recursive(n)")
        print("5 - bubble_sort(a)")
        print("6 - quick_sort(a)")
        print("7 - counting_sort(a)")
        print("8 - radix_sort(a, base)")
        print("9 - heap_sort(a)")
        print("10 - bucket_sort(a, buckets)")
        print("11 - Stack(интерактивный стек)")
        print("Примечание: counting_sort и radix_sort принимают только целые числа")

        choice = input("\nНомер (1–11) или 'exit': ").strip()
        if choice == 'exit':
            print("Выход")
            break
        if choice not in map(str, range(1, 12)):
            print("Ошибка: неверный номер")
            continue

        try:
            # Математические функции
            if choice in ('1', '2', '3', '4'):
                n = int(input("n = ").strip())
                func = {
                    '1': factorial,
                    '2': factorial_recursive,
                    '3': fibo,
                    '4': fibo_recursive
                }[choice]
                print(f"Результат: {func(n)}\n")

            # Сортировки
            elif choice in ('5', '6', '7', '8', '9', '10'):
                arr = parse_numbers(input("Массив (через пробел): "))
                res = []
                if choice == '5':
                    res = bubble_sort(arr)
                elif choice == '6':
                    res = quick_sort(arr)
                elif choice == '7':
                    res = counting_sort(arr)
                elif choice == '8':
                    base_input = input("Основание (По умолчанию, без указания = 10): ").strip()
                    base = int(base_input) if base_input else 10
                    res = radix_sort(arr, base)
                elif choice == '9':
                    res = heap_sort(arr)
                elif choice == '10':
                    buckets_input = input("Число блоков (По умолчанию, без указания = len(a)): ").strip()
                    buckets = int(buckets_input) if buckets_input else None
                    res = bucket_sort(arr, buckets)
                print(f"Исходный: {arr}")
                print(f"Результат: {res}\n")

            else:
                stack_inter()

        except ValueError as e:
            print("Ошибка ввода:", e)
        except RecursionError:
            print("Ошибка: превышена глубина рекурсии")
        except Exception as e:
            print("Ошибка:", type(e).__name__, "—", e)


if __name__ == "__main__":
    main()
