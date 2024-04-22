# importing copy module
# import copy
# li1 = [1, 2, [3, 5], 4]
# # using copy for shallow copy
# l2=copy.copy(li1)
# print(l2)
#
# # # 2nd method-------------
# li1 = [4, 8, 2, 10, 15, 18]
# li_copy = li1[:]
# print(li_copy)



# # # Python | Count occurrences of an element in a list------------
# l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
# count=0
# x=[i for i in l if i==1]
# print(len(x))

# Python | Remove empty tuples from a list

# Python program to remove empty tuples from a
# list of tuples function to remove empty tuples
# using len()
# def meth(tup):
#     for i in tup:
#         if len(i)==0:
#             tup.remove(i)
#     print(tup)
#
# tup=[(), ('ram', '15', '8'), (), ('laxman', 'sita'),
#           ('krishna', 'akbar', '45'), ('', ''), ()]
# meth(tup)

# def meth(l):
#     l[0],l[-1]=l[-1],l[0]
#     print(l)
#
# l=[1,2,3,4,5]
# meth(l)

# # Python program to print positive and negative  numbers in a list
# l= [-10, -21, -4, 45, -66, 93]
# n=0
# x=[n for n in l if n>0]
# print(x)
# y=[n for n in l if n<0]
# print(y)


# # # Python program to print all positive numbers in a range------
# start,end=0,22
# for i in range(start,end+1,2):
#     print(i,end=' ')

# # Python – Remove empty List from List-------
# # Initializing list
# test_list = [5, 6, [], 3, [], [], 9]
# x=[i for i in test_list if i!=[]]
# print(type(x))
# print(x)

# Python program to print all odd numbers in a range-----------
start, end = 4, 19
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")