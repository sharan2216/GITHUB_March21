# # # Getter and Setter method---------------------------------------
# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def set_meth(self):
#         return self.name,self.age
#
#     def get_age(self):
#         print(f'name is {self.name} and age is {self.age}')
#
# obj=A("Raj",22)
# obj.set_meth()
# obj.get_age()

# # Getter and Setter method---------------------------------------
class B:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def set_meth(self):
        return self.name,self.age

    def get_age(self):
        if self.age>18:
            print(f'name is {self.name} and age is {self.age}')
        else:
            print("Does not qualified")

obj1=B("Raj",21)
obj1.set_meth()
obj1.get_age()
obj2=B("Raj",15)
obj2.set_meth()
obj2.get_age()