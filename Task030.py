#30.	Вычислить число ПИ(отношение длины окружности к ее диаметру, константа) c заданной точностью d
#Пример: при d = 0.001,  = 3.141. 10-1d10-10
# from math import factorial
# from decimal import *
# def chudnovsky(n):
#     pi=Decimal(0)
#     k=0
#     while k<n:
#         pi+=(Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))*(13591409+545110134*k)/(640320**(3*k)))
#         k+=1
#         print('Шаг: {} из {}'.format(k,n))
#     pi=pi*Decimal(10005).sqrt()/4270934400
#     pi=pi**(-1)
#     return pi
# N=int(input('задайте значение точности '))
# getcontext().prec=N
# val=chudnovsky(N/14)
# print(val)


import math
def New_pi(d):
    if 0.1 >= d >= 10 ** -10:
        for_round = len(str(d))-2
        pi = math.pi
        new_pi = round(pi, for_round)
    else:
        new_pi = 'd не в заданном диапазоне'
    return new_pi

d = 0.001
#int(input('введите коэффициент точности (от 10**-1 до 10**-10: '))
print(New_pi(d))
