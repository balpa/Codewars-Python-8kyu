"""Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments."""

def is_divide_by(number, a, b):
    return True if (number%a)==0 and (number%b)==0 else False
