# Inheritance in python.
# Single Inheritance:-

class Employee:
    company = "Google"
    def showDetails(self):  
        print("This is an Employee")

class Programmer(Employee):
    language = "python" 
    #company = "Youtube" 
    def showDetails(self):  
        print(f"The language is {self.language}")

    def showDetails(self):  
        print("This is a programmer")    
    
e = Employee()   
e.showDetails() 

p = Programmer()
p.showDetails()
print(p.company)


        


