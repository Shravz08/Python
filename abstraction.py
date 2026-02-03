# 12/01/2026
#abc --- module ---- provides tools to create abc
#ABC --- functionality ---- 
#Abstract class in which one or more abstarct methods
#Abstract method is method without implementation
#Concrete method is an abstract class with complete implementation

# from abc import ABC,abstractmethod
# class Animal():            # abstrat class
   
#    @abstractmethod
#    def movement(self):     # abstarct method
#       pass
   
#    @abstractmethod      
#    def speak(self):      #  abstarct method
#       pass
   
# class Dog(Animal):         # 
#    def movement(self):   
#       return "Running...!"
   
#    def speak(self):
#       return "Barkkk...!"
   
# class Fish(Animal):
#    def movement(self):
#       return "Swimming...!"
   
#    def speak(self):
#       return "Bulb...!"

# # a = Animal()                  # we can not craete an object of abstract class
# # Print(a.movement())
   
# dog1= Dog()                   # object - of subclass to access the abstract  methods
# print(dog1.movement())
# print(dog1.speak())

# fish1= Fish()
# print(fish1.movement())
# print(fish1.speak())


# 1 
# from abc import ABC,abstractmethod
# class A:
#     @abstractmethod
#     def a_func(self):
#         pass
# class B(A):
#     def a_func(self):
#         return "This is from abstracted class"
# obj = B()
# print(obj.a_func())

# 2 
# from abc import ABC,abstractmethod
# class withImp:
#     @abstractmethod
#     def withoutimp(self):      # abstract method
#         pass

#     def widimp(self):                  # concrete method 
#         return "From Abstract class"

# class new(withImp):
#     def withoutimp(self):
#         return "This is the inherated part of code"
    
# o = new()
# print(o.withoutimp())
# print(o.widimp())

#3
# from abc import ABC,abstractmethod 
# class Vehicle:
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         return "This is the starting of a code..."
    
#     def stop(self):
#         return "This is the part to stop part"
    
# car1 = Car()
# print(car1.start())
# print(car1.stop())

# # 4 
# from abc import ABC,abstractmethod 
# class shape:
#     @abstractmethod
#     def draw(self,color,size):
#         pass

# class circle(shape):
#     def draw(self, color, size):
#         self.color = color
#         self.size = size
#         return f"The color of the circle is {self.color} and size is {self.size}"
    
# c1 = circle()
# print(c1.draw("Red",5))


#  5.Write a Python program to calculate the area of different shapes using abstraction.
# What to do:
# 1.	Create an abstract class called Shape with a method area().
# 2.	Make two classes that inherit from Shape:
# o	Circle: takes a radius and calculates area using 3.14 * radius * radius.
# o	Square: takes a side length and calculates area using side * side.
# 3.	Create one object of each class and print their areas
# from abc import ABC,abstractmethod 
# class shape:
#     @abstractmethod
#     def area(self,a):
#         pass

# class Circle(shape):
#     def area(self,a):
#         self.a = a
#         return 3.14 * a * a
    
# class square(shape):
#     def area(self,a):
#         self.a = a
#         return a * a
    
# ob= Circle()
# sq = square()
# print(ob.area(4))
# print(sq.area(4))

# 6. Write an abstract class Employee with abstract method calculate_salary().
# Create subclasses FullTimeEmployeeandPartTimeEmployee that implement salary calculation differently.
# from abc import ABC,abstractmethod 
# class Employee:
#     @abstractmethod
#     def calculate_salary(self,a):
#         pass

# class fullTimeEmp(Employee):

#     def calculate_salary(self,a):
#         self.salary = a
#         return self.salary
    
# class partTimeEmp(Employee):

#     def calculate_salary(self,a):
#         self.hrWorked = a
#         return self.hrWorked * 1000
    
# em1 = fullTimeEmp()
# print("Employee's Salary:",em1.calculate_salary(50000))
# em2 = partTimeEmp()
# print("Part time employee's salary",em2.calculate_salary(28))

