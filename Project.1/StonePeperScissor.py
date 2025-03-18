'''
stone 1
paper 0
scissor -1
'''
import random

computer = random.randint(-1, 1)
#computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice: ")
youstr = youstr.lower()

computerDict = {1: "stone", 0: "paper", -1: "scissor"}
print("Computer choice: ", computerDict[computer])

youDict = {"stone": 1, "paper": 0, "scissor": -1}


you = youDict[youstr]
print("result: ",end="")
if(you == computer):
    print("Draw")
elif(you == 1 and computer == -1):
    print("You Win")
elif(you == 0 and computer == 1):
    print("You Win")
elif(you == -1 and computer == 0):
    print("You Win")
else:
    print("You Lose")