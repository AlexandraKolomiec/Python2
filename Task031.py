#31.	Составить список простых множителей натурального числа N


# n=int(input("введите число: ")) 
# l=[]
# for i in range(1, n+1):
#     if (n%i==0):
#         l.append(i)
# print(l)

n=int(input("введите число: "))
list = []

for i in range(2,n):
    while n%i==0:
        n/=i
        list.append(i)
print(list)

