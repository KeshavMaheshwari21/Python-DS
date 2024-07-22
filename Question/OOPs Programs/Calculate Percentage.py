# Creating a class to find the Percentage by taking the marks as input from the user
class Percentage:
    
    # Default Constructor is made in which the list is passed for the subjects
    def __init__(self):
        self.subjects = ['Physics 1', 'Physics 2', 'Chemistry 1', 'Chemistry 2', 'Maths', 'English', 'Hindi']
    
    # Creating a method to calculate Percentage
    def mark_per(self):
        number = []
        total = 0
        count = 0

        # Taking the marks as input fromthe user and by append() function adding the number in an empty list until the subjects ends
        for subject in self.subjects:
            marks = int(input(f"Enter the Marks for {subject}: "))
            number.append(marks)
        
        # Calculating the total marks and number of subjects
        for marks in number:
            total += marks  # Calculate Total Marks
            count += 1      # Counts no. of subject
        

        total_marks = count * 100  # Counting total marks
        per = (total / total_marks) * 100 # calculating the percentage

        print("The Percentage:",per)

# Making the object
obj = Percentage()
obj.mark_per()
