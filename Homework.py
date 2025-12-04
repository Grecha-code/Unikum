''' Домашнее задание по Искусственному Интеллекту от Пашкова Алексея ИИ-71 '''

def first(num):
    result = [f"{i}: четное" if i % 2 == 0 else f"{i}: нечетное" for i in range(0, num + 1)]
    print(result)

def second():
    result = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
              for i in range(1, 100 + 1)]
    print(result)

def third(num):
    result = [i if i > 10 else 0 for i in range(0, num + 1)]
    print(result)

def fourth(num):
    result = {i: ("even" if i % 2 == 0 else "odd") for i in range(0, num + 1)}
    print(result)

def fifth(string):
    result = [len(string) if len(string) <= 5 else 5]
    print(result)

def sixth(my_list):
    result = [i if i > 0 else 0 for i in my_list]
    print(result)

def seventh(num):
    result = [num ** 0.5 if num > 0 else 0]
    print(result)

def eighth(my_list):
    result = [i ** 2 if i % 2 == 0 else i ** 3 for i in my_list]
    print(result)

def ninth(num):
    result = ["High" if num > 50 else "Medium" if num < 50 and num > 20 else "Low"]
    print(result)
