#14.	Подсчитать сумму цифр в вещественном числе
n=input('введите число ')
sum=0
for digit in n:
    if digit.isdigit():
        sum+=int(digit)
print('Сумма= ', sum)

# num=float(input('введите число '))
# num=str(num)
# #замена точки на пробел
# num1=num.replace('.',' ')
# num2=int(num1)
# #если ввели отрицательное значение
# if num2<0:
#     num2*=-1

# sum_didg=0
# while num2>0:
#     ost=num2%10
#     sum_didg+=ost
#     num2//=10
# print(sum_didg)