# call by value
str='shashi'
def meth(str):
    print(str)
    str='shashikant'
    print(str)

meth(str)
print(str)

# call by reference
def meth(l):
    print(list)
    list.append(11)
    print(list)

list=[1,2,3,4,5]
meth(list)
print(list)