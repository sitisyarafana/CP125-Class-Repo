#SITI SYARAFANA BINTI SABDIN C02
#This program accepts 5 integer input values from the user and is stored in a LIST.

def calculate_number():
    number_list = []

    #loop for 5 number
    for i in range(1, 6):
        number_value = int(input(f"Enter number {i}:"))
        number_list.append(number_value)

    #ascending number, sum of 5 number and max number in a list
    ascending_number = sorted(number_list)
    sum_number = sum(number_list)
    largest_number = max(number_list)

    print(f"Numbers in ascending order: {ascending_number}")
    print(f"Sum of all numbers: {sum_number}")
    print(f"Largest number: {largest_number}")

#call a function
calculate_number()