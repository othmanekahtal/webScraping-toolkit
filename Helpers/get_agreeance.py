def get_agreeance(ratio):

    if ratio > 3:
        return "absolutely agrees"
    elif 2 < ratio <= 3:
        return "strongly agrees"
    elif 1.5 < ratio <= 2:
        return "agrees"
    elif 1 < ratio <= 1.5:
        return "somewhat agrees"
    elif ratio == 1:
        return "neutral"
    elif 0.67 < ratio < 1:
        return "somewhat disagrees"
    elif 0.5 < ratio <= 0.67:
        return "disagrees"
    elif 0.33 < ratio <= 0.5:
        return "strongly disagrees"
    elif ratio <= 0.33:
        return "absolutely disagrees"
    else:
        return None