# Функция для шифрования/дешифрования сообщения
def caesar_cipher(text, key, mode='encrypt'):
    # Алфавит
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Преобразуем текст в верхний регистр и убираем пробелы
    text = text.replace(' ', '').upper()

    # Переменная для хранения результата
    result = ''

    # Цикл по каждому символу текста
    for char in text:
        if char in alphabet:
            # Индекс текущей буквы в алфавите
            index = alphabet.index(char)
            if mode == 'encrypt':
                # Смещение для шифрования
                new_index = (index + key) % 26
            elif mode == 'decrypt':
                # Смещение для дешифрования
                new_index = (index - key) % 26

            # Добавляем новую букву в результат
            result += alphabet[new_index]
        else:
            result += char  # Если символ не буква, оставляем его без изменений

    return result


# Пример использования
message = input("Введите сообщение: ")
key = int(input("Введите ключ (1-25): "))
mode = input("Введите режим (encrypt/decrypt): ")

# Выполнение шифрования или дешифрования
cipher_text = caesar_cipher(message, key, mode)
print(f"Результат: {cipher_text}")
