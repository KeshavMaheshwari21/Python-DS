# Variables is a small block of memory container 
# In C language int var = 10;
# In python no need of defining datatype

# var = 10
# print(var)

# #To check datatype of the variable

# print(type(var))

# Rules for declaring the variable
# 1. A-Z , a-z , 0-9 , _ only these characters can be used
# 2. Variable name cannot start with number
# 3. Variable name is case sensitive AGE = 10 , Age = 23 , age = 90 (all are different)
# 4. A variable name cannot be any of the Python keywords

# There are Some Reserved Keywords in Python whch cannot be used as a Variable

# var1 = 20
# var2 = 30

# Datatypes 

# For declaring a String variable the quotes is used weather double single 
# st = "Upflairs" # string
# print(type(st))
# print(st)

# [] brackets is used for indexing in Python
# Space( ) is also given index in Pyhton

# st = "Upflairs"
# print(st[4])

# WE WANT TO PRINT (air) FROM (Upflairs)
# For printing the Substring we need to find the starting point and the ending point
# start = 4 , end = 6+1(it doesn't consider the ending index)
# print(st[4:7:2]) # [starting : stoping : jump] jump is by default 1

# Indexing is two types
# 1. Positive Indexing (Forward) [0 - end]
# 2. Negative Indexing (Backward) [-1 - start]

# print(st[4]) (+ve Indexing)
# print(st[-4]) (-ve Indexing)

# print(st[2:]) --> In this case if the stoping point is not defined then it will go till end
# print(st[:4]) --> In this case if the startingpoint is not defined then it will start from 0

# print(st[::-1]) --> In this case the st will be print in reverse order

st = "Upflairs pvt ltd jaipur Rajasthan"

# print(st[-16:-10])

# len function is used to get the length of the String
# print(len(st))

# count function is used to find the number of occurrence of any Character/String in the variable
# print(st.count("Rajasthan"))

# Lower function is used to conver all the character in lower character
# Upper function is used to convert all the character in upper character
# print(st)
# print(st.upper())
# print(st.lower())


# ASSIGNMENT 1

# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.If the word contains a number or a symbol, the first letter after that will be converted to upper case.
# print(st.title())

# The first character is converted to upper case, and the rest are converted to lower case UPFLAIRS --> Upflairs
# print(st.capitalize())


# Replace function is used to replace the string from the given string
# print(st.replace('Upflairs','Flipkart'))

# We can also remove by not passing the removing string
# print(st.replace('Upflairs',''))

# Find function is used to find the index of the any character/string
# print(st.find('u'))

# ASSIGNMENT 2

# The startswith() method returns True if the string starts with the specified value, otherwise False --> string.startswith(value, start, end)
# print(st.startswith("U"))

# The split() method splits a string into a list --> string.split(separator, maxsplit)
# st.split

# The strip() method removes any leading, and trailing whitespaces --> string.strip(characters)
# st.strip()

# The center() method will center align the string, using a specified character (space is default) as the fill character --> string.center(length, character)
# st.center()

# The endswith() method returns True if the string ends with the specified value, otherwise False --> string.endswith(value, start, end)
# st.endswith()
