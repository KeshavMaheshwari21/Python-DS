def search(arr, x):
    count=0
    for i in arr:
        count+=1
        if i == x:
            print(count)
            break
    return -1
    
arr = [1,2,3,4,7,8,9]

search(arr,3)
