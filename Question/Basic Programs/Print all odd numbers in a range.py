n1 = int(input("Enter the first number of the Range : "))
n2 = int(input("Enter the second number of the Range : "))

if n2<=n1:
    n2 = int(input("Enter the second number greater than first : "))
    
odd_list = []

for i in range(n1,n2):
    if i%2!=0:
        odd_list.append(i)
        
print("\n List of Odd numbers :\n",odd_list)
