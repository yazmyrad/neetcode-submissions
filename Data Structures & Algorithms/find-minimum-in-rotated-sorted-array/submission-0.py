class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = 1001
        for num in nums:
            minval = min(minval, num)
        return minval