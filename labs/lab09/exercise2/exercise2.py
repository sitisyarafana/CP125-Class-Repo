import pandas as pd


def compare_averages(filename):
    df = pd.read_csv("labs/lab09/data/students.csv")

    mean_math = df["Math"].mean()
    mean_science = df["Science"].mean()
    mean_english = df["English"].mean()

    if mean_math >= mean_english and mean_math >= mean_science:
        best_subject = "Math"
    elif mean_science >= mean_math and mean_science >= mean_english:
        best_subject = "Science"
    else:
        best_subject = "English"

    if mean_math <= mean_english and mean_math <= mean_science:
        worst_subject = "Math"
    elif mean_science <= mean_english and mean_science <= mean_math:
        worst_subject = "Science"
    else:
        worst_subject = "English"

    return {
        "Math": mean_math,
        "Science": mean_science,
        "English": mean_english,
        "best_subject" : best_subject,
        "worst_subject" : worst_subject
      
    }