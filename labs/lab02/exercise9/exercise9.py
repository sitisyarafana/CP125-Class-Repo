def calculate_xp_required(current_level):
    """
    Calculate XP needed for next level (level * 100).
    """
    # TODO: Implement this
    current_level = current_level * 100
    return current_level


def can_level_up(current_xp, required_xp):
    """
    Check if player has enough XP to level up.
    """
    # TODO: Implement this
    required_xp = 100 - required_xp 
    if current_xp < 100:
        return True
    else:
        return False
    

def calculate_final_level(total_xp):
    """
    Calculate the final level reached.
    """
    # TODO: Implement this

    current_xp = total_xp
    final_level = 
    

def calculate_remaining_xp(total_xp):
    """
    Calculate XP leftover after leveling.
    """
    # TODO: Implement this
    pass
