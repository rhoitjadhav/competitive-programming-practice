# Make Array Consecutive 2

def makeArrayConsecutive2(statues):
    _min = min(statues)
    _max = max(statues)

    no_count = (_max - _min - 1) - (len(statues) - 2)

    return no_count
