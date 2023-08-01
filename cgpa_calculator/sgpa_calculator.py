subjects = dict()


#taking input from the user for the subjects and credits

print("enter an empty string to stop \n")

while True:
    subject = input("Enter the subject name: \n")
    if subject == "":
        break
    credit = int(input("Enter the credit: \n"))
    marks = int(input("Enter the marks: \n"))
    subjects[subject] = [credit,marks]


#function for calculating the grade for each subject

def calculate_grade(marks):
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    elif marks >= 35:
        return 4
    else:
        return 0


#caculating the sgpa
#formula = (credit1*grade1 + credit2*grade2 + credit3*grade3 + ...)/total_credits

sum_of_credits_and_grade = 0
total_credits = 0

for subject in subjects:
    credit = subjects[subject][0]
    grade = calculate_grade(subjects[subject][1])

    sum_of_credits_and_grade += credit*grade

    total_credits += credit

sgpa = sum_of_credits_and_grade/total_credits

print("Your sgpa is: ",round(sgpa,3))