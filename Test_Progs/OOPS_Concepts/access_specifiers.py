#Access Specifiers---------------
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self._rollno=rollno

    def display(self):
        print(f'name is {self.name} and rollno is {self._rollno}')

obj=Student("Raj",121)
print(obj.name)
print(obj._rollno)
obj.display()

# #Protected--------------------------------------------------
