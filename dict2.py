# # Classroom Questions
# Student={
#     "name":"Ram",
#     "age":19,
#     "course":"data science",
#     "City":"Pune",
#     "mob_no":354769809,
#     "CGPA":87.12,
#     "Hobbies":["Cooking", "Dancing","Reading"]
# }
# # 1. Write a program to iterate through a dictionary and print all keys.
# print(Student.keys())

# # 2. Write a program to iterate through a dictionary and print all values.
# print(Student.values())

# # 3. Write a program to add a new key-value pair to an existing dictionary.
# Student.update({"name":"Radha"})

# # 4. Write a Python function that takes a dictionary and a key, and returns the value if the key exists, else "Key not found".
# def get_value(Student,key):
#     return Student.get(key,"Key not found")
# print(get_value(Student,"course"))
# print(get_value(Student,"address"))

# # 5. Write a program to remove the "city" key from the dictionary person = {"name": "John", "age": 25, "city": "New York"} and print the resulting dictionary.
# person={
#     "name":"John",
#     "age":25,
#     "city":"New York"
# }
# person.pop("city")
# print(person)

# #  6. Write a Python program that inverts a dictionary fruit_prices = { "apple": 50,"banana": 20,"orange": 30,"mango": 60,"grapes": 40} i.e., swaps keys with values.
# fruit_prices = {
#     "apple": 50,
#     "banana": 20,
#     "orange": 30,
#     "mango": 60,
#     "grapes": 40
# }
# inverted={value:key for key, value in fruit_prices.items()}
# print(inverted)

# # 7. Write a program that updates a dictionary student_marks = {"Alice": 85, "Bob": 72, "Charlie": 90,"David": 65,"Eva": 78} with another dictionary 
# # students = {
# #     "Alice": {"Math": 85, "Science": 90},
# #     "Bob": {"Math": 70, "Science": 80},
# #     "Charlie": {"Math": 95, "Science": 88}
# # }
# student_marks = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 78}
# students = {
#      "Alice": {"Math": 85, "Science": 90},
#      "Bob": {"Math": 70, "Science": 80},
#      "Charlie": {"Math": 95, "Science": 88}
#  }
# student_marks.update(students)
# print(student_marks)

# # 8. Write a program that merges two dictionaries dict1 = {"name": "John", "age": 25} and dict2 = {"city": "New York", "country": "USA"}.
# dict1 = {"name": "John", "age": 25}
# dict2 = {"city": "New York", "country": "USA"}

# dict = {**dict1, **dict2}
# print(dict)

# Assignments For students
# 1. Write a program that iterates through the dictionary person = {"name": "John", "age": 25, "city": "New York"} and prints both the keys and values.
# person = {"name": "John", "age": 25, "city": "New York"}
# for key, value in person.items():
#     print(key, ":", value)

# # 2. Write a Python program that finds the key with the maximum value in a dictionary.
# diction={"a":12,"b":68,"c":31}
# max_key=max(diction , key=diction.get)
# print(max_key)

# # 3. Write a program that creates a dictionary from a list of numbers, where the keys are the numbers, and the values are their squares.
# num=[1,2,3,4,5]
# sq_dict={num : num**2 for num in num}
# print(sq_dict)

# # 4. Write a Python program that inverts a dictionary, i.e., swaps keys with values.
# dicti={"a":1, "b": 2 , "c": 3}
# inverted = {v:k for k , v in dicti.items()}
# print(inverted)

# # 5. fruit_prices = {"apple": 50, "banana": 20, "orange": 30, "mango": 60, "grapes": 40}
# fruit_prices = {"apple": 50, "banana": 20, "orange": 30, "mango": 60, "grapes": 40}

# # 1. Add a new fruit "pineapple": 70 to the dictionary.
# fruit_prices["pineapple"] = 70

# # 2. Update the price of "banana" to 25.
# fruit_prices["banana"] = 25

# # 3. Remove "orange" from the dictionary.
# fruit_prices.pop("orange")

# # 4. Check if "apple" exists as a key in the dictionary.
# print("apple" in fruit_prices)

# print(fruit_prices)

# # 6. employees = {"John": 50000, "Alice": 60000, "Bob": 45000,  "Diana": 70000,
# #     "Charlie": 55000}
# employees = {
#     "John": 50000,
#     "Alice": 60000,
#     "Bob": 45000,
#     "Diana": 70000,
#     "Charlie": 55000
# }

# # 1. Print all employee names.
# print(employees.keys())

# # 2. Print all salaries.
# print(employees.values())

# # 3. Calculate the total salary of all employees.
# total = sum(employees.values())
# print("Total salary:", total)

# # 4. Calculate the average salary.
# avg = total / len(employees)
# print("Average salary:", avg)

# # 5. Add a new employee "Eva": 65000 to the dictionary.
# employees["Eva"] = 65000

# # 6. Update "Bob"’s salary to 48000.
# employees["Bob"] = 48000

# # 7. Remove "Charlie" from the dictionary.
# employees.pop("Charlie")

# # 8. Check if "Alice" exists in the dictionary.
# print("Alice" in employees)

# # 9. Create a new dictionary of employees whose salary is more than 55000.
# high_salary={key : value for key , value in employees.items() if value > 55000}
# print(high_salary)

# # 10. Count how many employees earn less than 60000.
# count = sum(1 for value in employees.values() if value < 60000)
# print("Count:",count)


dict1={1:"A",2:"B",3:"C"}
# print(dict1.get(1))
print(dict(reversed(list(dict1.items()))))
#print(rev)