# 7. Create an abstract class BankAccount with methods deposit() and withdraw().
# Implement it in SavingsAccount and CurrentAccount with different withdrawal rules.
# from abc import ABC,abstractmethod 
# class BankAccount(ABC):
#     def __init__(self):
#         self.balance = 20000

#     @abstractmethod
#     def deposit(self,amount):
#         pass

#     @abstractmethod
#     def withdraw(self,amount):
#         pass

# class SavingsAcc(BankAccount):
#     # def __init__(self):
#     #     self.balance = 20000

#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += self.amount
#         return "Deposit Successfull"
    
#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount <= self.balance:
#             self.balance -= self.amount
#             return "Withdrawing Successfull"
#         else:
#             return "Insufficient balance"
        
# class CurrentAccount(BankAccount):

#     def __init__(self):
#         self.balance = 50000   

#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += amount
#         return "Deposit Successful"

#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount <= self.balance:
#             self.balance -= self.amount
#             return "Withdrawal Successful"
#         elif (self.balance+5000) <= self.amount:
#             self.balance -= self.amount
#             return "Withdrawal successful...."
#         else:
#             return "Insufficient balance"
# print("Savings acc---------")
# b1 = SavingsAcc()
# print(b1.deposit(3000))
# print(b1.withdraw(2000))
# print("Current acc---------")
# c = CurrentAccount()
# print(c.deposit(10000))
# print(c.withdraw(65000))
# print("Current Balance:", c.balance)

#--------------------------------------------------------------------------------------------------------
## 7. Create an abstract class BankAccount with methods deposit() and withdraw().
# Implement it in SavingsAccount and CurrentAccount with different withdrawal rules.
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.balance=balance
    
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdrwal(self):
        pass
    
    
class SavingsAccount(BankAccount):
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        
        return (f"depoited {self.balance} in your account")
        
    def withdrwal(self,amount):
        self.amount=amount
        if self.amount<self.balance:
            self.balance-=self.amount
            return (f"debited amount is{self.balance}")
        else:
            return ("insufficent balance")
    
class CurrentAccount(BankAccount):
    def withdrwal(self,amount):
        overdraft=5000
        self.amount=amount
        if self.amount+overdraft>= self.balance:
            self.balance-=amount
            return(f"money withdraw succesful remaining balance is{self.balance}")
        else:
             return("insufficient Balance")
            
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return (f"deposit{self.amount} in your account")
        
        
saving=SavingsAccount(100000)
print(saving.deposit(6900))
print(saving.withdrwal(500))

curr=CurrentAccount(100000)
print(curr.deposit(7000))
print(curr.withdrwal(112000))

# 8.Create an abstract class Database with methods connect(), disconnect(), and execute_query(query).
# Implement it for MySQLDatabase and MongoDBDatabase.
# from abc import ABC, abstractmethod
# class Database(ABC):

#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def disconnect(self):
#         pass

#     @abstractmethod
#     def execute_query(self, query):
#         pass

# class MySQLDatabase(Database):

#     def connect(self):
#         print("Connected to MySQL...")

#     def disconnect(self):
#         print("Disconnected...")

#     def execute_query(self, query):
#         self.query = query
#         print(f"MySQL executing query: {self.query}")

# class MongoDBDatabase(Database):

#     def connect(self):
#         print("Connected to MongoDB...")

#     def disconnect(self):
#         print("Disconnected from MongoDB...")

#     def execute_query(self, query):
#         self.query = query
#         print(f"MongoDB executing query: {self.query}")

# db1 = MySQLDatabase()
# db1.connect()
# db1.disconnect()
# db1.execute_query("SELECT * FROM users")

# print("-------------------")

# db2 = MongoDBDatabase() 
# db2.connect()
# db2.disconnect()
# db2.execute_query("{ find: 'users' }")
