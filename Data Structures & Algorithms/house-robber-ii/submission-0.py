class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_one(n, arr):
            ans = [0]*n
            ans[0] = arr[0]
            ans[1] = arr[1]
            ans[2] = arr[2] + ans[0]

            maxrob = max(ans[:3])
            for i in range(3, n):
                ans[i] = arr[i] + max(ans[i - 2], ans[i - 3])
                maxrob = max(maxrob, ans[i])
            return maxrob
        
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums)
        if n == 3: return max(nums)
        return max(rob_one(n-1, nums[:n-1]), rob_one(n-1, nums[1:]))