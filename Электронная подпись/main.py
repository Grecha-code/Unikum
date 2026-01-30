import hashlib


def hashing(text):
    full_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
    result = full_hash[0:16]

    return result


def crypted(text):
    all_chars = [chr(i) for i in range(65536)]
    key = (691, 779)
    code = []
    for i in text:
        code.append(all_chars.index(i) ** key[0] % key[1])
    return code


def encrypted(code):
    key2 = (571, 779)
    all_chars = [chr(i) for i in range(65536)]
    decode = ""
    for sim in code:
        decode += all_chars[(sim ** key2[0] % key2[1])]
    return decode


def home():
    print("Вариант B. Пашков Алексей ИИ-71")
    print("Главное меню\n1) Создать подпись\n2) Проверить подпись(окончательно подписать документ)")
    choice = int(input())

    if choice == 1:
        signature = input("Введите подпись: ")
        encrypted_signature = crypted(hashing(signature))
        with open('file.txt', 'w', encoding='utf-8') as file:
            file.write(str(encrypted_signature))
        print("Подпись создана и сохранена в file.txt")

    elif choice == 2:
        signature = input("Введите подпись из документа: ")
        new_encrypted_signature = crypted(hashing(signature))
        with open('file.txt', 'r', encoding='utf-8') as file:
            saved_signature = file.read()
        saved_signature_list = eval(saved_signature)
        if new_encrypted_signature == saved_signature_list:
            print("Подпись подтверждена!")
        else:
            print("Подписи не совпадают")

    else:
        print("Пожалуйста, введите другое число")

if __name__ == "__main__":
    home()