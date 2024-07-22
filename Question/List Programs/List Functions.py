# Function to count length of list without len()
ls = [23,43,56,76,87,98,90,65,34,21,1,2,3,4,5]

def my_len(ls):
    count=0
    for i in ls:
        count+=1
    print(count)

my_len(ls)

# Function to count sum length of list without sum()
ls = [1,2,3,4,5,6,7,8,9,10]

def my_sum(ls):
    sum=0
    for i in ls:
        sum+=i
    print("Sum : ",sum)
my_sum(ls)

# Average_finder
ls = [1,2,3,4,5,6,7,8,9,10]

def my_avg(ls):
    sum=0
    count=0
    for i in ls:
        sum+=i
        count+=1
    print("average : ",sum/count)
my_avg(ls)

# Even_finder
ls=[1,2,3,4,5,6,7,8,9,10]

def even_finder(ls):
    ls1=[]
    for i in ls:
        if(i%2==0):
            ls1.append(i)
    print("Even Numbers in List : ",ls1)
even_finder(ls)

# Average_finder_even()
ls=[1,2,3,4,5,6,7,8,9,10]

def even_finder_avg(ls):
    ls1=[]
    count = 0
    sum = 0
    for i in ls:
        if(i%2==0):
            count+=1
            sum+=i
    print("Average of Even Numbers in List : ",sum/count)
even_finder_avg(ls)

# min()
ls=[2,3,4,5,6,7,1,8,9,10]
def my_min(ls):
    min = ls[0]
    for i in ls:
        if(i<min):
            min = i
    print("The Min : ",min)
my_min(ls)


# max()
ls=[2,3,4,5,6,7,1,8,9,10]
def my_max(ls):
    max = ls[0]
    for i in ls:
        if(i>max):
            max = i
    print("The Max : ",max)
my_max(ls)
