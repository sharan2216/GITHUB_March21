# #Access Specifiers---------------
# class Student:
#     def __init__(self,name,rollno):
#         self.name=name
#         self._rollno=rollno
#
#     def display(self):
#         print(f'name is {self.name} and rollno is {self._rollno}')
#
# obj=Student("Raj",121)
# print(obj.name)
# print(obj._rollno)
# obj.display()

# #Protected--------------------------------------------------
# using public function showdata also we can access protected memebers outside the class ,
# so nothing is protected in python-------------
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self._rollno=rollno
    def display(self):
        print(f'name is {self.name} ans roll no is {self._rollno}')

class Parents(Student):
    pass

p1 = Parents("Roy", 111)
print(p1.name)
print(p1._rollno)
p1.display()

def showdata():
    p2= Parents("Roy", 111)
    print(p2.name)
    print(p2._rollno)
    p2.display()

showdata()