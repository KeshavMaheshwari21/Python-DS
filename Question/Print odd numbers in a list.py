num_list = int(input("Enter the no. of number to insert : "))
ls = []

for i in range(0,num_list):
    num = int(input(f"Enter the {i+1} number: "))
    ls.append(num)

odd_ls = []

for i in ls:
    if(i%2!=0):
        odd_ls.append(i)
        
if len(odd_ls)==0:
    print("\nNo Odd Numbers!")

else:    
    print("\nOdd numbers List :",odd_ls)
