import numpy as np
 
A = np.array([[1, 2], [3, 4]])
 
B = np.array([[4, 5], [6, 7]])

print("1. Addition")
print("2. Subtraction")
i = int(input("\nEnter the option : "))
if(i==1):
    print("\nAddition of two matrix")
    print(np.add(A, B))
elif(i==2):
    print("\nSubtraction of two matrix")
    print(np.subtract(A, B))
else:
    print("\nEnter the Correct Option!")
