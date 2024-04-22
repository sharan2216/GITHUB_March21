# # No of words and characters in a string:
#
# def meth(str):
#     d={}
#     l=str.split()
#     for i in l:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     print(d)
#
# str=input("enter a string : ")
# meth(str)
#
#
# #no of character in string-------------
# def meth(str):
#     d={}
#     for i in str:
#         if i in d:
#             d[i]=d[i]+1
#         else:
#             d[i]=1
#     print(d)
#
# str=input("enter a string : ")
# meth(str)
#

# Reverse String:=========

def meth(str):
    list=[]
    list=str.split()
    print(list)
    for word in list:
        list2=word[::-1]
        str2=''.join(list2)
        print(str2,end=' ')

str=input("enter a string : ")
meth(str)

print("----------------------------------")
#Reverse characters-------------
print(str[::-1])