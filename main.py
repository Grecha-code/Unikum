import time
print("Вариант B")

def first():
  print(f'1) 1000 бит = {1000/8} байт, {1000/8/1024} кб, {1000/8/1024/1024} мб, ')
  print(f'{1000/8/1024/1024/1024} гб, {1000/8/1024/1024/1024/1024} тб')

def second():
  print("2) 1 символ = 6 бит")
  print(60*1000*2*6, "бит")

def third():
  year_time = input('3) Какое сейчас время года?')
  if year_time == 'Лето':
    print("Какая сейчас погода?")
    a = int(input())
    if a >= 15:
      print("Футболка")
    else:
      print("Кофта")
  elif year_time == 'Осень':
    print("Какая сейчас погода?")
    a = int(input())
    if a >= 10:
      print("Кофта")
    else:
      print("Ветровка")
  elif year_time == 'Зима':
    print("Какая сейчас погода?")
    a = int(input())
    if a >= -5:
      print("Легкая куртка")
    else:
      print("Теплая куртка")
  elif year_time == 'Весна':
    print("Какая сейчас погода?")
    a = int(input())
    if a >= 7:
      print("Кофта")
    else:
      print("Ветровка/Легкая куртка")
  else:
    print("Такого времени года нету!")

first()
time.sleep(5)
second()
time.sleep(5)
third()