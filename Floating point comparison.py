"""Task
You have:

a float value that comes from a computation and may have accumulated errors up to ±0.001
a reference value
a function approx_equals that compare the two values taking into account loss of precision; the function should return True if and only if the two values are close to each other, the maximum allowed difference is 0.001
The function is bugged and sometimes returns wrong results.

Your task is to correct the bug."""

def approx_equals(a, b):
    return True if abs(a-b)<0.001 else False
