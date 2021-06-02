"""Given a non-empty array of integers, return the result of multiplying the values together in order. Example:"""
from functools import reduce
def grow(arr):
    return reduce((lambda x, y: x * y), arr)
