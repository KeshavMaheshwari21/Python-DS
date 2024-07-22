# Defining the function to find the number at the given index
def fibonacci(n):
    # Initializing the 1 & 2 element 0 & 1
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b
 
i = int(input("Enter the Index : "))
print("The Number at",i,";",fibonacci(i))
