def get_position(cars, car_number):
    for i in range(len(cars)):
        if cars[i] == car_number:
            return i
         

def has_overtaken(before, after, car1, car2):
    record1_start = get_position(before, car1)
    record2_start = get_position(before, car2)

    record1_end = get_position(after, car1)
    record2_end = get_position(after, car2)

    if record1_start > record2_start and record1_end < record2_end :
         return True
    
    return False
