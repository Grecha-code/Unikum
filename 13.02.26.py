def binary_8bit(text):
    return "".join(format(ord(char), '08b') for char in text)


def code(message, secret_text):
    message = message.lower()
    bits = binary_8bit(secret_text)
    result = ""
    bit_index = 0
    for i in range(len(message)):
        if bit_index < len(bits) and message[i].isalpha():
            bit = bits[bit_index]
            if bit == '1':
                result += message[i].upper()
            else:
                result += message[i].lower()
            bit_index += 1
        else:
            result += message[i]

    return result


if __name__ == "__main__":
    secret_input = input("Введите текст для прятания: ")
    message_input = input("Введите сообщение-контейнер: ")

    bits_need = len(binary_8bit(secret_input))

    letters_in_message = sum(i.isalpha() for i in message_input)

    if bits_need > letters_in_message:
        print(f"Ошибка: В сообщении должно быть минимум {bits_need} букв!")
        exit()

    print("Бинарный вид секрета:", binary_8bit(secret_input))
    print("Результат стеганографии:")
    print(code(message_input, secret_input))