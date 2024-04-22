# str="geeks for geek is good"
# str2=str.split(" ")
# print([x for x in str2 if len(x)%2==0])

# # check all vowels in a string----------------
# #
# def check(str):
#     if set("aeiou").issubset(set(str.lower())):
#         print("accepted")
#     else:
#         print("Not Accepted")
#
# str='aeIOU'
# # check(str)
# #
# # # # Python – Least Frequent Character in String--------------------
# str='shashikantsharan'
# n=len(str)
#
# d={}
# for i in str:
#     if i in d:
#         d[i]=d[i]+1
#     else :
#         d[i]=1
#
#
# res=min(d,key=d.get)
# res2=max(d,key=d.get)
# print(d)
# print(res)
# print(res2)


# Dictionary:-----------

# site_stats = {'site': 'tecbeamers.com', 'traffic': 10000, "type": "organic"}
# print(site_stats["traffic"])
# print(site_stats.get("traffic"))
# print(site_stats.get("type"))

# site_stats1 = {'site': 'tecbeamers.com', 'traffic': 10000, "type": "organic"}
# for k,v in site_stats1.items():
#     print(k ,v)
# print()


# Palindrome and Symmetrical

# def meth():
#     str=input("enter a string :")
#     mid=int(len(str)/2)
#     first_half=str[:mid]
#     second_half=str[mid:]
#
#     if first_half==second_half:
#         print("symmetrical")
#     else:
#         print("not symmetrical")
#
#     if first_half==second_half[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")
#
# meth()


# # Find words which are greater than given length k
# str="My name is shashi sharan and my surname is kant"
# l=str.split()
# k=3
#
# print(l)
# for i in l:
#     if len(i)>=k:
#         print(i)
#
# # Python program for removing i-th character from a string
# def remove(str,i):
#
#     a=str[:i]
#     b=str[i+1:]
#     res=a+b
#     print(res)
#
# str="mynameiskant"
# remove(str,7)

# Python – Replace duplicate Occurrence in String
def meth():
    str1='my name is kant'
    str2='my sir name is kant'
    l1=str1.split()
    print(l1)
    l2=str2.split()
    print(l2)
    l3=[]
    l4=[]
    for i in l1:
        if i in str2 and i not in l3:
            l3.append(i)
    for j in l2:
        if j in str1 and j not in l3:
            l3.append(j)

    l4=' '.join(l3)

    print(l4)


meth()