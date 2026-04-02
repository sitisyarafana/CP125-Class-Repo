import pandas as pd

def explore_data(filename):
    # Loads CSV into DataFrame using the filename passed from the test
    df = pd.read_csv(filename)

    # 1. total_students: count the number of rows
    total_students = len(df)
    
    # 2. subjects: strictly Math, Science, and English only
    subjects = ["Math", "Science", "English"]
    
    # 3. math_average: average of Math column rounded to 1 decimal
    math_average = round(df["Math"].mean(), 1)
    
    # 4. highest_math_student: name of the student with the max Math score
    # idxmax finds the index of the highest value, then .loc gets the name
    highest_math_idx = df["Math"].idxmax()
    highest_math_student = df.loc[highest_math_idx, "Name"]
    
    # Returns the dictionary with the specific keys required
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_student
    }