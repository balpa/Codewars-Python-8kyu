"""Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string."""

def ensure_question(s):
    return f"{s}?" if "?" not in s else s
