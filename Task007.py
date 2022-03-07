#7.	Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат-
#отвечает на утвердительный вопрос «да» или «нет», возвращая значение типа bool
# не(X+Y+Z)= неX + неY+ неZ
x=80
y=-3
z=3.14
if not(x+y+z)==(not x)+(not y)+(not z):
    print(True)
else:
    print(False)
if ((False, False) and(False, True) and(True, False) and(True, True)):
    print('Верно')
else:
    print('Неверно')