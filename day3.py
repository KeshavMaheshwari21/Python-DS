#  BOOLEAN DATATYPE 

# When in any variable True/False is stored then it is defined as boolean datatype
# In boolean only True/False is stored
# var1 = True
# var2 = False
# print(var1,var2)
# print(type(var1),type(var2))

#  LIST DATATYPE
# LIST is an alternative of ARRAY
# LIST is collection of variable but not similar datatype
# LIST is of dynamic & referential nature ( Size is not fixed & can store multiple datatype )

# Declaring a list
# ls = [12,23,45,54,1.2,1.3,1.21,'upflairs',True] 
# print(ls)
# print(type(ls))

# Indexing is same as string
# ls = [10,12,13,14,'Upflairs',16]
# print(ls[4][4:7])

# Mutable - changable (LIST)
# Immutable - unchangable

# Changing the first index in the list

# student_name=['taniya','yash','prerna','ruchika','aditya','kalika','yash']

# student_name[0] = 'Tanya' manipulation / updation

# Append function is used to add the data in list in python & inserts data at last position
# student_name.append('ritu')

# Pop function is used to remove the item from the last position
# student_name.pop()

# Insert function is used to insert element at given index and rest of the items are shifted
# student_name.insert(1,'gurpreet')

# Remove function is used to remove the item from the list
# student_name.remove('prerna')

# Del function is used to remove the item by giving the index in the list
# del student_name[2]

# Count function is used to print number of time the item is present
# print(student_name.count('yash'))

# ls1 = ['A','B','C','D','E']
# ls2 = [1,2,3,4,5,6,8,7]

# Reverse function is used to reverse the list
# ls1.reverse()
# print(ls1)

# Sort function is used to sort the list
# ls2.sort() # Ascending Order
# ls2.sort(reverse=True) # Descending order
# print(ls2)

# Min is an aggregate function used to find minimum in list
# print(min(ls2))

# Max is an aggregate function used to find maximum in list
# print(max(ls2))

# Sum function is used to find sum of all items in the list
# print(sum(ls2))

# c
# ls2 = ['F','G']
# print(ls1+ls2)

# # ls1.append(ls2)
# ls1.extend(ls2)
# print(ls1)

# ls1 = ['A','B','C','D','E']

# ls1.clear()

# print(ls1.index('C'))

# ls2=[10,20,3.1,'upflairs pvt ltd',500,400]

# ls2[2]=100
# print(ls2[3][0:8])
# ls2[ls2.index('upflairs pvt ltd')]="flipkart pvt ltd"
# print(ls2)


#           TUPLE
# TUPLE ARE IMMUTABLE unchangeable


# tp1 = (25,12,14,45,"upflairs",True,2.2)
# tp1.count()
# tp1.index()
# print(type(tp1))


# <<<<<<<<<<<<   SET   >>>>>>>>>>>>
# SET does not allow duplicate items


# st = {32,2,1,4,5,6,54,65,76,54,7,54}
# print(type(st))

# st.add(5000)

# st.remove(54)

# st.discard(54)

# st1 = {52,41,63,96,78,54}
# st2 = {52,41,65,55,22}

# st1.update(st2) # st1 + st2

# st1.intersection(st2)

# print(st1.intersection(st2))


# <<<<<<<<   DICITIONARY   >>>>>>>
# pairs = (key:value)

# marks = {'mohit':90,'rohit':69,'rokcy':89,'keshav':99}
# print(type(marks))