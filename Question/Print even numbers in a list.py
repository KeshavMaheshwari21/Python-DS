num_list = int(input("Enter the no. of number to insert : "))
ls = []

for i in range(0,num_list):
    num = int(input(f"Enter the {i+1} number: "))
    ls.append(num)

even_ls = []

for i in ls:
    if(i%2==0):
        even_ls.append(i)
        
if len(even_ls)==0:
    print("\nNo Even Numbers!")

else:    
    print("\nEven numbers List :",even_ls)
