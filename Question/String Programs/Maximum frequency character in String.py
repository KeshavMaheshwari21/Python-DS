str = input("Enter the String : ")

freq = {}
for i in str:
 if i in freq:
  freq[i] += 1
 else:
  freq[i] = 1
res = max(freq, key = freq.get) 
 
print ("The maximum of all characters in KeshavMaheshwari is :",res)
