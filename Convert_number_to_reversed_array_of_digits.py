"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

"""

def digitize(n):
    a = [int(x) for x in str(n)]
    a.reverse()
    return a
