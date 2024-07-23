def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = int(input("Enter the Number : "))
print('{} has occurred {} times'.format(x,countX(lst, x)))
