# Lab 02 Exercise 2: Camping Logistics
# Write your code below:

import math

def calculate_event_cost(participants, tent_capacity, tent_price, meal_price):
    # TODO: Implement this function
    # Calculate total cost for tents and meals
    tent_needed =  math.ceil(participants / tent_capacity)
    tent_cost = tent_price * tent_needed
    food_cost = meal_price * participants
    total_cost = tent_cost + food_cost
    return total_cost

# Test your code here
print("Testing Camping Logistics...")
