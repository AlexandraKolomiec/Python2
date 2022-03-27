#Реализовать алгоритм перемешивания списка

# import random
# N=[3,5,7,9,18,27]
# print(N)
# print(random.shuffle(N))

from random import randrange
def mix_list(items):
    i=len(items)
    while i>1:
        i=i-1
        j=randrange(i)
        items[j], items[i]=items[i], items[j]
    return items

list=[1, 2, 3, 4, 5]
print(f'Первоначальный список: {list}')
print(f'Перемешанный список: {mix_list(list)}')
    

