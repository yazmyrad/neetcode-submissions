class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for k in range(n):
            i, j = 0, n-1
            while i<j:
                curr = nums[i]+nums[j]
                if curr == -nums[k] and i!=k and j!=k and sorted([nums[i], nums[j], nums[k]]) not in ans:
                    ans.append(sorted([nums[i], nums[j], nums[k]]))
                    i += 1
                elif curr > -nums[k]: j -=1
                else: i += 1
        return ans