# Bundling of data in a single entity
# This helps protect the integrity of data,
# prevents accidental modification,
# promotes modular programming

# features 
# data hiding -- pvt and protected
# Access thr method -- geeter and setter
# Cotrol and Security

# Eg. Bank class , banmk balance is private and withdraw and deposit methods are public to make changes in the balance
# 
# public -- access anywhere
# protected -- access within the class and subclass
# private -- can not access directly (we need to access using methods)
# super() -- to access the methods and constructor from parent class to child
# getter() method
# setter() method


# public attributes
# class Person:
#     def __init__(self,name):
#         self.name= name


#     def display(self):
#         return self.name
    
# p1 = Person("Raj")
# print(p1.name)
# print(p1.display())

# protected attributes
class Employee:
    def __init__(self,disignation):
        self.disination= disignation

class Manager(Employee):
    def display(self):
        return self.disination
mn1 = Manager("Senoir")
print(mn1.disination)
print(mn1.display())