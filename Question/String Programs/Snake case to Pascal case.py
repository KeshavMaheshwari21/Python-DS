str = input("Enter the String in Snake Case : ")

res = str.replace("_", " ").title().replace(" ", "")
 
print("Pascal case :",res) 
