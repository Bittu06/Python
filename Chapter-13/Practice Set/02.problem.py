""""
Write a program to input name, marks and phone number of a student and format it 
using the format function like below: 
“The name of the student is Harry, his marks are 72 and phone number is 99999888”
"""

name = input("Enter the name of the student: ")
marks = int(input("Enter the marks of the student: "))
phone_number = int(input("Enter the phone number of the student: "))

StudentDetails = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_number)
print(StudentDetails)