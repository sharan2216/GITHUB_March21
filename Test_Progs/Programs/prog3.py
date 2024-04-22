# #4a3b2c1a
#
# def meth(str):
#     count=0
#     l2=[]
#     # l=str.split()
#     for i in str:
#         if i not in l2:
#             l2.append(i)
#             count=str.count(i)
#             print(f'{i}:{count}',end=' ')
#         # l2.append(i)
#
# str=input("enter a string :")
# meth(str)
#Sorting:-------------
l=[3,5,2,1,8,7]
n=len(l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
