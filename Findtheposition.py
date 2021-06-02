"""When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1""""

def position(alphabet):
    alp = ".abcdefghijklmnopqrstuvwxyz"
    return f"Position of alphabet: {alp.index(alphabet)}"
