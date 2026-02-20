from stegano import lsb
from stegano import exifHeader
from steganocryptopy.steganography import Steganography


def first():
    secret = lsb.hide("images/img.png", "Pivil poshli v coliz a potom kushatt")
    secret.save("images/secret.png")
    result = lsb.reveal("images/secret.png")
    return result


def second():
    exifHeader.hide("images/img.png", "images/secret.jpg", "Пошли кумыс попьём")
    result = exifHeader.reveal("images/secret.jpg")
    result = result.decode()
    return result


def third():
    Steganography.generate_key("")
    secret = Steganography.encrypt("key.key", "images/img.png", "secret_message.txt")
    secret.save("images/secret2.png")
    result = Steganography.decrypt("key.key", "images/secret2.png")
    return result


if __name__ == "__main__":
    print("Введите пароль для получния текста:")
    password = input()
    with open("file.txt", "r") as file:
        if password in file and len(password) == 8:
            print("Пароль правильный! Вот текст, который вам хотели оставить:")
            print(first())
            print(second())
            print(third())
        else:
            print("Пароль не верный!")