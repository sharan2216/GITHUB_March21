# def meth(*args):
#     tot=0
#     for i in args:
#         tot=tot+i
#     print(tot)
#
# meth(121)

def meth(**kwargs):
    reslist=[]
    for key,value in kwargs.items():
        reslist.append("{} has {} ".format(key,value))
    print(reslist)

meth(google="JAVA",Micro="PYTHON",Amazon=".NET")