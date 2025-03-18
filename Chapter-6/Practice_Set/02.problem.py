"""Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user."""

Bittu ={
    "maths": 0,
    "science": 0,
    "english": 0
}

Bittu["maths"] = int(input("Enter your maths marks: "))
Bittu["science"] = int(input("Enter your science marks: "))
Bittu["english"] = int(input("Enter your english marks: "))

total = Bittu["maths"] + Bittu["science"] + Bittu["english"]
percentage = (total / 300) * 100

if(Bittu["maths"] >= 33 and Bittu["science"]>=33 and Bittu["english"]>=33 and percentage>=40):
    print("Congratulations! You have passed.")

else:
    print("Sorry! You have failed.")

    