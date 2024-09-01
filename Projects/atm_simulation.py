# Taking the name as string input from the User
name =  input("Please Enter your name : ")


# Printing the name of the User which is taken as the input
print("Welcome",name,"!!")


# Print the message at output ffor taking the input to perform the operation
# The string written in 3 single / double quotes in executed as it is in Python
message = '''
How may I help You!!!

Please select any of the option,
Type 1 >>>> CHECK BALANCE
Type 2 >>>> DEPOSIT
Type 3 >>>> WITHDRAWAL
'''
print(message)


# Taking the input of the operation and storing in variable "i"
task = int(input("Please Enter the Option : "))


# Setting default balance 5000 in Account
balance = 5000


# If the input is 1 the acoount balance will be printed
if(task==1):
    # Check Balance
    print("The Balance in your Account :",balance,'INR')


# If the input is 2 then the amount to deposit is asked and the amount is added in the variable "balance" and then printing the "balance"
elif(task==2):
    # Deposit Amount
    deposit_amt = int(input("Enter the Amount to Deposit : "))
    
    if deposit_amt >= 0:
        balance += deposit_amt
        print("Deposited Successfully!!!")
        print("The Balance in your Account after Deposit :",balance,'INR')

    else:
        print("Please Enter a Valid Deposit Amount!!!")


# If the input is 3 then the amount to withdraw is asked
# If the entered amount to withdram is greater then balance then "Insufficiant Amount" will be printed
# Else the amount is subtracted from the balance and the current balance is printed
elif(task==3):
    # Withdraw Amount
    withdraw_amt=int(input("Enter the Amount to Withdraw : "))

    if withdraw_amt>0 :

        if(withdraw_amt>balance):
            print("Insufficiant Amount!!!")
            print("The Amount in your Account :",balance,'INR')

        else:
            balance -= withdraw_amt
            print("Withdrawl Successfull!!!")
            print("The Balance in your Account after Withdrawl :",balance,'INR')
    
    else:
        print("Please Enter a Valid Withdraw Amount!!!")

      
# If the input is not 1, 2, & 3 then the message "Please Select the above mentioned Input" will be printed
else:
    print("Please Select Valid Option mentioned above!!!")
print("Thank You",name,"!!!")