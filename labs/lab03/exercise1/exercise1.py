def count_bright_spots(pixels):
    
    count = 0
    
    for i in range(1, len(pixels) - 1 ):
        current_pixels = pixels[i]
        left_pixels = pixels[i - 1]
        right_pixels = pixels[i + 1]

        if current_pixels > left_pixels and current_pixels > right_pixels:
            count += 1

    return count