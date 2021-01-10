# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False

        top = -1
        stack = []
        similar = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
                top += 1
            if c == "}" or c == "]" or c == ")":
                if top == -1:
                    return False
                if stack[top] == similar[c]:
                    stack.pop()
                    top -= 1
                else:
                    return False

        if len(stack) > 0:
            return False

        return True

s = Solution()
print(s.isValid('{[]}'))
