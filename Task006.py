#6.	Дано число обозначающее день недели. Вывести его название и указать является ли он выходным
print('введите число от 1 до 7')
d=int(input())
if d==1:
    print('понедельник, будний день')
elif d==2:
    print('вторник, будний день')
elif d==3:
    print('среда, будний день')
elif d==4:
    print('четверг, будний день')
elif d==5:
    print('пятница, будний день')
elif d==6:
    print('суббота, наконец-то выходной!')
elif d==7:
    print('воскресенье, наконец-то выходной!')
else:
    print('неверная цифра')