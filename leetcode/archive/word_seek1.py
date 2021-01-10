# grids = [['E', 'L', 'E', 'K', 'T', 'R', 'A', 'H', 'T', 'H', 'O', 'R', 'G', 'V'], ['S', 'I', 'L', 'V', 'E', 'R', 'A', 'O', 'R', 'W', 'T', 'N', 'S', 'H'], ['A', 'U', 'A', 'U', 'A', 'W', 'R', 'E', 'H', 'S', 'I', 'N', 'U', 'P'], ['H', 'N', 'E', 'R', 'K', 'C', 'T', 'N', 'W', 'H', 'A', 'M', 'R', 'R'], ['A', 'F', 'T', 'E', 'H', 'S', 'I', 'I', 'T', 'M', 'A', 'S', 'F', 'A'], ['I', 'C', 'Y', 'M', 'I', 'L', 'D', 'R', 'R', 'N', 'C', 'A', 'E', 'A'], ['I', 'E', 'I', 'M', 'A', 'O', 'I', 'E', 'E', 'A', 'E', 'R', 'R', 'L'], ['W', 'W', 'Y', 'T', 'W', 'N', 'D', 'V', 'R', 'M', 'G', 'E', 'I', 'O'], ['I', 'N', 'V', 'I', 'D', 'I', 'B', 'L', 'E', 'G', 'A', 'G', 'R', 'O'], ['T', 'D', 'H', 'S', 'P', 'A', 'E', 'O', 'H', 'D', 'C', 'N', 'O', 'P'], ['C', 'I', 'O', 'S', 'K', 'T', 'T', 'Z', 'T', 'G', 'E', 'A', 'N', 'D'], ['H', 'F', 'K', 'O', 'K', 'P', 'R', 'N', 'N', 'L', 'K', 'R', 'M', 'A'], ['E', 'B', 'W', 'O', 'M', 'A', 'N', 'P', 'A', 'E', 'U', 'T', 'A', 'E'], ['U', 'O', 'F', 'A', 'L', 'C', 'O', 'N', 'P', 'F', 'L', 'S', 'N', 'D']]

# Enter your code here. Read input from STDIN. Print output to STDOUT
def word_seek(grid, word):
    n = len(grid)
    m = len(grid[0])
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0]:
                for k in range(8):
                    if is_word_exist(grid, i, j, word, 0, k):
                        return word + " " + str(i) + " " + str(j)
                    
    return word + " -1 -1"


def is_word_exist(grid, i, j, word, word_index, dire):
    if len(word) == word_index:
        return True

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[word_index]:
        return False
    
    helper = grid[i][j]
    grid[i][j] = "_"

    if dire == 0:
        res = is_word_exist(grid, i + 1, j, word, word_index + 1, dire=0)
    elif dire == 1:
        res = is_word_exist(grid, i - 1, j, word, word_index + 1, dire=1)
    elif dire == 2:
        res = is_word_exist(grid, i, j + 1, word, word_index + 1, dire=2)
    elif dire == 3:
        res = is_word_exist(grid, i, j - 1, word, word_index + 1, dire=3)
    elif dire == 4:
        res = is_word_exist(grid, i + 1, j - 1, word, word_index + 1, dire=4)
    elif dire == 5:
        res = is_word_exist(grid, i + 1, j + 1, word, word_index + 1, dire=5)
    elif dire == 6:
        res = is_word_exist(grid, i - 1, j + 1, word, word_index + 1, dire=6)
    else:
        res = is_word_exist(grid, i - 1, j - 1, word, word_index + 1, dire=7)
    
    grid[i][j] = helper

    return res


if __name__ == "__main__":
    grids = []
    words = []
    while True:
        grid = input()
        if grid == "":
            break
        else:
            grids.append(list(grid))
    
    while True:
        try:
            word = input()
        except EOFError:
            break
        if word == "":
            break
        else:
            words.append(word)
    
    for word in words:
        word = word.strip()
        result = word_seek(grids, word)
        print(result)
