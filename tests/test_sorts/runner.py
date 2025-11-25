"""Функции для запуска генерации тест-кейсов, их прогона, бенчмарка"""

from tests.test_sorts.generators import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array
from tests.test_sorts.benchmark import timeit_once
from src.modules.simple_sorts import bubble_sort, quick_sort, counting_sort
from src.modules.complex_sort import radix_sort, bucket_sort, heap_sort

# Глобальное хранилище для хранения сгенерированных массивов
GENERATED_ARRAYS = {}

def generate_test_cases():
    """Меню для генерации тест-кейсов"""
    global GENERATED_ARRAYS
    print("\nГенерация тест-кейсов")
    name = input("Имя массива (например: random_100): ").strip()
    if not name:
        print("Ошибка: имя не может быть пустым")
        return

    print("\nВыберите тип:")
    print("1 - Массив со случайными целыми числами")
    print("2 - Почти отсортированный массив")
    print("3 - Массив с множеством дубликатов")
    print("4 - Массив с числами по убыванию")
    print("5 - Массив со случайными дробными числами")

    typ = input("Тип (1–5): ").strip()
    try:
        if typ == '1':
            n = int(input("Количество чисел: "))
            lo = int(input("Нижняя граница: "))
            hi = int(input("Верхняя граница: "))
            distinct = input("Уникальные числа? (да/нет): ").lower() in ('да', 'y', 'yes')
            seed = input("Сид (По умолчанию, без ввода - случайный): ").strip()
            seed = int(seed) if seed else None
            arr = rand_int_array(n, lo, hi, distinct=distinct, seed=seed)
        elif typ == '2':
            n = int(input("Количество чисел: "))
            swaps = int(input("Количество переставлений чисел: "))
            seed = input("Сид (По умолчанию, без ввода - случайный): ").strip()
            seed = int(seed) if seed else None
            arr = nearly_sorted(n, swaps=swaps, seed=seed)
        elif typ == '3':
            n = int(input("Количество чисел: "))
            k = int(input("Количество уникальных чисел: "))
            seed = input("Сид (По умолчанию, без ввода - случайный): ").strip()
            seed = int(seed) if seed else None
            arr = many_duplicates(n, k_unique=k, seed=seed)
        elif typ == '4':
            n = int(input("Количество чисел: "))
            arr = reverse_sorted(n)
        elif typ == '5':
            n = int(input("Количество чисел: "))
            lo = float(input("Нижняя граница: "))
            hi = float(input("Верхняя граница: "))
            seed = input("Сид (По умолчанию, без ввода - случайный): ").strip()
            seed = int(seed) if seed else None
            arr = rand_float_array(n, lo=lo, hi=hi, seed=seed)
        else:
            print("Неверный выбор")
            return

        GENERATED_ARRAYS[name] = arr
        sample = arr[:]
        print(f"\n'{name}' создан: {sample}")
    except Exception as e:
        print("Ошибка генерации:", e)


def test_sorts_arr():
    """Меню для тестирования сгенерированных массивов и вывода их бенчмарка"""
    global GENERATED_ARRAYS
    if not GENERATED_ARRAYS:
        print("\nНет сгенерированных массивов, используйте пункт 12")
        return

    print("\nТестирование сгенерированных массивов")
    print("Доступные массивы:")
    array_names = list(GENERATED_ARRAYS.keys())
    for i, name in enumerate(array_names, 1):
        arr = GENERATED_ARRAYS[name]
        elem_type = type(arr[0]).__name__ if arr else "пустой"
        print(f"{i}. {name} - {len(arr)} элементов, тип: {elem_type}")

    try:
        idx = int(input("Введите номер массива для тестирования: ")) - 1
        if idx < 0 or idx >= len(array_names):
            raise IndexError
        selected_name = array_names[idx]
        test_array = GENERATED_ARRAYS[selected_name]
    except (ValueError, IndexError):
        print("Ошибка: указан недопустимый номер массива")
        return

    print("\nДоступные сортировки:")
    print("1 - bubble_sort")
    print("2 - quick_sort")
    print("3 - counting_sort (требует целые числа)")
    print("4 - radix_sort (требует целые числа)")
    print("5 - heap_sort")
    print("6 - bucket_sort (рекомендуется для float принадлежащих [0, 1))")

    try:
        raw_input = input("Укажите номера сортировок через пробел (например: 1 2 5): ")
        selected_indices = [int(x) for x in raw_input.split() if x.isdigit()]
        selected_indices = [i for i in selected_indices if 1 <= i <= 6]
        if not selected_indices:
            print("Ни одна сортировка не выбрана.")
            return
    except Exception:
        print("Ошибка при обработке ввода")
        return

    # Запрос числа блоков для bucket_sort
    buckets = None
    if 6 in selected_indices:
        try:
            b_input = input("Число блоков для bucket_sort (По умолчанию, без ввода - длина массива): ").strip()
            buckets = int(b_input) if b_input else len(test_array)
        except ValueError:
            print("Некорректное число блоков, будет использовано значение по умолчанию.")
            buckets = None

    sort_algorithms = {
        1: ("bubble_sort", bubble_sort),
        2: ("quick_sort", quick_sort),
        3: ("counting_sort", counting_sort),
        4: ("radix_sort", radix_sort),
        5: ("heap_sort", heap_sort),
        6: ("bucket_sort", lambda a: bucket_sort(a, buckets=buckets)),
    }
    reference = sorted(test_array)
    print(f"\nЗапуск тестов на массиве '{selected_name}' (n = {len(test_array)})...")
    print(f"{'Алгоритм':<15} | {'Корректность':<12} | {'Время (сек)':>12}")
    print("-" * 50)
    passed = 0
    total = len(selected_indices)
    for idx in selected_indices:
        name, func = sort_algorithms[idx]
        try:
            result = func(test_array[:])
            is_ok = (result == reference)
            status = "OK" if is_ok else "FAIL"
            if is_ok:
                passed += 1
            t = timeit_once(func, test_array[:])
            print(f"{name:<15} | {status:<12} | {t:>12.6f}")
        except Exception as e:
            print(f"{name:<15} | {'ERROR':<12} | {'-':>12} - {type(e).__name__}")
    print(f"\nИтог: {passed} из {total} сортировок прошли проверку корректности.")
