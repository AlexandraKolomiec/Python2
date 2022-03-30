#21.	Определить, позицию второго вхождения строки в списке либо сообщить, что её нет

from calendar import c


spisok_1=["qwe", "qwe", "asd", "zxc", "qwe", "ertqwe"]
stroka_1="qwe"
count=0
print(f'Количество вхождений {spisok_1.count(stroka_1)}')
if spisok_1.count(stroka_1)<2:
    #count=-1
    print('Второго вхождения нет')

else:
    for i in range(len(spisok_1)):
        if spisok_1[i]==stroka_1:
            count+=1
            if count==2:
                count=i
                break
    print(f'Позиция второго вхождения {stroka_1} {count}')            

"""Второй вариант"""
# spisok_1=["qwe", "qwe", "asd", "zxc", "qwe", "ertqwe"]
# stroka_1="zxc"

# if spisok_1.count(stroka_1)<2:
#         print('Второго вхождения нет')
# countString=0
# countPos=0
# for i in spisok_1:
#     if stroka_1 in i:
#         countString+=1
#     if countString==2:
#         print(countPos)
#     countPos+=1



# i = 0
#while i < len(K):
    #index_of_qwe = K.index("qwe") 
    #i += 1
#print(index_of_qwe)
    
# for i in K:
#     if "qwe" in K:
#         index_of_qwe = K.index("qwe")
# print(index_of_qwe)

#i=K.find("qwe")
#print(i)

#result=findall("qwe", "asd", "zxc", "qwe", "ertqwe")
#print(result)


