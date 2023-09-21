print("Введите число:")
num = int(input())

j = 0 

for i in range(2, num// 2+1):
    if (num % j == 0):
        j += 1
if (j <= 0):
    print("Число простое")
else:
    print("Число не простое")

