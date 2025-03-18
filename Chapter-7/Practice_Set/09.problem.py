"""Write a program to print the following star pattern. 
* * * 
*   *    for n = 3 
* * *  """
n=3

for i in range(n):
    for j in range(n):
        if i==1 and j==1:
            print(" ",end="")
        else:
            print("*",end="")
    print() # This print() is used to print a newline   