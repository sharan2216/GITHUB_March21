# def meth(*args):
#     total=0
#     for i in range(0,*args):
#         total=total+i
#     print(total)
#
# meth(9)

def meth1(**kwargs):
    res=[]
    for key,value in kwargs.items():
        res.append("{} has {} value".format(key,value))
    print(res)
meth1(google="java",micro="python")