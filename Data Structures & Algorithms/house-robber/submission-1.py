class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        ans = [0]*n
        ans[0] = nums[0]
        ans[1] = nums[1]
        ans[2] = nums[2] + ans[0]

        maxrob = max(ans[:3])
        for i in range(3, n):
            ans[i] = nums[i] + max(ans[i - 2], ans[i - 3])
            maxrob = max(maxrob, ans[i])
        return maxrob