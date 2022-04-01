#31.	Составить список простых множителей натурального числа N


# n=int(input("введите число: ")) 
# l=[]
# for i in range(1, n+1):
#     if (n%i==0):
#         l.append(i)
# print(l)

n=int(input("введите число: "))
list = []
"""1 вариант"""
for i in range(2,n):
    while n%i==0:
        n/=i
        list.append(i)
print(list)


"""2 вариант"""
def f(n,d):
    while d<=n:
        if n%d==0:
            list.append(d)
            n//=d
        elif n%d!=0:
            d+=1
f(n,2)
print(list)            
