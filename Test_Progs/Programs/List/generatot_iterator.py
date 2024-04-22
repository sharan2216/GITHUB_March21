#generator

def meth1():
    for i in range(1,10):
        yield i*i

a=meth1()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# iterator

def meth():
    l=[1,2,3,4,5]
    l2=iter(l)
    print(next(l2))

meth()