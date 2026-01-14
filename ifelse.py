
# Marks >= 90: Grade A

# Marks >= 80: Grade B

# Marks >= 70: Grade C

# Marks >= 60: Grade D

# Marks 60: Grade F

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
#     print("Fail")

# year = int(input("Entr the year:"))
# if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year ")
# else :
#     print(f"{year} is not a leap year")


# age =int(input("Enter your age:"))

# if (age >= 18 ):
#     print("You are eligible to give a vote ")
# else :
#     print("You are not eligible to give a vote.")


num1= int(input("Enter the number 1:"))
num2= int(input("Enter the number 2:"))
operator=input("Enter the opertaor between(+,-,*,/):")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Enter the valid operator") 