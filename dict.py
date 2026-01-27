#Creating dict
Student={
    "name":"Ram",
    "age":19,
    "course":"data science",
    "City":"Pune",
    "mob_no":354769809,
    "CGPA":87.12,
    "Hobbies":["Cooking", "Dancing","Reading"]
}
#print(Student)
print(Student.keys())
print(Student.values())
print(Student.items())
#Creating dict using dict constructor
lecture=dict(
    teacher="shree",
    course="data science",
    time=["12pm","2pm","4pm"]
)
#print(lecture)
Student["surname"]="Patil"
#print(Student)

Student.update({"rollno":34})
#print(Student)

Student["age"]=21
#print(Student)

Student.update({"name":"Radha"})
#print(Student)

Student.pop("mob_no")
#print(Student)

#Student.popitem()
#print(Student)

#del Student["CGPA"]
#print(Student)

#Student.clear()
#print(Student)