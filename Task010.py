#10.Найти расстояние между двумя точками пространства

from cmath import sqrt


print('введите значение x для точки A')
xA=int(input())
print('введите значение y для точки A')
yA=int(input())
print('введите значение x для точки B')
xB=int(input())
print('введите значение y для точки B')
yB=int(input())
print(sqrt(((xB-xA)**2)+((yB-yA)**2)))
