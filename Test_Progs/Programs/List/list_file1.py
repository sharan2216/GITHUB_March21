# # Python program to interchange first and last elements in a list
def swap(list):
    n=len(list)
    temp=list[0]
    list[0]=list[n-1]
    list[n-1]=temp
    print(list)

list=[1,2,3,4,5]
swap(list)