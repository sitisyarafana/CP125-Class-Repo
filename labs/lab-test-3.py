import csv

def read_average(filename):
    f = open(filename, "r", newline="")
    reader = csv.reader(f)
    total_height = 0
    count = 0

    next(reader)

    for row in reader:
        print(row)
        total_height += float(row[1])
        count += 1
    f.close()

    if count > 0:
        average = total_height / count
        print("Average :", average)
        return average
    
def add_data(filename):

    Gender = input("Gender: ")
    Height = input("Height: ")
    Weight = input("Weight: ")
    BMI = input("BMI: ")

    new_row = [Gender, Height, Weight, BMI]

    f = open(filename, "a", newline="")
    writer = csv.writer(f)
    writer.writerow(new_row)
    f.close()

    f = open(filename, "r", newline="")
    reader = csv.reader(f)
    for row in reader:
        print(row)
    f.close()
    return

averages = read_average("labs/bmi.csv")
data = add_data("labs/bmi.csv")
print(averages)
print(data)
   