def calculate_bounce_height(current_height):
    """
    Calculate the next bounce height (80% of current).
    """
    # TODO: Implement this
    current_height = (current_height * (80/100))
    return current_height


def is_ball_stopped(height):
    """
    Check if the ball has stopped (height < 1).
    """
    # TODO: Implement this
    if height < 1:
        return True
    else:
        return False


def calculate_bounce_count(initial_height):
    """
    Count how many times the ball bounces.
    """
    # TODO: Implement this
    count = 0
    height = initial_height

    while height >= 1:
        height = calculate_bounce_height(height)
        count += 1

    return count


def calculate_total_distance(initial_height):
    """
    Calculate total distance traveled.
    """
    # TODO: Implement this
    if initial_height <= 0:
        return 0.0
    
    total_distance = float(initial_height)
    height = initial_height

    while height >= 1:
        bounce_height = calculate_bounce_height(height)
        total_distance += (bounce_height * 2)
            
    return total_distance
