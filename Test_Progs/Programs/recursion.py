def meth(str):
    d={}
    for i in str:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1

    max_char=max(d,key=d.get)
    min_char=min(d,key=d.get)

    print(max_char)
    print(min_char)


str=input("enter a string :")
meth(str)
