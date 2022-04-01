#27.	Строка содержит набор чисел. Показать большее и меньшее число
#Символ-разделитель - пробел


"""не работает на отрицательных числах"""
input_string= input('ВВедите числа через пробел ').split(' ')
numbers=[]
for i in input_string:
    if i.isdigit():numbers.append(int(i))

print(f'наибольшее число = {max(numbers)}.\nнаименьшее число= {min(numbers)}')

# str=369, 88, 17, 45, 1111, -3, 15, -222

# max_number=int(max(str))
# min_number=int(min(str))
# print(max_number,' ', min_number)
# print(type(str))
