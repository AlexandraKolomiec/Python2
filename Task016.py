#16.	Задать список из n чисел последовательности (1+1/n)n*n и вывести на экран их сумму
N=[]
numbers=int(input('введите значение '))
n=1
for i in range(numbers):
        n=(1+1/n)**n
        N.append(n)
print(N)
print(round(sum(N)))