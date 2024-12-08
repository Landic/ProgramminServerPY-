x = 10                  #Змінні не оголушуються, створюються при запису
print(x, type(x))       # 10 <class 'int'>
x = 2j                  # Орієнтованість на математику: підтримка різних чисел
print(x, type(x))       # 2j <class 'complex'>
y = 10 + x              # Нестрога типізація / неявне перетворення типів
print(y, type(y))       # (10+2j) <class 'complex'>
s = "y = " + str(y)
print(s, type(s))
x = 2 ** 256
print (x, type(x))
if x > 2  ** 128:
    print("Number")
    print("greater than")
    print("2^128")
else:
    pass


x = input("Enter x = ")
print(x, type(x))
y = float (x)
print(y, type(y))


s2 = "Hello"
s1 = 'Hello'
s3 = """Hello,
    World"""

t = 10, 20, 30
print(t, type(t))
x,y,w = t
print(x, type(x))
x,y = y,x
print(x, type(x))
x,y = 1, 1
x,y = y,x + y
print(x,y)
s = "x = %s, y = %s, w = %s" % t
print(s)

s = f"x = {x}, y = {y}, w = {w}"
print(s)

x,y = 14, 6
print("%d + %d = %f" % (x,y, x + y))

w = 10 if x > 2 else 20
x = 10
while x > 0:
    x -=1
    print(x, end = ', ')
else:
    print("while-else ", x)


r10 = range(10)
print(r10, type(r10))
for x in r10:
    print(x, end=', ')
for x in range(10,1,2):
    print(x, end=', ')
for x in range(10,1,-2):
    print(x, end=', ')