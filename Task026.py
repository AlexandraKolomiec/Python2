#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
 #Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def negafib(n): 
    if n in [-1,0,1]: 
        return abs(n) 
    elif n < 0: 
        n = abs(n) 
        return (-1)**(n+1)*(negafib(n-1)+negafib(n-2)) 
    else: 
        return negafib(n-1)+negafib(n-2) 
 
n = int(input('Введите число n = ')) 
list = [] 
for i in range(-n,n+1): 
    list.append(negafib(i)) 
print(list)

"""второй вариант"""
# number = 8

# def fib_rec(number_int):
#     if number_int in (1, 2):
#         return 1
#     return fib_rec(number_int - 1) + fib_rec(number_int - 2)

# def negafib(number_int):
#     fib1 = fib2 = 1
#     for i in range(-number_int, 1):
#         fib1, fib2 = fib2, fib1 - fib2
#     return fib2

# fib_list = [fib_rec(item) for item in range(number, 0, -1)]
# fib_list.reverse()   

# negafib_list = [negafib(item) for item in range(number + 1)]
# negafib_list.reverse()

# negafib_list.extend(fib_list)
# print(f"k = {number}: {negafib_list}")


# print(list)
