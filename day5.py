# ________ASSIGNMENT OPERATORS________

# Assignment Operator is used to store value in variable

# = # x = 3
# += # x += 3 --> x = x + 3
# -= # x -= 3 --> x = x - 3
# *= # x *= 3 --> x = x * 3
# /= # x /= 3 --> x = x / 3
# ** # x ** =3 --> x = x ** 3
# // # x // =3 --> x = x // 3

# x = int(input("Enter the number : "))
# x += 3
# print("Addition",x)

# x = int(input("Enter the number : "))
# x -= 3
# print("Subtraction",x)

# x = int(input("Enter the number : "))
# x *= 3
# print("Multiplication",x)

# x = int(input("Enter the number : "))
# x /= 3
# print("Division",x)

# x = int(input("Enter the number : "))
# x **= 3
# print("Exponentiation",x)

# x = int(input("Enter the number : "))
# x //= 3
# print("Floor Division",x)

# ________COMPARISION OPERATORS________

# == # Equal
# != # Not Equal
# >  # Greater than
# <  # Less than
# >= # Greater than or Equal to
# <= # Less than or Equal to

# x = int(input("Enter the number : "))
# y = int(input("Enter the number : "))
# print( x == y )
# print( x != y )
# print( x > y )
# print( x < y )
# print( x >= y )
# print( x <= y )


#_________CONDITIONAL STATEMENT__________
# IF-ELSE STATEMENT


# if(condition):
#   block of code for if
# else:
#   block of code for else

# In Python the {} is not used for if statement block the term Indentation( 4 whiteespace ) is used which determines till where the if block is.

# Python program to find greater number from 3 numbers
# num1 = int(input("Enter num1 :"))
# num2 = int(input("Enter num2 :"))
# num3 = int(input("Enter num3 :"))
# if(num1>num2 and num1>num3):
#     print("num1 is greater")
# elif(num2>num1 and num2>num3):
#     print("num2 is greater")
# else:
#     print("num3 is greater")


#_________LOGICAL OPERATOR__________


# __AND__ --> this gate return true if both the condition are true
# 0 --> False
# 1 --> True
#   A    B     RESULT
#   0    0       0
#   0    1       0
#   1    0       0
#   1    1       1


# __OR__ --> this gate return true if one of the condition is true
# 0 --> False
# 1 --> True
#   A    B     RESULT
#   0    0       0
#   0    1       1
#   1    0       1
#   1    1       1


# __NOT__ --> this gate opposites the input if true then false and vice-versa
# 0 --> False
# 1 --> True
#   A    RESULT
#   0      1
#   1      0
# print(not False)
# print(not True)


#_________MEMBERSHIP OPERATOR__________
# In and Not In


# student_list = ['keshav','manvik','gaurang','vinayak']

# In --> returns true when item is present in the list

# if 'keshav' in student_list:
#     print('Present')
# else:
#     print('Not Present')

# Not In --> returns true when item is not present in the list

# if 'eklavya' not in student_list:
#     print("not present")
# else:
#     print("present")


