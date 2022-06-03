# Example file for working with loops.

def main():
    x = 0

    # define a while loop.
    while (x<5):
      print(x)
      x= x+1    
    
    # define a for loop.
    for x in  range(10,15):
        print(x)

    # use a for loop over a collection.
    days = ["sun","Mon","Tue","Wed","Thurs","Fri","Sat"]
    for d in days:
        print(d)

    # Use the break & continue statements.
    for x in range(5,10):
        #if(x==7): break
        if(x%2==0):continue
        print(x)

    # Using the enumerate() function to get index.
    days = ["Mon","Tue","Wed","Thurs","Fri","Sat"]
    for i,d in enumerate(days):
            print(i,d)     

if __name__=="__main__":
 main()