#28.	Найти корни квадратного уравнения Ax² + Bx + C = 0
import math
from modulefinder import Module
print('введите значения для уравнения')
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))

discr=b**2-4*a*c
print(discr)
if discr>0:
    quad_eq1=(-b+ math.sqrt(discr))/(2*a)
    quad_eq2=(-b- math.sqrt(discr))/(2*a)
    print(quad_eq1, quad_eq2)
elif discr==0:
    quad_eq3=-b/(2*a)
    print(quad_eq3)
else:
    print('нет корней')


# import cmath
# sol1=(-b+cmath.sqrt(discr))/(2*a)
# sol2=(-b-cmath.sqrt(discr))/(2*a)
# #sol3=-b/(2*a)
# print(sol1, sol2, sol3)