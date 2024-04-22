# Duplicate caharcter

def meth(str):
    l2=[]
    count=0
    for i in str:
        if str.count(i)>1 and i not in l2:
            l2.append(i)
    print(l2)

str=input("enter a string :")
meth(str)

# UNDuplicate caharcter
def meth2(str):
    l2=[]
    count=0
    for i in str:
        if str.count(i)==1 and i not in l2:
            l2.append(i)
    print(l2)

str=input("enter a string :")
meth2(str)