
def was_backward_detected(waypoints):
    """
    Return True if drone moved backward in x or y, False otherwise.
    Use tuple unpacking.
    """
    # x1, y1, z1 - previous point
    # x2, y2, z2 - current point
    x1, y1, z1 = waypoints[0]

    for item in waypoints[1:] :
        x2, y2, z2 = item

        if x2 < x1 or y2 < y1:
            return True
        
        x1, y1 = x2, y2

    return False

        

      
# Test
path = ((0, 0, 10), (5, 5, 12), (4, 6, 10), (10, 10, 15))
result = was_backward_detected(path)
print(f"Backward Movement: {result}")  # Expected: True
