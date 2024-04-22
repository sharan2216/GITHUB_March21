try:
    num1=int(input("enter a number 1 :"))
    num2=int(input("enter a number 2 :"))
    result = num1/num2
    print(result)

except (TypeError,ZeroDivisionError,Exception)as err:
    print(err)
else:
    print("something went wrong")
finally:
    print("This is a Final statement Have a Nice Day")