#23.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def MultPair(listMultPair):
#     listAdd=[]
#     if (len(listMultPair)%2==0):
#         for i in range(0, len(listMultPair)//2):
#             listAdd.append(listMultPair[i]*listMultPair[len(listMultPair)-1-i])
#     else:
#         for i in range(0, (len(listMultPair)+1)//2):
#             listAdd.append(listMultPair[i]*listMultPair[len(listMultPair)-1-i])
#     return listAdd

# list1=[2, 3, 4, 5, 6]
# list2=[2, 3, 4, 5, 6, 7]
# print(MultPair(list2))       

import math
lst=[2,3,4,5,6]
res_lst=[]
len_res_lst=math.ceil(len(lst)/2)
temp=0

for i, x in enumerate(lst):
    if len(res_lst)!=len_res_lst:
        temp=lst[i]*lst[-1-i]
        res_lst.append(temp)
print(res_lst)