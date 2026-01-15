import hashlib
import json


def hashing(password):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()


def ensure_file_exists():
    try:
        with open('file.json', 'r', encoding='utf-8') as file:
            json.load(file)
    except:
        with open('file.json', 'w', encoding='utf-8') as file:
            json.dump({}, file)


def break_password():
    try:
        with open('file.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except:
        data = {}
    login = input('Введите ваш логин: ')
    if login in data:
        password = input('Введите ваш новый пароль: ')
        data[login] = hashing(password)

        with open('file.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Регистрация успешна!")
    else:
        print("Логин отсутствует в базе дынных!")
        return


def verify():
    global login
    ensure_file_exists()

    try:
        type_of_login = int(input('Добро пожаловать!\n1) Логин\n2) Регистрация '))
    except:
        print("Введите 1 или 2")
        return

    if type_of_login == 1:
        login = input('Введите ваш логин: ')
        password = input('Введите ваш пароль: ')

        try:
            with open('file.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except:
            data = {}

        hashed = hashing(password)
        if login in data and data[login] == hashed:
            login_()
        else:
            print("Некорректный логин или пароль")
            print("Восстановить пароль?\n1) Да\n2) Нет")
            choice_of_break_password = int(input())
            if choice_of_break_password == 1:
                break_password()
            else:
                return

    elif type_of_login == 2:
        login = input('Введите ваш новый логин: ')
        password = input('Введите ваш новый пароль: ')
        hashed_password = hashing(password)

        try:
            with open('file.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except:
            data = {}

        if login in data:
            print("Такой логин уже есть в системе!")
            return

        data[login] = hashed_password

        with open('file.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Регистрация успешна!")
        login_()


def login_():
    print(f"Добро пожаловать в личный кабинет, {login}!")

verify()