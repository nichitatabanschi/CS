# Caesar cipher with two keys: permutation + shift
def caesar_cipher_permuted(text, key1, key2, mode='encrypt'):
    # Step 1: Create a permuted alphabet using key2 (like 'CRYPTOGRAPHY')
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    permuted_alphabet = ''

    # First, add unique letters from key2
    for char in key2.upper():
        if char not in permuted_alphabet:
            permuted_alphabet += char

    # Then, add the remaining letters from the normal alphabet
    for char in alphabet:
        if char not in permuted_alphabet:
            permuted_alphabet += char

    # Выводим созданный переставленный алфавит
    print(f"Переставленный алфавит (permuted alphabet): {permuted_alphabet}")

    result = ''

    # Step 2: Encrypt or decrypt using the permuted alphabet and key1 shift
    text = text.upper().replace(' ', '')

    for char in text:
        if char in permuted_alphabet:
            idx = permuted_alphabet.index(char)
            if mode == 'encrypt':
                new_idx = (idx + key1) % len(permuted_alphabet)
            elif mode == 'decrypt':
                new_idx = (idx - key1) % len(permuted_alphabet)
            result += permuted_alphabet[new_idx]
        else:
            result += char  # Non-alphabet characters are unchanged

    return result

# Get inputs from the console
message = input("Введите сообщение для шифрования/дешифрования: ")
key1 = int(input("Введите числовой ключ сдвига (key1): "))  # Shift key
key2 = input("Введите ключ перестановки (key2): ")  # Permutation key
mode = input("Введите режим ('encrypt' для шифрования или 'decrypt' для дешифрования): ").lower()

# Encrypt or decrypt the message
result_message = caesar_cipher_permuted(message, key1, key2, mode)

# Print the result
print(f"Результат: {result_message}")
