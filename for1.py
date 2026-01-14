


#all even from 1 to 100 using for loop
# for i in range(2,101,2):
#  print(i)

# list1=[1,5,8,5,3,6]
# even=[]
# odd=[]

# for i in list1:
#   if i % 2 ==0 :
#     even.append(i)
#   else:
#     odd.append(i)
# print("Even",even)
# print("Odd",odd)

# str = "congratulations"
# vowel=[]
# con=[]

# for i in str:
#     if i in "aeiouAEIOU":
#      vowel.append(i)
#     else:
#      con.append(i)
# print("vowel:",vowel)
# print("con",con)

#multiplication table of num N
# N = int(input("Enter the Number:"))
# #N = 8
# for i in range(1, 11):
#  print(i*N)

# str="it is Python programming"
# ch = "i"
# count = 0

# for i in str:
#     if i == ch:
#        count += 1
# print(count)

# str = "It is again a python program"
# vowels = "a","e","i","o","u","A","I","E","O","U"
# count = 0

# for i in str:
#     if i in vowels:
#         count += 1

# print(count)

marks={"python":90, "java":80 , ".Net": 80, "c++":70}
sum=0

for mark in marks.values():
    sum += mark

print(sum)

#sum of all even from 1 to 100 
addition=0
for i in range (2,101,2):
   # while i < 101:
    addition += i

print(addition)

