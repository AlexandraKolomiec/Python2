#10.Найти расстояние между двумя точками пространства

from cmath import sqrt

xA=int(input('введите значение x для точки A '))
yA=int(input('введите значение y для точки A '))
xB=int(input('введите значение x для точки B '))
yB=int(input('введите значение y для точки B '))
print(sqrt(((xB-xA)**2)+((yB-yA)**2)))
