#24.	В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов.
#  Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
numbers_list=[1.1, 1.2, 3.1, 5, 10.01]

def get_decimal_part(float_number, int_digits_after_point):
    return round((float_number %1), int_digits_after_point)

dec_part_list=[]
for i in range(0, len(numbers_list)):
    if type(numbers_list[i])==float:
        dec_part_list.append(get_decimal_part(numbers_list[i],2))

max=max(dec_part_list)
min=min(dec_part_list)
print(f'Разница между max и min значением дробной части= {max-min}.')

# float_spisok = [1.1, 1.2, 3.1, 5.002, 10.000001, 11.13, 10.11, 122324.52, 0.14]

# max = 0.000
# min = 1.000
# for i in range(len(float_spisok)):
#     float_spisok[i]=round(float_spisok[i]-int(float_spisok[i]),10)
#     if max<float_spisok[i]:
#         max = float_spisok[i]
#     if min>float_spisok[i]:
#         min = float_spisok[i]
# x=max-min

# print(max,min)
# print(type(x))
# print(x)           