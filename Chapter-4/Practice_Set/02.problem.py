# Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

for i in range(6):
    marks.append(int(input(f"Enter the mark of student {i+1}: ")))
marks.sort()

print("The marks of students are:", marks)
\