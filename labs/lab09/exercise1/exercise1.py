import pandas as pd

def explore_data(filename):
    # Load the CSV
    df = pd.read_csv("labs/lab09/data/students.csv")

    # 1. total_students: The number of rows in the data
    total_students = len(df)
    
    # 2. subjects: A specific list of the three core subjects
    subjects = ["Math", "Science", "English"]
    
    # 3. math_average: Mean of the Math column, rounded to 1 decimal place
    math_average = round(df["Math"].mean(), 1)
    
    # 4. highest_math_student: Find the row index of the max Math score, 
    # then look up the 'Name' at that index.
    highest_math_idx = df["Math"].idxmax()
    highest_math_student = df.loc[highest_math_idx, "Name"]
    
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }