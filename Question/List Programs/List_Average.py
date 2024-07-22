ls = [1,2,3,4,5,6,7,8,9,10]

def my_len(ls):
    sum=0
    count=0
    for i in ls:
        sum+=i
        count+=1
    print("average : ",sum/count)
    
my_len(ls)
