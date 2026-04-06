import pandas as pd


def critical_inventory(filename):
    df = pd.read_csv(filename)

    total = len(df)
    critical = df.loc[(df["StockLevel"] < df["ReorderThreshold"]) & (df["DaysSinceRestock"] > 30), "ProductName"]
    name = set(critical)

    return {
        "total_products": total,
        "critical_count": len(name),
        "critical_products": name
        }

result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)