from itertools import permutations

def oneLetterDiff(first_string, second_string):
    letter_pairs = list(zip(first_string, second_string))

    misses = []
    for a, b in letter_pairs:
        if a != b:
            misses.append(True)
        else:
            misses.append(False)
        # misses.append(a != b)

    # misses = (a != b for (a,b) in letter_pairs)
    
    return True if sum(misses) == 1 else False

def stringsRearrangement(a):
    arrangements = list(permutations(a))
    for current_arrangement in arrangements:
        string_comparisons = list(zip(current_arrangement, current_arrangement[1:]))
        result = []
        for a, b in string_comparisons:
            result.append(oneLetterDiff(a, b))
        
        if all(result):
            return True
    return False

a = ["ab", "bb", "ba"]

result = stringsRearrangement(a)
print(result)
