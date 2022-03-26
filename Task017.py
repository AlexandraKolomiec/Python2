#17.Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
# multpos=[]
# import random
# n=random.randrange(-5,5,1)
# for i in range(10):
#     #i+=-1
#     multpos.append(n)
# print(multpos)

num=int(input('Введите число '))
list=[]
i=1
for i in range(-num, num+1):
    list.append(i)
print(list)
result=1
with open('file.txt','r') as data:
    for line in data:
        temple=int(line)
        result*=list[temple]
print(result)











