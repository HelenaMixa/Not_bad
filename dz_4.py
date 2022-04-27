# Python program to demonstrate use of staticmethod и classmethod
from datetime import date


class StaticMethod:
    "Emulate StaticMethod"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f

    def __call__(self, *args, **kwds):
        return self.f(*args, **kwds)


class ClassMethod:
    "Emulate classmethod"

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)

        def new_func(*args):
            return self.func(cls, *args)
        return new_func


class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# a static method to check if a Member is adult or not.
    @staticmethod
    def isadult(age):
        return age > 18
    
    @StaticMethod
    def my_isadult(age):
        return age > 18

# a class method to create a Member object by birth year
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display (self):
        print(self.name +"'s age is " + str(self.age))

    @ClassMethod
    def my_from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

  
class Dancer(Member):
    pass

if __name__ == '__main__':

# test StaticMethod
# print the result
    print (Member.isadult(19))
    print (Member.my_isadult(19))

#test ClassMethod
# print the result
    person = Member('Adam', 19)
    person.display() 
    
    person1 = Member.from_birth_year('John', 1985) 
    person1.display() 
    person2 = Member.my_from_birth_year('John', 1985) 
    person2.display() 

    person3 = Dancer.from_birth_year('Manya', 1995) 
    person3.display() 
    person4 = Dancer.my_from_birth_year('Manya', 1995) 
    person4.display() 
    
