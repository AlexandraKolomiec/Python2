#12.	Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
num_of_elements=int(input('введите количество элементов словаря '))
dict_result={}
for i in range(1, num_of_elements+1):
    dict_result[i]=3*i+1
    print(dict_result)