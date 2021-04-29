class Solution:
    def convert(self, string: str, numRows: int) -> str:
        if numRows == 1: 
            return string

        n = len(string)
        result = [[] for _ in range(numRows)]

        index = 0
        flag = True
        for i in range(n):
            result[index].append(string[i])

            if flag:
                index += 1
            else:
                index -= 1
            
            if index >= numRows - 1:
                flag = False

            if index == 0:
                flag = True
        output = ''
        for r in result:
            output += "".join(r)

        return output


sol = Solution()
string = 'AB'
numRows = 1
result = sol.convert(string, numRows)
print(result)
