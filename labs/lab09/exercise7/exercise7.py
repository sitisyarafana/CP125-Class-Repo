import pandas as pd


def promotion_candidates(filename):
    df = pd.read_csv(filename)
    
    average = float(df["PerformanceScore"].mean())

    candidate = df.loc[(df["PerformanceScore"] > average) & (df["YearsOfService"] >= 2), "EmployeeName"]
    name = set(candidate)
    count = len(name)

    return{
        "average_performance": average,
        "min_years_required": 2,
        "candidate_count": count,
        "candidate_names": name 
        }

result = promotion_candidates("labs/lab09/data/employees.csv")
print(result)
