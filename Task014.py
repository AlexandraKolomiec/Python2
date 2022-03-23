#14.	Подсчитать сумму цифр в вещественном числе
n=input('введите число ')
sum=0
for digit in n:
    if digit.isdigit():
        sum+=int(digit)
print('Сумма= ', sum)