
def analyze_performance(lap_times):

    First_half = []
    Second_half = []
    mid = (len(lap_times) + 1) // 2
    First_half = lap_times [: mid]
    Second_half = lap_times [mid :]

    First_average = sum(First_half) / len(First_half) 
    Second_average = sum(Second_half) / len(Second_half)

    if Second_average > First_average :
        return True
    else:
        return False


# Test
laps = [60, 62, 61, 63, 65, 68, 70, 72]
result = analyze_performance(laps)
print(f"Faded: {result}")  # Expected: True
