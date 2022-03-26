#17.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
# multpos=[]
# import random
# n=random.randrange(-5,5,1)
# for i in range(10):
#     #i+=-1
#     multpos.append(n)
# print(multpos)

# num=int(input('Введите число '))
# list=[]
# i=1
# #(-num, num+1,2)- шаг через 2 (,2)
# for i in range(-num, num+1):
#     list.append(i)
# print(list)
# result=1
# with open('file.txt','r') as data:
#     for line in data:
#         temple=int(line)
#         result*=list[temple]
# print(result)
import random

n=int(input('Введите число '))
def func(n):
    """создание списка из n элементов"""
    result=[]
    for i in range(-n, n,2):
        result.append(i)
    return result

spisok=func(n)
print(spisok)
"""random.randrange(n) рандомный индекс"""
positions=[random.randrange(n) for i in range(random.randrange(n))]#компрехэншэн/сжатие цикла+ рандомные значения
with open('file.txt','w') as data:
    for i in range(0,len(positions)): #конкретная позиция в файле
        data.write(f'{positions[i]}\n')

mult=1
path='file.txt'
data=open(path, 'r')
for line in data:
    print(line)
    #n=int(line)
    mult*=spisok[int(line)]
data.close
print(mult)












