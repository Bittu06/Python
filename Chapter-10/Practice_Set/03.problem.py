"""Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute?"""

class Demo:
    a = 10

o = Demo()
print(o.a) # print the class attribute because intance attribute is not defined
o.a = 0 # instance attribute is created 
print(o.a) # print the instance attribute beacuse it is defined
print(Demo.a)