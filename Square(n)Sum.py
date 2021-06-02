"""Complete the square sum function so that it squares each number passed into it and then sums the results together."""

def square_sum(numbers):
    sumarr = list(map(lambda x:x**2, numbers))
    return sum(sumarr)
