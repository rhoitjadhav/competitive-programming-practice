from typing import List


def electionsWinners(votes: List, k: int) -> int:
    gmax = max(votes)
    gmax_count = votes.count(gmax)
    
    if k == 0: 
        if gmax_count > 1:
            return 0

        else:
            return 1

    result = 0    

    for v in votes:
        if v + k > gmax:
            result += 1
    
    return result    


votes = [1, 1, 1, 1, 1]
k = 0

result = electionsWinners(votes, k)
print(result)
