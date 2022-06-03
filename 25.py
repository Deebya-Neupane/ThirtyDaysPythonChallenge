# Inheritance in python.
# Multi-level Inheritance:-

class Father:
    Country = "Nepal"
    def showDetails(self):
        print("I am a father.") 

class Son(Father):
    Nationality = "Nepali" 

    def careFather(self):
        print(f"I take care of my{self.father}")

    def showDetails(self):
        print("I am a son.") 

class Grandson(Son): 
    Nationality = "American"   

    def careFather(self):
        print(f"I can't take care of my father as I am far away from him.")

    def showDetails(self):
        print("I am a Grandson.")     
    
f = Father()
f.showDetails()
#print(f.Nationality) # throws an error.

s = Son()
s.showDetails()
print(s.Nationality)

g = Grandson()
g.showDetails()
print(g.Nationality)
print(s.Country)



        


