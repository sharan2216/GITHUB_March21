# from array import *
# l=[1,4,2,5,2,1,5]
# arr=array('i',[1,4,2,5,2,1,5])
# print(arr)
# arr.append(11)
# print(arr)
# for i in arr:
#     print(i,end=' ')
#
# print("\n7th Program------------")
# arr3 = array('i', [9, 8, 7, 6])
# arr3.insert(1,4)
# for i in arr3:
#     print(i,end=' ')
#
#
# print("\n8th Program------------")
# # Python Program to Find Largest Element in an Array
# max=arr3[0]
# for i in arr3:
#     if i>max:
#         max=i
# print(max)
#
# #Reverse-------
# print(arr3[::-1])
from array import array

# Python Program to Find Sum of Array

# def meth(arr):
#     sum=0
#     for i in arr:
#         sum=sum+i
#     print(sum)
#
#
# arr=[1,2,3,4,5]
# meth(arr)


# arr=[1,4,2,5,2,1,5]
# # print(set(arr))
# # print(list(set(arr)))
# arr.reverse()
# for i in arr:
#     print(i,end=' ')

# print("-------------------")
# arr2 = array('i',[1,3,5,7,9,3,1])
# print("\n6th Program------------")
# count=0
# for i in arr2:
#     if i==1:
#         count=count+1
# print(count)
# arr1 = array('i',[1,3,5,7,9,3,1])
# print("\n POP Program------------removes element at specified position")
# print(arr1)
# arr1.pop() #removes the last element in the list
# print(arr1)
# arr1.pop(3)
# print(arr1)
# arr1.pop()
# print(arr1)
#
# arr12 = array('i',[1,3,5,7,9,3,])
# print("\n12th Program------------removes first occurrence of a specified position")
# print(arr12)
# arr12.remove(3)
# print(arr12)

# 3. Write a Python program to reverse the order of the items in the array.
# Sample Output
arr1 = array('i',[1,3,5,7,9,3,])
print("\n3rd Program------------")
arr1.reverse()
for i in arr1:
    print(i,end=' ')