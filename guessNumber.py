import random

number = random.randint(1, 10)
print("Отгадай число в диапазоне от 1 до 10:")



IsDone = False

while IsDone != True:
    print("Введи своё число:")
    UserNum = int(input())

    if number == UserNum:
        print("Верно, загаданое число:", number)
        IsDone = True
    else:
        print("Неверно, попробуй ещё раз")
        IsDone = False



