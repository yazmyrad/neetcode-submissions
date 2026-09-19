class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n
        for i in range(n):
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    result[j] = i - j
                
                stack.append(i)
        return result