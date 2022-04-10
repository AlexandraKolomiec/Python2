#32.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# numbers=[1, 3, 5, 1, 5, 3, 101,3,1,11]
# uniq_num=list(set(numbers))
# print(uniq_num)

"""вариант2"""
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
my_set = set(my_list)
print(my_set)
my_list2 = list(my_set)
print(my_list2)

"""вариант3"""
# list = [1, 2, 3, 5, 1, 5, 3, 10]

# def number(list):
#     unnumber = []
#     for number in list:
#         if number in unnumber:
#             continue
#         else:
#             unnumber.append(number)
#     return unnumber

# print(number(list))