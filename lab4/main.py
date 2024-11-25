import random

# Таблица расширения E (Expansion)
E_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def permute(block, table):
    """Перестановка блока данных согласно заданной таблице."""
    return [block[i - 1] for i in table]

def generate_random_block(length):
    """Генерация случайного блока заданной длины."""
    return [random.randint(0, 1) for _ in range(length)]

def calculate_B_values(Ki, Ri_1):
    """
    Рассчитать значения B1, B2, ..., B8 для заданных Ki и Ri-1.
    1. Выполнить E-расширение для Ri-1.
    2. Выполнить XOR с Ki.
    3. Разделить результат на блоки B1, B2, ..., B8.
    """
    print("\nШаг 1: Выполняем E-расширение для R_{i-1}")
    ERi_1 = permute(Ri_1, E_TABLE)
    print("E(R_{i-1}):", ''.join(map(str, ERi_1)))

    print("\nШаг 2: Применяем XOR с K_i")
    XOR_result = [x ^ k for x, k in zip(ERi_1, Ki)]
    print("Результат XOR:", ''.join(map(str, XOR_result)))

    print("\nШаг 3: Разделяем на блоки B1, B2, ..., B8")
    B_blocks = [XOR_result[i:i + 6] for i in range(0, 48, 6)]
    for idx, B in enumerate(B_blocks, start=1):
        print(f"B{idx}: {''.join(map(str, B))}")

    return B_blocks

def main():
    print("DES: Вычисление B1, B2, ..., B8")

    # Выбор способа ввода данных
    input_type = input("Введите данные вручную (1) или сгенерировать случайно (2): ").strip()

    if input_type == "1":
        # Ввод вручную
        Ri_1 = list(map(int, input("Введите R_{i-1} (32 бита, через пробел): ").strip().split()))
        Ki = list(map(int, input("Введите K_i (48 бит, через пробел): ").strip().split()))
        if len(Ri_1) != 32 or len(Ki) != 48:
            print("Ошибка: длина R_{i-1} должна быть 32 бита, а K_i — 48 бит.")
            return
    elif input_type == "2":
        # Генерация случайных данных
        Ri_1 = generate_random_block(32)
        Ki = generate_random_block(48)
        print("Случайно сгенерированный R_{i-1} (32 бита):", ''.join(map(str, Ri_1)))
        print("Случайно сгенерированный K_i (48 бит):", ''.join(map(str, Ki)))
    else:
        print("Ошибка: некорректный выбор.")
        return

    # Вычисление B1, B2, ..., B8
    B_blocks = calculate_B_values(Ki, Ri_1)

    print("\nИтоговые блоки B:")
    for idx, B in enumerate(B_blocks, start=1):
        print(f"B{idx}: {''.join(map(str, B))}")

# Исправленная строка для запуска программы
if __name__ == "__main__":
    main()
