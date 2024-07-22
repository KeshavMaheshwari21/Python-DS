num_list = int(input("Enter the no. of number to insert : "))
ls = []

for i in range(0,num_list):
    num = int(input(f"Enter the {i+1} number: "))
    ls.append(num)

def MoveRight(list):
    n = int(input("Enter the number of positions to move right : "))
    while n > 0:
        last_element = list[-1]
        for i in range(len(list) - 1, 0, -1):
            list[i] = list[i - 1]
        list[0] = last_element
        n -= 1
    
    print("Result after moving right :", list)

MoveRight(ls)
