# var in object is know as attribute
# func as methods
# __init__ method to initialise to attribute 

# 1. Write a Python program to create a class Person with the attributes name and age. 
# Instantiate an object of the class and print the attributes.
# class Person:

#   def __init__(self,name,age):
#     self.name= name
#     self.age = age

# p1 = Person("Ram",21)
# print(p1.name)
# print(p1.age)

# 2. Write a Python class Car with attributes make and model. 
# Add a method display_info() that prints the car’s make and model.
#  Create an instance and call this method.
# class Car:
#   def __init__(self,make,model):
#     self.make = make
#     self.model = model

#   def display_info(self): 
#       return f"Make of the car is {self.make} and model of the car is {self.model}"

# c1 = Car("BMW","M5")
# c2 = Car("TATA","XUV700")

# print(c1.display_info())
# print(c2.display_info())

# 3. Write a Python program that defines a class Person with a constructor that initializes role and salary. 
# Instantiate an object and print the values of role and salary.  
# class Person:
#   def __init__(self,role,salary):
#     self.role= role 
#     self.salary= salary
    
# p1 = Person("HOD",23000)
# print(p1.role)
# print(p1.salary)


# 4. Write a Python class Book with a default constructor.
# If no arguments are provided, set title and author to default values ("Unknown" and "Unknown").
# class Book:
#   def __init__(self,title = "Unknown",author = "Unknown"):
#     self.title = title
#     self.author=author

# b1 = Book()
# print(b1.title)

# 5. Write a Python program that creates a Rectangle class with a constructor that takes width and height as arguments.
#  The constructor should initialize these attributes and calculate the area. 
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height= height
#         self.area = width*height
    
# r1 = Rectangle(3,4)
# print(r1.area)


# 6. Define a simple Person class with a destructor __del__(). 
# Print a message when an object of the Person class is deleted.
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"Person {self.name} is created")

#     def __del__(self):
#         print(f"Person {self.name} is deleted")


# 7. Write a Python program that defines a Car class with two constructors: 
# one for setting make and model, and another for setting make, model, and year.
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
  

# 8. Write a Python program that defines a Person class with a constructor that takes age as an argument.
#  If the age is less than 18, assign the person to a "minor" group;
#  otherwise, assign them to an "adult" group.
class Person:
    def __init__(self, age):
        self.age = age
        if age < 18:
            self.group = "minor"
        else:
            self.group = "adult"

    def display_info(self):
        print(f"Age: {self.age}, Group: {self.group}")

p1 = Person(23)
p1.display_info()
