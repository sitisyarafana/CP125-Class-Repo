import pandas as pd

def high_performers(filename):
    df = pd.read_csv(filename)

    High_performance = df.loc[(df["Math"] > 85) & (df["Science"] > 85) & (df["English"] > 85) & (df["Physics"] > 85) & (df["Chemistry"] > 85), "Name"]
    names = set(High_performance)


    return {
        "count": len(names),
        "names": names
    }

result = high_performers("labs/lab09/data/students.csv")
print(result)
