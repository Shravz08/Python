str= 'Hey this String is made up of SINGLE quote'
print(str)
#print("Total count of characters is",len(str))
#print(str.upper())

str1= "This one is made of DOUBLE qoute"
print(str1)
#print(str.lower())

str2='''And this one is from TRIPLE qoutes'''
print(str2)
print("Counting of occurrences:",str.count("is"))

#print(str2.split())
separate= str2.split()
print("Number of words:", len(separate))


str3="2324s1dwe12"
print(str3.isdigit())

#sorted
str4="Its my string"
sorted_str4=''.join(sorted(str4))
print(sorted_str4)

#Palindrome
str5="1234321"
print(str5)

str6="I realy want to see how does this looks like in reverse"
split_it= str6.split()
