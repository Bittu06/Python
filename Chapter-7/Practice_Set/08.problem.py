"""Write a program to print the following star pattern: 
* 
** 
***      for n = 3 """

n = 3

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()