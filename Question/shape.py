# Write a Python program to create a class that represents a shape.
# Implement methods for different shapes like circle, triangle, and square.
class shape:

    def __init__(self):
        
        print("1. Circle")
        print("2. Triangle")
        print("3. Square")
        print("4. Rectangle")
        
        self.i = int(input("Enter the option :"))

        if(self.i==1):
            self.circle()

        elif(self.i==2):
            self.Triangle()

        elif(self.i==3):
            self.Square()

        elif(self.i==4):
            self.Rectangle()

        else:
            print("Please Enter a Valid Option!")

    def circle(self):

        print("\n1. Area")
        print("2. Primeter")
        
        j = int(input("Enter the Option :"))
        r = int(input("\nEnter the Radius :"))

        if(j==1):
            area = 3.14*r*r
            print("\nArea of Circle :",area)
        
        elif(j==2):
            perimeter = 2*3.14*r
            print("\nPerimeter of Circle :",perimeter)

        else:
            print("Chose Correct Option!")
        print("Thank You!")

    def Triangle(self):
        
        b = int(input("\nEnter the Base :"))
        h = int(input("Enter the Height :"))

        area = 0.5*b*h
        print("\nArea of Triangle :",area)
        print("Thank You!")

    def Square(self):

        print("\n1. Area")
        print("2. Primeter")
        
        j = int(input("Enter the Option :"))
        s = int(input("\nEnter the Side :"))

        if(j==1):
            area = s*s
            print("\nArea of Square :",area)
        
        elif(j==2):
            perimeter = 4*s
            print("\nPerimeter of Square :",perimeter)

        else:
            print("Chose Correct Option!")
        print("Thank You!")

    def Rectangle(self):

        print("\n1. Area")
        print("2. Primeter")
        
        j = int(input("Enter the Option :"))
        l = int(input("\nEnter the Length :"))
        b = int(input("\nEnter the Breadth :"))


        if(j==1):
            area = l*b
            print("\nArea of Rectangle :",area)
        
        elif(j==2):
            perimeter = 2*(l+b)
            print("\nPerimeter of Rectangle :",perimeter)

        else:
            print("Chose Correct Option!")
        print("Thank You!")

obj = shape()