# # 1.	Write a program to check if a given number is even or odd.
# num = int(input("Enter a number:"))
 
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 2. Write a program to check if a number is positive, negative, or zero. 
# num=int(input("Enter the number:"))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# 3.	Write a program to determine the grade of a student based on their marks. 
#              Marks >= 90: Grade A 
#              Marks >= 80: Grade B 
#              Marks >= 70: Grade C 
#              Marks >= 60: Grade D 
#              Marks < 60: Grade F

# marks=int(input("Enter the Marks:"))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 80:
#     print("Grade B")
# elif marks >= 70:
#     print("Grade C")
# elif marks >= 60:
#     print("Grade D")
# else :
#     print("Grade F")

# 4.	Write a program to find the maximum of three numbers.
# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# num3 = int(input("Enter the num3: "))

# if num1 > num2 and num1 >num3:
#     print("Max num1",num1)
# elif num2 > num1 and num2 > num3:
#     print("Max num2",num2)
# else:
#     print("MAx num3",num3)

# 5.	Write a program to check if a given year is a leap year. 
# Rules: 
# A year is a leap year if it is divisible by 4 but not divisible by 100 unless  it is divisible by 400. 
# Input: A single integer for the year. 
# Output: "Leap Year" or "Not a Leap Year". 

# year = int(input("Entr the year:"))
# if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year ")
# else :
#     print(f"{year} is not a leap year")

# 6.	Write a program to check if a person is eligible to vote.

# age =int(input("Enter your age:"))

# if (age >= 18 ):
#     print("You are eligible to give a vote ")
# else :
#     print("You are not eligible to give a vote.")

# 7.	Write a program that acts as a simple calculator. It should ask the user for two numbers and an operator (+, -, *, /) and perform the corresponding operation. 
# Input: Two integers and a mathematical operator.

# num1= int(input("Enter the number 1:"))
# num2= int(input("Enter the number 2:"))
# operator=input("Enter the opertaor between(+,-,*,/):")

# if operator == "+":
#     print(num1+num2)
# elif operator == "-":
#     print(num1-num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     print(num1/num2)
# else:
#     print("Enter the valid operator") 

# 8.	A student will not be allowed to attend the exam if his/her attendance
#  is less than 75%. Take following input from user – 
#    Number of classes held  
#    Number of classes attended  
#    And print on the percentage of class attended Is student is allowed 
#    to attend the exam or not.
# held = int(input("Classes held: "))
# attended = int(input("Classes attended: "))

# percentage = (attended / held) * 100
# print("Attendance =", percentage)

# if percentage >= 75:
#     print("Allowed to attend exam")
# else:
#     print("Not allowed to attend exam")

# 9.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
# salary = float(input("Enter salary: "))
# years = int(input("Enter years of service: "))

# if years > 5:
#     bonus = salary * 0.05
#     print("Bonus =", bonus)
# else:
#     print("No bonus")

# 10. Write a program to determine the type of triangle based on the lengths of its three sides. 
# 	All sides equal: "Equilateral" 
# 	Two sides equal: "Isosceles" 
# 	All sides different: "Scalene" 
# a = int(input("Side 1: "))
# b = int(input("Side 2: "))
# c = int(input("Side 3: "))

# if a == b == c:
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# else:
#     print("Scalene")

# Assignments For Students
# 1.Write a program to check if a number is within the range [10, 50].
# num= int(input("Enter the number:"))
# if 10 <= num <= 50:
#     print("Within range")
# else:
#     print("Out of Range")

# 2.Write a program to check if a number is divisible by both 3 and 5.
# num=int(input("Enter the number:"))
# if num % 3 ==0 and num % 5 == 0:
#     print("number is divisible by both 3 and 5")
# else:
#     print("Not divisible by both")

# 3.Write a program to validate a password. The program should check if the password meets the following conditions: 
# At least 8 characters long. 
# Contains both uppercase and lowercase letters.  
# Contains at least one digit. 
# Input: A string for the password. 
# Output: "Valid Password" or "Invalid Password". 
# password = input("Enter the password:")

# if(len(password) >= 8 and any(c.isupper() for c in password)) and ((c.islower() for c in password ) and (c.isdigit() for c in password)):
#    print("Valid pass")
# else:
#    print("Invalid")

# 4.Write a program to print "Fizz" if a number is divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both 3 and 5. Otherwise, print the number itself. 
# Input: A single integer.  
# Output: Fizz, Buzz, FizzBuzz, or the number.
# num=int(input("Enter the number:"))
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz") 
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# 5.Write a code that takes the temperature in Celsius as input and prints out what you should wear:
# •	Below 0°C: "Wear a heavy jacket!"
# •	0°C to 15°C: "Wear a jacket!"
# •	16°C to 25°C: "Wear a t-shirt!"
# •	Above 25°C: "Wear something light!"

# temp = float(input("Enter the Temperature in celcius: "))

# if temp < 0:
#     print("Wear a heavy jacket!")
# elif temp <= 15:
#     print("Wear a jacket!")
# elif temp <= 25:
#     print("Wear a t-shirt!")
# else:
#     print("Wear something light!")

# 6.A shop gives a discount of 10% if the cost of purchased quantity is  more than $1000. 
# Take appropriate inputs and print total cost for user. 
# qty = int(input("Enter quantity: "))
# price= float(input("Enter price per item: "))

# total = qty * price
# if total > 1000:
#     total -= total * 0.10
# print("Total cost =",total)

# 7.Write a Python function that calculates the total price of items in a shopping cart and applies a discount based on the total price:
# If the total is greater than $500, apply a 15% discount.
# If the total is between $200 and $500, apply a 10% discount.
# If the total is less than $200, apply no discount.

total = float(input("Enter total cart price: "))

if total > 500:
    total -= total * 0.15
elif total >= 200:
    total -= total * 0.10

print("Final price =", total)

