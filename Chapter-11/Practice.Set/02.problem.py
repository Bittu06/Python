#   Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    # Regular instance method - requires self
    def regular_method(self):
        print(f"This dog is barking")
    
    # Static method - doesn't require self or cls
    @staticmethod
    def bark():
        print("Barking...")

    # Class method - requires cls
    @classmethod
    def make_sound(cls):
        print(f"A {cls.__name__} is making sound")


d = Dog()
d.regular_method()
d.bark()
d.make_sound()