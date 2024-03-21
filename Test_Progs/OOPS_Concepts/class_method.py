# # class method
class Employee:
    Company="INFY"
    def __init__(self,name,age,loc):
        self.name=name
        self.age=age
        self.loc=loc

    def meth1(self0):
        print(f"name is {self0.name} and age is {self0.age} and location is {self0.loc}")

    @classmethod
    def get_company(cls):
        print("Company name is:",cls.Company)

obj=Employee("Rahul",21,"Pune")
obj.meth1()
obj.get_company()
Employee.get_company()