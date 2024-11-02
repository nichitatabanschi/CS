import re

class PlayfairCipher:
    def __init__(self, key):
        self.key = self.process_key(key)
        self.grid = self.create_grid(self.key)

    def process_key(self, key):
        # Убираем повторяющиеся символы и делаем их заглавными
        processed_key = []
        for char in key.upper():
            if char not in processed_key and 'А' <= char <= 'Я':
                processed_key.append(char)
        return ''.join(processed_key)

    def create_grid(self, key):
        alphabet = [chr(i) for i in range(ord('А'), ord('А') + 32)] + ['Я']  # Русский алфавит (33 буквы)
        grid = []
        used_chars = set(key)
        grid.extend(key)

        # Добавляем оставшиеся буквы алфавита, которых нет в ключе
        for letter in alphabet:
            if letter not in used_chars:
                grid.append(letter)
                used_chars.add(letter)

        return [grid[i:i + 6] for i in range(0, len(grid), 6)]  # создаем 6x6 таблицу

    def find_position(self, char):
        for i, row in enumerate(self.grid):
            if char in row:
                return i, row.index(char)
        return None

    def prepare_text(self, text):
        # Убираем символы, не относящиеся к алфавиту
        text = re.sub(r'[^А-Я]', '', text.upper())
        prepared_text = ""
        i = 0
        while i < len(text):
            char1 = text[i]
            if i + 1 < len(text):
                char2 = text[i + 1]
                if char1 == char2:
                    prepared_text += char1 + 'Ъ'
                    i += 1
                else:
                    prepared_text += char1 + char2
                    i += 2
            else:
                prepared_text += char1 + 'Ъ'
                i += 1
        return prepared_text

    def encrypt_pair(self, char1, char2):
        row1, col1 = self.find_position(char1)
        row2, col2 = self.find_position(char2)

        if row1 == row2:
            return self.grid[row1][(col1 + 1) % 6] + self.grid[row2][(col2 + 1) % 6]
        elif col1 == col2:
            return self.grid[(row1 + 1) % 6][col1] + self.grid[(row2 + 1) % 6][col2]
        else:
            return self.grid[row1][col2] + self.grid[row2][col1]

    def decrypt_pair(self, char1, char2):
        row1, col1 = self.find_position(char1)
        row2, col2 = self.find_position(char2)

        if row1 == row2:
            return self.grid[row1][(col1 - 1) % 6] + self.grid[row2][(col2 - 1) % 6]
        elif col1 == col2:
            return self.grid[(row1 - 1) % 6][col1] + self.grid[(row2 - 1) % 6][col2]
        else:
            return self.grid[row1][col2] + self.grid[row2][col1]

    def encrypt(self, plaintext):
        plaintext = self.prepare_text(plaintext)
        ciphertext = ""
        for i in range(0, len(plaintext), 2):
            ciphertext += self.encrypt_pair(plaintext[i], plaintext[i + 1])
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i in range(0, len(ciphertext), 2):
            plaintext += self.decrypt_pair(ciphertext[i], ciphertext[i + 1])
        return plaintext

def main():
    while True:
        choice = input("Выберите операцию (1 - шифрование, 2 - дешифрование, 3 - выход): ")
        if choice == '3':
            break
        elif choice not in ('1', '2'):
            print("Неверный выбор, попробуйте снова.")
            continue

        key = input("Введите ключ (не менее 7 символов): ")
        if len(key) < 7:
            print("Ключ должен содержать не менее 7 символов.")
            continue

        message = input("Введите сообщение (только русские буквы): ")
        if re.search(r'[^А-Яа-я]', message):
            print("Сообщение должно содержать только русские буквы.")
            continue

        cipher = PlayfairCipher(key)

        if choice == '1':
            result = cipher.encrypt(message)
            print("Зашифрованное сообщение:", result)
        elif choice == '2':
            result = cipher.decrypt(message)
            print("Расшифрованное сообщение:", result)

if __name__ == "__main__":
    main()
