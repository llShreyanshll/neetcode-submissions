class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(':')', '{':'}', '[':']'}
        stack = []

        for ch in s:
            if ch in paren:
                stack.append(ch)
            else:
                if stack and paren[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False

        return True if not stack else False