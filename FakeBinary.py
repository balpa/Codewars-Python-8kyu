"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string."""

def fake_bin(x):
    nums = [int(x) for x in str(x)]
    random = list(map(lambda x : 0 if x < 5 else 1, nums))
    return ''.join(map(str,random))
