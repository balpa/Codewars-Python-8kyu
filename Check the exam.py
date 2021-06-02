"""The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

If the score < 0, return 0."""

def check_exam(arr1,arr2):
    count = 0
    for x in range(len(arr1)):
        if arr1[x] == arr2[x]:
            count+=4
        elif arr1[x] == "" or arr2[x] == "":
            count += 0
        else:
            count -= 1
    return count if count > 0 else 0
