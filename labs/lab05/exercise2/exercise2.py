
def find_largest_drop(readings):
    """
    Return the largest consecutive temperature drop, or 0.0 if none.
    """
    largest_drop = 0.0

    if len(readings) < 2:
         return 0.0
         

    for i in range(1, len(readings)) :
            prev_temp = readings[i-1]
            curr_temp = readings[i]

            drop = prev_temp - curr_temp
        
            if drop > largest_drop:
                largest_drop = drop

    return largest_drop
        


# Test
temps = (32.5, 31.0, 31.5, 28.0, 24.5)
result = find_largest_drop(temps)
print(f"Largest Drop: {result}")  # Expected: 3.5
