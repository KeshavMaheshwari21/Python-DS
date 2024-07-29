def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

arr = []
n = int(input("Enter the length of List : "))

for i in range(0,n):
    j = int(input("Enter the number : "))
    arr.append(j)

arr.sort()  # sort the array

x = int(input("\nEnter the Number to Search : "))

result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
    print("\nElement is present at index", str(result))
else:
    print("\nElement is not present in array")
