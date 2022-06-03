# Inheritance in python.
# Multiple Inheritance:-

class Employee:
    company = "Google"
    ecode = 120

class Freelancer:
    Company = "Upwork" 
    level = 1

    def upgradeLevel(self):  
        self.level = self.level + 2

class Programmer(Employee, Freelancer): 
    name = "Deebya"    
    
p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)


        


