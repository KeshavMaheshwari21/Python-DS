# ______________ LOOPS _______________

# 1. for
# 2. while
# 3. do-while

# __ FOR __
# for i  in range(10): # 10
#     print(i+1,"Hello")

# for i  in range(0,10,2): # 10
#     print(i+1,"Hello")


# __ WHILE __
# i=1
# while i<=10 :
#     print("hello world",i)
#     i+=1


# for i in range(100):
#     print("hello")


# condition = True
# while condition:
#     user_input = input("Do you wnat to quit this program press Y/N : ")
#     if(user_input=='Y' or user_input=='y'):
#         condition=False
#     print("Welcome")


# _______break___&___continue______


# for i in range(10):
#     print(i)
#     if i == 5:
#         break # Break keyword stops the current execution of the loop


# for i in range(10):
#     if i == 5:
#         continue # Continue keyword is used to ignore the current execution
#     print(i)

# ls = [1,2,3,4,85,76,78,89,9]
# if 85 in ls:
#     print("present")
#     print(ls.index(85))
# else:
#     print("Not Present")


# count = 0
# for i in ls:
#     if i==85:
#         print(count)
#         break
#     count+=1

# ls min(),max() without min()&max()

# *
# * *
# * * *
# * * * *
# * * * * *

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# ls = [1,2,3,85,4,5,6,7,85]
# temp = 0
# count = 0
# for i in ls:
#     if i == 85 :
#         if temp == 1:
#             print("the 2 index of 85 is ",count)
#             break
#         temp=1
#     count+=1

# count=int(input("Enter the Number : "))
# for i in range(count):
#     for j in range(i+1):
#         print("*",end=" ")
#     print(' ')

# rows = int(input("Enter number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# To find the minimum and maximum item from the list
# ls = [1,2,3,4,5,6,7,100,98,0,-1]
# max = ls[0]
# min = ls[0]
# for i in range(len(ls)):
#     if(ls[i]>max):
#         max=ls[i]
#     if(ls[i]<min):
#         min=ls[i]
# print("The Max : ",max)
# print("The Min : ",min)
