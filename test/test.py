def has_distinction(scores):
    for score in scores:
        if score < 80:
            return False
    return True