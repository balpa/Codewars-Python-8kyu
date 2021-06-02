"""Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know."""

def maps(a):
    res = list(map(lambda x : x*2,a))
    return res
