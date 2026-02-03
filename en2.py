# # public attributes
# # class Person:
# #     def __init__(self,name):
# #         self.name= name


# #     def display(self):
# #         return self.name
    
# # p1 = Person("Raj")
# # print(p1.name)
# # print(p1.display())

# # protected attributes
# # class Employee:
# #     def __init__(self,disignation):
# #         self._disination= disignation

# # class Manager(Employee):
# #     def display(self):
# #         return self._disination
# # mn1 = Manager("Senoir")
# # print(mn1._disination)
# # print(mn1.display())


# # private attributres
# # class Bank:
# #     def __init__(self,balance):
# #         self.__balance= balance

# #     def check_balance(self):
# #         return self.__balance

# #     def deposit(self,amount):
# #         self.amount= amount
# #         self.__balance += self.amount
# #         return f"modifid balance is : {self.__balance}"

# # b1 = Bank(10000)
# # print(b1.check_balance())
# # print(b1.deposit(5000))

# 1.Write a Python class Car with a public attribute brand and a public method get_brand().
#   Create an object of Car and access the attribute and method directly from outside the class.
# class Car:
#     def __init__(self,brand):
#         self.brand = brand

#     def get_brand(self):
#         return self.brand
    
# car1 = Car("BMW")
# print(car1.brand)
# print(car1.get_brand())

# 2. Create a class Person with a protected attribute age. 
# Create a subclass Student that accesses the protected attribute age of the parent class.
# class Person:
#     def __init__(self,age):
#         self._age= age

# class Student(Person):
#       def __init__(self,name,age):
#           self.name = name
#           super().__init__(age)
#       def info(self):
#         return f"Age of the {self.name} is {self._age}"
    
# stud1 = Student("Radha",23)
# print(stud1._age)
# print(stud1.name)
# print(stud1.info())

# 3. Write a Python class Account with a private attribute balance and a method deposit() that modifies the balance. 
# Show how a private attribute is not directly accessible from outside the class.
# class Account:
#     def __init__(self,balance):
#         self.__balance = balance

#     def deposit(self,amount):
#         if amount >0:
#           total_bal =  self.__balance + amount
#           return f"Deposit successfull... \nCurrent balance:{total_bal}"
#         else:
#             print("Deposit valid amount")

#     def show_bal(self):
#         return f"Initial balance is {self.__balance}"
    
# acc1 = Account(10000)
# # print(acc1.__balance)
# print(acc1.deposit(5000))
# print(acc1.show_bal())

# 4. Write a Python class Student with a private attribute age. 
# Create getter and setter methods to access and modify the age attribute.
# class Student:
#     def __init__(self,age):
#         self.__age= age 
    
#     def get_age(self):
#         return f"Age of student :{self.__age}"
    
#     def set_age(self,newAge):
#         if newAge > 0 :
#            newAge += self.__age 
#            return f"Updated age of student is {newAge}"
#         else:
#             return "Add valid age"

# s1 = Student(21)
# print(s1.get_age())
# print(s1.set_age(3))

# # 5. Use property decorators in Python to implement getter and setter methods for a private attribute radius.
#  Create a method to calculate the area of a circle using radius.
class Circle:
    def __init__(self,radius):
        self.__radius = radius

    def get_rad(self):
        return f"Current Radius of the circle is {self.__radius}"
    
    def set_rad(self,rad):
        self.rad = rad
        self.__radius = self.rad
        return f"Updated radius is : {self.__radius}"

    def calArea(self):
        self.Area = 3.14 * self.__radius *self.__radius
        return f"Area of a circle is {self.Area}"
    
c1 = Circle(5)
print(c1.get_rad())
print(c1.calArea())
print(c1.set_rad(7))
print(c1.calArea())
