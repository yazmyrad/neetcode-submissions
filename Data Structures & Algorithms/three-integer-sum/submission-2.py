class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for i in range(n):
            j, k = i+1, n-1
            while j<k:
                curr = nums[k]+nums[j]
                if curr == -nums[i] and [nums[i], nums[j], nums[k]] not in ans:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif curr > -nums[i]: k -=1
                else: j += 1
        return ans