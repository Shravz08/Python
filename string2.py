# name='Vaibhav'
# print(len(name))

# surname = "Patil"

# city= '''Pune'''

# str="""hii we are here to learn python"""

# print(name)

# print(surname)

# print(city)

# print(str)

# str1="This is vishal\"s device"
# print(str1)

# info="Wikipedia is hosted by the Wikimedia Foundation,\n a non-profit organization that also hosts a range of other projects.\n You can support our work with a donation."
# print(info)

# path= "C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"

# print(len(path))

# Given s = "Python", what is the output of s[0:3]?

# What does s[:4] return if s = "Programming"?

# For s = "Hello World", what is s[6:]?

# What does s[-1] return for s = "India"?

# What is the output of "abcdef"[1:5]?

# Given s = "Computer", what does s[-5:-1] return?

# What is the result of s[::2] for s = "ABCDEFGHIJ"?

# For s = "Developer", what is the output of s[::-1]?

# If s = "DataScience", what is s[2:8:2]?

# What does s[-8::3] produce for s = "Technology"?

# str="we are learning python here. python is easy language"

# str1="Hefshine Softwares" ----> Softwares Hefshine

# str2= "madam",   racecar

# print(str1.swapcase())

# print(sorted(str1))

# print(str1.isspace())

# print(str1.isalpha())

# print(str1.isalnum())

# print(str.split())

# print(str.count("is"))

# print(str.find("python"))

# print(str.capitalize())

# print(str.endswith("easy"))

# print(str.startswith("W"))

# print(str.replace("python", "java"))

# print(str.strip())

# print(len(str))

# print(str.upper())

# print(str.lower())

#1. 1. Create a string using single quote , double quotes and triple quotes and print it.
# 2. Count the number of occurrences of a specific character in a string.  
# str="All is well"
# ch="l"
# print(str.count(ch))

# 3. Write a program to count the number of words in a string.
# info= "Hii we are here to learn python"
# splt_str=info.split()
# print(splt_str)
# print(len(splt_str))


# 4. Write a program to check if a string contains only digits. 
# str= input("Enter the string: ")
# print(str.isdigit())

# 5. How can you sort the characters of a string alphabetically.
# str="Prajakta"
# sorted_str= sorted(str)
# final_str= "".join(sorted_str)
# print(final_str)

# 6. Write a program to find whether a given string is a palindrome.
# str=input("Enter the string: ")
# if str == str[::-1]:
#     print(f"{str} is palindrome")
# else:
#     print(f"{str} is not palindrome")    

# s ="My name is {} and I am {} years old".format(26,"Vishwas")
# print(s)

#7. Write a Python code to reverse the words in a sentence.
info= "Hii we are here to learn python"
splited_str = info.split()
reversed_lst= splited_str[::-1]
joined_str= " ".join(reversed_lst)
print(joined_str)

# 8. Accept comma separated sequence of words as input and
#     print the words in sorted form (alphanumerically) 
# Sample Words : orange, red, white, black, green  
# Expected Result : black, green, orange, red, white 
# str="orange,red,white,black,green"
# splited_words=str.split(",")
# sorted_words= sorted(splited_words)
# joined_words = ",".join(sorted_words)
# print(joined_words)

# 9. Write a program to swap comma and dot in a string.                 
# Sample string: "47,89,56.3"  
# # Expected Output: "47.89.56,3" 

# str= "47,89,56.3.67"  #input("Enter the string: ")
# str= str.replace(",", "@")    #47@89@56.3.67
# str=str.replace(".", ",")     #47@89@56,3,67
# str=str.replace("@", ".")     #47.89.56,3,67

# print(str)


# 1. Replace all occurrences of a substring with another substring.


# 2. Check if the string starts with a given prefix or ends with a given suffix.

# 3. Remove all whitespace from a string.
# str="   H   ii How   ar   e     you   "
# print(str.replace(" ", ""))

# 4. Read a string. Exchange first and last character of a string. Display it.
# str="hefshine softwares"
# print(str[-1]+str[1:-1] +str[0])  #string concatination


# name="sakshi"
# surname="patil"

# print(name*3)


# fullname= name + " " +surname
# print(fullname)


# 5. Write a program to remove all spaces from a string in Python.




# 6. Read a line from user. Print three strings using odd  indexed characters, 
# even indexed characters and every third character.
# line="Sarvesh is a very good guy."
# odd_indexed_str= line[1:len(line):2]
# print("Odd indexed string is : ",odd_indexed_str )

# even_indexed_str = line[0:len(line):2]
# print("Even indexed string is : ",even_indexed_str )

# every_third_ch= line[0:len(line):3]
# print("Every third indexed char string is : ", every_third_ch )


# 7. Write a Python program to check if a substring exists in a given string.
# str=input("Enter the string: ")
# substring= input("Enter the substring: ")

# if substring in str:
#     print(f"{substring} exists in {str}")
# else:
#     print(f"{substring} doesn't exists in {str}")    



# 8. Write a Python program to check if two strings are anagrams.
#      (contain  the same characters in a different order).
str1=input("Enter the string1: ")
str2=input("Enter the string2: ")

if sorted(str1) == sorted(str2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")    