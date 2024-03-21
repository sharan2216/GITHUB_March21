# # Getter and Setter method---------------------------------------
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def set_meth(self):
        return self.name,self.age

    def get_age(self):
        print(f'name is {self.name} and age is {self.age}')

obj=A("Raj",22)
obj.set_meth()
obj.get_age()