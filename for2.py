# 1. Write a Python program that uses a while loop to print the numbers from 10 to 1 in descending order.
# num = 10
# while num >= 1:
#     print(num)
#     num -= 1

# 2. Write a Python program that calculates the sum of all the numbers in a list using   a for loop.
# lst = [1, 2, 3, 4, 5]
# total = 0
# for num in lst:
#     total += num

# print(total)

# 3. Write a Python program that counts the number of digits in a given number using a while loop.
# num = int(input("Enter a number: "))
# count = 0

# while num != 0:
#     num //= 10
#     count += 1

# print("Number of digits:", count)

# 4. Write a Python program that takes an integer as input and uses a while loop to reverse the digits of that number.  
# num = int(input("Enter a number: "))
# reverse = 0

# while num != 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10

# print("Reversed number:", reverse)
 
# 5. Write a Python program that calculates the sum of digits of a given number using a while loop.
# num = int(input("Enter a number: "))
# total = 0

# while num != 0:
#     digit = num % 10
#     total += digit
#     num //= 10

# print("Sum of digits:", total)

# 6. Write a Python program that calculates the power of a number x raised to n (i.e., x^n) using a while loop.
# x = int(input("Enter base: "))
# n = int(input("Enter power: "))

# result = 1
# i = 1

# while i <= n:
#     result *= x
#     i += 1

# print("Result:", result)

# 7. Write a Python program that finds the common elements between two lists using a for loop.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common = []
# for item in list1:
#     if item in list2:
#         common.append(item)

# print("Common elements:", common)

# 9. Write a Python program that generates and prints the first 10 multiples of 5 using a while loop.
# i = 1
# while i <= 10:
#     print(5 * i)
#     i += 1

# 10. Write a Python program that uses a for loop to find all anagrams of a given word from a list of words. An anagram is a word that can be formed by rearranging the letters of another word.


#1. Write a Python program to print the numbers from 1 to 10 using while loop.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# 2. Write a Python program that takes a number 100 as input and calculates the sum of all integers from 1 to 100 using a while loop.
# total = 0
# i = 1

# while i <= 100:
#     total += i
#     i += 1

# print("Sum:", total)

# 3. Write a Python program that calculates the factorial of a number N using a while loop.
# N = int(input("Enter a number: "))
# fact = 1

# while N > 0:
#     fact *= N
#     N -= 1

# print("Factorial:", fact)

# 4. Write a Python program that uses a for loop to print all even numbers from 1 to 100.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# 5. WAP to Separate and store even and odd element into two different lists.
# numbers = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even list:", even)
# print("Odd list:", odd)

# 6. WAP to Separate and store vowels  and consonants element into two different lists.
# string = "PythonProgramming"
# vowels = []
# consonants = []

# for ch in string.lower():
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowels.append(ch)
#         else:
#             consonants.append(ch)

# print("Vowels:", vowels)
# print("Consonants:", consonants)

# 7. Write a Python program that uses a for loop to print the multiplication table for a given number N.
# N = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(N, "x", i, "=", N * i)

# 8. Write a Python program that uses a for loop to count how many times a specific character appears in a string.
# string = "programming"
# char = 'g'
# count = 0

# for ch in string:
#     if ch == char:
#         count += 1

# print("Count:", count)

# 9. Write a Python program that uses a for loop to count how many vowels (a, e, i, o, u) appear in a given string (case-insensitive).
# string = "Hello World"
# count = 0

# for ch in string.lower():
#     if ch in "aeiouAEIOU":
#         count += 1

# print("Number of vowels:", count)

# 10.Write a Python program to find the sum of all values in a dictionary (assuming all values are numeric).
my_dict = {'a': 10, 'b': 20, 'c': 30}
total = 0

for value in my_dict.values():
    total += value

print("Sum of values:", total)


