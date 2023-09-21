print("Введите начало:")
first = int(input())

print("Введите конец")
second = int(input())

firstNum = int(first)
secondNum = int(second)

for num in range(firstNum, secondNum):

    if num <= 1:
        continue
    for i in range(2, num):
        if(num % i) == 0:
            break
        else:
            print(num)

