def sub(a,b):
    print(a-b)

def deco(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return sub(a,b)
    return inner

obj=deco(sub)
obj(78,10)