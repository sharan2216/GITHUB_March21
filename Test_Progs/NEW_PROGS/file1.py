try:
    with open("D:\\demo21.txt","r") as file:
        data=file.read()
except FileNotFoundError as err:
    print(err)