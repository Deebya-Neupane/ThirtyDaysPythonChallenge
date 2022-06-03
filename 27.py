# Decorators in Python(A decorator in Python is a function that 
# takes another function as its argument, and returns yet another function .)

'''def function1():
    print("Stay safe everyone.")

func2 = function1
del function1
func2()    

def executor(func):
    func("Hello")
executor(print)    '''

def dec1(func1):
    def nowexec():
        print("Now Executing")
        func1()
        print("Executed")
    return nowexec    

@dec1
def How_is_life():
    print("Life is beautiful.")        
  
#How_is_life = dec1(How_is_life) 
How_is_life()

