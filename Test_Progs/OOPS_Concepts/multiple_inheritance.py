class A:
    def __init__(self,name):
        self.name=name
    def dispaly(self):
        print(f'Name is {self.name}')

class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def display(self):
        print(f'name is {self.name} age is {self.age} ')
class C(A):
    def __init__(self,name,loc):
        super().__init__(name)
        self.loc=loc

    def display(self):
        print(f'name is {self.name} and salary is {self.loc}')

b1=B("raj",21)
c1=C("Tom",22)
print(b1.name)
print(b1.age)
print(b1.display())
print("------------------------------")
print(c1.name)
print(c1.loc)
print(c1.display())


