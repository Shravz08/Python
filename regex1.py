# Regex  ----- spl seq of char
# Regex creates the pattern to find a str 
# REgex func ---- findall -- list of all matching , search --first occurance of char , split -- split str by occurance of char ,sub -- replaces all occurance of a char
# Meta Char --- [] "[a-m]"
# \   -- "\d"
# spl seq --- 
# r = raw str
# \b --- starts with and ends with for a word
# \B not starts with and ends with for a word
# \d for digit 
# \D for 
# Set for char matching 


# examples
# extract date from str of format DD-MM-YYYY

import re 
# text = "Meetings are schedule from 12-01-2026 to 03-03-2026. and important dates are 2026-02-08 and 2026-04-8"
# pattern = r"\d{2}-\d{2}-\d{4}"
# result = re.findall(pattern,text)
# print(result)

text = "anu having an amazing day"
pattern = r"\ba+[a-zA-Z]*"
res = re.findall(pattern,text)
print(res)