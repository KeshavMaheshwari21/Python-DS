string1 = "How are you ?"
string2 = input("Enter the String to search :- ")

# Make sure the capital must be cappita and small must be small
if string2 in string1:
    print("\nYes! it is present in the string")
else:
    print("\nNo! it is not present")
