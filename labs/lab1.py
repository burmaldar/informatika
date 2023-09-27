#задание1
import math

def task1():
  pass

#задание2
def task2(x):
    b= -2
    c= 3
    return ((c*(x**3)+x)/(b*(x**2)))+(x**(1/3))


x=float(input())
print(task2(x))
#задание 3
import math
def task3():
    x = float(input())
    return ((math.sin(x)+math.cos(x))/(math.cos(x)-math.sin(x))*math.tan(x))
print(task3())
#задание4
import math
g = float(input())
s = float(input())
l = ((g**2+((s/math.pi)*(1/2)))**1/2)
print(l)
