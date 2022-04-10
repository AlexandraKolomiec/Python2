#35.	В файле находится N натуральных чисел, записанных через пробел.
#  Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его

with open("Task035.txt", 'r') as file2:
    data2 = file2.read()
data2 = list(map(int,(data2.split())))
print(data2)

for  i in range(len(data2)-1):
    if data2[i] != data2[i+1]-1:
        data2.insert(i+1, data2[i]+1)
print(data2)

"""1 2 3 4 5 7 8 9 10 13 15 16 17 18"""

