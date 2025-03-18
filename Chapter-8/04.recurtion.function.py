def fectorial(num):
        if num==1 or  num==0:
            return 1
        else:
            return num*fectorial(num-1)
        

N = int(input("Enter the number:"))

print(f"The factorial of {N} is {fectorial(N)}")