#29.	Найти НОК двух чисел
print('введите первое число')
a=int(input())
print('введите второе число')
b=int(input())

i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print('НОК равно', i)
