def simple_interest():
    
    p = int(input("\nEnter the Principal : "))
    r = float(input("Enter the Rate : "))
    t = int(input("Enter the Time : "))

    si = (p * t * r)/100
    print('Simple Interest is', si)

def compound_interest():
    
    p = int(input("\nEnter the Principal : "))
    r = float(input("Enter the Rate : "))
    t = int(input("Enter the Time : "))

    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print("Compound interest is", CI)
 
print("Enter the Option :-")
print("1. Simple Interest")
print("2. Compound Interest")
n = int(input("\nEnter the Option :"))

if(n==1):
    simple_interest()
elif(n==2):
    compound_interest()
else:
    print("\nEnter a Valid Option!")
