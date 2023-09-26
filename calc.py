import math





print("1.Сложение")
print("2.Вычитание")
print("3.Умножение")
print("4.Деление")
print("5.Возведение в степень")
print("6.извлечение квадратного")
print("7.Факториал")
print("8.Синус")
print("9.Косинус")
print("10.Тангенс")
print("11.Выход из программы")

isDone = True
    

while isDone != False:

    try:
        print("Выберите действие:")
        action = int(input())

        if action == 1:
            print("Введите первое число:")
            first = int(input())
            print("Введите второе число:")
            second = int(input())

            result = first + second
            
            print("Ответ:", result)
            isDone = True
        
        if action == 2:
            print("Введите первое число:")
            first = int(input())
            print("Введите второе число:")
            second = int(input())

            result = first - second
            
            print("Ответ:", result)
            isDone = True

        if action == 3:
            print("Введите первое число:")
            first = int(input())
            print("Введите второе число:")
            second = int(input())

            result = first * second
            
            print("Ответ:", result)
            isDone = True     

        if action == 4:
            print("Введите первое число:")
            first = int(input())
            print("Введите второе число:")
            second = int(input())

            result = first / second
            
            print("Ответ:", result)
            isDone = True

        if action == 5:
            print("Введите первое число:")
            first = int(input())
            print("Введите степень:")
            second = int(input())

            result = first ** second
            
            print("Ответ:", result)
            isDone = True  

        if action == 6:
            print("Введите число:")
            first = int(input())

            result = math.sqrt(first)
            
            print("Ответ:", result)
            isDone = True       

        if action == 7:
            print("Введите число:")
            first = int(input())
            
            fac = 1
            while first > 1:
                fac *= first
                first -= 1
 
            print("Ответ:", fac)
            isDone = True    
            
        if action == 8:
            print("Введите число:")
            first = float(input())

            result = math.sin(first)
          
            print("Ответ в радианах", result)
            isDone = True  
            
        if action == 9:
            print("Введите число:")
            first = float(input())

            result = math.cos(first)
            
            print("Ответ в радианах", result)
            isDone = True    

        if action == 10:
            print("Введите число:")
            first = float(input())

            result = math.tan(first)
          
            print("Ответ в радианах", result)
            isDone = True  


        if action == 11:
            break;    



    except:
        print(" ")
        print("Данные были введенны не верно, повторите попытку:")