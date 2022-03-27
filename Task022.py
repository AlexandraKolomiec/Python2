#22.	Найти сумму чисел списка стоящих на нечетной позиции
spisok=[124, -2, 389, 43, 25, 96, -7, 0, 81, 9]
sum_odd_pos=0
for i in range(len(spisok)):
    if i%2!=0:
        sum_odd_pos+=spisok[i]
print(sum_odd_pos)

