# Operator overloading.

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")  
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's multiply")  
        return self.num * num2.num

    def __truediv__(self, num2):
        print("Let's divide")  
        return self.num / num2.num    

n1 = Number(12)
n2 = Number(6)
sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)
div = n1 / n2
print(div)

        


