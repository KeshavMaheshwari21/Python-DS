num_list = int(input("Enter the no. of number to insert : "))
ls = []

for i in range(0,num_list):
    num = int(input(f"Enter the {i+1} number: "))
    ls.append(num)

def MoveLeft(list):
    n = int(input("Enter the number of positions to move left : "))
    while n!=0:
        first_element = list[0] 
        for i in range(0,len(list)-1):
            list[i] = list[i+1]
        list[-1] = first_element
        n-=1
    print("Result after moving left :", list)

MoveLeft(ls)
