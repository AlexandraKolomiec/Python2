#11.	Сформировать список из  N членов последовательности.Для N = 5: 1, -3, 9, -27, 81 и т.д.

#N=[None for _ in range(5)]
N=[]
n=1
N.append(n)
for i in range(5):
    n*=-3
    N.append(n)
print(N)

