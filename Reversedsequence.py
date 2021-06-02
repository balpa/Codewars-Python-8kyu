"""Build a function that returns an array of integers from n to 1 where n>0."""

def reverse_seq(n):
    arr = []
    for x in range(1,n+1):
        arr.append(x)
    arr.reverse()
    return arr
