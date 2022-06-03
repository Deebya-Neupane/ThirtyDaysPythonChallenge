# Example file for working with files.

def main():
    # Open file for writing and create it if it doesn't exist.
    f = open("textfile.txt", "w+")

    # Open the file for appending text to the end.
    #f = open("textfile.txt", "r") 


    # Write some lines of data to the file.
    for i in range(5):
      f.write("This is line " + str(i) + "\n") 

    # Close the file when done.    
    f.close() 

    # Open the  file back up and read the contents.
    '''if f.mode == 'r':
       # contents = f.read() 
        #print(contents)
        fl = f.readlines()
        for x in fl:
          print(x)'''

if __name__=="__main__":
    main()        