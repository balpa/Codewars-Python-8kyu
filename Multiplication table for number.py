"""Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:"""

def multi_table(number):
    final = []
    for x in range(1,11):
        final.append(f"{x} * {number} = {x*number}")
    return '\n'.join(final)
