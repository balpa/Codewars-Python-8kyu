"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them."""

def abbrev_name(name):
    names = name.split(" ")
    return f"{names[0][0].upper()}.{names[1][0].upper()}"
