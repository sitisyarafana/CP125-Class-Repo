# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    names = set()

    file1 = open(file1, "r")
    file2 = open(file2, "r")

    for line in file1 :
        names.add(line.strip())

    for line in file2 :
        names.add(line.strip())

    sorted_name = sorted(list(names))

    w = open(output_file, "w")

    for name in sorted_name :
            w.write(name + "\n")

    return len(sorted_name)






# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
