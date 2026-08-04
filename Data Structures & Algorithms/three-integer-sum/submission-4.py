class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            j, k = i+1, n-1
            while j<k:
                curr = nums[k]+nums[j]
                if curr == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j<k: j += 1
                elif curr > -nums[i]: k -=1
                else: j += 1
        return ans