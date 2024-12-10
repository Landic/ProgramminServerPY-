def fibonacci(count):
    if(count <= 0):
        print("Кількість елементів повинна бути більше 0")
        return
    x,y = 0, 1
    for i in range (1, count + 1):
        print(i, " ", x)
        x, y = y, x + y

count = int(input("Введіть кількість елементів -> "))
fibonacci(count)