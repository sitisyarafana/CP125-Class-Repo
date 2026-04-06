import pandas as pd
import matplotlib.pyplot as plt


def plot_subject_maximums(filename):
    df = pd.read_csv(filename)

    plt.plot(df.index, df["Math"] & df["Science"] & df["English"] & df["Physics"] & df["Chemistry"])
    plt.xlabel("Subject")
    plt.ylabel("Maximum Score")
    plt.title("Maximum Scores by Subject")
    #plt.show()

    return len(df)

count = plot_subject_maximums("labs/lab09/data/students.csv")
print(count)
