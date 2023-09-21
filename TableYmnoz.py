print("таблица умножения:")

i = 0
j = 0

for i in range(1, 10):
    for j in range(1, 10):
        print("%4d" % (i * j), end= "")
    print()