class Calculator:

    def __init__(self):
        print("Welcome!")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        self.i = int(input("Enter the Option :"))

        if(self.i==1):
            self.Addition()

        elif(self.i==2):
            self.Subtraction()

        elif(self.i==3):
            self.Multiplication()

        elif(self.i==4):
            self.Division()

        else:
            print("Chose Option 1-4!")

        print("Thank You!")

    def Addition(self):
        i = int(input("Enter the num1 :"))
        j = int(input("Enter the num2 :"))
        sum = i+j
        print("\nThe Addition :",sum)

    def Subtraction(self):
        i = int(input("Enter the num1 :"))
        j = int(input("Enter the num2 :"))
        sub = i-j
        print("\nThe Subtraction :",sub)

    def Multiplication(self):
        i = int(input("Enter the num1 :"))
        j = int(input("Enter the num2 :"))
        product = i*j
        print("\nThe Multiplication :",product)

    def Division(self):
        i = int(input("Enter the num1 :"))
        j = int(input("Enter the num2 :"))
        div = i/j
        print("\nThe Division :",div)

obj = Calculator()
