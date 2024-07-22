def prime(x, y):
    prime_list = []
    
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = int(input("Enter the starting : "))
ending_range = int(input("Enter the ending : "))

lst = prime(starting_range, ending_range)

if starting_range == ending_range:
    print("\nEnter a Valid range!")
    
elif len(lst) == 0:
    print("\nThere are no prime numbers in this range")
    
else:
    print("\nThe prime numbers in this range are: ", lst)
