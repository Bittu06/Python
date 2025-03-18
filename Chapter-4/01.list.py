#Python lists are containers to store a set of values of any data type. 

students_1 = ['Bittu', 25, 'CSE', 1180, False]

print(students_1[3]) # Output: 1180

students_1[0]='Rahul'

print(students_1) # Output: ['Rahul', 25, 'CSE', 1180, False]
#The list is mutable, which means you can change the values of the list.

print(students_1[0:2])

students_1.append('Bittu')
print(students_1) # Output: ['Rahul', 25, 'CSE', 1180, False, 'Bittu']
#The append() method adds an element to the end of the list.

list_1 = [61, 32, 23]
list_1.sort()
print(list_1) # Output: [23, 32, 61]
#The sort() method sorts the list in ascending order.

list_1.reverse()
print(list_1) # Output: [61, 32, 23]
#The reverse() method reverses the list.

list_2 = [53,83,23]
list_2.insert(1, 45)
print(list_2) # Output: [53, 45, 83, 23]
#The insert() method inserts an element at the specified index. 

list_2.remove(45)
print(list_2) # Output: [53, 83, 23]
#The remove() method removes the first occurrence of the specified element.

print(list_2.pop(1)) # it will pop the element at index 1
print(list_2) # Output: [53, 23]
#The pop() method removes the element at the specified index.

