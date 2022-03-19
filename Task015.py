#15.	Написать программу получающую набор произведений чисел от 1 до N.
#Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
mult=[]
n=1
mult.append(n)
for i in range(3):
    n*=n+1
    mult.append(n)
print(mult)

