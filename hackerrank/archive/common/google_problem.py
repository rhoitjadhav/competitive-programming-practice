"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


array = [10, 15, 3, 6]

def find(array, key):
    for arr in array:
        b = key - arr

        if b in array:
            return True

    return False

print(find(array, 17))