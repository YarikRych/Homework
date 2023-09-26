import math
x = int(input())
y = int(input())
z = int(input())
def task1(x,y,z):
    a1 = (abs(x**2-6))*0.5 - (abs(y**2-5))*0.5
    a2 = 1 + x**2/(y**3+1) + y**2/(x**3+1)
    a = a1/a2
    b = x**3 * ((math.atan(z))**3 + math.e)
    return a,b
print(task1(x,y,z))


x = int(input())
def task2(x):
    a = 2
    b = -1
    c = 3
    f = (x+a)**(1/3) + (c*x**2)/(b+x)
    return f
print(task2(x))


import math
x = int(input())
def task3(x):
    f = (math.cos(math.sin(math.cos(1/x**3))**2)**3)**2 - abs(x**3 + 3**x)
    return f

print(task3(x))


    
