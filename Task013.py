#13.	Пользователь задаёт две строки. Определить количество вхождений одной строки в другой

firststring=input('введите первую строку  ')
print(f"{firststring}")
secondstring=input('введите вторую строку  ')
print(f"{secondstring}")

firststring_count=firststring.count(secondstring)
print(firststring_count)
secondstring_count=secondstring.count(firststring)
print(secondstring_count)



