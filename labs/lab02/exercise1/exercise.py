# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    # TODO: Implement this function
    # Calculate round trip cost and checks if within budget
    pass

    trip = one_way_km * 2
    liter = trip / km_per_liter
    total_price = price_per_liter * liter
    return trip, liter, total_price

def is_money_enough(budget):
    if budget >= total_price:
        return "Pass"
         
# Test your code here
print("Testing Road Trip Budgeter...")
