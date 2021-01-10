# Word Search
class Solution:
    def exist(self, board, word):

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.is_word_exist1(board, i, j, word, 0):
                        return True

        return False
    
    def is_word_exist(self, board, i, j, word, index):
        if len(word) == index:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False

        temp = board[i][j]
        board[i][j] = ""

        result = self.is_word_exist(board, i + 1, j, word, index + 1) or \
                self.is_word_exist(board, i - 1, j, word, index + 1) or \
                self.is_word_exist(board, i, j + 1, word, index + 1) or \
                self.is_word_exist(board, i, j - 1, word, index + 1)
        
        board[i][j] = temp
        
        return result

    def is_word_exist1(self, board, i, j, word, index):
        if len(word) == index:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False


        helper = board[i][j]
        board[i][j] = "$"

        result = self.is_word_exist1(board, i + 1, j, word, index + 1) or \
                self.is_word_exist1(board, i - 1, j, word, index + 1) or \
                self.is_word_exist1(board, i, j + 1, word, index + 1) or \
                self.is_word_exist1(board, i, j - 1, word, index + 1)
        
        board[i][j] = helper
        
        return result


if __name__ == "__main__":
    s = Solution()

    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','D','E']
    ]

    word = "DDC"

    print(s.exist(board, word))
