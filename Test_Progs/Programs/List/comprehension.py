
#list comprehension--------
l2=[i for i in range(1,10)if i%2==0]
print(l2)


#set comprehension---------
s={i for i in range(10) if i%2==0}
print(s)

#dict comprehension------
d={i:i*2 for i in range(1,10)}
print(d)

