#Palindrome--------
def meth(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=(rev*10)+dig
        num=num//10
    if (rev==temp):
        print("Palindrome")
    else:
        print("not a palindrome")

num=int(input("enter number :"))
meth(num)


