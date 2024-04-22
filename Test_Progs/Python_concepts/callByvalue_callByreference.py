#
# #call by Value= =value keeps on changing as per current variable value------------------
# str="ABHI"
# def meth1(str):
#     print(str)
#     str="Abhi Nahi to kabhi nahin"
#     print(str)
#
# meth1(str)
# print(str)

# callByRefrence=once value gets updated in the list it remains unchanged--------------
def meth2reference(list):
    print(list)
    list.append(22)
    print(list)

list=[1,2,3]
meth2reference(list)
print(list)

