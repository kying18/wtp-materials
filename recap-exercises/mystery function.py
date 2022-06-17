from cmath import inf
from numpy import average



def pick_favorite_number(options):
    """
    Returns the number from list of options that is closest
    to the average of all the options.
    If there are no options, returns 0.
    """
    if len(options) == 0:
        return 0
    favorite_number = inf
    average_of_options = sum(options)/len(options)
    for i in options:
        if abs(average_of_options-i) < abs(average_of_options-favorite_number):
            favorite_number = i
    return favorite_number









prices = [3, 5, 1, 6]
print(pick_favorite_number(prices))
