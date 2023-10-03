import re
 
# initializing string
test_string = "There are 24 apples for 48 persons"
 
# printing original string
print("The original string : " + test_string)
 
# getting numbers from string
temp = re.findall(r'\d+', test_string)
res = list(map(int, temp))
 
# print result
print("The numbers list is : " + str(res))

