def has_warming_trend(temps):
    
    for i in range(len(temps) - 2):
        
        day1 = temps[i]
        day2 = temps[i + 1]
        day3 = temps[i + 2]

        if day2 > day1 and day3 > day2:
            return True
        
    return False