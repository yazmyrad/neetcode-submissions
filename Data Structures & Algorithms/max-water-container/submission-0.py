class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxVal = 0
        while i<j:
            amount = (j-i)*min(heights[i], heights[j])
            maxVal = max(maxVal, amount)
            if heights[i] < heights[j]: i += 1
            else: j -= 1
        return maxVal