def meth():
    for i in range(10):
        if i==7:
            break
        else:
            print(i,end=" ")

meth()
print()
def meth2():
    for i in range(10):
        if i==7:
            continue
        else :
            print(i,end=" ")

meth2()
print()

def meth3():
    for i in range(10):
        if i==7:
            pass
        print(i,end=" ")

meth3()