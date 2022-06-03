# Example file for using class methods in python.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):  
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves    
    
Deebya = Employee("Deebya", 500, "Manager" )
Deepika = Employee("Deepika", 900, "CEO" )

Deebya.change_leaves(25)
 
print(Deepika.no_of_leaves)


        


