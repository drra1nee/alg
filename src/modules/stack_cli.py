"""
Реализация взаимодействия со стеком через команды
"""

from .stack import Stack

def stack_inter():
    """Интерактивное взаимодействие со стеком"""
    stack = Stack()
    print("\nStack")
    print("Доступные команды:")
    print("  push <число> - добавить число (int/float)")
    print("  pop - извлечь верхний элемент")
    print("  peek - посмотреть верхний элемент")
    print("  min - текущий минимум")
    print("  len - количество элементов")
    print("  empty - проверить, пуст ли стек")
    print("  clear - очистить стек")
    print("  show - показать строковое представление стека(от вершины до дна)")
    print("  quit - выйти в главное меню")
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
            print("Неожиданная ошибка:", type(e).__name__, "-", e)
