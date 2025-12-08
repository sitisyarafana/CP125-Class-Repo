# Lab 02 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km, km_per_liter, price_per_liter, budget):
    trip = one_way_km * 2
    liter = trip / km_per_liter
    total_price = price_per_liter * liter
    return budget >= total_price
         
# Test your code here
print("Testing Road Trip Budgeter...")
