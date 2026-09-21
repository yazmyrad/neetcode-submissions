class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        pse, stack = [-1]*n, []
        max_area = 0
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
            
        nse, stack = [n]*n, []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                nse[stack.pop()] = i
            stack.append(i)
            
        for i in range(n):
            l, r = pse[i], nse[i]
            width = r - l - 1
            max_area = max(max_area, width*heights[i])
            
        return max_area