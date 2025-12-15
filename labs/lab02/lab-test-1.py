#NAME : SITI SYARAFANA BINTI SABDIN
#PROBLEM DESCRIPTION : WE NEED TO GIVE A GRADE TO THE STUDENT BASED ON THEIR MARK

def determine_grade(mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 60 and mark <= 79:
        grade = "B"
    elif mark >= 50 and mark <= 59:
        grade = "C"
    elif mark >= 40 and mark <= 49:
        grade = "D"
    else:
        grade = "F"

    return grade

mark = float(input("Enter the student's mark:"))
grade = determine_grade(mark)

print(f"Mark: {mark}, Grade: {grade}")