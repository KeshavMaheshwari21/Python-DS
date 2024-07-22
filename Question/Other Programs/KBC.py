questions = [
    ['1: The International Literacy Day is observed on:','Sep 8','Sep 15','Aug 9','8 Jan',1],
    ['2: The language of Lakshadweep. a Union Territory of India, is','Tamil','Hindi','Malayalam','None',3],
    ['3: Bahubali festival is related to','Hinduism','Jainism','Islam','Budhism',2],
    ['4: Which day is observed as the World Standards  Day?','June 26','Oct 14','Nov 15','Dec 2',2],
    ['5: Who is the author of the epic "Meghdoot"?','Valmiki','Kalidas','Vishakadatta','Brahma',2],
    ['6: Pongal is a popular festival of which state?','Karnataka','Kerala','Tamil Nadu','Andhra Pradesh',3]
]

income=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

money=0

count=0
for question in questions:
    print(question[0])
    print('1.',question[1])
    print('2.',question[2])
    print('3.',question[3])
    print('4.',question[4])
    
    i = int(input("Enter the option or press 0 to quit : "))
    
    if(i==question[-1]):
        money=income[count]
        count+=1
        print("\nRigth Answer!\n")
    
    if(i==0):
        print("The Money to take home : ",money)
        break
    
    if(i!=question[-1]):
        
        if(count>=4):
            money = 10000
        
        if(count>=9):
            money = 320000
        
        if(count == 14):
            money = 10000000
        print("Wrong Answer!")
        print("\nThe correct answer is : ",question[-1],'\n')
        print("The Money to take home : ",money)
        break
    
    if(count==len(questions)):
        print("Congratulations!!")
        print("The Money to take home : ",money)
print("Thank You!!!")