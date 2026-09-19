class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for i in s:
            if stack and i not in d:
                stack.append(i)
                continue
            if stack and i in d and stack[-1] == d[i]:
                stack.pop()
            else:
                stack.append(i)
                continue
        if stack: return False
        return True